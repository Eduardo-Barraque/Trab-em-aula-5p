xhr = new XMLHttpRequest();
xhr.open("GET", "lista_produto/");
xhr.send(null);
xhr.onreadystatechange = function () {
    if (xhr.readyState === 4 && xhr.status === 200) {
    document.getElementById("lista_produto").innerHTML = xhr.response;}
}