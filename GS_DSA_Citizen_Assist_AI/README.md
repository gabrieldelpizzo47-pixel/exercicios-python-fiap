# Citizen Assist AI — Central de Informações ao Cidadão

**Global Solution 2026.2 — Data Structures and Algorithms (DSA) — FIAP 1CC**

## Integrantes
- **Patrick Fernandes Martins Pais** — RM 572899
- **Gabriel Del Pizzo Pintor** — RM 570436
- **Ian Rodrigues Martins** — RM 570540

## 1. Problema e público
Pessoas que precisam localizar orientações sobre serviços urbanos, educação e sustentabilidade podem ter dificuldade para organizar essas informações e encontrar uma resposta rapidamente. O protótipo reúne registros consultáveis por identificador, título ou categoria.

**Importante:** os registros iniciais foram criados **somente como exemplos didáticos**. Eles não representam cadastro oficial de serviços públicos. Antes de utilizar uma orientação na prática, deve-se consultar o órgão responsável. O sistema não coleta dados pessoais do usuário nem se apresenta como canal oficial.

## 2. Objetivo
Demonstrar, em Python, a implementação manual de uma **lista simplesmente encadeada**, operações **CRUD**, **busca linear**, **Selection Sort**, validação de entradas e análise de registros. O trabalho é um assistente introdutório **baseado em menus e consultas**, sem IA generativa, conforme permitido no enunciado da disciplina.

## 3. Como executar
Requisito: **Python 3.9+**. Não há dependências externas.

1. Baixe os arquivos deste repositório para uma mesma pasta.
2. Abra a pasta no VS Code ou em um terminal.
3. Execute:

   ```bash
   python main.py
   ```

   No Windows, se `python` não funcionar, tente `py main.py`.
4. Digite o número da opção desejada e siga as instruções.

O sistema inicia com **quatro exemplos didáticos** para facilitar testes e demonstração. Os dados ficam **em memória enquanto o programa estiver aberto**; a persistência em arquivo não é exigida nesta atividade.

## 4. Funcionalidades e menu
| Opção | Funcionalidade |
|---|---|
| 1 | Cadastrar registro, com ID único |
| 2 | Consultar registro por ID |
| 3 | Pesquisar registros por trecho do título ou categoria |
| 4 | Atualizar campos de um registro existente |
| 5 | Excluir registro, religando os nós |
| 6 | Percorrer e listar todos os registros |
| 7 | Ordenar alfabeticamente pelo título com Selection Sort |
| 8 | Exibir total de registros e quantidade por categoria |
| 0 | Encerrar o programa |

Tratamento de erros: ID repetido, ID não positivo, opção inexistente, campos obrigatórios vazios, consultas sem resultados, atualizações/exclusões inexistentes e lista vazia.

## 5. Modelo dos dados
Cada objeto `Registro` tem seis atributos:
- `identificador` (inteiro positivo único)
- `titulo` (texto)
- `categoria` (texto)
- `descricao` (texto)
- `requisitos` (texto)
- `local` (texto, com orientações de onde consultar)

A classe `No` contém um `registro` e a referência `proximo`. A classe `ListaEncadeada` mantém referências `inicio` e `fim`, além do contador `tamanho`.

Exemplo conceitual da estrutura:

```text
inicio -> [Registro 101 | próximo] -> [Registro 102 | próximo] -> [Registro 103 | None] <- fim
```

Cada novo nó é anexado ao final, a remoção religa a cadeia e a ordenação troca os **registros** entre os nós, preservando as referências de encadeamento.

## 6. Algoritmos implementados pela equipe
**Busca linear:** o código percorre a lista nó a nó a partir de `inicio` até encontrar o ID ou chegar a `None`. Para pesquisar por título ou categoria, visita cada registro e compara a palavra-chave sem diferenciar maiúsculas e minúsculas. Se nada for encontrado, retorna `None` ou lista vazia e o menu apresenta uma mensagem clara.

**Selection Sort:** a partir de cada nó, procura o menor título na parte ainda não ordenada, depois troca os objetos `Registro` armazenados nos dois nós. Repete até o final. A comparação normaliza acentos para uma ordenação mais natural em português. **Não utiliza `sort()` nem `sorted()`.**

### 6.1. Análise de complexidade Big-O
Considere `n` como a quantidade de registros; para simplificar, o tamanho dos textos é limitado.

| Operação | Tempo no pior caso | Justificativa |
|---|---|---|
| Inserção com ID único | **O(n)** | Confere antes se o ID já existe (busca linear). Após validar, anexar usando `fim` custa O(1). |
| Consulta por ID | **O(n)** | Pode percorrer todos os nós até encontrar o ID ou terminar. |
| Pesquisa por título/categoria | **O(n)** | Percorre todos os registros uma vez. |
| Atualização | **O(n)** | Localiza o registro e troca apenas seus campos. |
| Remoção por ID | **O(n)** | Procura o nó e religa as referências; a religação é O(1). |
| Listagem e contagem por categoria | **O(n)** | Percorrem todos os nós uma vez. |
| Selection Sort | **O(n²)** | Dois percursos encadeados para selecionar repetidamente o menor título. |

**Memória:** a lista ocupa **O(n)** no total. A busca por ID, remoção e o Selection Sort utilizam **O(1)** de memória auxiliar (além dos textos). A pesquisa/listagem criam listas de resultados com até **O(n)** elementos; a contagem usa espaço proporcional ao número de categorias.

## 7. Testes e evidências
O arquivo `testes.py` contém testes automatizados, incluindo lista vazia, inserção e duplicidade, busca encontrada/não encontrada, atualização, exclusão (início/meio/fim/único), ordenação, contagem e entradas inválidas.

Execute:

```bash
python testes.py
```

O arquivo `EVIDENCIAS_TESTES.md` explica os casos testados e inclui o resultado observado. O registro completo de execução está em `resultado_testes.txt`.

## 8. Demonstração prática sugerida
Durante a apresentação, execute `main.py` e mostre **o funcionamento do algoritmo**, não apenas a interface:

1. Liste os registros iniciais (opção **6**) e consulte o ID **102** (opção **2**).
2. Pesquise `urb` na categoria (opção **3**) e mostre os resultados.
3. Cadastre um registro novo com ID **105** (opção **1**) e consulte-o.
4. Atualize o título do ID **105** (opção **4**).
5. Ordene por título (opção **7**) e explique os dois laços de Selection Sort no código.
6. Exiba as quantidades por categoria (opção **8**).
7. Exclua o ID **105** (opção **5**) e comprove que a consulta já não o encontra.
8. Tente consultar ID inexistente e inserir ID duplicado, para demonstrar validações.

### Evidência das estruturas
No código, mostre rapidamente os métodos `inserir`, `consultar`, `excluir` e `ordenar_por_titulo`, destacando as referências `inicio`, `proximo` e `fim`. Isso demonstra que a lista encadeada e o algoritmo foram realmente implementados.

## 9. Arquivos
- `main.py` — sistema completo e menu interativo.
- `testes.py` — testes automatizados sem dependências externas.
- `EVIDENCIAS_TESTES.md` — casos, critérios, resultados e instruções de captura.
- `resultado_testes.txt` — saída real de uma execução dos testes.
- `README.md` — descrição, execução, técnicas e análise Big-O.

## 10. Limitações e possíveis extensões
- Dados apenas em memória: o programa não salva alterações ao encerrar.
- Exemplos iniciais são ilustrativos e **não verificados como serviços públicos reais**.
- Pode ser estendido com persistência de arquivos, fontes oficiais verificadas ou interface web, mas isso não é necessário para os requisitos centrais de DSA.
