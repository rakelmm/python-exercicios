# Uma possível solução
```python
from datetime import date

# Armazenamento dos cadastros
nomes = []
cpfs = []
nascimentos = []

# Lista com nº de dias de cada mês
DIAS_MES = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]

# O programa executa continuamente até o usuário selecionar a opção "Encerrar"
while True:
  # Apresenta o menu
  print()
  print('Digite o nº da opção desejada:')
  print('[1] Inserir novo cadastro')
  print('[2] Alterar CPF')
  print('[3] Trocar sobrenomes')
  print('[4] Remover cadastro')
  print('[5] Listar todos os cadastros')
  print('[6] Encerrar')

  # Lê a opção do usuário
  opcao = input()

  if opcao == '1':  # Inserir novo cadastro
    # Lê o ID
    uid = input('ID (opcional): ')

    # Valida o ID
    if (uid != '' and 
        (not uid.isdecimal() or not (0 < int(uid) < len(nomes) + 2))):
      print('ID inválido')
      continue

    # Lê o primeiro nome
    nome = input('Primeiro nome: ').capitalize()

    # Valida o primeiro nome
    if not nome.isalpha():
      print('Nome inválido')
      continue
    
    # Lê o sobrenome
    sobrenome = input('Sobrenome (apenas o último): ').capitalize()

    # Valida o sobrenome
    if not sobrenome.isalpha():
      print('Sobrenome inválido')
      continue
    
    # Adiciona o sobrenome ao nome
    nome += ' ' + sobrenome
    
    # Lê o CPF
    cpf = input('CPF (apenas dígitos): ')
    
    # Valida o CPF
    if cpf.isdecimal() and len(cpf) == 11:
      # Valida 1º dígito verificador
      soma = 0
      for i in range(9):
        soma += int(cpf[i]) * (10 - i)
      r = soma % 11
      if r < 2:
        dv = 0
      else:
        dv = 11 - r
      if int(cpf[9]) == dv:
        # Valida 2º dígito verificador
        soma = 0
        for i in range(1, 10):
          soma += int(cpf[i]) * (11 - i)
        r = soma % 11
        if r < 2:
          dv = 0
        else:
          dv = 11 - r
        cpf_valido = int(cpf[10]) == dv
      else:
        cpf_valido = False
    else:
      cpf_valido = False
    if not cpf_valido:
      print('CPF inválido')
      continue
    if 5 < int(cpf[8]) < 9:
      print('CPF não aceito por ser da Região Sudeste')
      continue
      
    # Lê a data de nascimento
    data_nasc = input('Data de nascimento (dd/mm/aaaa): ')

    # A variável "hoje" contém a data de hoje.
    # Para o dia do mês, use:  hoje.day
    # Para o mês, use:         hoje.month
    # Para o ano, use:         hoje.year
    hoje = date.today()
    
    # Valida a data de nascimento
    if (len(data_nasc) == 10 and 
        data_nasc[:2].isdecimal() and 
        data_nasc[3:5].isdecimal() and 
        data_nasc[6:].isdecimal() and 
        data_nasc[2] == data_nasc[5] == '/'):
      # Separa e converte os campos da data de nascimento
      dia = int(data_nasc[:2])
      mes = int(data_nasc[3:5])
      ano = int(data_nasc[6:])

      if 0 < ano < hoje.year:
        if 0 < mes < 13:
          # Se o nascimento foi em fevereiro de um ano bissexto
          if (mes == 2 and
              (ano % 400 == 0 or (ano % 4 == 0 and ano % 100 != 0))):
            data_nasc_valida = 0 < dia < 30
          else:
            data_nasc_valida = 0 < dia <= DIAS_MES[mes - 1]
        else:
          data_nasc_valida = False
      elif ano == hoje.year:  # Se o nascimento foi neste ano
        if 0 < mes < hoje.month:
          # Se o nascimento foi em fevereiro de um ano bissexto
          if (mes == 2 and
              (ano % 400 == 0 or (ano % 4 == 0 and ano % 100 != 0))):
            data_nasc_valida = 0 < dia < 30
          else:
            data_nasc_valida = 0 < dia <= DIAS_MES[mes - 1]
        elif mes == hoje.month:  # Se o nascimento foi neste mês
          data_nasc_valida = 0 < dia <= hoje.day
        else:
          data_nasc_valida = False
      else:
        data_nasc_valida = False
    else:
      data_nasc_valida = False
    if not data_nasc_valida:
      print('Data de nascimento inválida')
      continue

    if uid == '':  # ID não preenchido
      # Insere cadastro no final
      nomes.append(nome)
      cpfs.append(cpf)
      nascimentos.append(data_nasc)
    else:  # ID preenchido
      # Insere cadastro na posição correspondente ao ID
      nomes.insert(int(uid) - 1, nome)
      cpfs.insert(int(uid) - 1, cpf)
      nascimentos.insert(int(uid) - 1, data_nasc)

    print('Cadastro inserido com sucesso.')
    
  elif opcao == '2':  # Alterar CPF
    # Lê o ID
    uid = input('ID (opcional): ')

    # Valida o ID
    if not uid.isdecimal() or not (0 < int(uid) < len(nomes) + 1):
      print('ID inválido')
      continue

    uid = int(uid)
    
    # Lê o CPF
    cpf = input('Novo CPF: ')
    
    # Valida o CPF
    if cpf.isdecimal() and len(cpf) == 11:
      # Valida 1º dígito verificador
      soma = 0
      for i in range(9):
        soma += int(cpf[i]) * (10 - i)
      r = soma % 11
      if r < 2:
        dv = 0
      else:
        dv = 11 - r
      if int(cpf[9]) == dv:
        # Valida 2º dígito verificador
        soma = 0
        for i in range(1, 10):
          soma += int(cpf[i]) * (11 - i)
        r = soma % 11
        if r < 2:
          dv = 0
        else:
          dv = 11 - r
        cpf_valido = int(cpf[10]) == dv
      else:
        cpf_valido = False
    else:
      cpf_valido = False
    if not cpf_valido:
      print('CPF inválido')
      continue
    if 5 < int(cpf[8]) < 9:
      print('CPF não aceito por ser da Região Sudeste')
      continue
      
    # Atualiza o CPF
    cpfs[uid - 1] = cpf

    print('CPF atualizado com sucesso.')
    
  elif opcao == '3':  # Trocar sobrenomes
    # Lê o 1º ID
    uid = input('ID 1: ')

    # Valida o ID
    if not uid.isdecimal() or not (0 < int(uid) < len(nomes) + 1):
      print('ID inválido')
      continue
    
    uid1 = int(uid)
    
    # Lê o 2º ID
    uid = input('ID 2: ')

    # Valida o ID
    if not uid.isdecimal() or not (0 < int(uid) < len(nomes) + 1):
      print('ID inválido')
      continue
    
    uid2 = int(uid)

    # Divide os nomes correspondentes em primeiro nome e sobrenome
    nome1 = nomes[uid1 - 1].split()
    nome2 = nomes[uid2 - 1].split()
    
    # Troca os sobrenomes, atualizando os cadastros
    nomes[uid1 - 1] = nome1[0] + ' ' + nome2[1]
    nomes[uid2 - 1] = nome2[0] + ' ' + nome1[1]

    print('Sobrenomes trocados com sucesso.')
    
  elif opcao == '4':  # Remover cadastro
    # Lê o ID
    uid = input('ID (opcional): ')

    # Valida o ID
    if not uid.isdecimal() or not (0 < int(uid) < len(nomes) + 1):
      print('ID inválido')
      continue

    uid = int(uid)

    #  Remove os valores do cadastro correspondente
    nomes.pop(uid - 1)
    cpfs.pop(uid - 1)
    nascimentos.pop(uid - 1)

    print('Cadastro removido com sucesso.')
    
  elif opcao == '5':  # Listar todos os cadastros
    # Se não há nenhum cadastro, imprime mensagem informando
    if len(nomes) == 0:
      print('Nenhum cadastro')
      continue

    # A variável "hoje" contém a data de hoje.
    # Para o dia do mês, use:  hoje.day
    # Para o mês, use:         hoje.month
    # Para o ano, use:         hoje.year
    hoje = date.today()
    
    # Para cada cadastro...
    for i in range(len(nomes)):
      # Imprime os dados do cadastro
      print()
      print('ID:', i + 1)
      print('Nome:', nomes[i])
      print('CPF:', cpfs[i])
      print('Data de nascimento:', nascimentos[i])

      # Separa e converte os campos da data de nascimento
      dia_nasc = int(nascimentos[i][:2])
      mes_nasc = int(nascimentos[i][3:5])
      ano_nasc = int(nascimentos[i][6:])

      # Calcula a idade da pessoa em dias
      # Inicializa a contagem de dias em zero
      dias = 0

      # Para cada ano desde o nascimento da pessoa...
      for ano in range(ano_nasc, hoje.year + 1):
        # Define o 1º mês a ser contado no ano
        mes_inicial = 1

        # Se for ano de nascimento, começa a contar do mês de nascimento
        if ano == ano_nasc:
          mes_inicial = mes_nasc
          
        # Define o último mês a ser contado no ano
        mes_final = 12
        
        # Se for ano em que estamos, conta até o mês em que estamos
        if ano == hoje.year:
          mes_final = hoje.month
          
        # Para cada mês a ser contado neste ano...
        for mes in range(mes_inicial, mes_final + 1):
          # Se forem o ano e o mês em que estamos, soma o dia de hoje
          if ano == hoje.year and mes == hoje.month:
            dias += hoje.day
          else:
            # Senão, soma o nº de dias do mês
            dias += DIAS_MES[mes - 1]

            # Se for fevereiro e o ano for bissexto, soma mais 1 dia
            if (mes == 2 and 
              (ano % 400 == 0 or (ano % 4 == 0 and ano % 100 != 0))):
              dias += 1
          
          # Se forem o ano e o mês de nascimento, 
          # subtrai o dia de nascimento
          if ano == ano_nasc and mes == mes_nasc:
            dias -= dia_nasc
            
      # Imprime a idade em dias
      print('Idade em dias:', dias)
      
  elif opcao == '6':  # Encerrar
    print('Até logo!')
    break
    
  else:  # Opção inexistente
    print('Opção inválida')
```