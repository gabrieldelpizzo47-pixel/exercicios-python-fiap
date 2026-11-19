# Relatório energético — Citizen Assist AI

**Disciplina:** Soluções em Energias Renováveis e Sustentáveis — Global Solution FIAP 2026.2  
**Público:** moradores de residências que desejam economizar energia na iluminação.  
**Pergunta:** para a *mesma necessidade de iluminar 10 pontos por 4 h/dia durante 30 dias*, o que muda ao instalar lâmpadas LED ou optar pela geração solar fotovoltaica?

## 1. Dados e premissas

| Variável | Valor do exemplo | Unidade | Situação |
|---|---:|---|---|
| Quantidade de lâmpadas | 10 | unidades | Estimativa didática |
| Potência por lâmpada atual | 60 | W | Hipótese de referência |
| Potência por LED | 9 | W | Hipótese; validar luminosidade (lúmens) |
| Funcionamento | 4 | h/dia | Hipótese de uso |
| Período de referência | 30 | dias | Mês padronizado |
| Tarifa efetiva adotada | 1,00 | R$/kWh | Hipótese, NÃO tarifa real |
| Preço unitário LED | 12,00 | R$ | Hipótese, NÃO cotação |
| Horas equivalentes de sol pleno | 4,5 | h/dia | Hipótese; não é média local medida |
| Fator de desempenho fotovoltaico | 0,75 | adimensional | Hipótese de perdas no sistema |
| Custo hipotético de fotovoltaico | 5.500,00 | R$/kWp | Hipótese linear; pode ser inadequada a sistemas pequenos |

Todos os valores iniciais são **estimativas exemplificativas**. São configuráveis na aplicação. A metodologia é ancorada em referências públicas reunidas em `REFERENCIAS.md`.

## 2. Cálculos reproduzíveis

Fórmula de consumo: **Energia (kWh) = quantidade × potência (W) ÷ 1000 × horas/dia × dias**.

**Referência — iluminação atual:**

`10 × (60 ÷ 1000) × 4 × 30 = 72,0 kWh/mês`.

Custo energético estimado: `72 × R$1,00/kWh = R$72,00/mês` (somente componente simplificada do consumo de iluminação).

**Alternativa 1 — troca por LED:**

`10 × (9 ÷ 1000) × 4 × 30 = 10,8 kWh/mês`.

Economia `72 − 10,8 = 61,2 kWh/mês` ou `61,2/72 × 100 = 85%`.

Economia teórica simplificada: `61,2 × R$1,00 = R$61,20/mês`, `R$734,40/ano` para 12 meses iguais.

Investimento hipotético: `10 × R$12 = R$120,00`.

Retorno simples ilustrativo: `120/61,2 = 1,96 meses`, ignorando substituições, tributos, reajustes, mão de obra e diferenças de luminosidade.

**Alternativa 2 — solar fotovoltaica para a demanda ORIGINAL:**

Modelo simplificado de geração: `Geração (kWh/mês) = potência instalada (kWp) × horas de sol pleno/dia × fator de desempenho × dias`.

Potência teórica requerida: `72 / (4,5 × 0,75 × 30) = 0,7111 kWp`.

Geração teórica: `0,7111 × 4,5 × 0,75 × 30 ≈ 72 kWh/mês`.

Custo extremamente simplificado: `0,7111 × R$5.500/kWp ≈ R$3.911,11`. Esta linearidade pode ser irrealista em sistemas tão pequenos.

Teto de valor energético equivalente: `72 × R$1,00 = até R$72,00/mês` **antes de** tarifas remanescentes, cobrança mínima, regras de compensação, períodos com geração/consumo descompassados e demais despesas. NÃO equivale a desconto real garantido. O retorno calculado pelo programa como hipótese **não serve para projeto financeiro**.

### Comparação padronizada — 30 dias, mesma necessidade

| Indicador | Referência atual | Alternativa 1: LED | Alternativa 2: solar* |
|---|---:|---:|---:|
| Energia requerida para iluminação | 72,0 kWh | 10,8 kWh | 72,0 kWh |
| Redução real de demanda | 0 | 61,2 kWh | 0 (geração, não eficiência) |
| Geração própria renovável estimada | 0 | 0 | 72,0 kWh |
| Energia teórica líquida da rede, somente para iluminação | 72,0 | 10,8 | 0* |
| Custo inicial hipotético | R$0 | R$120 | R$3.911,11* |
| Benefício financeiro energético hipotético/mês | R$0 | R$61,20 | até R$72,00* |

\* Não existe instalação projetada, orçamento, medição local ou garantia de compensação total. Energia teórica líquida da rede zero NÃO significa fatura zero. Esta é uma comparação de conceitos, não uma proposta comercial de fotovoltaico.

## 3. Viabilidade e impactos ambientais

**LED — eficiência:** investimento inicial baixo no cenário; substituição geralmente simples; reduz demanda elétrica e desperdício. Entretanto, é necessário escolher a luminosidade (fluxo luminoso em lúmens), tonalidade, qualidade e vida útil adequadas. A produção e descarte de componentes eletrônicos têm impactos ambientais.

**Solar — fonte renovável:** gera eletricidade sem combustão local durante operação e pode reduzir energia comprada da rede em determinadas condições. Porém exige radiação local suficiente, espaço, estrutura, instalação, homologação, avaliação da distribuidora, manutenção, orçamento e análise tarifária. Fabricação de módulos e inversores, uso de materiais e descarte também geram impactos. O caso demonstra **geração**, e não redução do consumo físico da iluminação.

**Recomendação:** começar por redução de desperdício e LED quando a iluminação atual for ineficiente; depois dimensionar geração solar com o consumo pós-eficiência de **toda a residência**, tarifa real e dados de radiação local (INPE), com profissional habilitado. A alternativa mais viável pode variar conforme o contexto.

## 4. Integração ao assistente

O app lê os valores numéricos preenchidos pelo usuário, chama `calcular()` em `calculos.js` e atualiza cards e gráfico comparativo. O módulo `app.js` classifica perguntas por palavras-chave e monta orientações dinâmicas com os resultados:

- “Quanto economizo com LED?” → consumo anterior, novo consumo, economia em kWh/R$, investimento ilustrativo, limitações e referência.
- “Como funciona energia solar?” → potência teórica, geração estimada, custo hipotético, regras da ANEEL e referência ao INPE.
- “Qual a melhor alternativa?” → comparação para a mesma necessidade e recomendação condicionada.
- “Quais os limites?” e “Quais as fontes?” → transparência e consulta às fontes.
- Perguntas fora do escopo → informa que não encontrou orientação; não inventa resultado.

Nenhuma mensagem usa dados pessoais ou cria a impressão de serviço público oficial.

## 5. Testes e próximos passos

Foram verificados automaticamente 12 casos de cálculos e entradas inválidas (`node testes_calculos.js`). Testes reais com cidadãos precisam ser feitos e documentados em `TESTES_USUARIOS.md` antes da entrega. A equipe deverá registrar as dúvidas, o entendimento, comentários e ajustes efetivamente feitos, sem nomes ou contatos.

## 6. Referências

Consulte `REFERENCIAS.md` para URLs, assuntos e limites de cada fonte.
