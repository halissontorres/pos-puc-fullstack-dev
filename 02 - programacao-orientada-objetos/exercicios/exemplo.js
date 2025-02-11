const empregado = {
    nome: 'João',
    salarioBase: 2000,
    qtHorasExtras: 1,
    valorHoraExtra: 15,
    calculaSalario: function() {
        return this.salarioBase + (this.qtHorasExtras * this.valorHoraExtra);
    }
};

console.log(empregado.calculaSalario());