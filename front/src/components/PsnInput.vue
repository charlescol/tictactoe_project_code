<template>
  <div class="root">
    <h2>Enter a Pseudonym</h2>
      <input type="text" placeholder="PSN" v-model="psn"/>
      <button class="validate_button" @click="handleSubmit">Validate</button>
  </div>
</template>

<script>
  export default {
    name: "PsnInputComponent",
    data() {
      return {
        psn: "", // current user psn
      };
    },
    methods : {
      /* Emit event when submit button is clicked */
      handleSubmit : function(){
          this.$emit('psnEnteredEvent', {'psn' : this.psn}) 
       }
    }

};

</script>

<style lang="css" scoped>
  .root {
    width: 400px;
    margin: 0 auto;
    background-color: #fff;
    padding: 30px;
    margin-top: 100px;
    border-radius: 20px;
  }

  input {
    border: none;
    outline: none;
    border-bottom: 1px solid #ddd;
    font-size: 1em;
    padding: 5px 0;
    margin: 10px 0 5px 0;
    width: 100%;
  }

  .validate_button {
    background-color: #3498db;
    padding: 10px 20px;
    margin-top: 10px;
    border: none;
    color: white;
  }

  .validate_button:active{
    background-color:darkgray;
    padding: 10px 20px;
    margin-top: 10px;
    border: none;
    color: white;
}
</style>