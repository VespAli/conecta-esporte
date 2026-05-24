# Conecta Esporte

**Desenvolvimento de um Ambiente Digital para Divulgação das Modalidades Esportivas**

Projeto Integrador em Computação I - UNIVESP (2026)

## Sobre o Projeto

Aplicação web para centralizar e divulgar informações sobre as modalidades esportivas oferecidas pela Secretaria Municipal de Esportes (SEMEA) de Assis/SP.

## Tecnologias

- **Python 3.x** - Linguagem de programação
- **Flask** - Micro-framework web
- **SQLite** - Banco de dados relacional
- **SQLAlchemy** - ORM (mapeamento objeto-relacional)
- **Bootstrap 5** - Framework CSS para interface
- **Jinja2** - Motor de templates HTML
- **Git/GitHub** - Controle de versão

## Como Rodar Localmente

### 1. Instalar Python
Baixe em: https://www.python.org/downloads/ (versão 3.10+)

### 2. Criar ambiente virtual (recomendado)
```bash
python -m venv venv
```

### 3. Ativar ambiente virtual
- **Windows:** `venv\Scripts\activate`
- **Mac/Linux:** `source venv/bin/activate`

### 4. Instalar dependências
```bash
pip install -r requirements.txt
```

### 5. Iniciar o banco de dados e popular com dados
```bash
python seed_data.py
```

### 6. Rodar a aplicação
```bash
python app.py
```

### 7. Acessar no navegador
Abra: http://127.0.0.1:5000

### Login administrativo
- **E-mail:** admin@semea.assis.sp.gov.br
- **Senha:** semea2026

## Estrutura de Pastas

```
conecta_esporte/
├── app.py                 # Aplicação principal (rotas + modelos)
├── seed_data.py           # Script para popular o banco
├── requirements.txt       # Dependências Python
├── Procfile              # Config para deploy (Heroku/Render)
├── .gitignore            # Arquivos ignorados pelo Git
├── static/
│   └── css/
│       └── style.css     # Estilos customizados
└── templates/
    ├── base.html         # Template base (navbar + footer)
    ├── index.html        # Página principal
    ├── modalidades.html  # Lista de modalidades
    ├── inscricao.html    # Formulário de inscrição
    ├── calendario.html   # Calendário semanal
    ├── login.html        # Login admin
    └── admin/
        ├── dashboard.html      # Painel principal
        ├── inscricoes.html     # Gerenciar inscrições
        ├── modalidades.html    # Gerenciar modalidades
        ├── nova_modalidade.html # Formulário nova modalidade
        └── noticias.html       # Gerenciar notícias
```

## Equipe

- Alex Lafaiete Godoi
- Alisson Gomes Paulino
- Amanda Vitoria Rosa
  
## Orientador
David Miguel Soares Junior

---
Universidade Virtual do Estado de São Paulo (UNIVESP) - 2026
