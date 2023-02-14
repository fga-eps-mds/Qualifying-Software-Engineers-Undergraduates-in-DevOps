# Introdução

Git e GitHub são duas ferramentas complementares no mundo de desenvolvimento de software, mas que acabam gerando muitas dúvidas a novatos e desenvolvedores iniciantes. Eu mesmo usava GitHub nos meus primeiros meses de desenvolvimento jurando que já podia me dizer profissional no Git. Baita erro.Afinal, qual a diferença entre eles? É essa dúvida que quero sanar aqui, mas não só com uma explicação teórica dizendo que Git é a ferramenta e GitHub só usa ele em formato de site. Quero mostrar-lhes a diferença na prática, mostrando os primeiros passos com o Git isoladamente, sua integração com o GitHub e como o GitHub não é só uma Hub comum do Git, mas todo um centro de trabalho online.

Espero que aproveitem o que escrevi e de verdade, não leia isso de uma vez, muito menos na ordem. Use isso com um complemento aos seus estudos com o Git, um guia. Veja as partes que lhe interessam por agora, treine-as e depois vá para o próximo tópico que precisa. Além disso, saiba que a melhor fonte de informação sobre tanto o Git quanto o GitHub sempre será suas próprias documentações, isso aqui é só uma simplicação feita para não deixar os iniciantes perdidos.


# Índice
- [Introdução ao Git](#introdução-ao-git)
    - [O que é o Git?](#o-que-é-o-git)
- [Introdução ao GitHub](#introdução-ao-github)
    - [Funcionalidades do GitHub](#funcionalidades-do-github)
- [Usando Git](#usando-o-git)
    - [Apresentando-se ao Git](#apresentando-se-ao-git)
    - [Integrando seu Git e GitHub](#integrando-seu-git-e-github)
    - [Acesso a um Repositório](#acesso-a-um-repositório)
    - [Mudança/Criação de Branches](#mudançacriação-de-branches)
    - [Adição de Mudanças no Repositório](#adição-de-mudanças-no-repositório)
    - [Atualizar um Repositório Remoto com as Alterações de um Repositório Local](#atualizar-um-repositório-remoto-com-as-alterações-de-um-repositório-local)
    - [Exportanto/Mesclando Alterações entre Branches](#exportandomesclando-alterações-entre-branches)
    - [Resolvendo Conflitos de Versões](#resolvendo-conflitos-de-versões)
- [Usando GitHub](#usando-o-github)
    - [Recursos Básicos](#recursos-básicos)
    - [Repositórios](#repositórios)
    - [Organização e Comunicação com Issues](#organização-e-comunicação-com-issues)
    - [Solicitando alterações com Pull Requests](#solicitando-alterações-com-pull-requests)
    - [Wiki, Projects e Discussions](#wiki-projects-e-discussions)
    - [Estatísticas com Insights](#estatísticas-com-insights)
    - [Automação com GitHub Actions](#automação-com-github-actions)
- [Conclusão](#conclusão)
<br><br><br>

# Introdução ao Git

Git é uma ferramenta de controle de versionamento. Muitas equipes de software (e até de outras áreas) o usa a fim de gerar uma organização melhor de seus projetos, principalmente quando várias pessoas estão trabalhando num mesmo arquivo.

## O que é o Git?

O Git cria em sua máquina local um *repositório*, estrutura esta que serve para armazenar alterações. De forma mais detalhada, o Git cria uma pasta *.git* no computador. A pasta que carrega a pasta .git irá se tornar um repositório, que irá registrar as alterações feitas no local, sejam elas criações de documentos, apagamento de arquivos, edição de textos, etc.

# Introdução ao GitHub

<a href="https://github.githubassets.com/images/modules/logos_page/GitHub-Mark.png"><img width=40% src="https://github.githubassets.com/images/modules/logos_page/GitHub-Mark.png" alt="GitHub"> </a>


Nada diferente de quaisquer outros *Hubs de ferramentas*, o GitHub é um centro online de repositórios Git. De forma mais detalhada, você acessa o site do GitHub, cria a sua conta e pode criar e adicionar repositórios Git de forma remota, fora de seu computador, através de um link que pode ser acessado por outras pessoas mundo afora. Ainda que sejam realmente repositórios Git, vamos denominar aqui todo repositório no GitHub de **repositório remoto** para facilitar a compreensão.

O GitHub entretanto tornou-se tão famoso que estendeu suas funcionalidades de ser somente um *Hub do Git* para uma ferramenta completa de edição de repositórios Git remotamente, um IDE de código completo (através do recente GitHub Copilot) e muito mais. Você pode criar seus repositórios arquivos e mudanças, tudo pelo próprio GitHub e sem tocar um dedo diretamente na interface própria do Git. Toda essa funcionalidade do GitHub, ainda que bastante benéfica, é o que faz as pessoas confundirem o Git e GitHub, visto que a maioria dos iniciantes em programação só mexem no GitHub e acabam não conhecendo o que de fato seria o Git nisso tudo. O dever desse artigo é justamente conseguir separar o conceito dessas duas ferramentas para você e te deixar apto o bastante para usar ambas as ferramentas juntas ou separadamente.

### Funcionalidades do GitHub

Boa parte das funcionalidades do GitHub se voltam a projetos de Código Aberto (Open Source), limitando algumas das funcionalidades para projetos que pretendem ter seus códigos privados.

- Principais:
  - Compartilhar, criar, editar e excluir repositórios Git remotamente ao mundo todo.
  - Cria uma interface simples de manipulação de repositórios Git.
  - Possibilitar a disponibilização dos seus repositórios para todo mundo (repositórios públicos) ou somente para pessoas escolhidas a dedo (repositórios privados).

- Desenvolvimento direto de Software:
  - Editor de código simples.
  - IDE com o recente GitHub Copilot.
  - A aba Wiki de todo repositório, que permite aos colaboradores documentarem o projeto no formato de uma página Wiki.

- Comunicação:
  - A aba Discussions de todo repositório, que permite ao dono abrir um Fórum integrado ao projeto.
  - A aba Issues de todo repositório, que permite aos colaboradores levantar questões, problemas e sugestões
  - A aba Pull Requests que possibilita aos colaboradores proporem uma nova versão no repositório, com as alterações já feitas.

- Deploy:
  - Possibilidade de criar *Releases* do seu projeto, salvando todas as alterações até aquele momento num arquivo comprimido.
  - Integração Contínua através de ferramentas disponibilizadas e implementadas via GitHub Actions.
  - Disponibilização de Lints e ferramentas de teste também através do Git Hub Action.
  - Criação de um site estático de apresentação do seu produto através do GitHub Pages.

Sem contar diversas outras funcionalidades disponibilidas pelo próprio GitHub ou até mesmo através de extensões de terceiros. Alguns recursos de terceiros famosos são o ZenHub, GitLab e o Code Climate.

# Usando o Git

O Git é uma ferramenta de Linha de Comando e funciona melhor através de terminais de sistemas Unix. Se este é o seu caso, instale o Git (o comando para isso depende de qual distribuição do Linux você usa, por isso é melhor pesquisar o comado do seu caso específico).

## Apresentando-se ao Git

Quando trabalhando com o Git em individual, é importante identificar quem você é para o programa. Para fazer isso, digite:

    git config --global user.name "<nome>"
Para inserir um nome. Também use o seguinte comando para associar um email.

    git config --gloval user.email "<email>"

Por fim, digite os mesmos comandos sem determinar um parâmetro para checar as informações.

## Integrando seu Git e GitHub

Ao adicionar o mesmo email e nome da conta do seu GitHub, as contas do seu Git e GitHub estarão conectadas, mas verá que ao tentar "acessar" repositórios privados do GitHub pelo Git, um código de autenticação será pedido e rejeitado independente do que colocar. Isso acontece porque o sistema de autenticação por terminal Git para o GitHub a principio foi retirado em 2018. Para contornar esse problema e acessar repositórios privados, você precisa instalar o GitHub CLI, uma interface própria do GitHub para terminal. Instale para o seu sistema operacional e autentique-se com o comando:

    gh auth login

Ao seguir os passos do GitHub CLI após esse comando, você poderá importar os seus repositórios privados sem mais complicações.

## Acesso a um repositório

### Opção 1: Criar Repositório

Para criar um repositório vazio, crie uma pasta, acesse ela através do terminal e digite:
    
    git init

Isso criará *.git*, que iniciará um repositório Git local em seu computador, abrangendo tudo que estiver dentro dessa pasta. Você também pode usar esse comando numa pasta já usada e cheia de arquivos, não tem problema.

### Opção 2: Importar repositório

Você pode muito bem também importar um repositório direto do GitHub. Para fazer isso, entre num repositório remoto do GitHub e selecione o botão *Code*. As três opções (HTTPS, SSH e GITHUB CLI) são todas formas de se importar um repositório, mas vamos nos conter com a mais fácil por enquanto, a HTTPS.

1. Copie a URL disponibilizada no HTTPS.
2. Acesse atraveś do terminal o local que você quer impotar o seu repositório. Não é necessário criar uma nova pasta como na Opção 1, a importação já cria a pasta para vocẽ.
3. Digite (substituindo a "< url >" pela URL do HTTPS)
```    
git clone <url>
```
4. Espere o loading e pronto, vocẽ terá feito uma **cópia** local o seu repositório remoto.

<a href="https://www.mmfava.com/talk/2021-08-14-git-github-rstudio/images/fig/repo_remoto.jpg"><img width=100% src="https://www.mmfava.com/talk/2021-08-14-git-github-rstudio/images/fig/repo_remoto.jpg" alt="Repositório local vs Repositório remoto"> </a>

## Mudança/Criação de Branches

Uma *branch* é uma ramificação do seu repositório. Vocẽ pode colocar uma série de alterações que você não tem certeza se irá realmente adicionar no projeto numa branch alternativa por exemplo. Existem várias utilidades para branches, portanto saber usá-las é imprescindível.

Para checar quais branches seu repositório possui e em qual você está, use:

    git branch

Para trocar de branch no Git, digite no terminal num local pertencente ao seu repositório o comando (substitua "< nome da branch >" pelo nome da sua branch):

    git switch <nome da branch>
Ou:

    git checkout -b <nome da branch>

O comando anterior criará uma nova branch caso uma branch com o nome inserido ainda não existir.

## Adição de mudanças no repositório.

É comum editores de texto não salvarem automaticamente suas mudanças e o mesmo acontece no Git. O Git apresenta uma interface (não gráfica) básica de aplicação de mudanças, cujas características precisam ser detalhadas.

Qualquer mudança nos arquivo é salva normalmente, porém elas não são automaticamente registradas no repositório como aplicáveis. Visto isso, as alterações podem ter 3 estados:
- Mudanças disponíveis;
- Mudanças prontas para submição; e
- Mudanças submetidas.

Ao fazer uma alteração no arquivo, toda alteração torna-se **disponível** para registramento. Você pode selecionar elas para serem submetidas através do comando:

    git add <caminho e nome do arquivo>

As alterações são identificadas pelos nomes dos arquivos em que foram feitas. Se mais de uma alteração foi feita em um mesmo arquivo e **elas estiverem no mesmo estado de sumissão**, as alterações se somam e são representadas pelo Git como somente uma alteração.

É possível trocar o nome da alteração por um ponto final no comando *git add*. Ao fazer isso, todas as alterações *disponíveis* mudarão para *prontas para submissão*.

Para submeter as alterações *prontas para submissão* ao seu repositório local, use o comando *git commit*. O commit seria equivalente a um *botão confirmar*. O comando pode ter várias formas, mas a mais comum e básica é:

    git commit -m "<mensagem>"

Onde *< mensagem>* será trocada por um texto que descreva que mudanças foram adicionadas.

Por fim, para ver se suas alterações foram submetidas, use o comando:

    git status

Tal comando permite com que você veja uma série de informações sobre a branch atual em que você está, incluindo as alterações pendentes e o estado delas. Alterações submetidas não estarão mais pendentes.


**AVISO: É importante ressaltar que TODAS as alterações e submissões são exclusivas da branch em que você está. Se você submeter alterações na branch X, a branch Y continuará do inalterada. Para interagir mudanças feitas numa branch com a outra, veja mais na [sessão Merge](#exportandomesclando-alterações-entre-branches)**


<a href="https://uidaholib.github.io/get-git/images/workflow.png"><img width=100% src="https://uidaholib.github.io/get-git/images/workflow.png" alt="Transições do alterações entre locais"> </a>


## Atualizar um repositório remoto com as alterações de um repositório local.

Um repositório Git é local e está somente na sua máquina, mesmo quando importado de um repositório remoto no GitHub. É importante conseguir atualizar alterações feitas num repositório local em um remoto a fim de manter seus colaboradores e colegas de equipe atualzados.

### Para repositórios importados do GitHub.

Ao usar o *git push < url>*, você gerou uma conexão entre os repositórios local e remoto. Portanto, para aplicar as alterações do local para o remoto, basta um:

    git push

Entretanto, caso esta seja a sua primeira vez fazendo um push, talvez você tenha que escrever antes o seguinte comando para escolher a branch (pode ser um nome de uma branch que não existe no remoto ainda) em que as alterações locais serão exportadas.:

    git push --set-upstream origin <branch atual>

Não se preocupe muito com push upstream, use o push normal e se estiver faltando uma branch upstream, o git avisará e irá sugerir o comando para você.

### Para repositórios locais não importados

Ao criar um repositório vazio, o GitHub normalmente te dá as instruções de como exportar um repositório local não conectado ao novo repositório remoto criado.

Em resumo, você adiciona uma conexão com o comando:

    git remote add origin <url>.git

Caso seu repositório local já possui uma branch e alterações submetidas, basta só seguir os passos da [sessão anterior](#para-repositórios-importados-do-github)

## Exportando/mesclando alterações entre branches

Muitas vezes você quer exportar/importar alterações entre ramificações ao invés de repositórios. Ramificações muitas vezes são criadas para testar a adição de novos recursos sem afetar o desempenho do produto oficial. Quando os novos recursos são implementados e aprovados, desenvolvedores querem adicioná-los à ramificação principal.

O Git lida com isso através do comando:

    git merge <nome da branch>

O comando exportará as alterações da branch descrita para a ramificação em que o git atualmente se encontra. Por isso tenha certeza de checar sua branch com *git branch*

O Git faz automaticamente um *git merge* quando você usa um *git pull*.

O GitHub também usa o git merge com uma ferramenta gráfica em seu site chamada *Pull Request*. Para iniciantes, o Pull Request é muito mais intuitivo e controlado, portanto recomendo sua utilização no lugar do git merge em boa parte das situações básicas.

    CURIOSIDADE: o comando git pull é na verdade o mesmo que chamar um git fetch, que importa as alterações de outro repositório, e logo depois um git merge, que mescla as alterações importadas no repositório. O merge pode ser usado em operações entre repositórios porque elas nada mais são do que operações entre branches de diferentes repositórios.

## Resolvendo conflitos de versões

Caso você esteja importando ou exportando alterações entre repositórios remotos e locais, principalmente em trabalhos em grupo, você em pouco tempo se deraparará com conflitos de versões.

Conflitos acontecem quando o histórico de alterações de dois repositórios ou branches é pouco ou nada parecido, mas alguém quer exportar ou importar alterações entre ambos. O Pull Request não consegue lidar muito bem com muitos desses conflitos, portanto sobra para você lidar com eles no próprio Git.

Para lidar com conflitos assim, existem várias ferramentas, mas o que irei mostrar aqui é através da mudança de estratégia de mesclagem.

Normalmente o Git usa a estratégia de *merge* com *fast foward*. Essa estratégia só cria um link da branch a ser importada para atual e funciona muito bem quando não há demais alterações na branch atual desde a criação da branch a ser mesclada. Entretanto, se houver alterações na branch atual que não haviam sido adicionadas na branch a ser mesclada, um git merge normal, ou seja, com fast foward, gerará erro e não mesclará nada.

Para resolver isso, alguns usam a estratégia de tirar o fast foward, usando um:

    git merge --no-ff

Mas a estratégia mais comum para o caso é realmente um:

    git rebase

A diferença entre merge e rebase é que o merge tenta posicionar as alterações da branch a ser mesclada relacionando a última alteração ao final da branch principal. Já um rebase vai pegar as alterações da ramificação a ser mesclada, copiá-las e tentar aplicá-las no final da branch atual. Como um rebase copia e reaplica as alterações, ela normalmente resolve problemas que o merge não resolve, mas acaba reestruturando o histórico de mudanças como efeito colateral. Por isso tome bastante cuidado ao user o rebase em trabalhos em grupos com pessoas que pouco conhece, principalmente em projetos abertos, visto que a colaboração muitas vezes é contabilizada pelo histórico.

<a href="https://miro.medium.com/max/868/1*g48HJkKNsZwNlWEM6Z82ig.jpeg"><img src="https://miro.medium.com/max/868/1*g48HJkKNsZwNlWEM6Z82ig.jpeg" alt="Merge vs Rebase"> </a>

# Usando o GitHub

## Recursos básicos

É importante ressaltar que não vale a pena aprofundar nosso tutorial em algumas ferramentas básicas do GitHub. Lembrem-se que o mesmo é uma ferramenta de interface gráfica, portanto muitas funcionalidades já são muito bem explicadas através de técnicas da UI e UX. Algumas funcionalidades que não serão aprofundadas são:

<table>
    <tr>
        <th>Funcionalidade</th>
        <th>Como usar?</th>
    </tr>
    <tr>
        <td>Cadastro/Login</td>
        <td>Clique nos botões "Sign in" ou "Sign up" no menu principal do GitHub e siga as intruções lá contidas. Se for para autenticar-se no GitHub CLI, instale-o e digite <i>gh auth login</i></td>
    </tr>
    <tr>
        <td>Criar um perfil decente/interativo/profissional/bonito</td>
        <td>O seu perfil possui um ReadMe.md, lá você pode editar seu perfil em geral. Mas para fazer um perfil elaborado, é melhor procurar tutoriais específicos para isso.</td>
    </tr>
    <tr>
        <td>Criar repositório público ou privado</td>
        <td>Aperte no botão de criar repositório e escolha qual tipo de repositório você quer.</td>
    </tr>
    <tr>
        <td>Editar as permissões, integrantes, visibilidade do repositório ou apagá-lo</td>
        <td>Ao ser administrador de um repositório, vá na aba <i>Settings</i> e você verá todas as opções.</td>
    </tr>
    <tr>
        <td>Editar arquivos dos repositórios, criar novos arquivos ou enviar um arquivo novo para o repositório</td>
        <td>Há botões próprios para todas essas funções, basta achá-los. Formas alternativas são descritas no tutorial de Git</td>
    </tr>
</table>

## Repositórios

Existem alguns artefatos altamente recomendados para ser ter em qualquer aplicação, sendo esses:
- .gitignore;
- Licença; e
- ReadMe.md

### .gitignore

Arquivos .gitignore são únicos em cada repositório e tem o importante dever de instruir o Git a ignorar a adição de novas alterações. Arquivos assim são importantes no em qualquer projeto Git ou GitHub para impedir o desenvolvedor de comparilhar arquivos temporários, cache, configurações próprias do seu sistema de desenvolvimento e outros artefatos que não deveriam ser incluídos.

O GitHub possui alguns modelos de .gitignore para muitas linguagem de programação e framework, mas saiba que é extremamente fácil construir um .gitignore. Você só cria um arquivo com este nome e escreve o caminho e nome de um arquivo a ser ignorado. Um arquivo por linha. Exemplo:

    .__pycache__/
    .vscode/
    a.out
    testes/desabafo.txt

Claro que há .gitignore mais elaborado, mas é o bastante por agora.

### Licença

No caso de projetos reais, a licença é extremamente importante para delimitar as permissões que as outras pessoas têm sobre o seu produtos. Como o GitHub foca bastante em projetos Open Source, muitas das licenças oferecidas por padrão são dessa área, sendo uma etapa importante desses projetos. Inclusive, projetos que não pretendem ser Open Source acabam por possuir muitas limitações no GitHub.

Uma comparação das licenças disponíveis é bem descrita em muitos locais da internet, inclusive no próprio GitHub.

Caso tenha dúvidas em que licença usar para o seu projeto, visite o [site recomendado pelo próprio GitHub](https://choosealicense.com/).

### Read Me

A capa de qualquer repositórios no GitHub é o ReadMe. Sendo um arquivo em formato Markdown (.md), é extremamente importante que o seu repositório possua um ReadMe.md elaborado, seja seu projeto algo privado ou público. Um ReadMe bem escrito costuma ter alguns elementos em comum:

- **Uma descrição breve do que seria o projeto**, qual sua finalidade e objetivo. Alguns possuem até uma ilustração da logo do projeto.
- **Instruções de instalação e acesso do produto**, principalmente se você planeja que alguém acesse seus conteúdos. Essa parte em específico pode ser bem detalhada inclusive.
- **Tecnologias e técnicas usadas** são importantes de serem adicionadas, pois dá uma dimensão da pilha de tecnologias que eles precisam ter conhecimento para colaborar com o projeto.
- Instruções de **Como contribuir** com o projeto.

Você também pode inserir mais o que quiser no Readme, não sinta-se preso a esse padrão. O importante é que qualquer tipo de usuário entenda o que fazer a respeito do seu projeto.

    AVISO: o Readme, assim como o repositório, normalmente são vistos por desenvolvedores e possíveis colaboradores futuros. Sempre tenha em mente o público que acessa o GitHUb. Visto isso, um Readme não é muito adequado para uma capa de venda do produto, algo assim seria melhor feito em páginas web, como através do GitHub Pages.

## Organização e Comunicação com Issues

A aba *Issues* está presente em qualquer repositório GitHub. Ela pode ser personalizada para servir a diversos propósitos, todos focados na comunicação dos colaboradores ou equipe. Em outras palavras, é o primeiro recurso deste tutorial com influências da cultura DevOps. O GitHub possui várias ferramentas DevOps, já que muitos das pequenas equipes de código aberto possuem uma maior produtividade e integração ao adotar essa cultura.

Issues são basicamente "questões" levantadas no projeto. Elas possuem dois estados: aberta e fechada.

<a href="https://i0.wp.com/user-images.githubusercontent.com/22751162/120507746-b259cf00-c38c-11eb-8d2d-942a8c756ec8.png?ssl=1"><img src="https://i0.wp.com/user-images.githubusercontent.com/22751162/120507746-b259cf00-c38c-11eb-8d2d-942a8c756ec8.png?ssl=1" alt="Issues no GitHub"> </a>


As issues oferecem Templates, sendo esta uma métrica para julgar se o seu projeto está bem estruturado para a recepção da comunidade Open Source. Os templates de issue que você adicinou ou escreveu para o repositório ficam disponíveis para qualquer usuário usar ao tentar adicionar uma issue.

Nesses Templates, podemos ver alguns usos das Issues, sendo eles:

### Reportar bugs

Todo produto de software possui bugs e é importante que os usuários tenham alguma forma de denunciá-los. Ter conhecimento de quais bugs aflingem seu produto é essencial para a cultura DevOps, pois possibilita que o time coloque a correção na sua lista de tarefas para um conserto ágil com os colaboradores.

Ao reportar um bug, é interessante que o usuário explique o bug, mostre como replicá-lo (caso possível) e insira algumas informações do sistema utilizado que ele considera relevante para a situação. O sistema operacional usado e a versão do software disponibilizado em que houve o bug são alguns exemplos de informações normalmente relevantes para um desenvolvedor. Trate de usar um template que instrua muito bem o usuário a escrever essas informações.

### Registrar recursos a serem desenvolvidos
Funcionalidades são sugeridas por alguém da equipe e muitas vezes implementada por algum outro contribuidor, portanto é essencial que o item esteja bem descrito. Um template simples de adição funcionalidades costuma conter:
- Descrição do recurso.
- Tarefas e etapas que você considera importante para a adição do componente. Marque elas num formato de CheckList, pois as Issues reconhecem e rastreiam quantas tarefas já foram feitas.
- Critérios de Aprovação, em que se detalha se o recurso precisa passar por alguma ferramenta de teste e quais requisitos de qualidade o produto deve ter.

É comum que Issues de "recursos a implementar" sejam criadas no repositório sem que ninguém tenha se proposto a fazer ainda. Até que um colaborador comenta na issue se propondo a trabalhar na funcionalidade, descreve a solução que ele pensou e por fim tenta implementar a funcionalidade ao pedir um pedido de mesclagem (Pull Request)

### Propor ideias de recursos

Assim como há uma issue para relatar bugs, qualquer pessoa pode sugerir funcionaldades ao projeto. Disso surgem ideias vagas e algumas propostas muito bem pensadas e detalhadas. A proposta de funcionalidades também é adequada para ser feita através do fórum criado pela aba Discussions, depende de qual ambiente a equipe do projeto prefere.

### Registrar decisões da equipe
É importante registrar a tomada de decisões importantes sobre o projeto em algum lugar e a aba Issues acaba sendo um lugar adequado para isso. A aba Discussions também é adequada para esta função.

<br><br>

O GitHub também oferece o uso de ***tags*** para classificar as issues. É sugerido que você faça tags para as diferentes áreas de desenvolvimento do seu projetos, tecnologias utilizadas, níveis de dificuldade da issue e níveis de urgência. Saiba que você pode atribuir quantas tags quiser em uma issue.

As ***Milestones*** são outra forma de personalizar sua experiência com issues. Cada Milestone possui um prazo de término e uma barra de progresso que sobe a medida que você termina issues marcadas com a Milestone. É um recurso simples que adiciona um tom de responsabilidade e planejamento ao GitHub.

Há também várias extensões que podem ser adicionadas ao GitHub para adicionar mais recursos às issues. Uma extensão famosa é o [ZenHub](https://www.zenhub.com/), ferramenta capaz de adicionar estimativas de dificuldade, dependências e épicos para cada issue, além de gerar mais análises de dados que o GitHub não gera.

## Solicitando alterações com Pull Requests

De forma bastante rasa, Pull Requests são equivalentes ao comando *git merge*, só que representado numa interface gŕafica. Você cria uma nova branch ou fork, escreve o código, adiciona e confirma as alterações feitas e por fim insere sua atualização na branch principal.

Mas a verdade é que o Pull Request é muito mais que um simples comando de mesclagem, ele segue a filosofia DevOps e o método XP(Extreme Programming), implementando alguns elementos que ambas as influências acham essenciais no desenvolvimento de software.

Uma Pull Request precisa ser revisada e aceita por outros colaboradores para de fato ser aplicada. Esses e mais alguns recursos garantem um bom trabalho em equipe para projetos de código aberto, cujas mudanças podem ser **propostas** por qualquer um. Pull Requests não aceitas são fechadas sem mesclagem nenhuma e normalmente carregam um feedback do revisor descrevendo qual o problema das alterações.

<a href="https://miro.medium.com/max/1400/0*K8P35YttgYS3TrU1"><img src="https://miro.medium.com/max/1400/0*K8P35YttgYS3TrU1" alt="Pull Request"> </a>

Normalmente Pull Requests também possuem um template simples para que os colaboradores descrevam o que foi feito.

### Recursos
- Pareamento/Revisão: o pareamento é uma ferramenta importada do método XP. Acredita-se que a qualidade do código aumenta quando fazemos sabendo que alguém vai ler e revisar. Por isso uma das bases do XP é que todo código deve ter uma revisão adequada e troca de feedback entre os envolvidos. O GitHub incorpora essa prática ao exigir um corretor e permitir que não só ele veja as modificações feitas, como também possa comentar na própria Pull Request qual seu julgamento sobre as mudanças feitas.

- Revisão alterações: você têm acesso a todos os *commits* que seriam adicionados caso a Pull Request fosse aceita.

- Ver alterações nos próprios arquivos: é uma versão mais detalhada da revisão de alterações, não só mostrando os commits que seriam adicionados, como também o que cada um desses mudou no código em si, linha por linha.

- Checagem(veja a aba [Actions](#GitHubActions)): para evitar que mesclagens mal revisadas quebrem o funcionamento de um código, desenvolvedores adicionam testes ao GitHub. Ou seja, toda Pull Request deve passar por todos os testes ativos de um repositório para serem aceitas, assim como conflitos com mesclagens pelo Git. Um revisor pode ver quais testes não deram certo e buscar mais sobre para dar um feedback completo ao contribuidor.

<br>

Pull Requests também podem receber mais recursos com extensões, como a do ZenHub. Esta adiciona dependências, issues relacionadas, estimativas de dificuldade, épicos, sprints e muito mais.

## Wiki, Projects e Discussions

A aba **Wiki** é um lugar onde você pode adicionar uma página Wiki ao seu repositório. Escrita em Markdown, com a capacidade de receber centenas de páginas e um menu lateral que as organiza, a aba é ótimo lugar para guardar a documentação do seu site. Muitas pessoas entretanto preferem usar o GitHub Pages, com ferramentas como o Jekkins e MkDocs, dando um incremento nos design e funcionalidade da sua documentação.

A aba **Projects** serve como uma forma de organizar sua equipe através das diversas issues que normalmente um projeto recebe.

É difícil ver prazos, quais issues já estão sendo feitas por alguém e quais são mais urgentes na aba Issues. Até porque, a aba não é feita para ver informações das issues, mas sim listá-las. A fim de facilitar a organização dos desenvolvedores, a aba Projects gera testruturas que permitem uma fácil visualização e classificação das issues. Você pode criar uma tabela com prioridades, datas de entrega, envolvidos, tudo em colunas que podem ser visualizadas de uma vez só. Também pode criar um Kanban, clássica ferramenta de gerenciamento de equipe sobre atividades, com os cartões sendo as issues e cada coluna um estado da Issue.

<a href="https://github.githubassets.com/images/modules/site/issues/issue-custom-fields-reduced-motion.jpg"><img src="https://github.githubassets.com/images/modules/site/issues/issue-custom-fields-reduced-motion.jpg" alt="Tabela de Project no GitHub"> </a>

<a href="https://github.githubassets.com/images/modules/site/issues/illo/issues-board.png"><img src="https://github.githubassets.com/images/modules/site/issues/illo/issues-board.png" alt="Kanban's Project no GitHub"> </a>

Estabelecido como uma ferramenta de fórum para a comunidade do seu repositório, a aba **Discussions** tem grande utilidade para projetos Open Source.

Para quem não conhece, fórums são ambientes de conversa, parecidos com chats, mas separados por tópicos/discussão. Cada tópico é uma conversa diferente iniciada por uma pergunta, relato, afirmação, sugestão. Outras pessoas podem comentar sobre o tópico, reagir a elas (com emojis) ou destacá-las apertando numa seta. No GitHub, os tópicos/discussões são separadas em categorias, ajudando contribuídores que querem achar discussões específicas.

A descrição do funcionamento da aba Discussions é um pouco similar às issues, mas a grande diferença é que o foco nas Discussions é justamente a discussão entre as pessoas, enquanto as Issues focam em relatar problemas e registrar novas funcionalidades. Por isso as Discussions muitas vezes são usadas para sugerir funcionalidades ao invés da aba Issues.

<a href="https://www.freecodecamp.org/news/content/images/2022/05/screely-1652334880222-1.png"><img src="https://www.freecodecamp.org/news/content/images/2022/05/screely-1652334880222-1.png" alt="GitHub Discussions"> </a>

As três ferramentas são integradas com o GitHub e fornecem uma centralização de tudo relacionado ao seu projeto em um único lugar. Entretanto, como todas essas ferramentas não são o foco do GitHub, elas acabam sendo básicas em relação ao serviço que oferecem. Outras ferramentas e extensões especializadas nesses serviços possuem funcionalidades mais avançadas e flexíveis. Se é melhor usar um software externo ou não, depende do que for mais adequado ao seu projeto.

## Estatísticas com Insights

<a href="https://cdn.ttgtmedia.com/rms/editorial/012119_TSS_GitHub-contributors-insight_mobile.png"><img src="https://cdn.ttgtmedia.com/rms/editorial/012119_TSS_GitHub-contributors-insight_mobile.png"> </a>


A aba Insights é responsável por demonstrar diversos *insights* do projeto, ou seja, diversas estatísticas com base nas atividades no repositório. É uma aba essencial principalmente para os gestores do projeto e para a criação de projetos Open Source.

A aba Insights possui dez categorias, sendo a maioria delas somente disponível se o seu repositório for público. As categorias são bem auto explicativas, então sugiro que você mesmo vá lá, explore e se divirta vendo as diferentes informações e gráficos apresentados.

Entretanto se você é novo em projetos Open Source, há uma categoria que é muito interessante de conferir, a *Community Standards*. Ela lista alguns pré requisitos para que o seu projeto Open Source tenha qualidade e atraia contribuídores no GitHub. Há várias sugestões ali de atividades que vimos e não vimos durante o tutorial, mas garanto que até as sugestões que parecem mais assustadoras e trabalhosas são bem simples graças a ajuda do GitHub. 

## Automação com GitHub Actions

O GitHub Actions é mais uma ferramenta focada em oferecer métodos mais ágeis de se desenvolver softwares em seu site. Com o foco em criar um ambiente de *integração contínua* (CI) e *entrega contínua* (CD), vindos da cultura DevOps, o GitHub Actions permite às equipes criem fluxos de trabalho nas alterações enviadas ao repositório.

Um fluxo de trabalho (ou *workflow*) seria uma série de tarefas que devem ser seguidas ao realizar alguma atividade. Por exemplo: em empresas, toda alteração feita no código de um software pré existente deve sofrer uma série de testes para garantir que a aplicação não fique fora do ar. É possível aplicar fluxos de trabalho em quaisquer eventos que ocorram em seu repositório, sejam as alterações propostas em Pull Requests ou descrições de problemas nas issues. 



Cada etapa de um fluxo de trabalho é descrita num único arquivo *.yml*, sendo que todas podem conter comandos para serem executados no terminal. O uso de comandos no terminal abre a possibilidade ao uso de softwares CLI e chamada de scripts, que por sua vez possibilitam a execução de código em quaisquer linguagens. Com uma variedade de personalização tão grande, essa é sem dúvidas uma das ferramentas mais importantes do GitHub.

<a href="https://docs.github.com/assets/cb-63715/images/help/images/workflow-graph.png"><img src="https://docs.github.com/assets/cb-63715/images/help/images/workflow-graph.png"> </a>

### Como criar fluxos de trabalho?

Para criar um fluxo de trabalho:

1. Selecione a aba Actions.
2. Escolha um modelo de workflow que melhor represente o que você pretende fazer. O GitHub possui uma grande variedade deles, mas caso não um que goste, faça um do zero clicando no respectivo link no site.
3. Ao clicar, ele dará a opção de você editar o fluxo. Caso esteja satisfeito, aplique sua modificação.

Perceba que é bem fácil de entender o que cada parte do código *.yml* é:

- *name*: nome do fluxo ou etapa.
- *on*: quando ocorrerá o workflow.
- *jobs*: as etapas que o fluxo de trabalho deve percorrer quando for ativado.
    - *deploy*: etapa de lançamento de uma aplicação.
    - *build*: etapa de montagem de uma aplicação no computador.
- *steps*: as tarefas que uma etapa do fluxo deve seguir.
- *run*: executa um comando no terminal.

Há mais algumas palavras usadas nos fluxos do GitHub, mas perceba que não é difícil de entender e configurar. Sem contar que ao configurar um fluxo, você pode procurar por trechos ou etapas de fluxo num menu lateral.

As possibilidades são imensas. Alguns dos fluxos de trabalhos mais aplicados são:

### Adiçao em issues:

Em projetos Open Source, sempre há um certo fluxo de issues sendo postadas, sejam essas sendo de sugestões de funcionalidades ou relato de bugs. Para facilitar a vida das contribuídores, é possível criar fluxos que a cada inserção de issues, o GitHub classifica a issue com uma tag "Não lida" ou "Urgente".

Você também pode adicionar um script que leia as informações básicas do sistema do usuário quando um alguém cria uma issue e as adicione em sua descrição.

### Testes

Uma das ferramentas mais comuns às entregas contínuas são o uso de testes que exigem critérios específicos para gerarem um resultado limpo de bugs. Há centenas de fluxos no GitHub Actions que permitem a chamada dos seus scripts de teste quando há solicitações de Pull Requests. Isso poupa o trabalho do contribuidor ter que importar e testar o código por si mesmo, sem contar que já dá uma respota imediata parcial se a Pull Request será ou não aceita.


### Lints

Lints são ferramentas que checam se as políticas e padrões usados no desenvolvimento e certas linguagens e frameworks estão sendo respeitadas. É um recurso essencial para garantir uma qualidade contínua nos códigos produzidos, sem contar que ajuda em evitar bugs e no entendimento do código por outros desenvolvedores. Há várias bibliotecas e aplicativos de linters disponíveis por aí e o GitHub Actions consegue facilmente criar um Workflow que chame essas ferramentas. Há vários pré-prontos por sinal.

### GitHub Pages

Sendo um recurso do Actions usado por todo tipo de desenvolvedor, o GitHub Pages é uma forma de hospedar e lançar seus sites estáticos sem pagar nada. É possível lançar um site no Pages através de um arquivo Html/CSS/Javascript, de templates como os do Jekylls e MkDocs e até de linguagens próprias como Hugo.

Criar uma página com o Pages é na verdade bem mais fácil do que qualquer outro fluxo do Actions, principalmente se não estiver usando um framework. É só:
1. Adicionar seu arquivos do site no diretório superior ou numa pasta docs.
2. Ir na aba de Configurações e selecionar a aba Pages.
3. Selecionar a branch e a pasta que você colocou o index.html do seu site.
4. Espere o deploy ser realizado (demora uns 2 minutos) e um link será gerado na aba Actions para o seu site.

Caso o index.html do seu site não seja um filho direto da pasta docs ou da /(root), prefira fazer isso pelo através da aba Actions do repositório.
<br><br><br>

# Conclusão

Assim encerramos esse longo post. De fato há vários outros recursos interessantes tanto no Git como no GitHub que poderiam entrar aqui, mas eu tentei condensar ao máximo para as coisas que de fato foram úteis para mim ao longo do aprendizado. Espero que alguém se beneficie do que escrevi e que meus amigos não tenham mais tanto medo do Git e GitHub.
Obrigado.
<br><br><br>
Autor: Raphael Mendes da Silva

Ano: 2023

Cargo: Estudante da UnB
