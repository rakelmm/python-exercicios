<p align="center">
    <img src="assets/logo_infnet.png" width="70" height="70" />
</p>

# *Assessment*

## Exercício 10

**Atenção:**
- É importante que você desenvolva o programa totalmente, do início ao fim, na IDE do Replit (**AQUI MESMO!!**⚠️**NÃO crie um repl no seu perfil do Replit para fazer o Assessment**⚠️). Você **NÃO** deve escrever o código em outra IDE e depois copiá-lo para cá.
- **NÃO** é permitido usar nenhum recurso que não faça parte do conteúdo desta disciplina, a menos que explicitamente autorizado no enunciado.
- Use comentários para explicar o que cada parte do código faz.
- Após concluir as tarefas, submeta suas soluções aqui e no Moodle (postando lá os links para seus projetos do Replit).

Neste exercício, você deverá criar uma nova versão do programa do Exercício 9, incluindo a validação de data de nascimento conforme a descrição a seguir.

## Validação de entrada

Caso um valor de entrada inválido seja detectado, o programa deverá notificar o usuário, **detalhando o problema identificado**, e encerrar a funcionalidade que estava sendo executada, retornando ao menu.

**Atenção:**

- Apenas as validações especificadas a seguir são necessárias. Considere que o usuário respeitará todos os demais aspectos não cobertos por estas especificações.
- Uma revisão dos métodos de strings pode ser útil: https://www.w3schools.com/python/python_ref_string.asp

### Data de nascimento

A data de nascimento deverá estar no formato dd/mm/aaaa, onde:

- dd são 2 dígitos representando o dia
- mm são 2 dígitos representando o mês
- aaaa são a dígitos representando o ano

O sistema **NÃO** deve aceitar datas INválidas. Por exemplo:
- Se o mês for 04 (abril), o dia deve estar entre 01 e 30.
- Se o mês for 02 (fevereiro), o dia deve estar entre:
  - 01 e 29, se o ano for bissexto
  - 01 e 28, caso contrário

Além disso, o sistema **NÃO** deve aceitar datas futuras (não estamos aceitando cadastros de viajantes do tempo no momento).

*Observações:*

- **NÃO** é permitido usar nenhum recurso do módulo datetime além do que está indicado nas instruções de uso do Exercício 6.
- As regras para determinar se um ano é bissexto podem ser encontradas em https://pt.wikipedia.org/wiki/Ano_bissexto#Calend%C3%A1rio_Gregoriano (se olharem bem esse artigo da Wikipédia, pode ser que encontrem mais coisa útil #ficaadica 🤐).
- As máquinas virtuais do Replit estão no fuso-horário UTC (pois estão no Reino Unido). Por isso, se você estiver no Brasil, o programa estará algumas horas adiantado.