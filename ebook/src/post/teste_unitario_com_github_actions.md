# Testes unitários e automatização com o Github Actions

Antes de mostrar como é implementado os testes unitários com o Github Actions, temos que entender o que é Pipeline.

## Pipeline CI/CD

No mundo da engenharia da computação, o termo pipelining é utilizado para descrever a estratégia onde o CPU procura a próxima instrução para executar, como se numa esteira de instruções já enviadas que são executadas, um comando após o outro. Na indústria de software o termo também continua com a mesma ideia. Uma pipeline é desenvolvida ou pensada como uma forma de reduzir trabalhos manuais do dia a dia de um desenvolvedor como: 
- Fez um código novo e precisa testar;
- Fez alguma alteração brusca;
- Testar a instalação de todas ferramentas necessárias. 

O pipeline de CI/CD inclui monitoramento e automação para melhorar o processo de desenvolvimento de aplicações principalmente nos estágios de integração e teste, mas também na entrega e na implantação. É possível executar manualmente cada etapa do pipeline, mas o real valor dele está na automação.
As etapas que compõem um pipeline são subconjuntos distintos de tarefas agrupadas no que chamamos de estágio do pipeline. Os estágios típicos do pipeline são:
- Compilação: estágio em que a aplicação é compilada.
- Teste: estágio em que o código é testado. O uso da automação neste estágio poupa tempo e esforços.
- Lançamento: estágio em que a aplicação é enviada ao repositório.
- Implantação: estágio em que o código é implantado no ambiente de produção.

Para concluir, uma pipeline nada mais é que um conjunto de instruções, steps, scripts, passos que deverão ser executadas sequencialmente que representam operações manuais, desde instalação de dependências, build, start e etc. Facilitando muito o nosso dia a dia de desenvolvimento.

## GitHub Actions

É uma ferramenta que facilita o processo de automatização de builds e deploys de um projeto. Através dele nós podemos construir um workflow com várias ações que vão descrever os passos necessários para compilar, testar, empacotar, criar releases e até fazer deploy do nosso sistema. O GitHub Actions nos permite implementar as técnicas de CI e CD de forma simples dentro do nosso repositório, não precisando mais fazer integrações com outros sistemas.
- Workflow: É onde vamos descrever todo o processo de automação para podermos compilar, testar e fazer deploy do nosso sistema.
- Actions: São tarefas que vamos utilizar dentro do workflow. Aqui vamos definir o que realmente nosso workflow vai fazer.
- Runners: É a máquina responsável por executar o workflow e as actions e nos prover o feedback do nosso processo. O Runner pode ser o GitHub-hosted, provido pelo próprio time ou self-hosted runner, onde você é responsável por gerenciar o servidor e os serviços instalados nele.
Caso você queira se aprofundar [Entendendo Github Actions.](https://docs.github.com/pt/actions/learn-github-actions/understanding-github-actions) 

## Criando automatização

1.No repositório crie uma folder .github/workflows/nomeDoArquivo.yaml GitHub Actions usa a sintaxe do YAML para definir o fluxo de trabalho. Cada fluxo de trabalho é armazenado como um arquivo YAML separado no seu repositório de código, em um diretório chamado .github/workflows.
2.Exemplo de código para realizar os teste unitarios de forma automatica em um porjeto python.

~~~markdown
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

[Mais exemplos.](https://docs.github.com/pt/actions/learn-github-actions/understanding-github-actions) 

3. Agora seja feliz, pois está economizando um tempo sagrado da sua vida.

## Por que escolhi esse tema?

Na matéria optativa desenvolvimento de software, eu juntamente com um grupo, desenvolvemos um aplicativo para pessoas praticarem esportes juntas especificamente o ciclismo. No decorrer do desenvolvimento desse projeto, surgiram alguns problemas que tiraram várias horas sono, pelo fato do código estar mal escrito e não tendo nenhum unitário.
Se naquela época eu conhecesse essas práticas de desenvolvimento ágeis e alguma ferramenta de automatização pipeline, eu com certeza teria economizado bastante tempo, teria uma saúde mental melhor e provavelmente teria conseguido finalizar o projeto.
