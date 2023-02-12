# Testes unitários e automatização com o Github Actions

Antes de mostrar como é implementado os testes unitários com o Github Actions, primeiro temos que entender como funciona o Pipeline CI/CD, teste unitários e Github Actions.

## ♾️Pipeline CI/CD

Pipeline CI/CD (Continuos Integration/Continuos Deployment) é um processo automatizado de desenvolvimento de software que visa integrar, testar e implantar rapidamente aplicativos e sistemas. É composto por uma série de etapas que são executadas de forma contínua e automática, cada uma construindo sobre a outra.

A CI (Continuos Integration) é o processo de integração de código e construção de uma aplicação em várias etapas, incluindo a validação do código, a compilação, o teste unitário e o teste de integração. O objetivo da CI é identificar rapidamente problemas de integração de código e corrigi-los antes que eles causem problemas mais graves.

A CD (Continuos Deployment) é o processo de implementar rapidamente a aplicação construída e validada na CI para produção. Isso geralmente inclui etapas como implementação em servidores de produção, teste de aceitação e monitoramento. O objetivo da CD é fornecer uma implementação mais rápida e confiável, sem interrupções ou erros humanos.

O pipeline CI/CD é uma parte fundamental da metodologia de DevOps, que visa aprimorar a colaboração entre desenvolvedores e operadores de TI, tornando o processo de desenvolvimento de software mais ágil e eficiente. Ao automatizar o processo de implementação, o pipeline CI/CD permite que as equipes de desenvolvimento liberem atualizações com mais frequência, com mais confiança e com menos erros. Caso você queira se aprofundar mais no assunto de automatização com [Pipeline CI/CD.](https://www.jetbrains.com/pt-br/teamcity/ci-cd-guide/ci-cd-pipeline/) 

## 🧪Teste Unitário

Teste unitário é um tipo de teste de software que visa testar pequenas unidades isoladas de código, geralmente métodos ou funções, para garantir que elas estejam funcionando corretamente. O objetivo do teste unitário é identificar problemas em partes individuais do código o mais cedo possível, para que eles possam ser corrigidos antes que afetem o sistema como um todo.

Os testes unitários são escritos pelos desenvolvedores e são executados frequentemente durante o desenvolvimento, com o objetivo de detectar problemas rapidamente e evitar que eles sejam propagados para outras partes do código. Os testes unitários também fornecem uma garantia de que o código continuará a funcionar corretamente mesmo quando ele é modificado ou mantido por outros desenvolvedores.

Os testes unitários geralmente são escritos usando frameworks de teste, como JUnit para Java, NUnit para .NET ou unittest para Python, que fornecem ferramentas para escrever, executar e gerenciar testes unitários de forma automatizada. Caso você queira se aprofundar: [Entendendo Testes unitários](https://dayvsonlima.medium.com/entenda-de-uma-vez-por-todas-o-que-s%C3%A3o-testes-unit%C3%A1rios-para-que-servem-e-como-faz%C3%AA-los-2a6f645bab3) 

## 🙀GitHub Actions

É uma ferramenta que facilita o processo de automatização de builds e deploys de um projeto. Através dele nós podemos construir um workflow com várias ações que vão descrever os passos necessários para compilar, testar, empacotar, criar releases e até fazer deploy do nosso sistema. O GitHub Actions nos permite implementar as técnicas de CI e CD de forma simples dentro do nosso repositório, não precisando mais fazer integrações com outros sistemas.
- Workflow: É onde vamos descrever todo o processo de automação para podermos compilar, testar e fazer deploy do nosso sistema.
- Actions: São tarefas que vamos utilizar dentro do workflow. Aqui vamos definir o que realmente nosso workflow vai fazer.
- Runners: É a máquina responsável por executar o workflow e as actions e nos prover o feedback do nosso processo. O Runner pode ser o GitHub-hosted, provido pelo próprio time ou self-hosted runner, onde você é responsável por gerenciar o servidor e os serviços instalados nele.
Caso você queira se aprofundar [Entendendo Github Actions.](https://docs.github.com/pt/actions/learn-github-actions/understanding-github-actions) 

## 🔨Criando as automatizações

1.No repositório crie uma folder .github/workflows/nomeDoArquivo.yaml GitHub Actions usa a sintaxe do YAML para definir o fluxo de trabalho. Cada fluxo de trabalho é armazenado como um arquivo YAML separado no seu repositório de código, em um diretório chamado .github/workflows.
2.Exemplo de código para realizar os teste unitarios de forma automatica em um porjeto python.

~~~YAML
name: teste-unitario-automatizado

on: # Quando o usuário realizar um push, será feito todas as automatizações definidas pelo usuário
  push:
  pull_request:
  schedule: [{cron: "0 0 * * *"}] # Quando estiver perto da meia noite será realizado as automações.

jobs:
  build:
    runs-on: ubuntu-latest # escolher os sitemas operacionais
    steps:
    - uses: actions/checkout@v3 # dependencias do Github Actions
    - name: Set up Python
      uses: actions/setup-python@v4
      with:
        python-version: '3.10'
    - name: Install dependencies
      run: |
        pip install --upgrade pip
    - name: Test with pytest
      run: | # Vai realizar os testes
        pip install pytest
        pip install pytest-cov
        pip install tqdm
        pip install certifik8
        pytest --cov-config=.coveragerc --cov=Certifik8
~~~

3. Agora vou explicar um pouco o que o código está fazendo. A seção "on" define quando o workflow será acionado, seja quando o usuário realiza um push, Pull request ou em um horário específico (neste caso, às 00:00 horas todos os dias).
Na seção "jobs", o trabalho "build" é definido, que será executado no sistema operacional linux "ubuntu". Os passos incluem a verificação do repositório, a configuração do Python 3.10, a instalação de dependências e a execução dos testes com o pytest. Além disso, outras bibliotecas como pytest-cov, tqdm e certifik8 são instaladas para fornecer cobertura de teste e recursos adicionais.
Ao final, o comando "pytest --cov-config=.coveragerc --cov=Certifik8" será executado para executar os testes unitários e fornecer informações sobre a cobertura de testes. 
[Caso queira mais exemplos.](https://docs.github.com/pt/actions/learn-github-actions/understanding-github-actions) 

4. Agora seja feliz, pois está economizando um tempo sagrado da sua vida.

## 🤔Por que escolhi esse tema?

Na matéria optativa desenvolvimento de software, eu juntamente com um grupo, desenvolvemos um aplicativo para pessoas praticarem esportes juntas especificamente o ciclismo. No decorrer do desenvolvimento desse projeto, surgiram alguns problemas que tiraram várias horas sono, pelo fato do código estar mal escrito e não tendo nenhum unitário. Alguns desses problemas foram:
- Ao fazermos algumas alterações no código, uma função entrou em conflito com a outra e não sabiamos onde estava esse erro, tivemos que revisar o código inteiro para encontrar.
- Também havia alguns bugs, como na hora de traçar as rota no mapa para os ciclistas. as rotas não eram traçadas nas ruas, ela simplemente fazia uma linha reta.

Se naquela época eu conhecesse essas práticas de desenvolvimento ágeis e alguma ferramenta de automatização pipeline, eu com certeza teria economizado bastante tempo, teria uma saúde mental melhor e provavelmente teria conseguido finalizar o projeto.
