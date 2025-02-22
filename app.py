import flet as ft
from models import Cadastro, Produto

def main(page: ft.Page):

    def cadastrar(e):
        try:
            novo_produto = Produto(nome=nome.value, preco=preco.value)
            Cadastro(novo_produto)
            print(f'{nome.value} cadastrado com sucesso!')
        except Exception as e:
            print(f'Erro ao cadastrar: {str(e)}')

    page.title = 'Gerenciamento de Produtos'
    titulo = ft.Text('Cadastro de produto')
    nome = ft.TextField(label='Nome', text_align=ft.TextAlign.LEFT)
    preco = ft.TextField(label='Preço', text_align=ft.TextAlign.LEFT)
    btn_cadastro = ft.ElevatedButton('Cadastrar', on_click=cadastrar)
    page.add(titulo, nome, preco, btn_cadastro)

ft.app(target=main)