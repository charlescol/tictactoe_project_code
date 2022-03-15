class Method {
    static GET = "GET";
    static PUT = "PUT";
    static DELETE = "DELETE";
}
/* Class to call http backend functions */
export default class Request {
    constructor() {
        this.http = new XMLHttpRequest(); 
    }
    /* Called when an user needs to be created 
    callback : callback function, 
    user : current user*/
    createUser(user, callback) {
        this._user(user, true, Method.PUT, callback)
    }
    /* Called when an user needs to be removed, 
    callback : callback function, 
    user : current user*/
    removeUser(user, callback) {
        this._user(user, false, Method.DELETE, callback)
    }
    /* Build user request 
    user : current user
    deserialize : if result need to be deserialized
    method : http method 
    callback : callback function*/
    _user(user, deserialize, method,  callback) {
        this.http.open(method, "https://kqki2iu3ya.execute-api.us-east-1.amazonaws.com/Prod/user", true);
        this.http.setRequestHeader("Content-type", "application/json");
        let self = this;
        this.http.onload = function (user) {
            // Callback function 
            if (this.status == 200) 
                user = deserialize ? callback(JSON.parse(this.responseText)) : callback(true);
            else  {
                user = deserialize ? callback(null) : callback(false);
            }
        };
        this.http.send(JSON.stringify(user));
    }
    /* Build play request 
    user : current user
    index : index of move
    callback : callback function*/
    play(user, index, callback) {
        this.http.open(Method.PUT, "https://kqki2iu3ya.execute-api.us-east-1.amazonaws.com/Prod/playedEvent", true);
        this.http.setRequestHeader("Content-type", "application/json");
        let self = this;
        this.http.onload = function (user) {
            // Callback function 
            if (this.status == 200) 
                user = callback(true);
            else 
                user = callback(false);
        };
        this.http.send(JSON.stringify({"user": user, "position" : index}));
    }

}
