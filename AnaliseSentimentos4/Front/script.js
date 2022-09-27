function darkMode() {
    var element = document.body;
    var content = document.getElementById("DarkModetext");
    element.className = "dark-mode";
    content.innerText = " ON";
}
function lightMode() {
    var element = document.body;
    var content = document.getElementById("DarkModetext");
    element.className = "Modo Claro";
    content.innerText = "OFF";
}

function Get(url){
    let request = new XMLHttpRequest(); // a new request
    request.open("GET",url,false);
    request.send();
    return request.responseText;          
}
function criaLinha(Usuario){


}

function main(){
    var url = "http://localhost:5000/api/Usuario";
    var data = Get(url);
    var Usuario = JSON.parse(data);
    console.log(Usuario);
    criaLinha(Usuario);
}

main();