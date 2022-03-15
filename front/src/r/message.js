/* Class to represent socket chat message*/
export default class Message {
	constructor(psn, message) {
		this.psn = psn;// sender's psn 
		this.message = message;// content
		this.type = 'message'; //  type of socket data
	}
}