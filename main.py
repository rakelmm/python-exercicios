from datetime import date

hoje = date.today()
hoje_year = hoje.year

id = []
nomes = []
cpfs = []
nascimentos = []
menuControle = 1

nascimentos_dias = []
anos_bissextos = []
anos_bissextos_por_nascimento = []

# ideia inicial foi criar um programa para controle de cadastro e listagem de usuários
while menuControle != 0:
  print('\n\n')
  print('-=' * 43)
  print('1 - Cadastrar usuário')
  print('2 - Listar usuários')
  print('3 - Remover ID')
  print('4 - Alterar CPF')
  print('5 - Trocar sobrenomes')
  print('0 - Sair')
  print('-=' * 43)
  
  opcaoMenu = int(input('\n\nOpção Menu: '))

# opcaoMenu 0, controla a saída do while e fechamento do programa.
  if opcaoMenu == 0:
    menuControle = 0
# opcaoMenu 1, onde é realizado o cadastro do novo usuario
  elif opcaoMenu == 1:
    idInput = input('Digite o ID do novo cadastro (ou deixe em branco para gerar automaticamente): ')
    if idInput != "" and idInput.isnumeric() == False:
      print('\n\n\033[0;31mO valor inserido não é do tipo numérico.\033[m\n\n')
      continue
    primeiroNome = input('Digite seu primeiro nome: ').capitalize().strip()
    sobrenome = input('Digite seu sobrenome: ').capitalize().strip()
    check_sobrenome = sobrenome.split()
    if len(check_sobrenome) > 1:
      print('\n\n\033[0;31mSobrenome só deve conter um nome\033[m\n\n')
      continue
    cpf = input('Digite seu CPF: ')
    cpf_remove_mascara = cpf.replace('.',"").replace('-',"")
    cpf_check_character = cpf_remove_mascara.isnumeric()
    if cpf_check_character == False:
      print('\n\n\033[0;31mCpf só deve conter valores númericos\033[m\n\n')
      continue
    cpf_len = len(cpf_remove_mascara)
    if cpf_len < 11:
      print('\n\n\033[0;31mCpf deve conter 11 caracters.\033[m\n\n')
      continue
    cpf_nono_digito = cpf_remove_mascara[8:9]
    if cpf_nono_digito == "6" or cpf_nono_digito == "7" or cpf_nono_digito == "8":
      print('\n\n\033[0;31mCpfs emitidos na Região Sudeste (ES, MG, RJ e SP) não são aceitos.\033[m\n\n')
      continue
    nascimento = input('Digite a data de nascimento (no formato dd/mm/aaaa): ')
    nascimento_split = nascimento.split("/")
    nascimento_dia = nascimento_split[0]
    if nascimento_dia.isnumeric() == False:
      print('\n\n\033[0;31mCValor inválido para o dia do nascimento\033[m\n\n')
      continue
    nascimento_mes = nascimento_split[1]
    if nascimento_mes.isnumeric() == False:
      print('\n\n\033[0;31mValor inválido para o mês de nascimento\033[m\n\n')
      continue
    nascimento_ano = nascimento_split[2]
    if nascimento_ano.isnumeric() == False:
      print('\n\n\033[0;31mValor inválido para o ano de nascimento\033[m\n\n')
      continue
    check_hoje = hoje.strftime("%d/%m/%Y").split("/")
    hoje_dia = check_hoje[0]
    hoje_mes = check_hoje[1]
    hoje_ano = check_hoje[2]
    if nascimento_ano >= hoje_ano and nascimento_mes >= hoje_mes and nascimento_dia >= hoje_dia:
      print('\n\n\033[0;31mNão pode ser inserido a data de hoje ou futura.\033[m\n\n')
      continue
      
    # Inicio bloco de teste da data de nascimento
    if nascimento_mes == "01":
      if nascimento_dia < "01" or nascimento_dia > "31":
        print('\033[0;31mDia inválido para o mês correspondente\033[m')
        continue
    elif nascimento_mes == "02":
      if (int(nascimento_ano) % 4 == 0 and int(nascimento_ano) % 100 != 0) or int(nascimento_ano) % 400 == 0:
        if nascimento_dia < "01" or nascimento_dia > "29":
          print('\033[0;31mDia inválido para o mês correspondente.\033[m')
          continue
      elif nascimento_dia < "01" or nascimento_dia > "28":
        print('\033[0;31mDia inválido para o mês correspondente.\033[m')
        continue
    elif nascimento_mes == "03":
      if nascimento_dia < "01" or nascimento_dia > "31":
        print('\033[0;31mDia inválido para o mês correspondente.\033[m')
        continue
    elif nascimento_mes == "04":
      if nascimento_dia < "01" or nascimento_dia > "30":
        print('\033[0;31mDia inválido para o mês correspondente.\033[m')
        continue
    elif nascimento_mes == "05":
      if nascimento_dia < "01" or nascimento_dia > "31":
        print('\033[0;31mDia inválido para o mês correspondente.\033[m')
        continue
    elif nascimento_mes == "06":
      if nascimento_dia < "01" or nascimento_dia > "30":
        print('\033[0;31mDia inválido para o mês correspondente.\033[m')
        continue
    elif nascimento_mes == "07":
      if nascimento_dia < "01" or nascimento_dia > "31":
        print('\033[0;31mDia inválido para o mês correspondente.\033[m')
        continue
    elif nascimento_mes == "08":
      if nascimento_dia < "01" or nascimento_dia > "31":
        print('\033[0;31mDia inválido para o mês correspondente.\033[m')
        continue
    elif nascimento_mes == "09":
      if nascimento_dia < "01" or nascimento_dia > "30":
        print('\033[0;31mDia inválido para o mês correspondente.\033[m')
        continue
    elif nascimento_mes == "10":
      if nascimento_dia < "01" or nascimento_dia > "31":
        print('\033[0;31mDia inválido para o mês correspondente.\033[m')
        continue
    elif nascimento_mes == "11":
      if nascimento_dia < "01" or nascimento_dia > "30":
        print('\033[0;31mDia inválido para o mês correspondente.\033[m')
        continue
    elif nascimento_mes == "12":
      if nascimento_dia < "01" or nascimento_dia > "31":
        print('\033[0;31mDia inválido para o mês correspondente.\033[m')
        continue
    # Fim bloco de teste da data de nascimento
    
    if len(id) == 0 and idInput == "":
      id.append(1)
      nomes.append(primeiroNome + " " + sobrenome)
      cpfs.append(cpf)
      nascimentos.append(nascimento)
    elif idInput == "":
      id.append((id[len(id) - 1]) + 1)
      nomes.append(primeiroNome + " " + sobrenome)
      cpfs.append(cpf)
      nascimentos.append(nascimento)
    elif len(id) == 0 and idInput != "":
      id.append(int(idInput))
      nomes.insert(int(idInput), primeiroNome + " " + sobrenome)
      cpfs.insert(int(idInput), cpf)
      nascimentos.insert(int(idInput), nascimento)
    else:
      id.append(id[len(id) -1] + 1)
      nomes.insert(int(idInput) -1, primeiroNome + " " + sobrenome)
      cpfs.insert(int(idInput) -1, cpf)
      nascimentos.insert(int(idInput) -1, nascimento)
    print("-=" * 43)  
    print('\n\033[32mUsuário CADASTRADO com sucesso 🎉!\033[m')
  
  elif opcaoMenu == 2:
    print("\n\nListagem de todos os cadastros:\n\n")
    print('-=' * 43)  
    print("ID\t\tNome\t\t\t\tCPF\t\t\tData de nascimento\t\tNascimento em dias")
    print('-=' * 43)

    # Idade em dias começa aqui
    for i in range(len(nascimentos)):
      x = nascimentos[i].split("/")
      day = int(x[0])
      month = int(x[1])
      year = int(x[2])
      nascimento = date(year,month,day)
      diferenca_dias = hoje - nascimento
   
    # O bloco de while calcula a quantidade de anos bissextos entre a data de nascimento e o dia que o programa rodar. Incrementando a diferença de dias já calculadas.
      while year <= hoje_year:
        if (year % 4 == 0 and year % 100 != 0) or year % 400 == 0:
            anos_bissextos.append(1)
        year += 1
    
      anos_bissextos_por_nascimento.append(sum(anos_bissextos))
      anos_bissextos.clear()
      
      nascimentos_dias.append(diferenca_dias.days + anos_bissextos_por_nascimento[i])
      # nascimentos_dias.append(diferenca_dias.days)
    
      for i in range(len(id)):
         print(f'{id[i]}\t\t{nomes[i]}\t\t{cpfs[i]}\t\t {nascimentos[i]}\t\t\t\t\t{nascimentos_dias[i]}')

# Funcionalidade de "Remover cadastro": 
  elif opcaoMenu == 3:
    idInput = input('Digite o ID que você quer remover: ')
    id.clear()
    nomes.pop(int(idInput) -1)
    cpfs.pop(int(idInput) -1)
    nascimentos.pop(int(idInput) -1)
    for i in range(len(nomes)):
      id.append(i+1)
    print("-=" * 43)  
    print('\n\033[32mUsuário REMOVIDO com sucesso 🎉!\033[m')
  
# Funcionalidade "Alterar CPF"
  elif opcaoMenu == 4:
    idInput = int(input('Digite o ID do Cadastro que deseja remover o CPF: '))
    novo_cpf = int(input('Insira novo CPF: '))
    cpfs[idInput -1] = novo_cpf
    print("-=" * 43)  
    print('\n\033[32mCPF ALTERADO com sucesso 🎉!\033[m')
  
# Funcionalidade "Trocar sobrenomes"
  elif opcaoMenu == 5:
    idInput = int(input('Digite o ID do Cadastro que deseja trocar o sobrenome: '))
    nome_novo = input('Insira novo sobrenome: ')
    sobrenome_novo = nomes[idInput -1].split()
    sobrenome_novo[1] = nome_novo
    nomes[idInput -1] = sobrenome_novo[0] + " " + sobrenome_novo[1]
    print("-=" * 43)  
    print('\n\033[32mSobrenome TROCADO com sucesso 🎉!\033[m')  
  else:
    print('\n\033[0;31mDesculpe! Essa funcionalidade ainda não foi implementada.\033[m')