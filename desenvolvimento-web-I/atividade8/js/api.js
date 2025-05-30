$(document).ready(function() {
    $('#btnBuscarIP').click(function() {
        // Usando a API RandomUser.me
        $.getJSON('https://randomuser.me/api/', function(data) {
            if (data.results && data.results.length > 0) {
                const user = data.results[0];
                $('#txtip').text('Nome: ' + user.name.first + ' ' + user.name.last);
                $('#txtcidade').text('Cidade: ' + user.location.city);
                $('#txtregiao').text('Estado: ' + user.location.state);
                $('#txtpais').text('País: ' + user.location.country);
                $('#txtprovedor').text('E-mail: ' + user.email);
            } else {
                alert('Erro ao buscar informações do usuário: dados não encontrados');
            }
        }).fail(function() {
            alert('Erro ao conectar com o serviço de usuários. Tente novamente mais tarde.');
        });
    });
});