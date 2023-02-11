# Git

Git é uma ferramenta de controle de versionamento. Muitos equipes de software (e até em outras áreas) o usa a fim de gerar uma organização melhor de seus projetos, principalmente quando várias pessoas estão trabalhando num mesmo arquivo.

## Introdução ao Git

O Git cria em sua máquina local um *repositório*, estrutura esta que serve para armazenar alterações. De forma mais detalhada, o Git cri uma pasta *.git* no computador. Todo arquivo e pasta no mesmo no mesmo local do *.git* ou com seus parentes superiores neste local irão estar dentro de um repositório, que irá registrar as alterações feitas no local, sejam elas criações de documentos, apagamento de arquivos, edição de textos, etc.

![Exemplo de Repositório Git]()

Conceitos Importantes:
- Repositórios (locais):
- Alterações:
- Pasta *.git*:

## Introdução ao GitHub

Nada diferente de quaisquer outros *Hubs de ferramentas*, o GitHub é um centro online de repositórios Git. De forma mais detalhada, você acessa o site do GitHub, cria a sua conta e pode criar e adicionar repositórios Git de forma remota, fora de seu computador, através de um link que pode ser acessado por outras pessoas mundo afora. Ainda que sejam realmente repositórios Git, vamos denominar aqui todo repositório no GitHub de **repositório remoto** para facilitar a compreensão.

O GitHub entretanto tornou-se tão famoso que estendeu suas funcionalidades de ser somente um *Hub do Git* para uma ferramenta completa de edição de repositórios Git remotamente, um IDE de código completo (através do recente GitHub Copilot) e muito mais. Você pode criar seus repositórios arquivos e mudanças, tudo pelo próprio GitHub e sem tocar um dedo diretamente na interface própria do Git. Toda essa funcionalidade do GitHub, ainda que bastante benéfica, é o que faz as pessoas confundirem o Git e GitHub, visto que a maioria dos iniciantes em programação só mexem no GitHub e acabam não conhecendo o que de fato seria o Git nisso tudo. O dever desse artigo é justamente conseguir separar o conceito dessas duas ferramentas para você e te deixar apto o bastante para usar ambas as ferramentas juntas ou separadamente.

### Funcionalidades do GitHub

Boa parte das funcionalidades do GitHub se voltam a projetos de Código Aberto (Open Source), limitando algumas das funcionalidades para projetos que pretendem ter seus códigos privados.

- Princpais:
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

![Repositório Local e Remoto]()

## Mudança/Criação e Branches

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

**AVISO: É importante ressaltar que TODAS as alterações e submissões são exclusivas da branch em que você está. Se você submeter alterações na branch X, a branch Y continuará do inalterada. Para interagir mudanças feitas numa branch com a outra, veja mais na [sessão Merge](#merge)**

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

CURIOSIDADE: o comando *git pull* é na verdade o mesmo que chamar um *git fetch*, que importa as alterações de outro repositório, e logo depois um *git merge*, que mescla as alterações importadas no repositório. O merge pode ser usado em operações entre repositórios porque elas nada mais são do que operações entre branches de diferentes repositórios.

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

![Merge vs Rebase](data:image/png;base64,iVBORw0KGgoAAAANSUhEUgAAAQgAAAC/CAMAAAA1kLK0AAABgFBMVEX///8AAAD//wD/AP9LTE4mJyvu7u4gISWurq+UlJXY2dkZGh8iIyf7+/v4+PhTU1V3eHno6OgNDxXg4OAAAAt9fX8UFRouLzKhoQDl5eUaGyAAAAaXl5mGhoj6+gBnaGq+vr9MAExTAFPLy8yKipFycgDs7ADW1gCamgCTkwBZWWZbXF62trdCQ0bNAM33APfXANcmJgA3NwA7OzssACzkAOTu7gDMzAC+AL5TUwB+fgA7OwBAQFQAABtra3nY2ADAwAAdHQCkpKVDUEMhACFmAGaysgBMTABfXwCUAJQTABMbABsAHQAAABjNzdCPl4+HAIehAKHU0L8dHQwlJR4cHDcoKEG3twBxcX8yMkITEy0zPjM4ADhYYlh6AHooOihoaACkqqQAEAB5g3k2SzYAKQBldGVJSVshIS8ZGTcAFACFjYVdXWtHWkc7SDsPKg9xZ1e9uLGfl4gsIw8VAAAOHStRSTlEVV7t7N0xQUuJg3AmGA2Zpa5GPDIiDQBqe4O1vgz4AAAOwElEQVR4nO1dDVvUxhbOCJvsZjfZzccm7pJsAlmosLsirIoiFyFWBGtBrVZogRbbqr3VW9daFT96//qdfOgDmGRyZxKXj7yPj8JjknPyZnLmzHlnJhQVE3zcA4kgqBbZBYxqMo6EghftlC24YEGe7ALMYDKOhIIGhZQtuCAmIpcR4SEjwkdGhI+MCB8ZET4yInwcHyLaZBf4AkRoKVtwwYLyKtEFcrmUEz8BdAmfFRr0Ks8CEZ9wmqUpVRlMcTAgmQINlLSzeKsudqqKaOKezw+W6rqqVBJ06QAkIDJGUSQMY0gIZaVeZEQW+wJ6joHn6wm6dAC8rjJ1BhCOC2NAF0sMw+Gfz4ISA8ykvAlCHnoI0h+I05pM9gKaxbpKJ+VNEDgTpPnufYJgEOYRGugk5EoIuMKX6T65PGG7s/BDTDzQeSllC46Rp4vT3zUJLqDdm56aSNNR+vH05enHqb59ENz9043GxdF57As0L481Gg9SDGbc90unTp1a+p4goMeBNnvKwRXc3FIA7vmn1xP1ai/sUdfCaMrZ69yYa+YB7suRP+Oef+pfiXq1F/NXXQNf4TfaWJi76JpZwCbidNpErH/lEZFem4NZm12Z925kGXdQszrlEfk4Ucc+QSh0m6m/GqsGACoLZqCVMxvYV5lwgsxVkEYPypstAAZrc+PQwvhGSsGStrtANmAGX7t/eXR6giDor0+NLv9ANo4PhFRQgVyFBPPzizcW59PplixDBqot+BbZGtHFBFZK/mmZZQC6HzM9nk+FBt5WATDSH87hQyoAwOh73rYUeOAsGBk69t48rSYSktIyyM7fD74NI0OrvffeeTm5SKm75U9Bg5GhcuC+D4n2qbece2f1HJD1Axl7gsVbug7jutWS4Xv3WdJ+OKrYdA6YXLsDuwnz8/9LjAjeYOoGA8RKUC93OIholZiyCNSDjcFFckRoRYZRWp83BheHgogC9LBomMFRMTEiNMAwpU7YxQ4DEa6HaiWkd0iMiJaoKEoxLPvrLxE07dy91pFFUQlTmoiJYK/dvPmj00fU9Kreah1CIqwfNzfra5ST3Gi2rod4SEoEC85OTp5DVsL7SIQEzg0MTA6vIQ4jJeLa2QGICz8hEuA+ap9brocDAFGHIySC33StDIwghhIsGCRLLXM53CLz156H2wj7Akx/MC044Ic9M9ejiCDXPgUC7fO85+HtKCLYdo1Q++TuXXCsTA5FNDxLETsVEu2zw9Sr+NrnNf/VEMIPkYBYbBFqnzubk9DK8B8RhwitIkOmfaok2ifrBcsoDx3tkyHVPnfA9jZAhGRdIdM+JVBiZGw3rZ+GR24iPGwnoH3SLBvR6rxDtCEy7dMqFrsEbvI06uREtE8WLRARa582kfZpoat8nEaufYIYVPJ91T7lGEmIkCeuDaOJoCemriw2CYKEdu/K1GN87bNYRh2RiPaJJIL7fanRaMwSaJ/LFxuNBVRuGA4kEdx9V/u8T1YgRhJBqn3WSLVPJBG25+EsWdkSSUTftU8kEb72eZVM+0QT0W/tE0lEMtonkoiqr32amAZYX/ucwDwfTUT+Z9fCz2R9PJIIGiy4yiK2hYnRBnxcALvbQAfLufHGqcb4HK4BD+juU9i4MTv9lCCTqE6NLt/H7+fR3Se3/t2NqfXITgOtWcZJqNgNM+q/+TKqbDJPkgAXB9E9L9+JLh1V0UOROAN5RKlOAKjcr0RSvC2JyCaBqFCxIoh8M7m8nqdBEa1LIojgc6hmhV+qq+i1XLGFTJUiibBBmS+3hZrEQgS1DBqIslqPUXxCFW+7OoIJfCJksc7EaLNRRBhAd/7yEfgKWa06wwyZSDMhRGg5RW3p+XwVmBKIbFf4RGhiiZHR/WI4EbTqOU9LVg2O5yvBFSKpC4lAh6IQIioGu9q2K62WIVG82o24Dj4RvFFnRHTPG0qECYC59/d8K/i4miLGmLoQRsS+INaKKJYRCDx8V4xxchgRVQD2j5HyYYGXLcWoaIQRsb/cooPQwiSJ5Me3YkgWwUTQXdA9UH/Ld0OuwO7soMuJ8YiA0bkbkreQEGGtre0gk4BgIiwADo5ICyFEbG2urAxfQ/VOIUrXQSIgEyCYCQIitkYuXdp+iIpjIav86NbBVloNJmLtuque/IIww4JK0A0eJELqfvYAfOSwN6DYcT289CviMBqUgy3YYH90NAKJ4G9OuvLJN5GE85AIMajlFdR9v1pACRxQwHatKh3MsQrjebgZNVThJC5c6ZKUnHt3nNfstWAiYkh+bFc0bFEMejfsfQm8HZxU8S1VbasK7rQ6X/JbiWhRUq7eKYihW4pwTndmDYqgY1Q0LaRF+GaGI4iQ1GJRCVa68jCRsvKFgu3089WQ7JNzEgF8pavutYiRCCLocr2uROWFMOHLi7aV1yrO9NHAQ65dcqyc/SnKFd4QS3UmqGWz3ZKidMtlxqDowfC51iYoMUO48wrWbjsenvst8iBNLjFRxWEddBDRWri1MjBwBzFfnK2K0S27ZpggSu22SVb5PRs5d2HlYXRuSdtDxZCM0YMORETPyP/y66+/oJxkO6hheLTOxFVIlK6dR4/WkL2ngZgoUk5mJRWvR3pCh829+oS8mYQbkRaiuaIN5Eh+FaUBw1dwY27OjO1SgInHcxsESpmJzEG4JlgEJOsQHUSPnx08Hh27+NU0vsjafjhzcWz2Cfb5aO1zYvZi4+IsdpncA7JmmV92auWNRdwqNA9cYWQW+4khi7fmZbecf9nEteACScRjT0c6jdsk2p4g1/gB8/wYSteMa2EmZYFnruGZwVa6lr6U5JcyEfMPvDV0uDqSdcMT5LAVIiQR2rhrYZxsrgiSCBY4KvCMjN0RP3GaRGPKxD0fSQQ95LwbCzFqjlFACzwmGF/6+Vv8iR70k8tLZ8IG6DGAVrqE3y+PL/+OzgMiEUPp4vPfk009WJ2YJ3haaCKghQ3iNV1xJD+JdFK6SqJ0xSEigfUasbTPvq7XiKN9JkGEiGaij0RwSWifSCN21U5C+0SDQPusSrnoIbYLMiJ4IIoqk4D2iQQ+EaJSZEQy7TMGWKNIon3GB4H2KRNqn/FQ6zCMjK19xgeZ9qkQaJ9xIRQJtM/46Jv2GR9SnEVGfe0+OSOW9kk6KT2m9qmRlfxyHfzM0lxb20GeTQdrcfGxNXznzghC++QgEQRDBScVUMVB3FKdo33ejlrJRDlaGg1idC0RWNtGap81vWWbMv7W9FzBqEqqgp4GFYwY2qfQ6lRMWSFKJD5qnxGEW0ARGYKlSFxnCKYC2EuAfKVrOKJOLjAKdFE2MS04iLXcURqsM4yC/47TMVOBYMTQPim66qzpIokRcbRPd8oZtobrgDMYJodbLPjUIuxWwQzLJ6SKUg+bCRMPz2Jon5AJkSRWOtNiRWyly4tiZ3+j9CEAwFC5YAZRWlMJ8wjht9uTk3cQyqIzA4RwxVScVCAEW472+W/oIW3ZlUEFsqG0Cm3JfVUtw/SP4gN3Qvk/wP8RQ/tcbTabJG8grTWbJvbZ7b3aJ83a1UFn3qjaqrZZXWa82GM+ffoU30JcNKeXFk4DfDssOLPw4EaSWwuy+WrXYQMOGUUn1WtOz1ydmSbV/FBYXXRq5WP4crLsLrC5kfRO5mxbL+cgE8D0l8ZMpbAL3F5MzJCpBqa3vmbsfqJeudBUplQfqq17ysuDNLdxpA6B0hWKtpPrwTg+7y2/G0t5Y0/iFjGaVovQRD3vBPGmt+rsdMpBwpz2YgR2bglcaXI5+W03OcuLW5KrxY3hrxqLiebiwtUlYGKfvwrOXJ25kma7NWG/dAaYKVrwYK2vN0nYppvr62ZSzgRb0Jpa2ttiZ0gSptlvDw4Jiil/RODIIPWPER0VZET4yIjwkRHhIyPCR0aEj4wIHxkRPnIdwrl/xwKO9qlga5/HBlzBqLD42ufxAdeRFQVf+zxGoG0S7fM4gavU8bXPYwUS7fOYwUjxc58Zjh7YR8+e7fTbiUMAE1y6cG77P/12o+/ggLsL+faJbxOmO+dlYPLPfjvSb+zc8SZq3eq3I/2GNeLycA61Tczxxy1nxtrkptlvP/oO4c/rl+6gNug/GWjv7HyBjzgfBXAnvhrho4NennYyQLTV63FCVsX2gSTCJFt/c2SAJOL5e9Ql3ph2nurZPEX1NJOi8lKbpu7aZhsObrWk57Kmh2Ai+DYLb0HS8hz1VredebOSc489bdX9YN3+6l4PGK8e7m69pl78rf/VpF6Ccq0HBsHf1F2gv3r9Be4hEQQT8QYwBufcxy71VtZfvof3VHlp9nbX3r2n3hlv92+YdneXuvuEosU3wJTugto/kCx4xptv6XfvJfavo9ImQohw1t5+aErsh/dvIQt/c/9Y1Itmb3eVlV7sStLb3b0H333tcEHXX4AuwzypvYNBxdnO9mbP+Z054kQ84WCrcO4jD4ngir0N+AbM871XYOdVLsfce7r3YIeIDUqQOef2aeofmKq+mqB7gP7w3vn9iCCMCBj6XjWd+3jehC2C/Zbnn1dg3Oy97s3xB+7OI4Ieonp/yeC/LhFvPgC5yEsfANgNuvxhhMoElbFdIoRXAEa856AI2tRbANT1uy/vlVadH/dv5Mzx7oOHfzja+5d6wUL2KOfLqEcig2fbq2EfNfSeuXMfPC/Q3o+8/4Eymka2dxgeSNdqf0HwqiwP5sg/rBYEwTpKAlq+XGeYwM2DTxoEAIlIeZnR0YBUVzLt04VZyuoRLmjTOhIdXNrYOn99+E+yD7QeC2w5W1tfIFrNfyzAelsSXNrqtyP9Rib5+eiteESceBG4Blwe7jzqtyN9xx/DF5wN+o9MzSA97IjfgK2Mhwx7gPwE+klBpn36yLRPH5n26SMjwkdGhI+MCB8ZET4yInxkRPjIiPCRY7JVfhTbtsK0zxMFXgVDnZS0z6OFdivTPj242ifhBqTHAzUm0z49WLmsHuFCyLRPF1vnr4/cMvvtRf+xteJqnyd+6UqmffrItE8fH7XP6C9enwB81D6jPuJxMuBpnw8zzY9qd89//QiPh/8B+XZ/rMzp5RoAAAAASUVORK5CYII=)

# Usando o GitHub

## Recursos básicos

É importante ressaltar que não vale a pena explicar algumas ferramentas básicas, que você descobre sem problemas tentando. 

Esses usos que não serão explicados são:
- Como fazer cadastro/login (se for no GitHub CLI, eu já expliquei.)
- Como criar um repositório público ou privado.
- Editar (as permissões e os arquivos), compartilhar (se for público, só compartilha o link) e deleter repositórios(é literalmente só ir nas configurações do repositório e procurar)  
- Como criar um perfil básico no GitHub, porque é fácil e para perfis trabalhados, há vários tutoriais melhores por aí.
