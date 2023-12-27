import subprocess
"""
@author: Matthias Stadlinger
@klasse: 5CN
"""
def execute_git_log(repo_path):
    """
    liest git logs aus
    :param repo_path:
    :return: git logs
    """
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
    """
    erzeugt graphik
    :param git_log_lines:
    :return: graphik
    """
    weekdays = []
    hours = []

    for line in git_log_lines:
        parts = line.split('|')
        commit_date = parser.parse(parts[2])
        weekdays.append(commit_date.weekday())  # Monday is 0, Sunday is 6
        hours.append(commit_date.hour)

    counts = Counter(zip(weekdays, hours))
    X, Y, sizes = zip(*[(hour, weekday, count * 10) for (weekday, hour), count in counts.items()])

    plt.figure(figsize=(10, 6), dpi=100)
    plt.scatter(X, Y, s=sizes, alpha=0.5)

    plt.xlabel('Stunde')
    plt.ylabel('Tag')
    plt.title('Matthias Stadlinger:'+str(len(git_log_lines)))

    plt.yticks(ticks=range(7), labels=['Mon', 'Tue', 'Wed', 'Thu', 'Fri', 'Sat', 'Sun'])

    plt.xticks(ticks=range(24), labels=range(24))

    plt.savefig("git_statistics.png", dpi=100)

    plt.show()

repo_path = "C:\\Users\\matth\\SEW_Jahr5\\"
git_log_lines = execute_git_log(repo_path)
create_graph(git_log_lines)
