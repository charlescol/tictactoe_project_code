<template>
<div id="wrapper">
  <div id="menu">
        <div style="clear:both"></div>
    </div>
     
    <div id="queuebox">
        <div v-for="(item, index) in items" :key="item">
            <div class="psn_list">
                <p v-html="index"/>
                <p v-html="item"/>
            </div>
            <hr size="1" width="90%" color="red"> 
        </div>
    </div>
    <p class="title">User Queue</p>
</div>
</template>

<script>
export default {
    name: "QueueComponent",
    props : {
        items:{ // list of users' psn
            type : Object,
            default : new Array()
        }
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


  
a {
    color:#0000FF;
    text-decoration:none; }
  
    a:hover { text-decoration:underline; }
  
#wrapper, #loginform {
    margin:0 auto;
    padding-bottom:25px;
    background: orchid;
    width:20%;
    border-radius: 5px;
    border:1px solid #ACD8F0; }
  
#loginform { padding-top:18px; }
  
    #loginform p { margin: 5px; }

.title{
    text-align: center;
    font-family: fantasy;
}


#queuebox {
    text-align:left;
    margin:0 auto;
    padding:10px;
    background:#fff;
    height:85%;
    border-radius: 5px;
    width:85%;
    border:1px solid #ACD8F0;
    overflow:auto; }

.psn_list{
    text-align: center;
    font-family: cursive;
    display: flex; /* or inline-flex */
    flex-direction: row;
    justify-content:space-between;
    align-items: center;
}
  
  
.error { color: #ff0000; }
  
#menu { padding:12.5px 25px 12.5px 25px; }

  
  
.msgln { margin:0 0 2px 0; }
</style>
