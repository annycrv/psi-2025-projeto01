from django.shortcuts import render

atores = [

    {
        "id": 1,
        "nome": "Millie Bobby Brown",
        "idade": "21 anos",
        "posicao": "Personagem: Eleven",
        "nascimento": "Data de Nascimento: 19 de fevereiro de 2004",
        "imagem": "website/img/millie.jpg",
        "atorimg": "website/img/a_millie.jpg",
        "conteudo": "Millie é uma atriz britânica que se tornou um fenômeno global ainda criança. Além de atuar, ela também é empresária e já foi indicada ao Emmy."
    },

    {
        "id": 2,
        "nome": "Finn Wolfhard",
        "idade": "22 anos",
        "posicao": "Personagem: Mike Wheeler",
        "nascimento": "Data de Nascimento: 23 de dezembro de 2002",
        "imagem": "website/img/finn.jpg",
        "atorimg": "website/img/a_finn.jpg",
        "conteudo": "Finn é ator e músico canadense. Participou de filmes como It: A Coisa e também é vocalista da banda The Aubreys."
    },

    {
        "id": 3,
        "nome": "Noah Schnapp",
        "idade": "20 anos",
        "posicao": "Personagem: Will Byers",
        "nascimento": "Data de Nascimento: 3 de outubro de 2004",
        "imagem": "website/img/noah.jpg",
        "atorimg": "website/img/a_noah.jpg",
        "conteudo": "Noah começou sua carreira dublando Charlie Brown e ganhou reconhecimento mundial em Stranger Things. Ele também estuda na Universidade da Pensilvânia."
    },

    {
        "id": 4,
        "nome": "Sadie Sink",
        "idade": "23 anos",
        "posicao": "Personagem: Maxine Mayfield",
        "nascimento": "Data de Nascimento: 16 de abril de 2002",
        "imagem": "website/img/sadie.jpg",
        "atorimg": "website/img/a_sadie.jpg",
        "conteudo": "Sadie é atriz e modelo. Já participou de produções da Broadway e chamou atenção em Stranger Things e no curta de Taylor Swift, 'All Too Well'."
    },

    {
        "id": 5,
        "nome": "Caleb McLaughlin",
        "idade": "23 anos",
        "posicao": "Personagem: Lucas Sinclair",
        "nascimento": "Data de Nascimento: 13 de outubro de 2001",
        "imagem": "website/img/caleb.jpg",
        "atorimg": "website/img/a_caleb.jpg",
        "conteudo": "Caleb começou no teatro interpretando Simba em O Rei Leão na Broadway. É conhecido por seu ativismo e presença positiva nas redes sociais."
    },

    {
        "id": 6,
        "nome": "Gaten Matarazzo",
        "idade": "22 anos",
        "posicao": "Personagem: Dustin Henderson",
        "nascimento": "Data de Nascimento: 8 de setembro de 2002",
        "imagem": "website/img/gaten.jpg",
        "atorimg": "website/img/a_gaten.jpg",
        "conteudo": "Gaten também veio do teatro musical e é um defensor da displasia cleidocraniana, condição que ele possui. É carismático e engajado com causas sociais."
    },

    {
        "id": 7,
        "nome": "Natalia Dyer",
        "idade": "30 anos",
        "posicao": "Personagem: Nancy Wheeler",
        "nascimento": "Data de Nascimento: 13 de janeiro de 1995",
        "imagem": "website/img/natalia.jpg",
        "atorimg": "website/img/a_natalia.jpg",
        "conteudo": "Natalia é atriz desde a adolescência. Tem um estilo discreto e já participou de filmes independentes e séries além de Stranger Things."
    },

    {
        "id": 8,
        "nome": "Joe Keery",
        "idade": "33 anos",
        "posicao": "Personagem: Steve Harrington",
        "nascimento": "Data de Nascimento: 24 de abril de 1992",
        "imagem": "website/img/joe.jpg",
        "atorimg": "website/img/a_djo.jpg",
        "conteudo": "Joe é ator e também músico, com o projeto solo 'Djo'. Seu personagem ganhou grande destaque por sua evolução e carisma."
    },

    {
        "id": 9,
        "nome": "Charlie Heaton",
        "idade": "31 anos",
        "posicao": "Personagem: Jonathan Byers",
        "nascimento": "Data de Nascimento: 6 de fevereiro de 1994",
        "imagem": "website/img/charlie.jpg",
        "atorimg": "website/img/a_charlie.jpg",
        "conteudo": "Charlie é britânico e já foi baterista antes de atuar. Tem um estilo mais reservado e é namorado de Natalia Dyer na vida real."
    },

    {
        "id": 10,
        "nome": "Winona Ryder",
        "idade": "53 anos",
        "posicao": "Personagem: Joyce Byers",
        "nascimento": "Data de Nascimento: 29 de outubro de 1971",
        "imagem": "website/img/winona2.jpg",
        "atorimg": "website/img/a_winona.jpg",
        "conteudo": "Winona é uma lenda de Hollywood, famosa desde os anos 90 por filmes como 'Edward Mãos de Tesoura' e 'Beetlejuice'."
    },

    {
        "id": 11,
        "nome": "David Harbour",
        "idade": "50 anos",
        "posicao": "Personagem: Jim Hopper",
        "nascimento": "Data de Nascimento: 10 de abril de 1975",
        "imagem": "website/img/david.jpg",
        "atorimg": "website/img/a_habour.jpg",
        "conteudo": "David teve uma carreira longa no teatro e TV antes do sucesso como Hopper. Também atuou em filmes como Hellboy e Viúva Negra."
    },

    {
        "id": 12,
        "nome": "Jamie Campbell Bower",
        "idade": "36 anos",
        "posicao": "Personagem: Vecna",
        "nascimento": "Data de Nascimento: 22 de novembro de 1988",
        "imagem": "website/img/jamie.jpg",
        "atorimg": "website/img/a_jamie.jpg",
        "conteudo": "Jamie é ator, cantor e modelo britânico. Atuou em 'Crepúsculo' e 'Harry Potter', e surpreendeu o público com sua atuação intensa como Vecna."
    },
]

conteu = [
    {
        "texto":"Stranger Things é uma série de ficção científica e suspense que conquistou milhões de fãs ao redor do mundo desde sua estreia em 2016. Ambientada nos anos 80, a história gira em torno de acontecimentos sobrenaturais que ocorrem na pequena cidade de Hawkins, Indiana. Misturando elementos de terror, nostalgia, amizade e aventura, a série cativa o público com seu enredo envolvente e referências à cultura pop da época <br> <br> Nosso site foi criado especialmente para quem deseja conhecer mais sobre o universo de Stranger Things. Aqui, reunimos informações sobre os personagens, curiosidades sobre a trama, conexões entre as temporadas e detalhes sobre os acontecimentos mais marcantes da série. O conteúdo foi organizado de forma clara e acessível, com o objetivo de facilitar a navegação e o aprendizado. <br> <br>  Este projeto foi desenvolvido por Anny Carolline e Williany Vitória como parte de uma atividade escolar. Nosso objetivo é unir entretenimento e conhecimento, apresentando de forma criativa uma das séries mais populares da atualidade. Esperamos que você aproveite o conteúdo e se aprofunde ainda mais nesse mundo cheio de mistérios e aventuras!",
    },

    {
        "texto2": "Stranger Things é uma série de televisão via streaming estadunidense dos gêneros ficção científica, terror, suspense e drama adolescente, criada, escrita e dirigida pelos irmãos Matt e Ross Duffer para a plataforma Netflix. Os irmãos Duffer, Shawn Levy e Dan Cohen são também os produtores executivos.<br> A série se passa na década de 1980, em Hawkins, Indiana, onde um grupo de crianças e adolescentes enfrenta forças sobrenaturais e conspirações secretas. A história começa com o desaparecimento misterioso de Will Byers, levando sua mãe, Joyce, o chefe de polícia Jim Hopper e seus amigos a investigar o ocorrido, descobrindo experimentos secretos e uma passagem para um mundo paralelo chamado 'Mundo Invertido'."
    },
]

def index(request):
    return render(request, "website/index.html", conteu[1])

def elenco(request):
    context = {
        "atores": atores,
    }
    return render(request, "website/elenco.html", context)

def ator(request, id_ator):
    return render(request, "website/ator.html", atores[id_ator-1])

def sobre(request):
    return render(request, "website/sobre.html", conteu[0])