function myFunction(valor) {
	if (valor < 10) {
		document.getElementById("numero").innerHTML = "Último Número Sorteado: 0" + valor;
	} else {
		document.getElementById("numero").innerHTML = "Último Número Sorteado: " + valor;
	}
	document.getElementById("button"+valor).style.backgroundColor = "red";
	document.getElementById("button"+valor).style.color = "white";
	document.getElementById("button"+valor).style.borderColor = "black";
}
function closeWindow() {
	close();
}
function reload() {
	window.location.reload();
}
function openWindown() {
	window.open("PedraMaior.html");
}