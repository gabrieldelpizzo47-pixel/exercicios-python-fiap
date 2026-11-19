# Citizen Assist AI — Energia Consciente

**Global Solution 2026.2 — FIAP — Soluções em Energias Renováveis e Sustentáveis (SERS)**

## Integrantes
- Patrick Fernandes Martins Pais — RM 572899
- Gabriel Del Pizzo Pintor — RM 570436
- Ian Rodrigues Martins — RM 570540

## Público e problema
Público: moradores de residências, especialmente pessoas que desejam compreender o consumo de iluminação e decidir se vale a pena substituir lâmpadas ou pesquisar energia solar.

Problema: dificuldade de interpretar potência em watts, consumo em kWh, impacto na conta e alternativas de economia ou fornecimento renovável. O assistente transforma os dados em cálculos transparentes e orientações acessíveis. ODS relacionados: **ODS 7 (energia acessível e limpa), ODS 11 (cidades e comunidades sustentáveis) e ODS 12 (consumo responsável)**.

## Como executar
1. Descompacte o projeto mantendo os arquivos na mesma pasta.
2. Abra **index.html** em um navegador atualizado (Chrome, Edge ou Firefox). Não precisa de servidor nem internet para calcular; apenas os links de fontes exigem conexão.
3. Ajuste quantidade de lâmpadas, watts, horas, dias, tarifa e, opcionalmente, custos e parâmetros solares.
4. Clique em **Atualizar análise** e compare as alternativas.
5. Na parte **Pergunte ao Citizen Assist**, escreva perguntas como “quanto economizo com LED?”, “como funciona energia solar?”, “qual a melhor alternativa?” ou use os botões de perguntas sugeridas.

O site funciona sem instalar bibliotecas ou conectar uma API. O assistente tem **respostas baseadas em regras**, não uma IA generativa. A resposta incorpora os resultados calculados na hora, cita fontes e avisa sobre limitações.

## Arquivos
- `index.html` — interface acessível e estrutura da aplicação.
- `style.css` — responsividade e estilo.
- `calculos.js` — funções separadas para validação e matemática energética.
- `app.js` — integração dos resultados com o assistente de orientações.
- `dados/premissas.csv` — dados hipotéticos do cenário com unidades, origem e observações.
- `ANALISE_ENERGETICA.md` — cálculos, alternativas, custos, viabilidade e impactos ambientais.
- `REFERENCIAS.md` — fontes públicas verificáveis e limites do que elas sustentam.
- `TESTES_USUARIOS.md` — roteiro e formulário para coletar testes reais, ainda pendentes.
- `testes_calculos.js` — testes técnicos automatizados (opcional: `node testes_calculos.js`).
- `ROTEIRO_VIDEO.md` — roteiro de gravação de até 3 minutos (apoio, não precisa ir ao Portal).
- `ENTREGA_PORTAL_MODELO.txt` — preencher com os links reais; é o **único arquivo enviado ao Portal** segundo o enunciado SERS.

## Problema e comparação no mesmo período
**Necessidade comum:** manter iluminação residencial por 4 horas diárias em 30 dias com 10 lâmpadas.

- Situação inicial: 10 lâmpadas de 60 W → **72 kWh/mês**.
- Alternativa 1, eficiência: 10 LEDs de 9 W (luminosidade equivalente a verificar no rótulo) → **10,8 kWh/mês**, poupando **61,2 kWh/mês (85%)** em relação à referência.
- Alternativa 2, renovável: manter o uso original e dimensionar **teoricamente** 0,711 kWp solar para gerar 72 kWh/mês no mesmo período. A geração real depende do recurso solar local, perdas e projeto. Não é a estimativa de uma instalação viável ou uma economia garantida na fatura.

O app compara **a mesma demanda de iluminação**. Para decisões reais, primeiro verifique a substituição por LED e, depois, avalie o dimensionamento fotovoltaico para **todo o consumo da residência**. Não some a economia integral da alternativa LED com a compensação integral solar sobre a mesma base, pois seria dupla contagem.

## Origem dos dados
Todos os valores iniciais (potências, quantidade, horas, preço, tarifa, horas de sol pleno, fator de desempenho e custo de solar por kWp) são **premissas hipotéticas de exercício**, não dados medidos na casa de uma pessoa ou cotações oficiais. Podem ser alterados na interface. A forma de calcular potência/energia segue a definição física de kWh; as fontes oficiais ajudam a justificar a **metodologia e as limitações**, e não validam esses preços específicos.

- Inmetro e MME/Procel: eficiência de fontes de luz e comparação via potência e luminosidade.
- INPE/Atlas Brasileiro de Energia Solar: recurso solar varia conforme a região; **4,5 h de sol pleno** no exemplo é hipótese didática, e não um dado geolocalizado extraído do Atlas.
- ANEEL: micro/minigeração distribuída, compensação de energia e custos remanescentes; não se deve tratar energia gerada como desconto garantido na fatura.

Links, descrição e data de consulta em `REFERENCIAS.md`. Para detalhes da comparação e impactos ambientais, veja `ANALISE_ENERGETICA.md`.

## Testes
- **Automatizados:** rodar `node testes_calculos.js`. Foram executadas 12 verificações do núcleo matemático no ambiente de desenvolvimento, incluindo casos inválidos.
- **Com usuários:** ainda devem ser feitos pela equipe com pessoas reais, registrando percepção de clareza, utilidade, limitações percebidas e ajustes realizados, **sem dados pessoais**. Consulte `TESTES_USUARIOS.md`. Não relatar testes com usuários que não ocorreram.

## Limitações e ética
Protótipo acadêmico, sem coleta de dados pessoais e sem vínculo com órgão oficial. Não apresenta cotações nem medições locais. O custo solar linear por kWp pode distorcer custos de sistemas muito pequenos; exigir orçamento e análise profissional para instalação. Conta de energia não se resume ao kWh compensado: podem existir cobranças mínimas, componentes tarifárias, impostos, taxas e restrições técnicas. Equipamentos LED devem ter fluxo luminoso adequado ao ambiente, e tanto LED quanto painéis têm impactos ambientais de fabricação e descarte.

## Link do vídeo
**PENDENTE** — adicionar aqui a URL real do vídeo técnico não listado no YouTube, de no máximo 3 minutos.
