# Evidências de testes — Citizen Assist AI (DSA)

**Método de teste:** testes automatizados com `unittest` da biblioteca padrão Python. Os testes usam a própria classe `ListaEncadeada`, e também validam entradas simuladas pelo menu. Não substituem a demonstração interativa solicitada pela disciplina.

## Cenários, resultados esperados e observados
| Caso | Situação testada | Resultado esperado | Resultado observado |
|---|---|---|---|
| T01 | Lista vazia: listar, consultar e excluir | Lista vazia, consulta inexistente, exclusão falha sem erro | **Aprovado** |
| T02 | Inserir dois registros com mesmo ID | Segundo cadastro recusado, tamanho não aumenta | **Aprovado** |
| T03 | Buscar por ID, título e categoria; procurar inexistente | Retorna registros correspondentes ou nenhum resultado | **Aprovado** |
| T04 | Atualizar registro existente e inexistente | Atualiza campos do existente; rejeita inexistente | **Aprovado** |
| T05 | Excluir nós do início, meio e fim; excluir último | Mantém sequência íntegra, limpa início/fim e permite reinserir | **Aprovado** |
| T06 | Ordenar títulos com Selection Sort | Ordem alfabética e preservação de IDs/registros | **Aprovado** |
| T07 | Contar categorias | Contagens corretas e total preservado | **Aprovado** |
| T08 | Informar ID não numérico (`abc`) | Mensagem de erro, nenhuma operação indevida | **Aprovado** |
| T09 | Informar ID zero (`0`) | Mensagem de inteiro positivo obrigatório | **Aprovado** |
| T10 | Informar campo obrigatório vazio | Rejeita texto em branco | **Aprovado** |
| T11 | Menu: opção inválida, listar vazio e sair | Mostra mensagens adequadas e encerra normalmente | **Aprovado** |

**Execução realizada:** `python testes.py`.

**Resultado registrado:** `Ran 11 tests ... OK` (11 testes executados, 11 aprovados). A saída individual está no arquivo `resultado_testes.txt` e pode ser reproduzida localmente.

## Evidências visuais para a demonstração
Para complementar os testes automatizados, durante a gravação ou apresentação do grupo faça capturas da tela mostrando:

1. **Inserção** de um registro novo e erro de ID duplicado.
2. **Busca** por ID/categoria e mensagem quando não há resultados.
3. **Atualização** e **exclusão** com nova consulta para confirmar a alteração.
4. **Ordenação** antes e depois e trecho do código do `Selection Sort`.
5. **Análise** com quantidade por categoria e execução de `python testes.py` com todos aprovados.

Não foram adicionadas capturas artificiais: as imagens devem ser obtidas durante a execução real na máquina do grupo.

## Limitações
Os dados iniciais são exemplos didáticos. Não há validação de serviços públicos reais ou armazenamento permanente. A demonstração deve apresentar o comportamento real dos métodos e suas referências entre os nós, conforme o enunciado.
