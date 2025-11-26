# 🏫 Escola de Idiomas — Sistema Completo de Gerenciamento

Este projeto é um sistema desenvolvido para gerenciar uma **Escola de Idiomas**, abrangendo operações de alunos, professores, cursos, matrículas e turmas. O objetivo principal é oferecer uma aplicação organizada, escalável e funcional, servindo tanto como solução prática quanto como estudo de boas práticas em Python, SQL e arquitetura de software.

---

## 📌 **Funcionalidades Principais**

### 👩‍🎓 **Alunos**

* Cadastro de novos alunos
* Autenticação com verificação de credenciais
* Consulta de cursos nos quais o aluno está matriculado
* Visualização de dados da turma (professor, horário, dias, alunos etc.)

### 👨‍🏫 **Professores**

* Cadastro e autenticação
* Seleção de curso para lecionar (obrigatória caso ainda não exista)
* Possibilidade de alterar o curso posteriormente
* Visualização de suas turmas e alunos

### 📚 **Cursos**

* Registro de cursos de diferentes idiomas
* Associação entre professores, alunos e turmas
* Regras de matrícula e organização

### 🏫 **Sistema de Matrículas**

* Verificação automática se o aluno já está matriculado
* Associação do aluno ao curso correto
* Exibição de mensagens claras sobre a situação da matrícula

### 📂 **Banco de Dados**

* Estrutura baseada em PostgreSQL
* Tabelas bem normalizadas, incluindo:

  * `aluno`
  * `professor`
  * `curso`
  * `aluno_curso`
  * `professor_curso`
  * `turma`
* Consultas SQL otimizadas
* Tratamento de erros comum, como valores duplicados e violação de chave única

---

## 🛠️ **Tecnologias Utilizadas**

* **Python 3.x**
* **PostgreSQL**
* **psycopg2** (conexão com o banco)
* **PowerShell / Terminal**
* Estrutura organizada em múltiplos arquivos `.py`

---

## 📁 **Estrutura do Projeto (Sugestão)**

```
/escola-de-idiomas
│
├── alunos/
│   ├── cadastro_aluno.py
│   ├── autenticacao_aluno.py
│   ├── visualizar_cursos.py
│
├── professores/
│   ├── identificacao_professor.py
│   ├── selecionar_curso.py
│   ├── visualizar_turma.py
│
├── cursos/
│   ├── cadastrar_curso.py
│   ├── listar_cursos.py
│
├── database/
│   ├── conexao.py
│   ├── tabelas.sql
│
├── main.py
└── README.md
```

---

## 🚀 **Como Rodar o Projeto**

1. Instale as dependências necessárias:

   ```bash
   pip install psycopg2
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

## 🎯 **Objetivo do Projeto**

Este sistema foi construído com foco em:

* Aprendizagem de boas práticas em Python
* Domínio de operações com bancos de dados
* Organização modular
* Experiência realista de criação de sistema
* Evolução contínua do código
* Preparação para portfólio profissional

---