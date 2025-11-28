# 🏫 Escola de Idiomas — Sistema Completo de Gerenciamento

Este projeto é um sistema desenvolvido para gerenciar uma **Escola de Idiomas**, abrangendo operações de alunos, professores, cursos e turmas. O objetivo principal é oferecer uma aplicação organizada, escalável e funcional, servindo tanto como solução prática quanto como estudo de boas práticas em Python e PostgreSQL.

---

## 📌 **Funcionalidades Principais**

### 👩‍🎓 **Alunos**

* Matrícula de novos alunos;
* Autenticação com verificação de credenciais;
* Consulta de cursos nos quais o aluno está matriculado;
* Visualização de dados da turma (professor, horário, dias, alunos etc.).

### 👨‍🏫 **Professores**

* Cadastro e autenticação;
* Seleção de curso para lecionar (obrigatória caso ainda não exista);
* Possibilidade de alterar o curso posteriormente;
* Visualização de suas turmas e alunos.

### 🧑‍🤝‍🧑 **Turmas**

* Criação e gerenciamento de turmas por curso (identificação por código);
* Atribuição de professor, horário e dia da semana;
* Listagem de alunos por turma e transferência de alunos entre turmas;
* Visualização de cronograma e informações da turma para alunos e professores.

### 📚 **Cursos**

* Registro de cursos de diferentes idiomas;
* Associação entre professores, alunos e turmas;
* Regras de matrícula e organização.

### 📂 **Banco de Dados**

* Estrutura baseada em PostgreSQL
* Tabelas bem normalizadas, incluindo:

  * `professor`
  * `aluno`
  * `turma`
  * `curso`
  * `aluno_curso`
  * `professor_curso`
  * `professor_turma`
  * `aluno_turma`
  * `curso_turma`

* Consultas SQL otimizadas
* Tratamento de erros comum, como valores duplicados e violação de chave única

---

## 🛠️ **Tecnologias Utilizadas**

* **Python 3.14**
* **PostgreSQL**
* **psycopg2** (conexão com o banco)
* **bcrypt** (criptografia)
* **regex** (validações)
* **PowerShell / Terminal**
* Estrutura organizada em múltiplos arquivos `.py`

---

## 📁 **Estrutura do Projeto**

```
/escola-de-idiomas
│
├── administrador/
├── alunos/
├── banco_de_dados/
├── criptografar/
├── cursos/
├── limpar_tela/
├── professores/
├── turmas/
├── unique/
├── .gitignore.py
├── main.py
├── README.py
└── requirements.md
```

---

## 🚀 **Como Rodar o Projeto**

1. Instale as dependências necessárias:

   ```bash
   pip install psycopg2
   pip install bcrypt
   ```
2. Configure o banco de dados PostgreSQL e execute o script de criação de tabelas:

   ```sql
   \i tabelas.sql
   ```
3. Ajuste os dados de conexão no arquivo `conexao.py`.
4. Execute o programa:

   ```bash
   python main.py
   ```

---

## 🧑‍💻 **Desenvolvedores**

### 👨 Vinícius Araújo Coêlho

* Estudante de Sistemas de Informação
* Desenvolvimento principal do sistema
* Estruturação, lógica, integração com banco
* Criação de funcionalidades de alunos e turmas

### 👨 Irmão do Desenvolvedor

* Estudante de Sistemas de Informação
* Apoio geral no desenvolvimento
* Testes, sugestões e melhorias
* Auxílio na estrutura e organização do sistema
* Criação de funcionalidades de professores e turmas

---

## 🎯 **Objetivo do Projeto**

Este sistema foi construído com foco em:

* Aprendizagem de boas práticas em Python
* Domínio de operações com bancos de dados
* Organização modular
* Experiência realista de criação de sistema
* Evolução contínua do código
* Preparação para portfólio profissional

---