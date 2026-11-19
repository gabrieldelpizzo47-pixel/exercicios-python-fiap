/* Citizen Assist AI — núcleo matemático, sem dependências externas.
   Todos os valores-padrão são premissas DIDÁTICAS, não preços/tarifas cotados.
   Fontes e limitações: README.md e REFERENCIAS.md. */
(function (root, factory) {
  const api = factory();
  if (typeof module !== 'undefined' && module.exports) module.exports = api;
  if (root) root.CitizenCalculos = api;
})(typeof window !== 'undefined' ? window : null, function () {
  const PADRAO = Object.freeze({
    lampadas: 10, potenciaAtual: 60, potenciaLed: 9,
    horas: 4, dias: 30, tarifa: 1.00,
    precoLed: 12, solPleno: 4.5, fatorDesempenho: 0.75,
    precoSolarPorKWp: 5500
  });
  const LIMITES = Object.freeze({
    lampadas: [1, 200], potenciaAtual: [1, 1000], potenciaLed: [1, 1000],
    horas: [0.1, 24], dias: [1, 31], tarifa: [0.01, 10],
    precoLed: [0, 1000], solPleno: [1, 8], fatorDesempenho: [0.3, 1],
    precoSolarPorKWp: [100, 30000]
  });
  function validar(entrada) {
    for (const campo of Object.keys(LIMITES)) {
      const n = Number(entrada[campo]);
      const [min, max] = LIMITES[campo];
      if (!Number.isFinite(n) || n < min || n > max) {
        throw new Error(`Campo ${campo}: informe valor entre ${min} e ${max}.`);
      }
    }
    if (!Number.isInteger(Number(entrada.lampadas))) throw new Error('Número de lâmpadas precisa ser inteiro.');
    if (Number(entrada.potenciaLed) >= Number(entrada.potenciaAtual)) {
      throw new Error('Neste cenário, a potência LED deve ser menor que a atual.');
    }
  }
  function calcular(entrada) {
    validar(entrada);
    const e = Object.fromEntries(Object.keys(LIMITES).map(k => [k, Number(entrada[k])]));
    const atualKWh = e.lampadas * e.potenciaAtual * e.horas * e.dias / 1000;
    const ledKWh = e.lampadas * e.potenciaLed * e.horas * e.dias / 1000;
    const economiaLedKWh = atualKWh - ledKWh;
    const economiaLedPercentual = economiaLedKWh / atualKWh * 100;
    const custoBase = atualKWh * e.tarifa;
    const custoLed = ledKWh * e.tarifa;
    const economiaLedReais = economiaLedKWh * e.tarifa;
    const investimentoLed = e.lampadas * e.precoLed;
    const retornoLedMeses = economiaLedReais > 0 ? investimentoLed / economiaLedReais : null;
    // Potência teórica para produzir, em um período, o consumo ORIGINAL de iluminação.
    const solarKWp = atualKWh / (e.solPleno * e.fatorDesempenho * e.dias);
    const solarGeracaoKWh = solarKWp * e.solPleno * e.fatorDesempenho * e.dias;
    const investimentoSolar = solarKWp * e.precoSolarPorKWp;
    // Teto monetário simplificado, SEM garantir compensação integral na conta.
    const solarTetoBeneficioReais = Math.min(atualKWh, solarGeracaoKWh) * e.tarifa;
    const retornoSolarTeoricoMeses = solarTetoBeneficioReais > 0 ? investimentoSolar / solarTetoBeneficioReais : null;
    return { entrada: e, atualKWh, ledKWh, economiaLedKWh, economiaLedPercentual,
      custoBase, custoLed, economiaLedReais, investimentoLed, retornoLedMeses,
      solarKWp, solarGeracaoKWh, investimentoSolar, solarTetoBeneficioReais,
      retornoSolarTeoricoMeses };
  }
  return { PADRAO, LIMITES, calcular, validar };
});
