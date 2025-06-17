import subprocess
import os

def execute(input, code):
    with open("code/script.py", "w", encoding="utf-8") as file:
        file.write(code)

    proc = subprocess.Popen(["python", "code/script.py"],stdin=subprocess.PIPE, stdout=subprocess.PIPE, stderr=subprocess.PIPE, text=True)
    try:
        scriptInput = input
        if scriptInput != "":
            stdout, stderr = proc.communicate(input=scriptInput, timeout=2)
        else:
            stdout, stderr = proc.communicate(timeout=2)
        
        if stderr != "":
            stderr = str(stderr)
            index = stderr.index("line")
            stderr = stderr[index:]

        return (str(stdout) + str(stderr))
    except:
        proc.terminate()
        return ("Erro de timeout. PUTA (Tempo limite de execução é de 2 segundos por caso.)")
    
def explain(problem):
    with open(f"code/{problem}/premissa.txt", "r", encoding="utf-8") as file:
        return(str(file.read()))
    
def solve(problem, code):
    pa = f"code/{problem}/in"
    casos = len([f for f in os.listdir(pa) if os.path.isfile(os.path.join(pa, f))])
    
    for t in range(0, casos):
            
        input = ""
        gabarito = ""
        with open(f"code/{problem}/in/{t}.txt", "r", encoding="utf-8") as file:
            input = str(file.read())
        with open(f"code/{problem}/out/{t}.txt", "r", encoding="utf-8") as file:
            gabarito = str(file.read())

        result = execute(input, code)
        if result != gabarito:
            return(f"Casos teste passados: {t}/{casos}\nDeu erro suae bosta.\nSeu output:\n{result}\n\nEsperado:\n{gabarito}")
        
    return(f"parabeins voce é foda e resolveu o problema {problem}")

def problemas():
    pa = "code/"

    answer = ""
    for f in os.listdir(pa):
        if not os.path.isfile(os.path.join(pa, f)):
            answer += str(f)
        
    return(answer)


# print(problemas())

# print(explain("Matematica Basica"))

code = ""
with open("submit.txt", "r", encoding="utf-8") as file:
    code = str(file.read())

print(solve("Matematica Basica", code))