from django.shortcuts import render

atores = [

    {
        "id": 1,
        "nome": "Millie Bobby Brown",
        "idade": "21 anos",
        "posição": "Eleven",
        "nascimento": "19 de fevereiro de 2004",
        "imagem": "website/img/millie.jpg",
        "conteudo": "Millie é uma atriz britânica que se tornou um fenômeno global ainda criança. Além de atuar, ela também é empresária e já foi indicada ao Emmy."
    },

    {
        "id": 2,
        "nome": "Finn Wolfhard",
        "idade": "22 anos",
        "posição": "Mike Wheeler",
        "nascimento": "23 de dezembro de 2002",
        "imagem": "website/img/finn.jpg",
        "conteudo": "Finn é ator e músico canadense. Participou de filmes como It: A Coisa e também é vocalista da banda The Aubreys."
    },

    {
        "id": 3,
        "nome": "Noah Schnapp",
        "idade": "20 anos",
        "posição": "Will Byers",
        "nascimento": "3 de outubro de 2004",
        "imagem": "website/img/noah.jpg",
        "conteudo": "Noah começou sua carreira dublando Charlie Brown e ganhou reconhecimento mundial em Stranger Things. Ele também estuda na Universidade da Pensilvânia."
    },

    {
        "id": 4,
        "nome": "Sadie Sink",
        "idade": "23 anos",
        "posição": "Maxine Mayfield",
        "nascimento": "16 de abril de 2002",
        "imagem": "website/img/sadie.jpg",
        "conteudo": "Sadie é atriz e modelo. Já participou de produções da Broadway e chamou atenção em Stranger Things e no curta de Taylor Swift, 'All Too Well'."
    },

    {
        "id": 5,
        "nome": "Caleb McLaughlin",
        "idade": "23 anos",
        "posição": "Lucas Sinclair",
        "nascimento": "13 de outubro de 2001",
        "imagem": "website/img/caleb.jpg",
        "conteudo": "Caleb começou no teatro interpretando Simba em O Rei Leão na Broadway. É conhecido por seu ativismo e presença positiva nas redes sociais."
    },

    {
        "id": 6,
        "nome": "Gaten Matarazzo",
        "idade": "22 anos",
        "posição": "Dustin Henderson",
        "nascimento": "8 de setembro de 2002",
        "imagem": "website/img/gaten.jpg",
        "conteudo": "Gaten também veio do teatro musical e é um defensor da displasia cleidocraniana, condição que ele possui. É carismático e engajado com causas sociais."
    },

    {
        "id": 7,
        "nome": "Natalia Dyer",
        "idade": "30 anos",
        "posição": "Nancy Wheeler",
        "nascimento": "13 de janeiro de 1995",
        "imagem": "website/img/natalia.jpg",
        "conteudo": "Natalia é atriz desde a adolescência. Tem um estilo discreto e já participou de filmes independentes e séries além de Stranger Things."
    },

    {
        "id": 8,
        "nome": "Joe Keery",
        "idade": "33 anos",
        "posição": "Steve Harrington",
        "nascimento": "24 de abril de 1992",
        "imagem": "website/img/joe.jpg",
        "conteudo": "Joe é ator e também músico, com o projeto solo 'Djo'. Seu personagem ganhou grande destaque por sua evolução e carisma."
    },

    {
        "id": 9,
        "nome": "Charlie Heaton",
        "idade": "31 anos",
        "posição": "Jonathan Byers",
        "nascimento": "6 de fevereiro de 1994",
        "imagem": "website/img/charlie.jpg",
        "conteudo": "Charlie é britânico e já foi baterista antes de atuar. Tem um estilo mais reservado e é namorado de Natalia Dyer na vida real."
    },

    {
        "id": 10,
        "nome": "Winona Ryder",
        "idade": "53 anos",
        "posição": "Joyce Byers",
        "nascimento": "29 de outubro de 1971",
        "imagem": "website/img/winona1.jpg",
        "conteudo": "Winona é uma lenda de Hollywood, famosa desde os anos 90 por filmes como 'Edward Mãos de Tesoura' e 'Beetlejuice'."
    },

    {
        "id": 11,
        "nome": "David Harbour",
        "idade": "50 anos",
        "posição": "Jim Hopper",
        "nascimento": "10 de abril de 1975",
        "imagem": "website/img/david.jpg",
        "conteudo": "David teve uma carreira longa no teatro e TV antes do sucesso como Hopper. Também atuou em filmes como Hellboy e Viúva Negra."
    },

    {
        "id": 12,
        "nome": "Jamie Campbell Bower",
        "idade": "36 anos",
        "posição": "Vecna",
        "nascimento": "22 de novembro de 1988",
        "imagem": "website/img/jamie.jpg",
        "conteudo": "Jamie é ator, cantor e modelo britânico. Atuou em 'Crepúsculo' e 'Harry Potter', e surpreendeu o público com sua atuação intensa como Vecna."
    },
]



def index(request):
    return render(request, "website/index.html")

def elenco(request):
    context = {
        "atores": atores,
    }
    return render(request, "website/elenco.html", context)

def ator(request, id_ator):
    return render(request, "website/ator.html", atores[id_ator-1])

def sobre(request):
    return render(request, "website/sobre.html")