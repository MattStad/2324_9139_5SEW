package labyrinth_02;

import java.util.Arrays;

/**
 * @author matth
 * @klasse 5CN
 */

public class Labyrinth {
	public static String[][] maps = {{
		"############",
		"#  #     # #",
		"## # ### # #",
		"#  # # # # #",
		"## ### # # #",
		"#        # #",
		"## ####### #",
		"#          #",
		"# ######## #",
		"# #   #    #",
		"#   #   # ##",
		"######A#####"
	}, {
		"################################",
		"#                              #",
		"# ############################ #",
		"# # ###       ##  #          # #",
		"# #     ##### ### # ########## #",
		"# #   ##### #     # #      ### #",
		"# # ##### #   ###   # # ## # # #",
		"# # ### # ## ######## # ##   # #",
		"# ##### #  # #   #    #    ### #",
		"# # ### ## # # # # ####### # # #",
		"# #        # #   #     #     # #",
		"# ######## # ######### # ### # #",
		"# ####     #  # #   #  # ##### #",
		"# # #### #### # # # # ## # ### #",
		"#                      # #     #",
		"###########################A####"
	}, {
		"###########################A####",
		"#   #      ## # # ###  #     # #",
		"# ###### #### # # #### ##### # #",
		"# # ###  ## # # # #          # #",
		"# # ### ### # # # # # #### # # #",
		"# #     ### # # # # # ## # # # #",
		"# # # # ### # # # # ######## # #",
		"# # # #     #          #     # #",
		"# ### ################ # # # # #",
		"# #   #             ## # #   # #",
		"# # #### ############# # #   # #",
		"# #                    #     # #",
		"# # #################### # # # #",
		"# # #### #           ###     # #",
		"# # ## # ### ### ### ### # ### #",
		"# #    #     ##  ##  # ###   # #",
		"# ####   ###### #### # ###  ## #",
		"###########################A####"
	}, {
		"#############",
		"#           #",
		"#           #",
		"#           #",
		"###########A#"
	}};

	/**
	 * Wandelt (unveränderliche) Strings in Char-Arrays
	 * @param map  der Plan, ein String je Zeile
	 * @return char[][] des Plans
	 */
	public static char[][] fromStrings(String[] map) {
		/**
		 * String to char[][]
		 */
		char[][] result = new char[map.length][map[0].length()];
		for (int i = 0; i < map.length; i++) {
			result[i] = map[i].toCharArray();
		}
		return result;
	}


	/**
	 * Ausgabe des Layrinths
	 * @param lab
	 */
	public static void printLabyrinth(char[][] lab) {
		for (char[] row : lab) {
			System.out.println(row);
		}
	}

	/**
	 * Suche den Weg
	 * @param zeile     aktuelle Position
	 * @param spalte     aktuelle Position
	 * @param lab
	 * @throws InterruptedException    für die verlangsamte Ausgabe mit sleep()
	 */
	public static boolean suchen(int zeile, int spalte, char[][] lab) throws InterruptedException {
		if (lab[zeile][spalte] == 'A') {
			printLabyrinth(lab);
			return true;
		}

		if(lab[zeile][spalte] =='#' || lab[zeile][spalte] =='X'){
			return false;
		}

		lab[zeile][spalte] = 'X';
		char[][] labClone = new char[lab.length][lab[0].length];
		for (int i = 0; i < lab.length; i++) {
			labClone[i] = lab[i].clone();
		}
		if (suchen(zeile + 1, spalte, labClone)){
			return true;
		}
		if (suchen(zeile, spalte + 1, labClone)) {
			return true;
		}
		if (suchen(zeile - 1, spalte, labClone)){
			return true;
		}
		if (suchen(zeile, spalte - 1, labClone)){
			return true;
		}

		lab[zeile][spalte] = ' ';
		return false;
	}

	public static int suchenAlle(int column, int row, char[][] labyrinth) {
		/**
		 * sucht alle Lösungsmöglichkeiten für ein Labyrinth
		 */
		if (labyrinth[column][row] == 'A') {
			return 1;
		} else if (labyrinth[column][row] == ' ') {
			labyrinth[column][row] = 'X';
			return suchenAlle(column - 1, row, copyLabyrinth(labyrinth))
					+ suchenAlle(column, row - 1, copyLabyrinth(labyrinth))
					+ suchenAlle(column + 1, row, copyLabyrinth(labyrinth))
					+ suchenAlle(column, row + 1, copyLabyrinth(labyrinth));
		}
		else{
			return 0;
		}
	}

	public static char[][] copyLabyrinth(char[][] labyrinth) {
		/**
		 * deepcopy für labyrinth
		 */
		char[][] copy = new char[labyrinth.length][];
		for (int i = 0; i < labyrinth.length; i++) {
			copy[i] = Arrays.copyOf(labyrinth[i], labyrinth[i].length);
		}
		return copy;
	}

	public static void main(String[] args) throws InterruptedException {
		/**
		 * Main Methode
		 */
		char[][] labyrinth = fromStrings(maps[0]);
		printLabyrinth(labyrinth);
		System.out.println("Ausgang gefunden: " + (suchen(1, 1, labyrinth) ? "ja" : "nein"));
		System.out.println("Ausgang gefunden: " + (suchen(1, 1, fromStrings(maps[1])) ? "ja" : "nein"));
		System.out.println("Ausgang gefunden: " + (suchen(1, 1, fromStrings(maps[2])) ? "ja" : "nein"));
		System.out.println("Ausgang gefunden: " + (suchen(1, 1, fromStrings(maps[3])) ? "ja" : "nein"));
		System.out.println("-----------------------------------------------------");
		// TODO: System.out.println("Anzahl Wege: " + suchenAlle(5, 5, labyrinth));
		System.out.println("Anzahl Wege: " + suchenAlle(1, 1, fromStrings(maps[0])));
		System.out.println("Anzahl Wege: " + suchenAlle(1, 1, fromStrings(maps[1])));
		System.out.println("Anzahl Wege: " + suchenAlle(1, 1, fromStrings(maps[2])));
		System.out.println("Anzahl Wege: " + suchenAlle(1, 1, fromStrings(maps[3])));

	}
}
