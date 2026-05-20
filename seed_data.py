# ============================================================
# SEED_DATA.PY - Popula o banco de dados com os dados reais
# ============================================================
# Este script lê os dados da planilha fornecida pela SEMEA
# e insere no banco de dados SQLite.
# 
# COMO USAR: python seed_data.py
# (rode apenas UMA VEZ, ou após apagar o banco .db)
# ============================================================

from app import app, db, Modalidade, Noticia

# Dados extraídos da planilha da SEMEA (modalidades e horarios.xlsx)
dados_modalidades = [
    ("Atletismo", "Estádio Tonicão", "Av. Antônio Zuardi, s/n - Vila Operaria", "Maria Rita", "2ª e 6ª", "08h00 às 11h00", "A partir de 4 anos"),
    ("Atletismo", "Estádio Tonicão", "Av. Antônio Zuardi, s/n - Vila Operaria", "Maria Rita", "2ª e 6ª", "14h00 às 17h00", "A partir de 7 anos"),
    ("Basquete", "Escola Lucas Thomas Menk", "Rua General Osório, 465 - Vila Central", "Benedito Carlos", "Terça-feira", "18h00 às 19h30", "10 a 14 fem"),
    ("Basquete", "Escola Lucas Thomas Menk", "Rua General Osório, 465 - Vila Central", "Benedito Carlos", "Terça-feira", "19h30 às 21h00", "10 a 14 masc"),
    ("Basquete", "Escola Lucas Thomas Menk", "Rua General Osório, 465 - Vila Central", "Benedito Carlos", "Quinta-feira", "18h00 às 19h30", "10 a 14 fem"),
    ("Basquete", "Escola Lucas Thomas Menk", "Rua General Osório, 465 - Vila Central", "Benedito Carlos", "Quinta-feira", "19h30 às 21h00", "10 a 14 masc"),
    ("Basquete", "Escola Maria Valverde", "R. Olímpio de Mello, 902 - Parque das Acacias", "Felipe Ranieri", "Terça-feira", "17h00 às 18h30", "7 a 13"),
    ("Basquete", "Escola Maria Valverde", "R. Olímpio de Mello, 902 - Parque das Acacias", "Felipe Ranieri", "Sexta-feira", "17h00 às 18h30", "7 a 13"),
    ("Basquete", "Escola Guiomar Namo de Melo", "R. José Antônio Ferreira, 125 - Vila Ouro Verde", "Felipe Ranieri", "Segunda-feira", "19h30 às 21h00", "9 a 14"),
    ("Basquete", "Escola Carolina Buralli", "R. Santa Cruz, 958 - Centro", "Wilson Azarias", "Sexta-feira", "17h00 às 18h30", "10 a 13"),
    ("Basquete", "Escola Carolina Buralli", "R. Santa Cruz, 958 - Centro", "Wilson Azarias", "Quarta-feira", "18h30 às 20h00", "10 a 13"),
    ("Basquete", "GEMA", "R. Fadlo Jabur, 40 - Centro", "Wilson Azarias", "Terça-feira", "18h30 às 20h00", "13 a 16"),
    ("Basquete", "GEMA", "R. Fadlo Jabur, 40 - Centro", "Wilson Azarias", "Quinta-feira", "19h00 às 22h00", "13 a 16"),
    ("Basquete", "Escola Angélica Amorim", "Av. Valter Antônio Fontana, 1300 - Vila Claudia", "Wilson Azarias", "Segunda-feira", "17h30 às 18h30", "9 a 12 anos"),
    ("Basquete", "Escola Angélica Amorim", "Av. Valter Antônio Fontana, 1300 - Vila Claudia", "Wilson Azarias", "Sexta-feira", "18h30 às 19h30", "13 a 14"),
    ("Ciclismo MTB", "Saída Posto GD", "Av. Abílio Duarte de Souza, 1 - Jardim Aeroporto", "Paulo Antunes", "Quarta-feira", "07h30 às 10h00", "Livre"),
    ("Futebol de campo", "Areninha", "R. Dr. Geraldo Nogueira Leite, s/n - Vila Operaria", "Diego Lara", "Segunda-feira", "19h30 às 21h30", "07 a 08"),
    ("Futebol de campo", "Areninha", "R. Dr. Geraldo Nogueira Leite, s/n - Vila Operaria", "Diego Lara", "Segunda-feira", "19h30 às 21h30", "09 a 10"),
    ("Futebol de campo", "Areninha", "R. Dr. Geraldo Nogueira Leite, s/n - Vila Operaria", "Diego Lara", "Sexta-feira", "19h30 às 21h30", "07 a 08"),
    ("Futebol de campo", "Areninha", "R. Dr. Geraldo Nogueira Leite, s/n - Vila Operaria", "Diego Lara", "Sexta-feira", "19h30 às 21h30", "09 a 10"),
    ("Futebol de campo", "Estadio Marcelino de Souza", "R. Horácio Rodrigues Tucunduva, s/n - Vila Ribeiro", "Diego Lara", "Terça-feira", "18h30 às 20h00", "07 a 08"),
    ("Futebol de campo", "Estadio Marcelino de Souza", "R. Horácio Rodrigues Tucunduva, s/n - Vila Ribeiro", "Ricardo Martins", "Terça-feira", "18h30 às 20h00", "12 a 13"),
    ("Futebol de campo", "Estadio Marcelino de Souza", "R. Horácio Rodrigues Tucunduva, s/n - Vila Ribeiro", "Diego Lara", "Quinta-feira", "18h30 às 20h00", "09 a 10"),
    ("Futebol de campo", "Estadio Marcelino de Souza", "R. Horácio Rodrigues Tucunduva, s/n - Vila Ribeiro", "Ricardo Martins", "Quinta-feira", "18h30 às 20h00", "12 a 13"),
    ("Futebol de campo", "Estadio Marcelino de Souza", "R. Horácio Rodrigues Tucunduva, s/n - Vila Ribeiro", "Júlio Matos", "Segunda-feira", "18h30 às 20h00", "15 a 17"),
    ("Futebol de campo", "Campo Unesp", "Av. Mario de Vitto, s/n - Parque Universitário", "Júlio Matos", "Terça-feira", "08h30 às 10h00", "08 a 10"),
    ("Futebol de campo", "Campo Unesp", "Av. Mario de Vitto, s/n - Parque Universitário", "Júlio Matos", "Terça-feira", "10h30 às 12h00", "11 a 13"),
    ("Futebol de campo", "Campo Unesp", "Av. Mario de Vitto, s/n - Parque Universitário", "Júlio Matos", "Terça-feira", "16h00 às 17h30", "13 a 15"),
    ("Futebol de campo", "Campo Unesp", "Av. Mario de Vitto, s/n - Parque Universitário", "Júlio Matos", "Quinta-feira", "08h30 às 10h00", "08 a 10"),
    ("Futebol de campo", "Campo Unesp", "Av. Mario de Vitto, s/n - Parque Universitário", "Júlio Matos", "Quinta-feira", "10h30 às 12h00", "11 a 13"),
    ("Futebol de campo", "Campo Unesp", "Av. Mario de Vitto, s/n - Parque Universitário", "Júlio Matos", "Quinta-feira", "16h00 às 17h30", "13 a 15"),
    ("Futebol de campo", "Complexo Esportivo Homero Rabello", "R. José Teixeira Sobrinho, 275 - Parque das Acácias", "Júlio Matos", "Segunda-feira", "18h30 às 20h00", "13 a 15"),
    ("Futebol de campo", "Complexo Esportivo Homero Rabello", "R. José Teixeira Sobrinho, 275 - Parque das Acácias", "Júlio Matos", "Quarta-feira", "18h30 às 20h00", "13 a 15"),
    ("Futebol de campo", "Estadio Marcelino de Souza", "R. Horácio Rodrigues Tucunduva, s/n - Vila Ribeiro", "Ricardo Martins", "Quarta-feira", "18h30 às 19h30", "07 a 08"),
    ("Futebol de campo", "Estadio Marcelino de Souza", "R. Horácio Rodrigues Tucunduva, s/n - Vila Ribeiro", "Ricardo Martins", "Quarta-feira", "19h30 às 20h30", "09 a 10"),
    ("Futsal", "Escola Manoel Simões", "R. Carlos Bompani, 280 - Vila Fiúza", "Carlos Matheus", "Segunda-feira", "18h00 às 19h00", "7 a 9"),
    ("Futsal", "Escola Manoel Simões", "R. Carlos Bompani, 280 - Vila Fiúza", "Carlos Matheus", "Segunda-feira", "19h00 às 20h00", "12 a 14"),
    ("Futsal", "Escola Manoel Simões", "R. Carlos Bompani, 280 - Vila Fiúza", "Carlos Matheus", "Terça-feira", "20h00 às 21h00", "12 a 14"),
    ("Futsal", "Escola Manoel Simões", "R. Carlos Bompani, 280 - Vila Fiúza", "Carlos Matheus", "Quarta-feira", "18h00 às 19h00", "Misto"),
    ("Futsal", "Escola Manoel Simões", "R. Carlos Bompani, 280 - Vila Fiúza", "Carlos Matheus", "Quarta-feira", "19h00 às 20h00", "12 a 14"),
    ("Futsal", "Escola Alides Celeste", "Av. São Cristóvão, 1120 - Jardim Parana", "Eduardo de Lima", "Segunda-feira", "18h00 às 19h30", "9 a 11"),
    ("Futsal", "Escola Alides Celeste", "Av. São Cristóvão, 1120 - Jardim Parana", "Eduardo de Lima", "Terça-feira", "18h00 às 19h30", "12 a 14"),
    ("Futsal", "Escola Alides Celeste", "Av. São Cristóvão, 1120 - Jardim Parana", "Eduardo de Lima", "Quarta-feira", "18h00 às 19h30", "9 a 11"),
    ("Futsal", "Escola Alides Celeste", "Av. São Cristóvão, 1120 - Jardim Parana", "Eduardo de Lima", "Quarta-feira", "19h30 às 21h00", "12 a 14"),
    ("Ginástica rítmica", "SEMEA", "R. Fadlo Jabur, 55 - Centro", "Tatiane e Juscielni", "2ª e 5ª", "08h00 às 09h00", "7 a 9"),
    ("Ginástica rítmica", "SEMEA", "R. Fadlo Jabur, 55 - Centro", "Tatiane e Juscielni", "2ª e 5ª", "09h00 às 10h00", "10 a 12"),
    ("Ginástica rítmica", "SEMEA", "R. Fadlo Jabur, 55 - Centro", "Tatiane e Juscielni", "3ª e 5ª", "14h00 às 15h00", "7 a 9"),
    ("Ginástica rítmica", "SEMEA", "R. Fadlo Jabur, 55 - Centro", "Tatiane e Juscielni", "3ª e 5ª", "15h00 às 16h00", "10 a 12"),
    ("Ginástica rítmica", "SEMEA", "R. Fadlo Jabur, 55 - Centro", "Tatiane e Juscielni", "3ª e 5ª", "16h00 às 17h00", "ETI"),
    ("Handebol", "Escola Maria Valverde", "R. Olímpio de Mello, 902 - Parque das Acacias", "M. Angélica", "2ª e 5ª", "16h30 às 18h30", "A partir de 7 anos"),
    ("Handebol", "Escola Henrique Zollner", "R. Santa Cruz, 959 - Vila Palhares", "M. Angélica", "4ª", "16h00 às 18h00", "A partir de 7 anos"),
    ("Handebol", "Escola Maria Clélia", "R. São Sebastião, 370 - Vila Arlindo Luz", "M. Angélica", "6ª", "16h00 às 18h00", "A partir de 7 anos"),
    ("Judô", "SEMEA", "R. Fadlo Jabur, 55 - Centro", "Guilherme Giberti", "Segunda-feira", "17h00 às 18h00", "7 a 9"),
    ("Judô", "SEMEA", "R. Fadlo Jabur, 55 - Centro", "Guilherme Giberti", "Terça-feira", "18h00 às 19h00", "10 a 15"),
    ("Judô", "SEMEA", "R. Fadlo Jabur, 55 - Centro", "Guilherme Giberti", "Terça-feira", "19h00 às 21h00", "Defesa pessoal"),
    ("Judô", "SEMEA", "R. Fadlo Jabur, 55 - Centro", "Guilherme Giberti", "Quinta-feira", "18h00 às 19h00", "10 a 15"),
    ("Judô", "SEMEA", "R. Fadlo Jabur, 55 - Centro", "Guilherme Giberti", "Quinta-feira", "19h00 às 21h00", "9 a 14"),
    ("Judô", "Centro Comunitário Inocoop", "R. Myrthes Spera Conceição, 21 - Conj. Hab. Nelson Marcondes", "Guilherme Giberti", "Quarta-feira", "17h00 às 19h30", "7 a 15"),
    ("Judô", "Centro Comunitário Inocoop", "R. Myrthes Spera Conceição, 21 - Conj. Hab. Nelson Marcondes", "Guilherme Giberti", "Sexta-feira", "17h00 às 19h30", "7 a 15"),
    ("Kickboxing", "SEMEA", "R. Fadlo Jabur, 55 - Centro", "Marega", "2ª e 4ª", "17h00 às 18h00", "7 a 10"),
    ("Kickboxing", "SEMEA", "R. Fadlo Jabur, 55 - Centro", "Marega", "2ª e 4ª", "18h00 às 19h00", "11 a 14"),
    ("Tênis de mesa", "Galpão Cultural", "Tv. Sorocabana, nº 40 - Centro", "Basílio", "2ª, 4ª e 6ª", "18h00 às 19h00", "A partir de 10"),
    ("Vôlei", "Escola Lucas Thomas Menk", "R. General Osório, 465 - Vila Central", "Ricardo Nazareno", "2ª e 4ª", "18h00 às 19h30", "10 a 14 fem"),
    ("Vôlei", "Escola Lucas Thomas Menk", "R. General Osório, 465 - Vila Central", "Ricardo Nazareno", "2ª e 4ª", "19h30 às 21h00", "10 a 14 masc"),
    ("Xadrez", "Parque Buracão", "R. Orozimbo Leão de Carvalho, 1319 - Vila Santa Cecilia", "Cristiane Meira", "Segunda-feira", "08h30 às 11h00", "A partir de 7"),
    ("Xadrez", "Parque Buracão", "R. Orozimbo Leão de Carvalho, 1319 - Vila Santa Cecilia", "Cristiane Meira", "Quinta-feira", "08h30 às 11h00", "A partir de 7"),
    ("Xadrez", "Parque Buracão", "R. Orozimbo Leão de Carvalho, 1319 - Vila Santa Cecilia", "Cristiane Meira", "Quinta-feira", "18h00 às 21h00", "A partir de 7"),
]

# Notícias exemplo para popular a página inicial
dados_noticias = [
    ("Assis inaugura novo Centro Esportivo no Bairro Bonfim", 
     "Com pista de atletismo profissional e quadra poliesportiva, o novo espaço atenderá mais de 2.000 jovens por mês. A inauguração aconteceu no dia 10 de maio com a presença do prefeito e secretário de esportes."),
    ("Copa Assis de Futebol Amador abre inscrições para 2026",
     "As equipes interessadas em participar da Copa Assis de Futebol Amador 2026 podem realizar suas inscrições na Secretaria Municipal de Esportes até o dia 30 de junho."),
    ("Assis conquista 15 medalhas nos Jogos Regionais",
     "Nossa delegação brilhou nas modalidades de natação, atletismo e judô nos Jogos Regionais 2026, trazendo 15 medalhas para o município."),
]


def popular_banco():
    """Insere todos os dados no banco de dados"""
    with app.app_context():
        # Cria as tabelas no banco (se não existirem ainda)
        db.create_all()

        # Limpa dados existentes (cuidado! só usar na inicialização)
        Modalidade.query.delete()
        Noticia.query.delete()

        # Insere modalidades
        for dados in dados_modalidades:
            m = Modalidade(
                nome=dados[0],
                local=dados[1],
                endereco=dados[2],
                instrutor=dados[3],
                dia_semana=dados[4],
                horario=dados[5],
                faixa_etaria=dados[6]
            )
            db.session.add(m)

        # Insere notícias
        for titulo, conteudo in dados_noticias:
            n = Noticia(titulo=titulo, conteudo=conteudo)
            db.session.add(n)

        db.session.commit()
        print(f"✓ {len(dados_modalidades)} modalidades inseridas")
        print(f"✓ {len(dados_noticias)} notícias inseridas")
        print("✓ Banco populado com sucesso!")


if __name__ == '__main__':
    popular_banco()
