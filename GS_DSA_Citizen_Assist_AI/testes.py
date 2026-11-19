"""Testes automatizados da estrutura e dos algoritmos. Executar: python testes.py"""
from unittest import TestCase, main
from unittest.mock import patch
from io import StringIO
from main import ListaEncadeada, Registro, ler_inteiro_positivo, ler_texto_obrigatorio, menu


def novo_registro(identificador, titulo, categoria="Serviços urbanos"):
    return Registro(identificador, titulo, categoria, "Descrição de teste", "Confirmar dados", "Portal oficial")


class TestesListaEncadeada(TestCase):
    def setUp(self):
        self.lista = ListaEncadeada()

    def test_lista_vazia_e_consulta_inexistente(self):
        self.assertEqual(self.lista.listar(), [])
        self.assertIsNone(self.lista.consultar(99))
        self.assertFalse(self.lista.excluir(99))
        self.assertEqual(self.lista.contar_por_categoria(), {})
        self.lista.ordenar_por_titulo()
        self.assertEqual(self.lista.tamanho, 0)

    def test_insercao_e_id_duplicado(self):
        self.assertTrue(self.lista.inserir(novo_registro(1, "Água")))
        self.assertFalse(self.lista.inserir(novo_registro(1, "Energia")))
        self.assertEqual(self.lista.tamanho, 1)

    def test_busca_por_id_e_texto(self):
        self.lista.inserir(novo_registro(1, "Coleta seletiva", "Sustentabilidade"))
        self.lista.inserir(novo_registro(2, "Curso gratuito", "Educação"))
        self.assertEqual(self.lista.consultar(1).titulo, "Coleta seletiva")
        self.assertEqual(len(self.lista.pesquisar("COLETA", "titulo")), 1)
        self.assertEqual(len(self.lista.pesquisar("educa", "categoria")), 1)
        self.assertEqual(self.lista.pesquisar("inexistente"), [])

    def test_atualizar(self):
        self.assertFalse(self.lista.atualizar(9, titulo="Teste"))
        self.lista.inserir(novo_registro(1, "Antes"))
        self.assertTrue(self.lista.atualizar(1, titulo="Depois"))
        self.assertEqual(self.lista.consultar(1).titulo, "Depois")
        self.assertEqual(self.lista.tamanho, 1)

    def test_excluir_inicio_meio_fim_e_unico(self):
        for i in (1, 2, 3, 4):
            self.lista.inserir(novo_registro(i, str(i)))
        self.assertTrue(self.lista.excluir(1))
        self.assertTrue(self.lista.excluir(3))
        self.assertTrue(self.lista.excluir(4))
        self.assertEqual([r.identificador for r in self.lista.listar()], [2])
        self.assertTrue(self.lista.excluir(2))
        self.assertEqual(self.lista.tamanho, 0)
        self.assertIsNone(self.lista.inicio)
        self.assertIsNone(self.lista.fim)
        self.assertTrue(self.lista.inserir(novo_registro(5, "Novo")))

    def test_selection_sort_e_integridade_dos_ids(self):
        self.lista.inserir(novo_registro(2, "Zoológico"))
        self.lista.inserir(novo_registro(3, "Água"))
        self.lista.inserir(novo_registro(1, "Coleta"))
        self.lista.ordenar_por_titulo()
        self.assertEqual([r.titulo for r in self.lista.listar()], ["Água", "Coleta", "Zoológico"])
        self.assertEqual({r.identificador for r in self.lista.listar()}, {1, 2, 3})
        self.assertEqual(self.lista.tamanho, 3)

    def test_contagem_categoria(self):
        self.lista.inserir(novo_registro(1, "A", "Urbanos"))
        self.lista.inserir(novo_registro(2, "B", "Urbanos"))
        self.lista.inserir(novo_registro(3, "C", "Educação"))
        self.assertEqual(self.lista.contar_por_categoria(), {"Urbanos": 2, "Educação": 1})

    @patch("builtins.input", return_value="abc")
    def test_entrada_numerica_invalida(self, _):
        with patch("sys.stdout", new_callable=StringIO):
            self.assertIsNone(ler_inteiro_positivo("ID: "))

    @patch("builtins.input", return_value="0")
    def test_id_zero_invalido(self, _):
        with patch("sys.stdout", new_callable=StringIO):
            self.assertIsNone(ler_inteiro_positivo("ID: "))

    @patch("builtins.input", return_value="   ")
    def test_campo_obrigatorio_vazio(self, _):
        with patch("sys.stdout", new_callable=StringIO):
            self.assertIsNone(ler_texto_obrigatorio("Título: "))

    @patch("builtins.input", side_effect=["x", "6", "0"])
    def test_menu_opcao_invalida_lista_vazia_e_sair(self, _):
        with patch("sys.stdout", new_callable=StringIO) as captura:
            menu(self.lista)
        self.assertIn("Opção inválida", captura.getvalue())
        self.assertIn("A lista está vazia", captura.getvalue())
        self.assertIn("Programa encerrado", captura.getvalue())


if __name__ == "__main__":
    main(verbosity=2)
