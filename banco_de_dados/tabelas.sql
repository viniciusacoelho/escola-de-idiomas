CREATE TABLE professores_teste(
	id_professor SERIAL PRIMARY KEY,
	nome_completo VARCHAR(100) NOT NULL,
	email VARCHAR(255) NOT NULL UNIQUE,
	cpf CHAR(14) NOT NULL UNIQUE,
	numero_telefone CHAR(15) NOT NULL UNIQUE, 
	endereco VARCHAR(255) NOT NULL,
	idioma_lecionado VARCHAR(255) NOT NULL,
	senha BYTEA NOT NULL
);

SELECT * FROM professores_teste ORDER BY id_professor ASC;

CREATE TABLE alunos_teste(
	id_aluno SERIAL PRIMARY KEY,
	nome_completo VARCHAR(255) NOT NULL,
	usuario VARCHAR(255) NOT NULL UNIQUE,
	email VARCHAR(255) NOT NULL UNIQUE,
	cpf CHAR(14) NOT NULL UNIQUE,
	data_nascimento DATE NOT NULL,
	numero_telefone CHAR(15) NOT NULL UNIQUE,
	senha BYTEA NOT NULL
);

SELECT * FROM alunos_teste ORDER BY id_aluno ASC;

CREATE TABLE cursos_teste(
    id_curso SERIAL PRIMARY KEY,
    nome_curso VARCHAR(255) NOT NULL UNIQUE
);

SELECT * FROM cursos_teste ORDER BY id_curso ASC;

CREATE TABLE aluno_curso(
	id_aluno INTEGER NOT NULL,
	id_curso INTEGER NOT NULL,
	PRIMARY KEY (id_aluno, id_curso),
	FOREIGN KEY (id_aluno) REFERENCES alunos_teste (id_aluno),
	FOREIGN KEY (id_curso) REFERENCES cursos_teste (id_curso)
);

SELECT * FROM aluno_curso;

SELECT a.id_aluno, a.nome_completo, c.id_curso, c.nome_curso FROM aluno_curso ac 
INNER JOIN alunos_teste a ON a.id_aluno = ac.id_aluno 
INNER JOIN cursos_teste c ON c.id_curso = ac.id_curso 
ORDER BY a.id_aluno ASC;

SELECT c.nome_curso from aluno_curso ac INNER JOIN cursos_teste c ON c.id_curso = ac.id_curso;

CREATE TABLE turmas_teste(
	id_turma SERIAL PRIMARY KEY,
	dia_semana VARCHAR(255) NOT NULL,
	horario VARCHAR(255) NOT NULL
);

SELECT * FROM turmas_teste ORDER BY id_turma ASC;

CREATE TABLE professor_turma(
	id_professor INTEGER NOT NULL,
	id_turma INTEGER NOT NULL,
	PRIMARY KEY (id_professor, id_turma),
    FOREIGN KEY (id_professor) REFERENCES professores_teste(id_professor),
	FOREIGN KEY (id_turma) REFERENCES turmas_teste(id_turma)
);

SELECT * FROM professor_turma ORDER BY id_turma;

SELECT t.id_turma, p.nome_completo FROM professor_turma pt
INNER JOIN turmas_teste t ON t.id_turma = pt.id_turma 
INNER JOIN professores_teste p ON p.id_professor = pt.id_professor
ORDER BY t.id_turma;

CREATE TABLE aluno_turma(
	id_aluno INTEGER NOT NULL,
	id_turma INTEGER NOT NULL,
	PRIMARY KEY (id_aluno, id_turma),
    FOREIGN KEY (id_aluno) REFERENCES alunos_teste(id_aluno),
	FOREIGN KEY (id_turma) REFERENCES turmas_teste(id_turma)
);

SELECT * FROM aluno_turma ORDER BY id_turma;

SELECT t.id_turma, a.nome_completo FROM aluno_turma att
INNER JOIN turmas_teste t ON t.id_turma = att.id_turma 
INNER JOIN alunos_teste a ON a.id_aluno = att.id_aluno 
ORDER BY t.id_turma ASC;

CREATE TABLE curso_turma(
	id_curso INTEGER NOT NULL,
	id_turma INTEGER NOT NULL,
	PRIMARY KEY (id_curso, id_turma),
    FOREIGN KEY (id_curso) REFERENCES cursos_teste(id_curso),
	FOREIGN KEY (id_turma) REFERENCES turmas_teste(id_turma)
);

SELECT * FROM curso_turma ORDER BY id_turma;

SELECT t.id_turma, c.nome_curso, t.dia_semana, t.horario FROM curso_turma ct
INNER JOIN cursos_teste c ON c.id_curso = ct.id_curso 
INNER JOIN turmas_teste t ON t.id_turma = ct.id_turma 
ORDER BY t.id_turma;

-- TODO: Testar isso
SELECT p.nome_completo, a.nome_completo, c.nome_curso, t.id_turma FROM professor_turma pt
INNER JOIN professores_teste p ON p.id_professor = pt.id_professor 
INNER JOIN alunos_teste a ON a.id_aluno = pt.id_aluno 
INNER JOIN cursos_teste c ON c.id_curso = pt.id_curso 
ORDER BY id_turma ASC;

-- TODO: Testar isso também
SELECT a.nome_completo, p.nome_completo, t.horario FROM turmas_teste t
INNER JOIN alunos_teste a ON a.id_aluno = t.id_aluno
INNER JOIN professores_teste p ON p.id_professor = t.id_professor;

-- +55 (82) 9 9829-1900
-- 12345678901234567890