class Carro:

    def __init__(self, request):
        self.request = request
        self.session = request.session

        carro = self.session.get('carro')

        if not carro:
            carro = self.session['carro'] = {}

        self.carro = carro

    def guardar_carro(self):
        self.session['carro'] = self.carro
        self.session.modified = True


    def adicionar(self, produto):

        produto_id = str(produto.id)

        if produto_id not in self.carro:

            imagem = produto.imagem.url if produto.imagem else ''

            self.carro[produto_id] = {
                "produto_id": produto.id,
                "nome": produto.nome,
                "preco": str(produto.preco),
                "quantidade": 1,
                "imagem": imagem
            }

        else:
            self.carro[produto_id]["quantidade"] += 1

        self.guardar_carro()


    def eliminar(self, produto):
        produto_id = str(produto.id)

        if produto_id in self.carro:
            del self.carro[produto_id]
            self.guardar_carro()

    def diminuir(self, produto):
        produto_id = str(produto.id)

        self.carro[produto_id]["quantidade"] -= 1

        if self.carro[produto_id]["quantidade"] < 1:
            self.eliminar(produto)
        else:
            self.guardar_carro()

    def limpar_carro(self):
        # Esvazia o carrinho que está na sessão
        self.session['carro'] = {}

        # Avisa que a sessão foi alterada
        self.session.modified = True