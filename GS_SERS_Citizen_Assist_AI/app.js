'use strict';
// A interface usa exclusivamente números calculados no arquivo calculos.js.
const { PADRAO, calcular } = window.CitizenCalculos;
const $ = id => document.getElementById(id);
const fmtNum = (n, d=1) => new Intl.NumberFormat('pt-BR',{minimumFractionDigits:d,maximumFractionDigits:d}).format(n);
const dinheiro = n => new Intl.NumberFormat('pt-BR',{style:'currency',currency:'BRL'}).format(n);
let resultado = null;
const perguntas = {
  led: /\b(led|lampad|ilumin|econom|trocar|substitu|investimento|preco|custo)\w*/i,
  solar: /\b(solar|sol|placa|fotovolta|painel|renovav|gerac)\w*/i,
  comparacao: /\b(melhor|escolher|compar|vale|vantagem|alternativa|recomend)\w*/i,
  limites: /\b(limi|risco|garanti|confiav|conta zer|duvida|restri)\w*/i,
  fontes: /\b(fonte|refer|origem|site|dado|onde pesquis)\w*/i
};
function normalizar(s) {return s.normalize('NFD').replace(/[\u0300-\u036f]/g,'').toLowerCase();}
function receber() {
  const input = {};
  for (const k of Object.keys(PADRAO)) {
    // Nunca usar Number('') -> 0: valores vazios devem ser recusados.
    if (!$(k).value.trim()) throw new Error(`Preencha o campo ${k}.`);
    input[k] = Number($(k).value);
  }
  return input;
}
function renderizar(r) {
  $('kwhAtual').textContent = fmtNum(r.atualKWh);
  $('valorAtual').textContent = `Custo aproximado apenas da iluminação: ${dinheiro(r.custoBase)}/mês`;
  $('baseValor').textContent = `${fmtNum(r.atualKWh)} kWh`;
  $('ledValor').textContent = `${fmtNum(r.ledKWh)} kWh`;
  $('solarValor').textContent = '0,0 kWh*';
  $('ledBar').style.width = `${100*r.ledKWh/r.atualKWh}%`;
  $('solarBar').style.width = '0%';
  $('economiaLed').textContent = `${dinheiro(r.economiaLedReais)}/mês`;
  $('economiaLedPercentual').textContent = `${fmtNum(r.economiaLedPercentual,0)}% menos energia na iluminação`;
  $('investimentoLed').textContent = dinheiro(r.investimentoLed);
  $('retornoLed').textContent = `Retorno simples: ${fmtNum(r.retornoLedMeses)} meses`;
  $('solarPotencia').textContent = `${fmtNum(r.solarKWp,2)} kWp`;
  $('solarGeracao').textContent = `Geração teórica: ${fmtNum(r.solarGeracaoKWh)} kWh/mês`;
  $('investimentoSolar').textContent = dinheiro(r.investimentoSolar);
  $('retornoSolar').textContent = `Teto teórico de benefício: até ${dinheiro(r.solarTetoBeneficioReais)}/mês`;
}
function responder(pergunta, r) {
  const p=normalizar(pergunta);
  // Categorias mutuamente exclusivas em ordem de intenção prioritária.
  if(perguntas.fontes.test(p)) return 'Referências consultadas: ANEEL para geração distribuída e compensação; INPE para dados de irradiação solar; MME/Procel e Inmetro para consumo e eficiência das lâmpadas. Veja links na seção “Fontes verificáveis”. Os preços e a insolação inicial são premissas didáticas, não dados oficiais.';
  if(perguntas.limites.test(p)) return `A análise vale somente para ${r.entrada.lampadas} lâmpadas usadas ${fmtNum(r.entrada.horas)} horas por dia durante ${fmtNum(r.entrada.dias,0)} dias. Preços, tarifa, sol e desempenho são hipóteses editáveis. O custo da conta tem tributos, encargos e regras de compensação; a energia solar não garante zerar a fatura. Verifique a luminosidade das LEDs e peça avaliação técnica e orçamento antes de instalar painéis. Este assistente não é canal oficial.`;
  if(perguntas.comparacao.test(p)) return `Para o mesmo serviço de iluminação, as LEDs reduzem a demanda estimada de ${fmtNum(r.atualKWh)} para ${fmtNum(r.ledKWh)} kWh/mês, por ${dinheiro(r.investimentoLed)} de investimento hipotético. Já a alternativa renovável dimensiona teoricamente ${fmtNum(r.solarKWp,2)} kWp para gerar ${fmtNum(r.atualKWh)} kWh/mês, com custo estimado de ${dinheiro(r.investimentoSolar)}. Minha sugestão é avaliar primeiro a eficiência com LED e, depois, dimensionar energia solar para o consumo real de toda a residência. Os valores não são garantidos. Fontes: Inmetro/Procel, INPE e ANEEL.`;
  if(perguntas.solar.test(p)) return `A opção solar fotovoltaica usa luz do sol como fonte renovável. Para compensar teoricamente ${fmtNum(r.atualKWh)} kWh/mês de iluminação, a simulação calcula ${fmtNum(r.solarKWp,2)} kWp, usando ${fmtNum(r.entrada.solPleno)} horas de sol pleno/dia e fator de desempenho ${fmtNum(r.entrada.fatorDesempenho,2)}. Investimento hipotético: ${dinheiro(r.investimentoSolar)}. O teto de benefício é ${dinheiro(r.solarTetoBeneficioReais)}/mês, NÃO uma economia garantida. É preciso verificar radiação local, espaço, sombreamento, orçamento e regras de compensação da ANEEL. Fonte: INPE/ANEEL.`;
  if(perguntas.led.test(p)) return `Ao trocar ${r.entrada.lampadas} lâmpadas de ${fmtNum(r.entrada.potenciaAtual,0)} W por LEDs de ${fmtNum(r.entrada.potenciaLed,0)} W, o consumo estimado cai de ${fmtNum(r.atualKWh)} para ${fmtNum(r.ledKWh)} kWh/mês. Economia: ${fmtNum(r.economiaLedKWh)} kWh e ${dinheiro(r.economiaLedReais)} por mês (${fmtNum(r.economiaLedPercentual,0)}% na iluminação). Custo inicial hipotético: ${dinheiro(r.investimentoLed)}; retorno simples: ${fmtNum(r.retornoLedMeses)} meses. Verifique equivalência em lúmens e preços reais. Fonte: MME/Procel e Inmetro.`;
  return 'Não encontrei uma orientação específica. Tente perguntar sobre LED, economia de energia, energia solar, comparação de alternativas, limitações ou fontes. Este assistente não é um canal oficial.';
}
function mostrarResposta(pergunta) {
  if (!resultado) return;
  const texto = responder(pergunta, resultado);
  $('resposta').querySelector('p').textContent = texto;
}
function atualizar(e) {
  if(e) e.preventDefault();
  try {
    const novo = calcular(receber());
    resultado = novo;
    renderizar(novo);
    $('erro').hidden = true;
    $('erro').textContent = '';
    if($('pergunta').value.trim()) mostrarResposta($('pergunta').value.trim());
  } catch(err) {
    $('erro').hidden=false;
    $('erro').textContent=err.message;
  }
}
function restaurar() {
  for(const [k,v] of Object.entries(PADRAO)) $(k).value=v;
  atualizar();
}
$('form-energia').addEventListener('submit', atualizar);
$('restaurar').addEventListener('click', restaurar);
$('form-pergunta').addEventListener('submit',e=>{
  e.preventDefault();
  const pergunta=$('pergunta').value.trim();
  if(!pergunta){$('resposta').querySelector('p').textContent='Digite sua dúvida para receber uma orientação.';return;}
  mostrarResposta(pergunta);
});
document.querySelectorAll('[data-question]').forEach(b=>b.addEventListener('click',()=>{
  $('pergunta').value=b.dataset.question;
  mostrarResposta(b.dataset.question);
}));
restaurar();
