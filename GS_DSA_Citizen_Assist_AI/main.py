
import unicodedata


def chave_alfabetica(texto: str) -> str:
    """Ignora acentos e diferenças de maiúsculas na ordenação."""
    normalizado = unicodedata.normalize("NFD", texto.casefold())
    return "".join(letra for letra in normalizado if unicodedata.category(letra) != "Mn")


class Registro:
    def __init__(self, identificador: int, titulo: str, categoria: str,
                 descricao: str, requisitos: str, local: str):
        self.identificador = identificador
        self.titulo = titulo
        self.categoria = categoria
        self.descricao = descricao
        self.requisitos = requisitos
        self.local = local


class No:
    def __init__(self, registro: Registro):
        self.registro = registro
        self.proximo = None


class ListaEncadeada:
    def __init__(self):
        self.inicio = None
        self.fim = None
        self.tamanho = 0

    def inserir(self, registro: Registro) -> bool:
        """Verifica ID em O(n), depois insere no final em O(1)."""
        if self.consultar(registro.identificador) is not None:
            return False
        novo = No(registro)
        if self.inicio is None:
            self.inicio = novo
        else:
            self.fim.proximo = novo
        self.fim = novo
        self.tamanho += 1
        return True

    def consultar(self, identificador: int):
        """Busca linear pelo ID, O(n) no pior caso."""
        atual = self.inicio
        while atual is not None:
            if atual.registro.identificador == identificador:
                return atual.registro
            atual = atual.proximo
        return None

    def pesquisar(self, termo: str, atributo: str = "titulo") -> list:
        """Pesquisa linear por trecho do título ou da categoria (sem diferenciar maiúsculas)."""
        if atributo not in ("titulo", "categoria"):
            raise ValueError("Atributo de pesquisa inválido")
        resultados = []
        atual = self.inicio
        termo = termo.casefold().strip()
        if not termo:
            return resultados
        while atual is not None:
            valor = getattr(atual.registro, atributo).casefold()
            if termo in valor:
                resultados.append(atual.registro)
            atual = atual.proximo
        return resultados

    def atualizar(self, identificador: int, titulo=None, categoria=None,
                  descricao=None, requisitos=None, local=None) -> bool:
        registro = self.consultar(identificador)
        if registro is None:
            return False
        alteracoes = {
            "titulo": titulo, "categoria": categoria, "descricao": descricao,
            "requisitos": requisitos, "local": local,
        }
        for nome, valor in alteracoes.items():
            if valor is not None and valor.strip():
                setattr(registro, nome, valor.strip())
        return True

    def excluir(self, identificador: int) -> bool:
        """Remove nó, religando referências; O(n) no pior caso."""
        atual = self.inicio
        anterior = None
        while atual is not None:
            if atual.registro.identificador == identificador:
                if anterior is None:
                    self.inicio = atual.proximo
                else:
                    anterior.proximo = atual.proximo
                if atual is self.fim:
                    self.fim = anterior
                self.tamanho -= 1
                return True
            anterior, atual = atual, atual.proximo
        return False

    def listar(self) -> list:
        registros = []
        atual = self.inicio
        while atual is not None:
            registros.append(atual.registro)
            atual = atual.proximo
        return registros

    def ordenar_por_titulo(self) -> None:
        """Selection Sort sobre nós da lista, O(n²) tempo e O(1) memória extra.

        Troca os registros entre os nós, preservando as ligações da lista.
        """
        i = self.inicio
        while i is not None:
            menor = i
            j = i.proximo
            while j is not None:
                chave_j = (chave_alfabetica(j.registro.titulo), j.registro.identificador)
                chave_menor = (chave_alfabetica(menor.registro.titulo), menor.registro.identificador)
                if chave_j < chave_menor:
                    menor = j
                j = j.proximo
            if menor is not i:
                i.registro, menor.registro = menor.registro, i.registro
            i = i.proximo

    def contar_por_categoria(self) -> dict:
        contagem = {}
        atual = self.inicio
        while atual is not None:
            categoria = atual.registro.categoria
            contagem[categoria] = contagem.get(categoria, 0) + 1
            atual = atual.proximo
        return contagem


def mostrar_registro(registro: Registro) -> None:
    print(f"\nID: {registro.identificador} | {registro.titulo}")
    print(f"Categoria: {registro.categoria}")
    print(f"Descrição: {registro.descricao}")
    print(f"Requisitos/orientações: {registro.requisitos}")
    print(f"Canal/local de consulta: {registro.local}")


def ler_inteiro_positivo(rotulo: str):
    entrada = input(rotulo).strip()
    try:
        numero = int(entrada)
        if numero <= 0:
            raise ValueError
        return numero
    except ValueError:
        print("Entrada inválida: digite um número inteiro positivo.")
        return None


def ler_texto_obrigatorio(rotulo: str):
    texto = input(rotulo).strip()
    if not texto:
        print("Campo obrigatório não pode ficar vazio.")
        return None
    return texto


def cadastrar(lista: ListaEncadeada):
    identificador = ler_inteiro_positivo("Identificador (inteiro positivo): ")
    if identificador is None:
        return
    if lista.consultar(identificador) is not None:
        print("Erro: já existe um registro com este identificador.")
        return
    campos = {}
    for campo, rotulo in (
        ("titulo", "Título: "),
        ("categoria", "Categoria: "),
        ("descricao", "Descrição: "),
        ("requisitos", "Requisitos/orientações: "),
        ("local", "Canal/local de consulta: "),
    ):
        valor = ler_texto_obrigatorio(rotulo)
        if valor is None:
            return
        campos[campo] = valor
    lista.inserir(Registro(identificador, **campos))
    print("Registro cadastrado com sucesso!")


def menu(lista: ListaEncadeada):
    while True:
        print("\n" + "=" * 52)
        print("CITIZEN ASSIST AI — INFORMAÇÕES AO CIDADÃO")
        print("=" * 52)
        print("1 - Cadastrar registro")
        print("2 - Consultar por ID")
        print("3 - Pesquisar por título ou categoria")
        print("4 - Atualizar registro")
        print("5 - Excluir registro")
        print("6 - Listar registros")
        print("7 - Ordenar registros por título (Selection Sort)")
        print("8 - Análise: quantidade por categoria")
        print("0 - Encerrar")
        opcao = input("Escolha uma opção: ").strip()

        if opcao == "0":
            print("Programa encerrado. Obrigado!")
            break
        elif opcao == "1":
            cadastrar(lista)
        elif opcao == "2":
            identificador = ler_inteiro_positivo("ID para consulta: ")
            if identificador is not None:
                registro = lista.consultar(identificador)
                if registro is None:
                    print("Nenhum registro encontrado com esse ID.")
                else:
                    mostrar_registro(registro)
        elif opcao == "3":
            tipo = input("Pesquisar (1) título ou (2) categoria? ").strip()
            if tipo not in ("1", "2"):
                print("Opção de pesquisa inválida.")
                continue
            termo = ler_texto_obrigatorio("Digite a palavra-chave: ")
            if termo is None:
                continue
            encontrados = lista.pesquisar(termo, "titulo" if tipo == "1" else "categoria")
            if not encontrados:
                print("Nenhum registro corresponde à pesquisa.")
            else:
                print(f"Foram encontrados {len(encontrados)} registro(s):")
                for registro in encontrados:
                    mostrar_registro(registro)
        elif opcao == "4":
            identificador = ler_inteiro_positivo("ID para atualizar: ")
            if identificador is None:
                continue
            registro = lista.consultar(identificador)
            if registro is None:
                print("Registro não encontrado.")
                continue
            mostrar_registro(registro)
            print("Digite novos valores. Enter mantém o valor atual.")
            atualizacoes = {}
            for campo, rotulo in (
                ("titulo", "Novo título: "),
                ("categoria", "Nova categoria: "),
                ("descricao", "Nova descrição: "),
                ("requisitos", "Novos requisitos/orientações: "),
                ("local", "Novo canal/local: "),
            ):
                texto = input(rotulo).strip()
                atualizacoes[campo] = texto if texto else None
            lista.atualizar(identificador, **atualizacoes)
            print("Registro atualizado com sucesso!")
        elif opcao == "5":
            identificador = ler_inteiro_positivo("ID para excluir: ")
            if identificador is None:
                continue
            if lista.excluir(identificador):
                print("Registro excluído com sucesso!")
            else:
                print("Registro não encontrado.")
        elif opcao == "6":
            registros = lista.listar()
            if not registros:
                print("A lista está vazia.")
            else:
                print(f"Total: {lista.tamanho} registro(s)")
                for registro in registros:
                    mostrar_registro(registro)
        elif opcao == "7":
            lista.ordenar_por_titulo()
            print("Registros ordenados por título (Selection Sort).")
            for registro in lista.listar():
                print(f"  {registro.identificador}: {registro.titulo}")
        elif opcao == "8":
            print(f"Total de serviços/orientações: {lista.tamanho}")
            categorias = lista.contar_por_categoria()
            if not categorias:
                print("Nenhum registro para analisar.")
            else:
                for categoria, quantidade in categorias.items():
                    print(f"  {categoria}: {quantidade}")
        else:
            print("Opção inválida. Escolha uma opção de 0 a 8.")


def carregar_exemplos(lista: ListaEncadeada):
    """Exemplos didáticos; NÃO constituem informações oficiais de serviços."""
    exemplos = [
        Registro(101, "Coleta seletiva", "Serviços urbanos",
                 "Orientações gerais para separação de resíduos recicláveis.",
                 "Verificar dias, materiais e regras da coleta na prefeitura local.",
                 "Portal oficial da prefeitura do município"),
        Registro(102, "Economia de energia", "Sustentabilidade",
                 "Dicas gerais de uso consciente de eletricidade.",
                 "Verificar consumo e potência dos aparelhos e comparar alternativas.",
                 "Concessionária e materiais oficiais sobre eficiência energética"),
        Registro(103, "Descarte de eletrônicos", "Serviços urbanos",
                 "Orientações para buscar locais adequados de descarte.",
                 "Consultar pontos de entrega habilitados na região.",
                 "Portal oficial da prefeitura e programas de logística reversa"),
        Registro(104, "Cursos de qualificação", "Educação",
                 "Orientações gerais sobre como procurar cursos públicos.",
                 "Confirmar requisitos, vagas e calendário no órgão responsável.",
                 "Portal oficial da instituição ofertante"),
    ]
    for registro in exemplos:
        lista.inserir(registro)


if __name__ == "__main__":
    base = ListaEncadeada()
    carregar_exemplos(base)
    print("AVISO: registros iniciais são exemplos didáticos, não canais oficiais.")
    print("Consulte sempre a instituição responsável antes de agir.")
    menu(base)
