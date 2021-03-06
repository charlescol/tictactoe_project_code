/* Class to represent the current User */
export default class User {
	constructor(psn) {
		this.version = "1.0.0";// front version of user
		this.psn = psn; // psn 
		this.id = null;// GUID (generated by backend) -> signature for back calls
		this.date = null;// date of creation (generated by backend)
	}
}