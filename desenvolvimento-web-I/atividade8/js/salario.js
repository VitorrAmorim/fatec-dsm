$(document).ready(function() {
    $('#calcularSalario').click(function() {
        // Obter valores dos inputs
        let nome = $('#txtnome').val();
        let idade = parseInt($('#txtidade').val());
        let salarioBruto = parseFloat($('#txtsalario').val());
        let dependentes = parseInt($('#txtdependentes').val());
        
        // Validar campos
        if (!nome || isNaN(idade) || isNaN(salarioBruto) || isNaN(dependentes)) {
            alert('Por favor, preencha todos os campos corretamente.');
            return;
        }
        
        // Cálculos
        let bonusIdade = idade > 50 ? 300 : 200;
        let inss = salarioBruto * 0.08;
        let valeTransporte = salarioBruto * 0.05;
        let valorDependentes = dependentes * 50;
        
        let salarioLiquido = salarioBruto - inss - valeTransporte + bonusIdade + valorDependentes;
        
        // Formatar para moeda
        function formatarMoeda(valor) {
            return valor.toLocaleString('pt-BR', {
                style: 'currency',
                currency: 'BRL',
                minimumFractionDigits: 2
            });
        }
        
        // Exibir resultados
        let mensagem = `Nome: ${nome}\n` +
                      `Número de Dependentes: ${dependentes}\n` +
                      `Salário Bruto: ${formatarMoeda(salarioBruto)}\n` +
                      `INSS (8%): ${formatarMoeda(inss)}\n` +
                      `Vale Transporte (5%): ${formatarMoeda(valeTransporte)}\n` +
                      `Bônus por Idade: ${formatarMoeda(bonusIdade)}\n` +
                      `Valor por Dependentes: ${formatarMoeda(valorDependentes)}\n` +
                      `\nSALÁRIO LÍQUIDO: ${formatarMoeda(salarioLiquido)}`;
        
        alert(mensagem);
    });
});