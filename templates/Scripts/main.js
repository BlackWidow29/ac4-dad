function mostrarOcultarSenha() {
    const senha = document.getElementById("senha", "senha1");
    if (senha.type == "password") {
        senha.type = "text";
    } else {
        senha.type = "password";
    }
}

function mostrarOcultarSenha1() {
    const senha = document.getElementById("exampleInputPassword3");
    if (senha.type == "password") {
        senha.type = "text";
    } else {
        senha.type = "password";
    }
}


$(document).ready(function () {
    $("li.nav-item").click(function (e) {
        e.preventDefault();
        $(".nav-item").removeClass("active");
        $(this).addClass("active");
    });
});