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

## Mudar de Branches

Uma *branch* é uma ramificação do seu repositório. Vocẽ pode colocar uma série de alterações que você não tem certeza se irá realmente adicionar no projeto numa branch alternativa por exemplo. Existem várias utilidades para branches, portanto saber usá-las é imprescindível.

Para checar quais branches seu repositório possui e em qual você está, use:

    git branch

Para trocar de branch no Git, digite no terminal num local pertencente ao seu repositório o comando (substitua "< nome da branch >" pelo nome da sua branch):

    git checkout -b <nome da branch>

O comando anterior criará uma nova branch caso uma branch com o nome inserido ainda não existir.

## Adição de mudanças no repositório.

É comum editores de texto não salvarem automaticamente suas mudanças e o mesmo acontece no Git. O Git apresenta uma interface (não gráfica) básica de aplicação de mudanças, cujas características precisam ser detalhadas.

Qualquer mudança nos arquivo é salva normalmente, porém elas não são automaticamente registradas no repositório como aplicáveis. Visto isso, as alterações podem ter 3 estados:
- Mudanças disponíveis
- Mudanças prontas para serem aplicadas.
- Mudanças aplicadas.

Ao fazer uma alteração no arquivo, toda alteração torna-se **disponível** para registramento. Você pode selecionar elas para serem aplicadas através d