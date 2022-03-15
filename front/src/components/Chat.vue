<template>
<div id="wrapper">
  <div id="menu">
        <div style="clear:both"></div>
    </div>
     
    <div id="chatbox">
        <div v-for="item in items" :key="item">
            <div v-html="item[0]"/>
            <div v-html="item[1]"/> 
        </div>
    </div>
     
    <div class="send_box" name="message"  >
        <input class="sendMsg_input" v-model="message" type="text" size="63" />
        <button class="sendMsg_btn" @click="handleSentEvent">Send</button>
    </div>
</div>
</template>

<script>
export default {
    name: "ChatComponent",
    data() {
      return {
        message: "",
        items:[]
      };
    },
    methods : {
        handleSentEvent : function(){
          this.message = this.message.replace('+', '');
          this.$emit('messageSentEvent', {'message' : this.message})
          this.message = "";
       },
       sendMessage : function(psn, message, color='black') {
            message = message.replace(/\s/g, '&nbsp;');
            let item = ['<style scoped>.psn_sender'+this.items.length+'{color:'+color+';font-family: cursive;}.msgln'+this.items.length+'{color:'+color+';word-wrap: break-word;padding-left: 7px;;padding-right: 7px;font-family: cursive;}</style><div><b class="psn_sender'+this.items.length+'">'+psn+'&nbsp;:</b>','<p class="msgln'+this.items.length+'">'+message+'</p></div>'];
            this.items.push(item);
       },
    }, 
};




</script>

<!-- Add "scoped" attribute to limit CSS to this component only -->
<style scoped>
    body {
    font:12px arial;
    color: #222;
    text-align:center;
    padding:35px; }
  
.send_box, p, span {
    margin:0;
    padding:0;}

.send_box {
    background-color: transparent;
    height: 10%;
    display: flex;
    flex-direction: column;
    justify-content: space-between;
    align-items: center;
    padding-right: 10px;
    padding-left: 10px;
    padding-top: 10px;
    padding-bottom: 3px;
}
.sendMsg_btn{
    height: 40%;
    width: 50%;
    border:1px solid gray;
    border-radius: 15px
}
.sendMsg_btn:active{
   background-color:darkgray;
}
.sendMsg_input{
    height: 40%;
    width: 90%;
    border:1px solid #ACD8F0;
    border-radius: 5px
}

.msgln{
    word-wrap: break-word;
    padding-left: 15px;
    padding-top: 0;
    padding-right: 7px;
    margin-top: 0;
}
  
input { font:12px cursive; }
  
a {
    color:#0000FF;
    text-decoration:none; }
  
    a:hover { text-decoration:underline; }
  
#wrapper, #loginform {
    margin:0 auto;
    padding-bottom:25px;
    background: skyblue;
    width:20%;
    border-radius: 5px;
    border:1px solid #ACD8F0; }
  
#loginform { padding-top:18px; }
  
    #loginform p { margin: 5px; }
  
#chatbox {
    text-align:left;
    margin:0 auto;
    padding:10px;
    background:#fff;
    height:80%;
    border-radius: 5px;
    width:85%;
    border:1px solid #ACD8F0;
    overflow:auto; }
  
#usermsg {
    width:395px;
    border:1px solid #ACD8F0; }
  
  
.error { color: #ff0000; }
  
#menu { padding:12.5px 25px 12.5px 25px; }

  
  
.msgln { margin:0 0 2px 0; }
</style>
