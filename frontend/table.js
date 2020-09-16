const restruant = document.querySelector(".restruant");
const fields = ["name", "price", "kcal"];
const menus = [
    {"name": "짜장면",
    "price": 3000,
    "kcal": 300,},
    {"name": "짬뽕",
    "price": 3500,
    "kcal": 350,},
    {"name": "울면",
    "price": 4000,
    "kcal": 200,},
    {"name": "특수짜장",
    "price": 3800,
    "kcal": 340,},
]
// 토글변수를 클로저로 관리하고 싶었는데 실패....
let priceToggle = true;
let kcalToggle = true;

function getPriceToggle(){
    priceToggle= !priceToggle;
    return priceToggle; 
}
function getKcalToggle(){
    kcalToggle = !kcalToggle;
    return kcalToggle;
}
// sortBtSomething 더 생길때마다 하나하나 함수를 더 만들어야하나? 뭔가 이것도 통합되는 함수 만들 수 있을거같은데...ㅠ
// 해결 ...ㅎㅎ
const getMenusByKey = (key) => {
    tempToggle = getKcalToggle();
    const deepcopiedMenus = JSON.parse(JSON.stringify(menus));
    if (key==""){
        return deepcopiedMenus;
    }
    deepcopiedMenus.sort(function(a,b){
        return (a[key] <= b[key]?1 :-1)  * (tempToggle ? -1:1 )
    });
    return deepcopiedMenus;
}


// 이 부분이랑 밑에 getMenuByKey 이거를 조금 더 깔끔하게... if else없이 구현할 수 있는 방법 없을까?
// 해결
const renderTableHandler=(e)=>{
        renderTable(e.target.abbr);
}

const totalNumHandler=(field, tPrice, tKcal, value)=>{
    if (field === "price") {
        return [tPrice + value, tKcal];
    } else{
        return [tPrice, tKcal + value];
    }
}

const renderTable = (key) => {
    // 기존의 tbody, tfoot 삭제
    restruant.removeChild(restruant.querySelector("tbody"));
    const tbody = document.createElement("tbody");
    let totalPrice = 0;
    let totalKcal = 0;
    const deepcopiedMenus = getMenusByKey(key);
    deepcopiedMenus.map(value => {
        const tr = document.createElement("tr");
        fields.forEach((field, idx) => {
            if (idx===0){
                const t = document.createElement("th");
                t.scope = "row";
                t.innerText = value[field];
                tr.appendChild(t);
            } else {
                const t = document.createElement("td");      
                [totalPrice, totalKcal] = totalNumHandler(field, totalPrice, totalKcal, value[field]);
                t.innerText = value[field];
                tr.appendChild(t);
            }
        })
        tbody.appendChild(tr);
    })
    restruant.appendChild(tbody);
    const totalPriceEls = restruant.querySelectorAll("tfoot td");
    // 총 가격
    totalPriceEls[0].innerText = totalPrice;
    totalPriceEls[1].innerText = totalKcal;
};


function init() {
    const colHeads = restruant.querySelectorAll("thead > tr > th");
    console.log(colHeads);
    colHeads.forEach(el => el.addEventListener("click", renderTableHandler));

    // 왜 map으로 순환돌리면 안되는거냐.... 
    // -> map은 새로운 객체를 만드는 것이기 때문에 이벤트리스너를 붙일 수 없다.
    // colHeads.map(el => el.addEventListener("click", renderTableHandler));
}

init();
