$(document).ready(function() {
    $('#btnBuscarIP').click(function() {
        // Usando a API ip-api.com (versão gratuita)
        $.getJSON('http://ip-api.com/json/?fields=status,message,country,regionName,city,isp,query', function(data) {
            if (data.status === 'success') {
                $('#txtip').text('IP: ' + data.query);
                $('#txtcidade').text('Cidade: ' + data.city);
                $('#txtregiao').text('Região: ' + data.regionName);
                $('#txtpais').text('País: ' + data.country);
                $('#txtprovedor').text('Provedor: ' + data.isp);
            } else {
                alert('Erro ao buscar informações do IP: ' + data.message);
            }
        }).fail(function() {
            alert('Erro ao conectar com o serviço de IP. Tente novamente mais tarde.');
        });
    });
});