// Executar: node testes_calculos.js
const assert = require('node:assert/strict');
const { PADRAO, calcular } = require('./calculos.js');
const perto = (a,b) => assert.ok(Math.abs(a-b)<1e-7, `esperado ${b}; obtido ${a}`);
let n = 0;
function teste(nome, fn) {fn();n++; console.log(`OK ${n} - ${nome}`);}
teste('Consumo atual 72 kWh',()=>perto(calcular(PADRAO).atualKWh,72));
teste('Consumo com LED 10.8 kWh',()=>perto(calcular(PADRAO).ledKWh,10.8));
teste('Economia 61.2 kWh = 85%',()=>{const r=calcular(PADRAO);perto(r.economiaLedKWh,61.2);perto(r.economiaLedPercentual,85);});
teste('Custo base 72 e economia LED R$61.20',()=>{const r=calcular(PADRAO);perto(r.custoBase,72);perto(r.economiaLedReais,61.2);});
teste('Custo LED 120, retorno 1.96 meses',()=>{const r=calcular(PADRAO);perto(r.investimentoLed,120);perto(r.retornoLedMeses,120/61.2);});
teste('Potência solar teoricamente necessária',()=>{const r=calcular(PADRAO);perto(r.solarKWp,72/(4.5*0.75*30));perto(r.solarGeracaoKWh,72);});
teste('Maior tempo aumenta o consumo',()=>assert.ok(calcular({...PADRAO, horas:6}).atualKWh>calcular(PADRAO).atualKWh));
teste('Tarifa altera gasto, não energia',()=>{const r=calcular({...PADRAO,tarifa:2});perto(r.atualKWh,72);perto(r.custoBase,144);});
teste('Recusa quantidade inválida',()=>assert.throws(()=>calcular({...PADRAO,lampadas:0}),/lampadas/));
teste('Recusa LED mais potente',()=>assert.throws(()=>calcular({...PADRAO,potenciaLed:61}),/potência LED/));
teste('Recusa tarifa não numérica',()=>assert.throws(()=>calcular({...PADRAO,tarifa:'x'}),/tarifa/));
teste('Recusa quantidade fracionária',()=>assert.throws(()=>calcular({...PADRAO,lampadas:1.5}),/inteiro/));
console.log(`\n${n} verificações aprovadas.`);
