from django.shortcuts import render

atores = [

    {
        "id": 1,
        "Nome": "Millie Bobby Brown",
        "Idade": "21 anos",
        "Posição": "Eleven",
        "Nascimento": "19 de fevereiro de 2004",
        "imagem": "website/img/millie.jpg",
    },

    {
        "id": 2,
        "Nome": "Finn Wolfhard",
        "Idade": "22 anos",
        "Posição": "Mike Wheeler",
        "Nascimento": "23 de dezembro de 2002",
        "imagem": "website/img/finn.jpg",
    },

    {
       "id": 3,
        "Nome": "Noah Schnapp",
        "Idade": "20 anos",
        "Posição": "Will Bayers",
        "Nascimento": "3 de outubro de 2004",
        "imagem": "website/img/noah.jpg",
    },

    {
       "id": 4,
        "Nome": "Sadie Sink",
        "Idade": "23 anos",
        "Posição": "Maxine Mayfiel",
        "Nascimento": "16 de abril de 2002",
        "imagem": "website/img/sadie.jpg",
    },
    
    {
       "id": 5,
        "Nome": "Caleb McLaughlin",
        "Idade": "23 anos",
        "Posição": "Lucas Sinclair",
        "Nascimento": "13 de outubro de 2001",
        "imagem": "website/img/caleb.jpg",
    },

    {
       "id": 6,
        "Nome": "Gaten Matarazzo",
        "Idade": "22 anos",
        "Posição": "Dustin Henderson",
        "Nascimento": "8 de setembro de 2002",
        "imagem": "website/img/gaten.jpg",
    },

    {
       "id": 7,
        "Nome": "Natalia Dyer",
        "Idade": "30 anos",
        "Posição": "Nancy Wheeler",
        "Nascimento": "13 de janeiro de 1995",
        "imagem": "website/natalia.jpg",
    },

    {
       "id": 8,
        "Nome": "Joe Keery",
        "Idade": "33 anos",
        "Posição": "Steve Harrington",
        "Nascimento": "24 de abril de 1992",
        "imagem": "website/img/joe.jpg",
    },

    {
       "id": 9,
        "Nome": "Charlie Heaton",
        "Idade": "31 anos",
        "Posição": "Jonathan Byers",
        "Nascimento": "6 de fevereiro de 1994",
        "imagem": "website/img/charlie.jpg",
    },

    {
       "id": 10,
        "Nome": "Winona Ryder",
        "Idade": "53 anos",
        "Posição": "Joyce Byers",
        "Nascimento": "29 de outubro de 1971",
        "imagem": "website/img/winona.jpg",
    },

    {
       "id": 11,
        "Nome": "David Harbour",
        "Idade": "50 anos",
        "Posição": "Jim Hopper",
        "Nascimento": "10 de abril de 1975",
        "imagem": "website/img/david.jpg",
    },

    {
       "id": 12,
        "Nome": "Jamie Campbell Bower",
        "Idade": "36 anos",
        "Posição": "Vecna",
        "Nascimento": "22 de novembro de 1988",
        "imagem": "website/img/jamie.jpg",
    },
]

def index (request):
    return render(request, "website/index.html")

def equipe (request):
    context = {
        "atores": atores
    }
    return render(request, "website/equipe.html", context)

def sobre (request):
    return render(request, "website/sobre.html")