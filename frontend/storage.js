const fetch = require("node-fetch");


class Store{

    constructor(base_url){
        this.base_url = base_url
        this.todoList = [];
    }


    async _fetch_todos(){
        let data = Object()
        const fetchedData = await fetch(this.base_url + "todos?fields=pk,content,is_completed,priority", {
            method: 'GET',
            headers: {
              'Content-Type': 'application/json'
            }
          })
        const jsonData =  await fetchedData.json()
        this.todoList = [];
        jsonData.forEach(el=>{
            // console.log(el)
            this.todoList.push(el)
        })
    }
    async get_todos(){
        await this._fetch_todos();
        return await this.todoList;
    }
}



const myStore = new Store("http://localhost:8000/api/v1/");

// 이렇게 안하고,
const todos = myStore.get_todos();
// console.log(todos)
setTimeout(function(){console.log(todos)},1000)