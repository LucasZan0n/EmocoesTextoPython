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