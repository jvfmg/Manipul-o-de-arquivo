import json, csv
def inserir_piloto(caminho):
    piloto = {}
    piloto["nome"] = input("Informe o nome do piloto que deseja inserir\n-")
    piloto["nacionalidade"] = input("Informe a nacionalidade de seu piloto\n-")
    piloto["equipe"] = input("Informe a equipe cujo piloto participa\n-")
    with open(caminho+"pilotos.csv","a") as arquivo:
        escriba = csv.writer(arquivo)
        arquivo.write("\n")
        escriba.writerow([piloto["nome"],piloto["nacionalidade"],piloto["equipe"]])
    return "Ação feita com sucesso"

def buscar_piloto(caminho):
    tem = ""
    nome_piloto = input("Qual o nome do piloto que deseja buscar?\n-")
    with open(caminho+"pilotos.csv","r") as arquivo:
        #tem = "s"
        bush = csv.DictReader(arquivo)
        for piloto_csv in bush:
            if piloto_csv["nome"] == nome_piloto:
                tem = "s"
                print(f"Nome: {piloto_csv["nome"]} | Nacionalidade: {piloto_csv["nacionalidade"]} | Equipe: {piloto_csv["equipe"]}") 
        if tem != "s":
            return "Não há pilotos com esse nome!"

def inserir_jotazon():
    heheha = []
    myanimelist = {}
    myanimelist["titulo"] = input("Informe o título do anime:\n-").lower() 
    myanimelist["genero"] = input("Informe o gênero:\n-").lower()
    myanimelist["criador"] = input("Informe o criador do anime:\n-").lower()
    myanimelist["quantidade"] = input("Informe a quantidade de episódios:\n-").lower()

    with open("animes.json","r") as arquivo:
        heheha = json.load(arquivo)
        heheha.append(myanimelist)
    with open("animes.json","w") as arquivo:
        json.dump(heheha, arquivo)
def buscar_anime():
    dados = []
    DNA = {}
    with open("animes.json","r") as arquivo:
        dados = json.load(arquivo)
    busca = input("Você deseja buscar por:\n1)Título\n2)Todos\n-")
    if busca == "1":
        titulo_b = input("Informe o Título:\n-").lower()
        for DNA in dados:
            if DNA["titulo"] == titulo_b:
                print(f"""Título: {DNA["titulo"]} | Gênero: {DNA["genero"]} | Criador: {DNA["criador"]} | Quantidade de Eps: {DNA["quantidade"]}""") 
    else:
        for DNA in dados:
            print(f"""Título: {DNA["titulo"]} | Gênero: {DNA["genero"]} | Criador: {DNA["criador"]} | Quantidade de Eps: {DNA["quantidade"]}""")

def conversor():
    heheha = []
    primeira_linha = 0
    parametros = [] 
    nome_csv = input("Informe o nome do arquivo:\n-")
    with open(nome_csv + ".csv", "r") as arquivo:
        escriba = csv.reader(arquivo)
        for linha in escriba:
            mandar_para_json = {}
            if primeira_linha == 0:

                parametros = linha
                primeira_linha = 1
                continue
            try:
                open(nome_csv + ".json","r")
            except FileNotFoundError: 
                with open(nome_csv + ".json","w") as arquivo:
                    arquivo.write("[]")
            with open(nome_csv + ".json","r") as arquivo:
                try:
                    heheha = json.load(arquivo)
                except json.decoder.JSONDecodeError:
                    pass
                for i in range(len(linha)):
                    mandar_para_json[parametros[i]] = linha[i]
                heheha.append(mandar_para_json)
            with open(nome_csv + ".json","w") as arquivo:
                json.dump(heheha, arquivo)













correcao = int(input("deseja corrigir qual dever?\n1)Copiar\n2)Escrever/Substituir\n3)Ler\n4)Pilotos f1\n5)Animes\n6)Conversor"))
if correcao == 1:
    nome = input("Informe o nome do arquivo a ser copiado (caminho completo): ")
    caminho = nome[:nome.rindex(".")]
    extensao = nome[nome.rindex("."):]
    modo_original = "r"
    modo_copia = "w"
    if extensao != ".txt":
        modo_original += "b"
        modo_copia += "b"

    with open(nome, modo_original) as original:
        with open(caminho +"_copy" + extensao, modo_copia) as copia:
            copia.write(original.read())
    print("arquivo copiado com sucesso")
elif correcao == 2:
    nome = input("me diga o nome do arquivo: ") + ".txt"
    camino = input("me diga o diretorio: ")
    substutuir = input("me diga oq deve ser colocado no arquivo? ")
    desejo = input("deseja \nW)Substuir \nA)Adicionar ao final\n")

    if desejo not in ["a","w"]:
        print("opção inválida")
    else:
        with open(f"{camino}{nome}",desejo) as lgl:
            lgl.write(desejo)
elif correcao == 3:
    nombre = input("Qual es el nombre del arquivo?\n")+ ".txt"
    camino = input("Qual es el camino (OMG is that a motherfucking breaking bad reference) del arquivo?\n")

    with open(camino + nombre, "r") as gus:
        print(gus.read())
elif correcao == 4:
    while True:

        escolha = int(input("Deseja\n1)Adicionar piloto\n2)Buscar informações de um piloto\n3)Sair do programa\n-"))
        camino = input("Informe o caminho onde deseja criar/ utilizar o arquivo pilotos.csv\n-")
        if escolha == 1:
            inserir_piloto(camino)
        elif escolha == 2:
            buscar_piloto(camino)
        elif escolha == 3:
            break
        else:
            print("favor escolher uma opção válida!")
elif correcao == 5:
    programa = input("Deseja: \n-1)Adicionar anime\n2)Buscar anime\n-")
    if programa == "1":
        inserir_jotazon()
    elif programa == "2":
        buscar_anime()
    else:
        exit("Seu animal escolha uma opção correta")
elif correcao == 6:
    conversor()