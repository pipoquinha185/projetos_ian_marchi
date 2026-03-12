import subprocess #subprocess.run(["cls"], shell=True)

ano_de_nascimento = 0
cpf = 0
codigo_curso = 0
nome = ""
curso = ""

codigo_eng = 2345
codigo_psi = 8931
codigo_med = 1992
codigo_odo = 6769

class Curso:
    def __init__(self, nome, codigo, vagas_maximas, vagas_preenchidas):
        self.nome = nome
        self.codigo = codigo
        self.vagas_max = vagas_maximas
        
        self.vagas_preenchidas = vagas_preenchidas   

    def registrar_vaga(self):
        if self.vagas_preenchidas < self.vagas_max:
            self.vagas_preenchidas += 1
            return True
        else:
            return False
        
cursos_disponiveis = [Curso("Engenharia da computação", codigo_eng, 40, 0), 
                      Curso("Psicologia", codigo_psi, 5, 5),
                      Curso("Medicina", codigo_med, 16, 16),
                      Curso("Odontologia", codigo_odo, 37, 16)]

print("================ Gerador de matricula ====================\n")
print("Bem vindo ao simualdor de matricula do futuro projeto foda\n" \
"Para que possamos continuar")
nome = input("Me diga seu nome: ")
ano_de_nascimento = input("Me diga ano que você nasceu: ")
cpf = input("Qual é seu cpf: ")

while (len(str(cpf)) != 11):
    cpf = input("Cpf inválido\nDigite  novamente:")

print("Qual curso prente fazer:\n\n-Engenharia da computação\n-Psicologia\n-Medicina\n-Odontologia\n")
#

#logica
matriculado = False

while not matriculado:
    curso = input("").lower()
    curso_encontrado = None


    for x in cursos_disponiveis:
        if curso == x.nome.lower(): #Eles são equivalentes, não iguais
            curso_encontrado = x
            break
    if curso_encontrado is None:
        print("Curso não reconhecido! Tente digitar novamete")
    else:
        if curso_encontrado.registrar_vaga():
            codigo_curso = curso_encontrado.codigo
            matriculado = True
        else:
            print(f"Cruso de {curso_encontrado.nome} sem vagas no momento! Escolha outro")
        
print("======================================================================================")
print("\nMuito obrigado! Agora vamos fazer o calculo\nAperte qualquer botão para continuar")
input()

def gerar_matricula(codigo_curso, cpf, ano_de_nascimento):
    matricula_ano = ano_de_nascimento[-2:]
    matricula_cpf = cpf[-2:]
    matricula_curso = str(codigo_curso)

    matricula = matricula_curso +  matricula_ano + matricula_cpf

    return matricula

subprocess.run(["cls"], shell=True)   

print("Muito obrigado, " + nome + " seu codigo de matricula é: ")
print(gerar_matricula(codigo_curso, cpf, ano_de_nascimento))



    

