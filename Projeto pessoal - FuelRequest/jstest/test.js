function solcot(){
    alert("Solicitada");
}
function questionario(){
    var nome;
    nome = prompt("qual seu nome?");
    alert("olá " + nome);
}

function mudtext(){
    var h1 = document.getElementsByTagName("h1");

    if (h1[0].innerHTML == "Solicitar Cotação"){
        h1[0].innerHTML = "Solicitado"
    }else{
        h1[0].innerHTML = "Solicitar Cotação"
    }
}

function incrementar(){
    var p = document.getElementById("p1");

    p1.innerHTML = parseInt(p.innerHTML) + 1

}