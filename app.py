# ============================================================
# CONECTA ESPORTE - Aplicação Principal
# Framework: Python Flask
# Banco de Dados: SQLite (via SQLAlchemy ORM)
# ============================================================
# Este é o arquivo principal da aplicação. Ele:
# 1. Configura o Flask e o banco de dados
# 2. Define os "modelos" (tabelas do banco)
# 3. Define as "rotas" (URLs que o usuário acessa)
# ============================================================

from flask import Flask, render_template, request, redirect, url_for, flash
from flask_sqlalchemy import SQLAlchemy
from flask_login import LoginManager, UserMixin, login_user, logout_user, login_required, current_user
from datetime import datetime
import os

# ------------------------------------------------------------
# CONFIGURAÇÃO DO FLASK
# ------------------------------------------------------------
# Flask() cria a aplicação web.
# __name__ diz ao Flask onde encontrar os arquivos (templates, static, etc.)
app = Flask(__name__)

# SECRET_KEY: necessário para sessões e mensagens flash (segurança)
app.config['SECRET_KEY'] = 'chave-secreta-conecta-esporte-2026'

# SQLALCHEMY_DATABASE_URI: onde o banco de dados fica salvo
# SQLite salva tudo em um arquivo .db na pasta do projeto
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///conecta_esporte.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

# Inicializa o banco de dados e o sistema de login
db = SQLAlchemy(app)
login_manager = LoginManager(app)
login_manager.login_view = 'login'  # redireciona para login se não autenticado


# ============================================================
# MODELOS (TABELAS DO BANCO DE DADOS)
# ============================================================
# Cada classe abaixo vira uma tabela no banco de dados.
# Cada atributo (db.Column) vira uma coluna na tabela.
# ============================================================

class Usuario(UserMixin, db.Model):
    """Tabela de usuários administrativos (login do painel SEMEA)"""
    id = db.Column(db.Integer, primary_key=True)
    nome = db.Column(db.String(100), nullable=False)
    email = db.Column(db.String(120), unique=True, nullable=False)
    senha = db.Column(db.String(200), nullable=False)  # Em produção, usar hash!


class Modalidade(db.Model):
    """Tabela de modalidades esportivas (Basquete, Futsal, etc.)"""
    id = db.Column(db.Integer, primary_key=True)
    nome = db.Column(db.String(100), nullable=False)
    local = db.Column(db.String(200), nullable=False)
    endereco = db.Column(db.String(300), nullable=False)
    instrutor = db.Column(db.String(100), nullable=False)
    dia_semana = db.Column(db.String(50), nullable=False)
    horario = db.Column(db.String(50), nullable=False)
    faixa_etaria = db.Column(db.String(100), nullable=False)


class Inscricao(db.Model):
    """Tabela de inscrições (pré-inscrições dos cidadãos)"""
    id = db.Column(db.Integer, primary_key=True)
    nome_completo = db.Column(db.String(200), nullable=False)
    rg = db.Column(db.String(20))
    cpf = db.Column(db.String(20), nullable=False)
    data_nascimento = db.Column(db.String(10), nullable=False)
    email = db.Column(db.String(120), nullable=False)
    cep = db.Column(db.String(10))
    logradouro = db.Column(db.String(200))
    modalidade_id = db.Column(db.Integer, db.ForeignKey('modalidade.id'), nullable=False)
    data_inscricao = db.Column(db.DateTime, default=datetime.utcnow)
    status = db.Column(db.String(20), default='pendente')  # pendente, confirmada, recusada

    # Relacionamento: cada inscrição pertence a uma modalidade
    modalidade = db.relationship('Modalidade', backref='inscricoes')


class Noticia(db.Model):
    """Tabela de notícias/comunicados da SEMEA"""
    id = db.Column(db.Integer, primary_key=True)
    titulo = db.Column(db.String(200), nullable=False)
    conteudo = db.Column(db.Text, nullable=False)
    data_publicacao = db.Column(db.DateTime, default=datetime.utcnow)


# ------------------------------------------------------------
# FLASK-LOGIN: como carregar o usuário da sessão
# ------------------------------------------------------------
@login_manager.user_loader
def load_user(user_id):
    return Usuario.query.get(int(user_id))


# ============================================================
# ROTAS PÚBLICAS (o que o cidadão vê)
# ============================================================

@app.route('/')
def index():
    """Página principal - mostra modalidades e notícias"""
    modalidades = Modalidade.query.all()
    noticias = Noticia.query.order_by(Noticia.data_publicacao.desc()).limit(3).all()

    # Agrupa modalidades por nome (para mostrar cards únicos)
    nomes_unicos = list(set([m.nome for m in modalidades]))
    nomes_unicos.sort()

    return render_template('index.html', 
                           modalidades=modalidades,
                           nomes_unicos=nomes_unicos,
                           noticias=noticias)


@app.route('/modalidades')
def modalidades():
    """Página com todas as modalidades e seus horários"""
    todas = Modalidade.query.order_by(Modalidade.nome, Modalidade.dia_semana).all()
    return render_template('modalidades.html', modalidades=todas)


@app.route('/inscricao', methods=['GET', 'POST'])
def inscricao():
    """Página de inscrição esportiva"""
    if request.method == 'POST':
        # Recebe os dados do formulário
        nova = Inscricao(
            nome_completo=request.form['nome_completo'],
            rg=request.form.get('rg', ''),
            cpf=request.form['cpf'],
            data_nascimento=request.form['data_nascimento'],
            email=request.form['email'],
            cep=request.form.get('cep', ''),
            logradouro=request.form.get('logradouro', ''),
            modalidade_id=int(request.form['modalidade_id']),
            status='pendente'
        )
        db.session.add(nova)
        db.session.commit()
        flash('Inscrição realizada com sucesso! Aguarde confirmação por e-mail.', 'success')
        return redirect(url_for('inscricao'))

    modalidades = Modalidade.query.order_by(Modalidade.nome).all()
    return render_template('inscricao.html', modalidades=modalidades)


@app.route('/calendario')
def calendario():
    """Página de calendário semanal"""
    modalidades = Modalidade.query.all()

    # Organiza por dia da semana
    dias = {
        'Segunda-feira': [], 'Terça-feira': [], 'Quarta-feira': [],
        'Quinta-feira': [], 'Sexta-feira': [], 'Sábado': []
    }

    for m in modalidades:
        dia = m.dia_semana.strip()
        # Trata dias compostos como "2ª e 6ª"
        if ' e ' in dia or ',' in dia:
            # Mapeia abreviações
            mapa = {'2ª': 'Segunda-feira', '3ª': 'Terça-feira', '4ª': 'Quarta-feira',
                     '5ª': 'Quinta-feira', '6ª': 'Sexta-feira'}
            for abrev, nome_dia in mapa.items():
                if abrev in dia:
                    if nome_dia in dias:
                        dias[nome_dia].append(m)
        else:
            if dia in dias:
                dias[dia].append(m)

    return render_template('calendario.html', dias=dias)


# ============================================================
# ROTAS DE AUTENTICAÇÃO (LOGIN/LOGOUT)
# ============================================================

@app.route('/login', methods=['GET', 'POST'])
def login():
    """Página de login para administradores"""
    if request.method == 'POST':
        email = request.form['email']
        senha = request.form['senha']
        usuario = Usuario.query.filter_by(email=email, senha=senha).first()
        if usuario:
            login_user(usuario)
            return redirect(url_for('admin_dashboard'))
        else:
            flash('E-mail ou senha incorretos.', 'danger')
    return render_template('login.html')


@app.route('/logout')
@login_required
def logout():
    logout_user()
    return redirect(url_for('index'))


# ============================================================
# ROTAS ADMINISTRATIVAS (PAINEL SEMEA - requer login)
# ============================================================

@app.route('/admin')
@login_required
def admin_dashboard():
    """Painel principal do administrador"""
    total_inscricoes = Inscricao.query.count()
    pendentes = Inscricao.query.filter_by(status='pendente').count()
    total_locais = db.session.query(Modalidade.local).distinct().count()
    total_modalidades = db.session.query(Modalidade.nome).distinct().count()

    inscricoes_pendentes = Inscricao.query.filter_by(status='pendente')\
        .order_by(Inscricao.data_inscricao.desc()).limit(10).all()

    return render_template('admin/dashboard.html',
                           total_inscricoes=total_inscricoes,
                           pendentes=pendentes,
                           total_locais=total_locais,
                           total_modalidades=total_modalidades,
                           inscricoes_pendentes=inscricoes_pendentes)


@app.route('/admin/inscricoes')
@login_required
def admin_inscricoes():
    """Lista todas as inscrições"""
    inscricoes = Inscricao.query.order_by(Inscricao.data_inscricao.desc()).all()
    return render_template('admin/inscricoes.html', inscricoes=inscricoes)


@app.route('/admin/inscricao/<int:id>/confirmar')
@login_required
def confirmar_inscricao(id):
    """Confirma uma inscrição pendente"""
    insc = Inscricao.query.get_or_404(id)
    insc.status = 'confirmada'
    db.session.commit()
    flash(f'Inscrição de {insc.nome_completo} confirmada!', 'success')
    return redirect(url_for('admin_dashboard'))


@app.route('/admin/inscricao/<int:id>/recusar')
@login_required
def recusar_inscricao(id):
    """Recusa uma inscrição pendente"""
    insc = Inscricao.query.get_or_404(id)
    insc.status = 'recusada'
    db.session.commit()
    flash(f'Inscrição de {insc.nome_completo} recusada.', 'warning')
    return redirect(url_for('admin_dashboard'))


@app.route('/admin/modalidades')
@login_required
def admin_modalidades():
    """Gerenciar modalidades"""
    todas = Modalidade.query.order_by(Modalidade.nome).all()
    return render_template('admin/modalidades.html', modalidades=todas)


@app.route('/admin/modalidade/nova', methods=['GET', 'POST'])
@login_required
def nova_modalidade():
    """Adicionar nova modalidade"""
    if request.method == 'POST':
        nova = Modalidade(
            nome=request.form['nome'],
            local=request.form['local'],
            endereco=request.form['endereco'],
            instrutor=request.form['instrutor'],
            dia_semana=request.form['dia_semana'],
            horario=request.form['horario'],
            faixa_etaria=request.form['faixa_etaria']
        )
        db.session.add(nova)
        db.session.commit()
        flash('Modalidade adicionada com sucesso!', 'success')
        return redirect(url_for('admin_modalidades'))
    return render_template('admin/nova_modalidade.html')


@app.route('/admin/modalidade/<int:id>/excluir')
@login_required
def excluir_modalidade(id):
    """Excluir uma modalidade"""
    mod = Modalidade.query.get_or_404(id)
    db.session.delete(mod)
    db.session.commit()
    flash('Modalidade excluída.', 'warning')
    return redirect(url_for('admin_modalidades'))


@app.route('/admin/noticias', methods=['GET', 'POST'])
@login_required
def admin_noticias():
    """Gerenciar notícias / comunicados"""
    if request.method == 'POST':
        nova = Noticia(
            titulo=request.form['titulo'],
            conteudo=request.form['conteudo']
        )
        db.session.add(nova)
        db.session.commit()
        flash('Notícia publicada!', 'success')
        return redirect(url_for('admin_noticias'))

    noticias = Noticia.query.order_by(Noticia.data_publicacao.desc()).all()
    return render_template('admin/noticias.html', noticias=noticias)


# ============================================================
# INICIALIZAÇÃO DO BANCO DE DADOS
# ============================================================

def criar_banco():
    """Cria as tabelas e insere dados iniciais se o banco não existir"""
    with app.app_context():
        db.create_all()

        # Cria usuário admin padrão se não existir
        if not Usuario.query.first():
            admin = Usuario(
                nome='Administrador SEMEA',
                email='admin@semea.assis.sp.gov.br',
                senha='semea2026'
            )
            db.session.add(admin)
            db.session.commit()
            print("✓ Usuário admin criado: admin@semea.assis.sp.gov.br / semea2026")


# ============================================================
# PONTO DE ENTRADA - Roda a aplicação
# ============================================================
if __name__ == '__main__':
    criar_banco()
    # debug=True recarrega automaticamente quando você muda o código
    app.run(debug=True)
