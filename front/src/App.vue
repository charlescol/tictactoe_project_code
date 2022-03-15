<template>
    <div app>
        <div psn v-if=!init>
            <PsnInputComponent @psnEnteredEvent="addUserPsnCommand" />
        </div>
        <div v-if=init class="container" > 
            <QueueComponent class='side_component' v-bind:items="users"/>
            <div class="middle_window">
                <p class="versus_p">{{ game.psn1 }} vs {{ game.psn2 }}</p>
                <BoardComponents v-bind:board="game.board" @clickedEvent="execPlayCommand"/>
                <div v-if=game.player class="currentPlayer"> 
                    <p >Waiting for :</p>
                    <p>{{ game.currentPlayer }}</p>
                </div>
                <div v-if=!game.player class="currentPlayer"> 
                    <p >Waiting for another player</p>
                </div>
                
            </div>
            <ChatComponent ref="chatRef" @messageSentEvent="sendMessage" class='side_component'/>
        </div>
    </div>
</template>

<script>
import BoardComponents from './components/Game.vue'
import ChatComponent from './components/Chat.vue'
import PsnInputComponent from './components/PsnInput.vue'
import Request from './Controller/Controller.js'
import User from './r/user.js'
import Game from './r/game.js'
import Message from './r/message.js'
import QueueComponent from './components/Queue.vue'

export default {
    name: 'App',
    components: {
        BoardComponents, // Board
        PsnInputComponent, // Psn Input when page openned
        ChatComponent, // Chat Widget
        QueueComponent // Queue Widget
    },
    data() {
        return {
            user: null, // curent user
            connection: null, // web socket connection
            init : false, // if the psn has been entered
            game : new Game(), // current game
            users: new Array() // current user queue
        };
    },
    methods: {
        /* Called when an user plays, payload.index : current click area*/
        execPlayCommand(payload) {
            var request = new Request().play(this.user, payload.index, result=>{});
        },
        /* Called when the user's psn is added*/
        addUserPsnCommand(payload) {
            var request = new Request().createUser(new User(payload.psn), data => {
                if (data != null)  {
                    this.user = data;
                    this.init = true;
                    /* Called when the user leaves */                    
                    window.addEventListener('beforeunload', (event) => {
                        var request = new Request().removeUser(this.user, result=>{});
                        event.preventDefault(); // Cancel the event as stated by the standard.
                        event.returnValue = '';// Chrome requires returnValue to be set.
                    });
                }
                else alert("Invalid psn, try again"); // When the request return value is invalid
            });
        },    
        /* Called when an user send a message to the chat */
        sendMessage: function(payload) {
            console.log(payload.index);
            this.connection.send('{"action" : "onbroadcast" , "data" : "chat+'+payload.message+'+'+this.user.psn+'"}');
        }
    },
    /* Called when the component is mounted */
    mounted: function(){
        //Init the socket connection
      this.connection = new WebSocket('wss://g78qc0xisd.execute-api.us-east-1.amazonaws.com/production');
      this.connection.onmessage = (event) => {
        let data = JSON.parse(event.data)
        if (data.type == "chat") { // if a chat message is received
            if (this.user.psn == data.psn) 
                this.$refs.chatRef?.sendMessage(data.psn, data.message, 'royalblue'); // chat message from current user
            else 
                this.$refs.chatRef?.sendMessage(data.psn, data.message); // chat message from others
        }
        else if(data.type == "board") { // if a board update message is received
            this.game.board = data.board.toUpperCase().split(',');
            this.game.psn1 = data.psn1;
            this.game.psn2 = data.psn2;
            this.game.player = (data.player != "") // if there is a current game 
            if (this.game.player) 
                // temporary, not fixed : data.board.lenght == undefined
                if (data.board != ',,,,,,,,') // temporary: fix backend problem (same state for player for the two first moves)
                    this.game.currentPlayer = (data.player=='True') ? this.game.psn1 : this.game.psn2;
                else // inverse state if first move
                    this.game.currentPlayer = (data.player=='True') ? this.game.psn2 : this.game.psn1;
        }
        else if(data.type == "user") { // if user queue update message is received
            this.users = data.queue.split(',');
        }
      }
    }
}
</script>

<style>
#app {
  padding: 0px;
     margin: 0px;
     background-color: transparent;
}
.container {
  background-color: whitesmoke;
  display: flex; /* or inline-flex */
  flex-direction: row;
  justify-content:space-evenly;
  align-items: center;
  position: fixed; /* or absolute */
  height:100%;
  width: 100%;
}
.versus_p  {
    font-size: 25px;
    text-align: center;
    font-family: fantasy;
}
.currentPlayer {
    font-size: 25px;
    text-align: center;
    font-family: Cursive;
    display: flex; /* or inline-flex */
    flex-direction: row;
    justify-content:space-evenly;
}
.side_component{
   height:70%; 
   width: 20%;
   background-color: blue;
}
</style>
