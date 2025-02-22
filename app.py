import flet as ft
from models import Cadastro, Produto, ListarProdutos

def main(page: ft.Page):

    retorno_cadastro = ft.Text()
    lista_produtos = ft.ListView(expand=True)

    def RenderizarListaDeProdutos():
        lista_produtos.controls.clear()
        for p in ListarProdutos():
            lista_produtos.controls.append(
                ft.Container(
                    ft.Text(p.nome),
                    alignment=ft.alignment.center,
                    bgcolor=ft.colors.BLACK,
                    padding= 10,
                    margin=5,
                    border_radius=10
                )
            )
        lista_produtos.update()

    def Cadastrar(e):
        try:
            novo_produto = Produto(nome=nome.value, preco=float(preco.value))
            Cadastro(novo_produto)
            retorno_cadastro.value = f'{nome.value} cadastrado com sucesso!'
            RenderizarListaDeProdutos()
        except Exception as e:
            retorno_cadastro.value = f'Erro ao cadastrar: {str(e)}'
        page.update()

    page.title = 'Gerenciamento de Produtos'
    titulo_produtos = ft.Text('Produtos')
    titulo_cadastro = ft.Text('Cadastro de produto')
    nome = ft.TextField(label='Nome', text_align=ft.TextAlign.LEFT)
    preco = ft.TextField(label='Preço', text_align=ft.TextAlign.LEFT)
    btn_cadastro = ft.ElevatedButton('Cadastrar', on_click=Cadastrar)

    page.add(
        titulo_produtos,
        lista_produtos,
        titulo_cadastro,
        nome,
        preco,
        btn_cadastro,
        retorno_cadastro
    )

    RenderizarListaDeProdutos()
    
ft.app(target=main)