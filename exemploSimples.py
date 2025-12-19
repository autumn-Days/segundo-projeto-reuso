from classes.facade import Facade

def main():
    programs = [
        ("codigosTeste/triviais/codigoPython.py","codigosTeste/triviais/outputs", "python3"),
        ("codigosTeste/triviais/codigoPythonDefeituoso.py","codigosTeste/triviais/outputs", "python3"),
        ("codigosTeste/triviais/codigoJavascript.js","codigosTeste/triviais/outputs", "node"),
        ("codigosTeste/triviais/codigoJavascriptDefeituoso.js","codigosTeste/triviais/outputs", "node"),
        ]
    
    interface = Facade()

    interface.setPrograms(programs)
    #Define que a execução dos executáveis devem ser feita paralelamente
    interface.setConcurrentBatch()

    #Exemplo da obtenção de outputs
    interface.runBatch(captureOutput=True, captureSignal=True)
    interface.runBatch(captureOutput=True)
    interface.runBatch(captureSignal=True)

    #Exemplo da obteção de tempo computacional
    interface.runBatch(cpuTime=True)

    #Define que a execução dos executáveis devem ser feitas sequencialmente
    interface.setSequentialBatch()
    interface.runBatch(realTime=True)
    
    #Exemplo da obtenção da média, desvio padrão populacional, mais lento e rápido
    results = interface.calcStats(mean=True,stdDevPop=True,slowest=True,fastest=True)
    mean, stdDevPop, slowest, fastest = results
    print(f"{mean}\n{stdDevPop}\n{slowest}\n{fastest}")

if __name__ == "__main__":
    main()