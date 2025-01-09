import random

# List of student names
students = [
    "Emanuel Filipe Miranda Esteves de Araújo",
    "André da Silva Marques Pinto",
    "Bela Alice Botelho Morais Costa",
    "Mariana Nunes Pinho Guedes",
    "Francisco Miguel Lima Rosa Mendonça e Almeida",
    "José Rogério Bernardo Ruas",
    "Josiana de Oliveira Martins Duarte",
    "Hugo Filipe Bento da Cruz",
    "Ana Sofia Sobral Cipriano",
    "Rui Manuel Malheiro de Sousa Coelho",
    "Maria Eduarda Ruiz Pena",
    "Ricardo Jorge Pinto Ribeiro",
    "Gonçalo Pereira Rodrigues da Cruz",
    "Fábio André Videira Santos",
    "Alexandra Escorcio Torres Caeiro",
    "Rita Filipe",
    "Sofia Rangel de Quadros e Osório de Valdoleiros",
    "Maria Beatriz Romeira Prista Pestana Leão Pedro",
    "Inês Leonor Maciel Leitão Ferraz",
    "Flávia Catarina Duarte Cunha",
    "Marie Hélène Augusto Domingues Oliveira",
    "David Ricardo Galhano Lopes",
    "Mário Diogo Lopes Guerra",
    "Ana Luísa Fernandes Pinto",
    "Diogo Miguel Freire Leitão Duarte Mendes Pedro",
    "Margarida Martins Mouro",
    "Ana Carolina Martins Silva",
    "Rita Franco Sérvio",
    "António Pedro Rocha Martins",
    "Salomão de Assis Campos Fernandes",
    "David Rodrigues Valente Peres",
    "Cláudio José Nunes Silva",
    "João Paulo Macieira Caldas da Costa",
    "Margarida Trindade Figueiredo Torres",
    "Inês Correia Gonçalves",
    "Sara Barbosa Meleiro das Neves",
    "António Pedro Barreira Carujo",
    "Inês Moreira da Rocha e Sousa",
    "Carla Patrícia Pires Gomes",
    "Gonçalo Jantarada Domingos",
    "Fátima Patrícia Sousa Gonçalves",
    "Micaela José Nunes Sousa",
    "Luís Pedro Silva e Reis",
    "Ana Luísa Carvalho Graça",
    "Cristina Isabel Moura Nunes",
    "Isabel Furtado Pereira Silva"
]

# Supervisors and their constraints
examiners = {
    "CMS": ["Gonçalo Jantarada Domingos", "Diogo Miguel Freire Leitão Duarte Mendes Pedro", "Inês Leonor Maciel Leitão Ferraz"],
    "IC": ["Emanuel Filipe Miranda Esteves de Araújo", "André da Silva Marques Pinto", "Bela Alice Botelho Morais Costa"],
    "JAP": ["Sara Barbosa Meleiro das Neves", "António Pedro Barreira Carujo"],
    "PG": ["Inês Leonor Maciel Leitão Ferraz", "Emanuel Filipe Miranda Esteves de Araújo"],
    "RC": ["Margarida Trindade Figueiredo Torres", "Inês Correia Gonçalves", "Sara Barbosa Meleiro das Neves"]
}

# Function to assign examiners
def assign_examiners(students, examiners):
    assignments = {}
    supervisor_workload = {supervisor: 0 for supervisor in examiners}

    for student in students:
        eligible_supervisors = [s for s in examiners if student not in examiners[s]]

        # Sort eligible supervisors by current workload to balance assignments
        eligible_supervisors.sort(key=lambda s: supervisor_workload[s])

        # Assign two supervisors with the least workload
        assigned = eligible_supervisors[:2]
        assignments[student] = assigned

        # Update workload
        for supervisor in assigned:
            supervisor_workload[supervisor] += 1

    return assignments, supervisor_workload

# Assign examiners
assignments, workload = assign_examiners(students, examiners)

# Display assignments
print("Lista Alunos:")
for student, assigned_supervisors in assignments.items():
    print(f"{student}: {', '.join(assigned_supervisors)}")

# Display workload balance
print("\nNúmero de Alunos por avaliador:")
for supervisor, load in workload.items():
    print(f"{supervisor}: {load}")
