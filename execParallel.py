from classes.facade import Facade

def main():
    programs = [
        ("codigosTeste/triviais/script1.py","codigosTeste/triviais/outputs", "python3"),
        ("codigosTeste/triviais/script1_defeituoso.py","codigosTeste/triviais/outputs", "python3"),
        ("codigosTeste/triviais/script2.js","codigosTeste/triviais/outputs", "node"),
        ("codigosTeste/triviais/programa1.out","codigosTeste/triviais/outputs","./")
        ]
    
    """
    #Teste da obtenção de outputs
    lista = execBatch(programs,captureOutput=True, captureSignal=True)
    time.sleep(3)
    lista = execBatch(programs,captureOutput=True)
    time.sleep(3)
    lista = execBatch(programs,captureSignal=True)
    time.sleep(3)
    """
    
    #TESTE COM CLASSES INDIVIDUAIS
    """ 
    runner = Runner(programs)
    lista = runner.execBatch(concurrent=True, cpuTime=True)

    analyser = Analyser(runner)
    print(analyser.mean(lista))
    """
    #Teste das estatísticas
    #está pegando
    """
    lista = execBatch(programs, concurrent=True, cpuTime=True)
    print(stats.fastest(lista))
    print(stats.slowest(lista))
    print(stats.mean(lista))
    print(stats.stdDevPop(lista))
    """

    interface = Facade()

    interface.setPrograms(programs)
    interface.setConcurrentBatch()
    interface.runBatch(captureOutput=True, captureSignal=True)
    
    print(interface.getResults())

    results = interface.calcStats(mean=True,stdDevPop=True,slowest=True,fastest=True)
    mean, stdDevPop, slowest, fastest = results
    print(mean, stdDevPop, slowest, fastest)
    
    #Testes dos tipos de execução com tipos de medidas diferentes
    #Está pegando
    """
    execBatch(programs,concurrent=False, cpuTime=True)
    time.sleep(0.5)
    execBatch(programs,concurrent=True, realTime=True)
    time.sleep(0.5)
    execBatch(programs,concurrent=False, realTime=True)
    """
    
if __name__ == "__main__":
    main()