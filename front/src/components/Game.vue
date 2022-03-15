<template>
  <div id="App">
            <div class="Game">
                <table class="GameBoard r-t-l r-t-r r-b-l r-b-r">
                    <tbody ref="cell">
                        <tr>
                            <td class="cell r-t-l" >{{ board[0] }}</td>
                            <td class="cell">{{ board[1] }}</td>
                            <td class="cell r-t-r">{{ board[2] }}</td>
                        </tr>
                        <tr>
                            <td class="cell">{{ board[3] }}</td>
                            <td class="cell">{{ board[4] }}</td>
                            <td class="cell">{{ board[5] }}</td>
                        </tr>
                        <tr>
                            <td class="cell r-b-l">{{ board[6] }}</td>
                            <td class="cell">{{ board[7] }}</td>
                            <td class="cell r-b-r">{{ board[8] }}</td>
                        </tr>
                    </tbody>
                </table>
            </div>
        </div>
</template>

<script>
export default {
    name: "BoardComponents",
    props: {
        board: {
            type: Object,
            default: new Array(" ", " ", " ", " ", " ", " ", " ", " ", " "),
        },
    },
    methods: {
        /* Get all squares which are empty. recursive function
            board : array of string, current board*/
        getEmptySpacesPos: function getEmptySpacesPos(board) {
            if (board.length === 0) return [];
            else {
                let head = board[0];
                let tail = board.slice(1, board.length);
                let pos = 9 - board.length;
                // an empty element can be "" or " "
                if (head === " " || head === "") return [pos].concat(this.getEmptySpacesPos(tail));
                else return this.getEmptySpacesPos(tail);
            }
        },
        /* Iterate from the html view to retrieve all board objects */
        getAllBoardElements : function getAllBoardElements() {
            return [...this.$refs.cell.children[0].children].concat([...this.$refs.cell.children[1].children], [...this.$refs.cell.children[2].children]);
        },
        /* Link each empty board elements with a click event in order to be used by parent */
        init: function init() {
            let emptySpaces = this.getEmptySpacesPos(this.$props.board);
            let boardElements = this.getAllBoardElements();
            for (let i=0; i < boardElements.length; i++) {
                boardElements[i].addEventListener("click", () => this.$emit('clickedEvent', {index : i}));
            }
            emptySpaces.forEach((spacePos) => { // iterate from empty elements
                
            });
        },
    },
    /* Called when mounted */
    mounted() {
        this.init(); // init click event when mounted
    },
};




</script>

<!-- Add "scoped" attribute to limit CSS to this component only -->
<style scoped>
   #App {
     justify-content: space-around;
     background-color: whitesmoke;
   }

   #App .Game {
     display: flex;
     justify-content: space-around;
   }

   .GameBoard {
     width: 300px;
     height: 300px;
     background: linear-gradient(purple, blue);
     box-shadow: 0px 5px 10px rgb(138, 89, 138);
   }

   .GameBoard .cell {
     text-align: center;
     border: none;
     width: 95px;
     height: 95px;
     background-color: whitesmoke;
   }

   .cell {
     text-align: center;
     font-size: 50px;
     font-weight: 900;
     color: red;
   }

   .r-t-l {
     border-top-left-radius: 20px;
   }
   .r-t-r {
     border-top-right-radius: 20px;
   }
   .r-b-l {
     border-bottom-left-radius: 20px;
   }
   .r-b-r {
     border-bottom-right-radius: 20px;
   }

   * {
     font-family: sans-serif;
   }
</style>
