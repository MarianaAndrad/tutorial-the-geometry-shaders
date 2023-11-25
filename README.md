# Instruções para Configuração e Execução
Este projeto inclui um script Python principal, **basic_geometry_shader.py**, uma pasta solution que contém dois arquivos adicionais: **solution.py**, que oferece uma resolução passo a passo de um problema, e **desafio.py**, que apresenta uma solução para um desafio proposto.

## Configuração

Para executar os scripts deste projeto, é necessário ter um ambiente Python configurado. Siga as instruções abaixo para configurar o ambiente:

1. **Instale o Python**: Se você ainda não tem o Python instalado, baixe e instale a versão mais recente do site oficial do Python.

2. **Crie um Ambiente Virtual (opcional)**: Recomenda-se usar um ambiente virtual para manter as dependências do projeto separadas e organizadas. Para criar um, execute:
    
```bash
python -m venv .venv
```

3. **Ative o Ambiente Virtual (opcional)**: Para ativar o ambiente virtual, execute:

```bash
source .venv/bin/activate 
```
ou no caso do Windows:

```bash
.venv\Scripts\activate 
```

1. **Instale as Dependências**: Para instalar as dependências do projeto, execute:

```bash
pip install -r requirements.txt
```


## Execução

Para executar o script principal, execute:

```bash
python basic_geometry_shader.py
```

Para executar o script de solução de problema, execute:

```bash
python solution.py
```

Para executar o script de solução de desafio, execute:

```bash
python desafio.py
```

## Extra

Numa outra pasta, **exploration**, há um script que gerará um arquivo de vídeo com a animação, com a utilização de um shader de geometria. Para executar o script, execute:

```bash
python exploration.py
```
