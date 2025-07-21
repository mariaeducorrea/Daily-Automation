# Automatizar Ativação de Ambiente Virtual Python

Este repositório contém scripts simples para ativação de ambiente virtual Python em diferentes terminais.

## Objetivo
Facilitar a ativação de ambientes virtuais Python em diferentes terminais de forma rápida e padronizada, evitando a repetição de comandos manuais.

## Passos 

### 1. Criar ambiente virtual

No terminal:
  ```bash
  python -m venv .venv
  ```
---
### 2. Criação de arquivos com os Scripts

### ativar.sh
- Será usado no teminal Git Bash

```bash
#!/bin/bash

source .venv/Scripts/activate 
#pode ser que o caminho esteja diferente, deve verificar!
```
- Após criado, execute o comando abaixo para liberar a execução:
```bash
chmod +x nome_arquivo
chmod +x ativar.sh
```
 


### ativar.ps1
- Será usado no terminal PowerShell
```bash
. .\.venv\Scripts\Activate.ps1
```
---
### 3. Ativar e Desativar Ambiente Virtual

Git Bash
```bash
#Ativar 
. ativar.sh

#Desativar
deactivate
```

PowerShell
```bash
#Ativar
.\ativar.ps1

#Desativar
deactivate
```


