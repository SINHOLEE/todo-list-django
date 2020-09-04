const todoForm = document.querySelector(".js-todoForm"),
    todoInput = todoForm.querySelector("input"),
    todoList = document.querySelector(".js-todoList");    


const TODOS_LS = "todos"; // 로컬 스토리지
let toDos = [];  // 이 스코프에서만 사용하는 투두라는 리스트를 생성한다.

function deleteToDo(event){
    const btn = event.target;
    const li = btn.parentNode;
    const cleanToDos = toDos.filter(obj=>parseInt(li.id) !==obj.id);
    todoList.removeChild(li); 
    toDos = cleanToDos;
    saveToDos();
    
}

function saveToDos(){
    localStorage.setItem(TODOS_LS, JSON.stringify(toDos));
}




function paintToDo(text){
    // console.log(text);
    if (text===""){
        return
    }
    const li = document.createElement("li");
    const deleteBtn = document.createElement("button");
    deleteBtn.addEventListener("click", deleteToDo);
    deleteBtn.innerText = "X";
    const span = document.createElement("span");
    const newId = toDos.length + 1;
    span.innerText = text;
    li.appendChild(span);
    li.appendChild(deleteBtn);
    li.id = newId;
    todoList.appendChild(li);
    const todoobj = {
        "text": text,
        "id": newId
    };
    toDos.push(todoobj);
    saveToDos();
}


function handleSubmit(event){
    event.preventDefault();
    const currentValue = todoInput.value;
    paintToDo(currentValue);    
    todoInput.value = ""; 
       
}

function loadTodos(){
    const loadedToDos = localStorage.getItem(TODOS_LS);
    if (loadedToDos !== null){
        console.log(loadedToDos);
        const parsedToDos = JSON.parse(loadedToDos);
        console.log(parsedToDos);
        parsedToDos.forEach(element => {
        paintToDo(element.text);        
    });
    }
} 


function init(){
    console.log("todo");
    loadTodos();
    todoForm.addEventListener("submit", handleSubmit);
    // todoList.addEventListener("click")
}

init();