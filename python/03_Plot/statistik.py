import subprocess

def execute_git_log(repo_path):
    format_string = "--pretty=format:%H|%an|%ad|%s"
    log_command = ["git", "-C", repo_path, "log", format_string]
    result = subprocess.run(log_command, capture_output=True, text=True, check=True)
    git_log_output = result.stdout.strip()
    return git_log_output.split('\n')


import matplotlib
matplotlib.use('TkAgg')
from dateutil import parser
from collections import Counter
import matplotlib.pyplot as plt

def create_graph(git_log_lines):
    weekdays = []
    hours = []

    for line in git_log_lines:
        # Split each line into its parts
        parts = line.split('|')
        # The date is the third part; use dateutil to parse it
        commit_date = parser.parse(parts[2])
        weekdays.append(commit_date.weekday())  # Monday is 0, Sunday is 6
        hours.append(commit_date.hour)

    # Count the frequency of commits for each weekday and hour
    counts = Counter(zip(weekdays, hours))

    # Unpack the counts into X (hours), Y (weekdays), and sizes (frequency)
    X, Y, sizes = zip(*[(hour, weekday, count * 10) for (weekday, hour), count in counts.items()])

    # Create the scatter plot
    plt.figure(figsize=(10, 6), dpi=100)
    plt.scatter(X, Y, s=sizes, alpha=0.5)

    # Set the axis labels and title
    plt.xlabel('Hour of the Day')
    plt.ylabel('Day of the Week')
    plt.title('Matthias Stadlinger:'+str(len(git_log_lines)))

    # Set the y-axis to show weekdays as text
    plt.yticks(ticks=range(7), labels=['Mon', 'Tue', 'Wed', 'Thu', 'Fri', 'Sat', 'Sun'])

    # Set the x-axis to show hours of the day
    plt.xticks(ticks=range(24), labels=range(24))

    # Save the plot as a PNG file
    plt.savefig("git_statistics.png", dpi=100)

    # Show the plot
    plt.show()

# Example usage
repo_path = "C:\\Users\\matth\\SEW_Jahr5\\"
git_log_lines = execute_git_log(repo_path)
create_graph(git_log_lines)
