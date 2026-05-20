# 📚 Roteiro de Estudo — O Que Aprender Para Refazer Este Projeto

Este arquivo é um guia pessoal para entender TUDO que foi usado neste projeto.
Siga na ordem. Cada tópico tem o "por que" e "onde estudar".

---

## Nível 1: Fundamentos (Semana 1-2)

### 1.1 Python Básico
**O que é:** A linguagem de programação usada no backend (servidor).
**O que precisa saber:**
- Variáveis, tipos de dados (string, int, list, dict)
- Funções (`def`)
- Condicionais (`if/else`)
- Loops (`for`, `while`)
- Importação de módulos (`import`)
- Classes e objetos (básico de POO)

**Onde estudar:**
- [Python para Zumbis (PT-BR, gratuito)](https://www.youtube.com/playlist?list=PLUukMN0DTKCtbzhbYe2jdF4cr8MOWClXc)
- Livro: "Introdução à Computação usando Python" - Perkovic (disponível na biblioteca UNIVESP)
- [Automate the Boring Stuff (EN, gratuito)](https://automatetheboringstuff.com/)

---

### 1.2 HTML & CSS Básico
**O que é:** HTML define a ESTRUTURA da página. CSS define o ESTILO (cores, fontes, espaçamentos).
**O que precisa saber:**
- Tags HTML: `<div>`, `<h1>`, `<p>`, `<a>`, `<form>`, `<input>`, `<table>`
- Atributos: `class`, `id`, `href`, `src`
- CSS: seletores, box model, flexbox, cores, fontes
- Como linkar CSS no HTML

**Onde estudar:**
- [Curso em Vídeo - HTML5 e CSS3 (PT-BR, gratuito)](https://www.youtube.com/playlist?list=PLHz_AreHm4dkZ9-atkcmcBaMZdmLHft8n)
- [MDN Web Docs (referência oficial)](https://developer.mozilla.org/pt-BR/docs/Learn)

---

### 1.3 Bootstrap
**O que é:** Um "kit de componentes prontos" em CSS. Em vez de estilizar tudo do zero, você usa classes como `btn btn-primary`, `card`, `table`, etc.
**O que precisa saber:**
- Grid system (row/col)
- Componentes: navbar, cards, buttons, forms, tables, alerts
- Utility classes (mt-3, text-center, d-flex, etc.)

**Onde estudar:**
- [Documentação oficial do Bootstrap 5](https://getbootstrap.com/docs/5.3/)
- [Bootstrap 5 Crash Course - Traversy Media (EN)](https://www.youtube.com/watch?v=4sosXZsdy-s)

---

## Nível 2: Web com Flask (Semana 3-4)

### 2.1 Como a Web Funciona
**Conceitos chave:**
- Cliente (navegador) ↔ Servidor (seu código Python)
- Requisição HTTP: GET (pedir página), POST (enviar formulário)
- URL → Rota → Função Python → Template HTML → Resposta

**Onde estudar:**
- Videoaulas da UNIVESP: "Conceitos fundamentais da Web" e "Arquitetura Cliente-Servidor" (Prof. Manzato)

---

### 2.2 Flask — O Framework
**O que é:** Um micro-framework que transforma seu código Python em um servidor web.
**O que precisa saber:**
- Criação de app (`Flask(__name__)`)
- Rotas (`@app.route`)
- Métodos HTTP (GET/POST)
- Templates Jinja2 (`render_template`)
- Formulários (`request.form`)
- Mensagens flash
- Redirecionamentos (`redirect`, `url_for`)

**Onde estudar:**
- [Tutorial DigitalOcean - Flask (o mesmo citado no PI!)](https://www.digitalocean.com/community/tutorials/how-to-make-a-web-application-using-flask-in-python-3)
- Videoaulas UNIVESP: "Criando um website de postagens" partes 1, 2 e 3 (Prof. Manzato)
- [Flask Mega-Tutorial (EN, excelente)](https://blog.miguelgrinberg.com/post/the-flask-mega-tutorial-part-i-hello-world)

---

### 2.3 Jinja2 — Templates
**O que é:** A linguagem dentro do HTML que permite inserir dados dinâmicos do Python.
**O que precisa saber:**
- `{{ variavel }}` — mostra valor
- `{% for item in lista %}` — loops
- `{% if condição %}` — condicionais
- `{% extends "base.html" %}` — herança de templates
- `{% block content %}{% endblock %}` — blocos substituíveis
- `{{ url_for('rota') }}` — gerar URLs

**Onde estudar:**
- [Documentação Jinja2](https://jinja.palletsprojects.com/en/3.1.x/templates/)
- Prática: leia os templates deste projeto e modifique coisas

---

## Nível 3: Banco de Dados (Semana 5)

### 3.1 SQL Básico
**O que é:** Linguagem para criar, consultar e modificar dados em bancos relacionais.
**O que precisa saber:**
- CREATE TABLE, INSERT, SELECT, UPDATE, DELETE
- WHERE, ORDER BY, JOIN
- Chave primária e chave estrangeira

**Onde estudar:**
- Videoaula UNIVESP: "Linguagem de consulta – SQL" (Profa. Sarajane)
- [SQL Tutorial - W3Schools](https://www.w3schools.com/sql/)

---

### 3.2 SQLAlchemy (ORM)
**O que é:** Permite manipular o banco de dados usando Python em vez de SQL puro.
**O que precisa saber:**
- Definir modelos (classes = tabelas)
- `db.Column` tipos (String, Integer, DateTime, etc.)
- `db.relationship` (relacionamentos entre tabelas)
- Operações CRUD: `.add()`, `.query.all()`, `.query.filter_by()`, `.commit()`, `.delete()`

**Onde estudar:**
- [Tutorial Flask-SQLAlchemy](https://flask-sqlalchemy.palletsprojects.com/en/3.1.x/quickstart/)
- [CRUD com Flask e SQLAlchemy - Codementor (citado no PI)](https://www.codementor.io/@garethdwyer/building-a-crud-application-with-flask-and-sqlalchemy-dm3wv7yu2)

---

## Nível 4: Extras (Semana 6+)

### 4.1 Git e GitHub
**O que é:** Controle de versão — salva histórico do código e permite trabalho em equipe.
**O que precisa saber:**
- `git init`, `git add`, `git commit`, `git push`
- Branches (básico)
- GitHub: criar repositório, push, README

**Onde estudar:**
- Videoaula UNIVESP: "GIT e GitHub" (Prof. Manzato)
- [Git - Guia Prático](https://rogerdudler.github.io/git-guide/index.pt_BR.html)

---

### 4.2 Deploy (Colocar Online)
**O que é:** Publicar a aplicação na internet para qualquer pessoa acessar.
**Opções gratuitas:**
- **Render.com** (recomendo, mais fácil que Heroku hoje)
- **PythonAnywhere** (grátis, simples)
- **Railway.app** (grátis para projetos pequenos)

**O que precisa saber:**
- Procfile (já incluído no projeto)
- gunicorn (servidor de produção)
- Variáveis de ambiente

**Onde estudar:**
- [Deploy Flask no Render](https://docs.render.com/deploy-flask)
- [Deploy Flask - StackAbuse (citado no PI)](https://stackabuse.com/deploying-a-flask-application-to-heroku/)

---

### 4.3 Flask-Login
**O que é:** Extensão que gerencia sessões de usuário (login/logout/proteção de rotas).
**O que precisa saber:**
- `UserMixin` — classe base para modelo de usuário
- `login_user()`, `logout_user()`
- `@login_required` — protege rotas
- `current_user` — acessa dados do usuário logado

**Onde estudar:**
- [Documentação Flask-Login](https://flask-login.readthedocs.io/en/latest/)

---

## Ordem Sugerida de Refação do Projeto

1. **Comece do zero** com um `app.py` mínimo (só "Hello World")
2. Adicione uma rota que mostra um template HTML
3. Crie o `base.html` com navbar e Bootstrap
4. Adicione o banco de dados com 1 modelo (Modalidade)
5. Crie o `seed_data.py` para popular
6. Faça a página de listagem de modalidades
7. Adicione o formulário de inscrição
8. Implemente login + painel admin
9. Suba no GitHub
10. Faça deploy no Render

**Tempo estimado para refazer entendendo tudo: 4-6 semanas estudando ~1h/dia**

---

## Conceitos Usados Neste Projeto (Checklist)

- [ ] Python: variáveis, funções, classes, imports
- [ ] HTML: estrutura de página, formulários, tabelas
- [ ] CSS: Bootstrap classes, CSS customizado
- [ ] Flask: rotas, templates, request, redirect, flash
- [ ] Jinja2: herança, loops, condicionais, variáveis
- [ ] SQLAlchemy: modelos, CRUD, relacionamentos
- [ ] SQLite: banco de dados em arquivo
- [ ] Flask-Login: autenticação
- [ ] Git: controle de versão
- [ ] Deploy: Procfile, gunicorn

---

*"A melhor forma de aprender programação é fazendo. Não tente entender tudo antes de começar — comece, erre, conserte, repita."*
