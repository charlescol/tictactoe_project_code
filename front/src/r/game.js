/* Class to represent the current Game */
export default class Game {
	constructor(board, psnP1, psnP2, currentPlayer) {
		this.board = new Array(" ", " ", " ", " ", " ", " ", " ", " ", " "); // curent board
		this.psn1 = psnP1; // player1's psn
		this.psn2 = psnP2;// player2's psn
		this.currentPlayer = currentPlayer;// current player psn
		this.player = false; // last player who has played (true : player1)
	}
}