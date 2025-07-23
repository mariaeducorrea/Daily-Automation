# Criador Automático de Diretórios para Projetos com Python e Poetry

Este script automatiza todo o processo de criação de um novo projeto Python utilizando **Poetry**, já com:

* Criação do diretório do projeto
* Criação do ambiente virtual
* Instalação automática de pacotes adicionais (se desejado)
* Abertura do projeto no VS Code (se estiver instalado)



## Objetivo

Facilitar a criação rápida e padronizada de projetos Python, especialmente para:

* Projetos pessoais ou profissionais
* Automação de ambiente de desenvolvimento
* Trabalhos com Poetry e ambientes virtuais



## Bibliotecas e ferramentas utilizadas

| Biblioteca/Ferramenta           | Para que serve?                                                     |
| ------------------------------- | ------------------------------------------------------------------- |
| `<span>os</span>`             | Manipular caminhos e diretórios                                    |
| `<span>subprocess</span>`     | Executar comandos do terminal dentro do script                      |
| `<span>shutil</span>`         | Verificar se o VS Code está disponível no sistema                 |
| `<span>Poetry</span>`         | Gerenciar dependências, ambientes virtuais e estrutura de projetos |
| `<span>VS Code (code)</span>` | (Opcional) Abre o projeto automaticamente após a criação         |



## Como usar o script

1. Abra o terminal na pasta onde está o arquivo `<span>criar_projeto.py</span>`
2. Rode o script:

```
python criar_projeto.py
```

3. O script vai te perguntar:
   * Nome do projeto
   * Caminho onde deseja criar o projeto
   * Versão do Python desejada (ex: 3.12)
   * Pacotes adicionais (opcional – separados por espaço)
4. Após a execução:
   * O ambiente virtual será criado
   * Os pacotes serão instalados
   * O VS Code será aberto (se estiver disponível)


## Exemplo de entrada

```
Nome do projeto: meu_teste
Local do projeto: C:/Users/SeuNome/Desktop/projetos
Versão python: 3.12
Pacotes a instalar: pandas numpy openpyxl
```



## Como empacotar com PyInstaller (.exe)

Se quiser transformar o script `<span>criar_projeto.py</span>` em um **executável **`<span><strong>.exe</strong></span>`, siga estes passos:

### 1. Instale o PyInstaller (se ainda não tiver)

```
pip install pyinstaller
```

### 2. Gere o executável com o comando:

```
pyinstaller --onefile criar_projeto.py

#ou desta forma para gerar com ico
pyinstaller --onefile --icon=icone_projeto.ico criar_projeto.py

```

* `<span>pyinstaller</span>` é o programa que gera o executável.
* `<span>--onefile</span>` indica que será criado **um único arquivo **`<span><strong>.exe</strong></span>`, que já inclui tudo o que seu script precisa para rodar, sem depender de outras pastas.
* `<span>criar_projeto.py</span>` é o arquivo Python que você quer transformar em `<span>.exe</span>`.

### 3. Resultado da geração

Após a execução do comando, será criada a pasta `<span>dist/</span>` dentro do seu diretório atual, e dentro dela estará o arquivo executável `<span>criar_projeto.exe</span>`.

Você pode executar esse arquivo em qualquer computador Windows, sem precisar do Python instalado.

### 4. Limpar arquivos temporários (opcional)

#### No Linux / Git Bash:

```
rm -rf build criar_projeto.spec
```

#### No Windows CMD:

```
rmdir /s /q build
 del criar_projeto.spec
```



## Dica: evitar que o terminal feche automaticamente

Ao final do script há uma linha:

```
input("Pressione Enter para sair...")
```

Ela serve para manter o terminal aberto até o usuário pressionar Enter — útil especialmente quando rodando o `<span>.exe</span>` clicando duas vezes.
