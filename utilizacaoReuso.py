from classes.facade import Facade
import matplotlib.pyplot as plt
import numpy as np
from typing import Tuple, List

def parse_sort_results(results):
    py_results = {}
    js_results = {}

    for output_path, (exec_path, time_taken, metric) in results:
        if "bubblesort" in output_path:
            algo = "bubblesort"
        elif "insertionsort" in output_path:
            algo = "insertionsort"
        elif "quicksort" in output_path:
            algo = "quicksort"
        elif "mergesort" in output_path:
            algo = "mergesort"
        else:
            continue

        if "/python_code/" in exec_path:
            py_results[algo] = time_taken
        elif "/js_code/" in exec_path:
            js_results[algo] = time_taken

    return py_results, js_results

def plot_sort_benchmarks(py, js):
    algorithms = ["bubblesort", "insertionsort", "quicksort", "mergesort"]
    labels = ["Bubble Sort", "Insertion Sort", "Quick Sort", "Merge Sort"]

    py_times = [py[a] for a in algorithms]
    js_times = [js[a] for a in algorithms]

    x = np.arange(len(algorithms))
    width = 0.25

    plt.figure(figsize=(10, 6))

    plt.bar(x-width/2, py_times,  width, label="Python")
    plt.bar(x+width/2, js_times,  width, label="JavaScript")

    plt.xticks(x, labels)
    plt.ylabel("Tempo (segundos)")
    plt.xlabel("Algoritmo")
    plt.title("Comparação de Tempo (CPU Time) - Algoritmos de Ordenação")
    plt.legend()

    plt.grid(axis="y", linestyle="--", alpha=0.6)
    plt.tight_layout()
    plt.show()

def save_outputs_to_file(outputs: List[Tuple[str, Tuple[str, str, None]]], filename: str):
    with open(filename, "w", encoding="utf-8") as f:
        for filepath, (stdout, stderr, _) in outputs:
            if "_py_" in filepath:
                language = "Python"
            else :
                language = "JavaScript"

            base = filepath.split('/')[-1]
            algo = base.split('_')[0]

            stdout_clean = stdout.strip()
            stderr_clean = stderr.strip()

            if stdout_clean:
                output_value = stdout_clean
            else:
                output_value = stderr_clean
            
            f.write(f"{algo} ({language}): {output_value}\n")

def main():

    programs = [
        ("test/python_code/quicksort_py.py","codigosTeste/results/outputs", "python3"),
        ("test/python_code/mergesort_py.py","codigosTeste/results/outputs", "python3"),
        ("test/python_code/insertionsort_py.py","codigosTeste/results/outputs", "python3"),
        ("test/python_code/bubblesort_py.py","codigosTeste/results/outputs", "python3"),

        ("test/js_code/quicksort_js.js","codigosTeste/results/outputs","node"),
        ("test/js_code/mergesort_js.js","codigosTeste/results/outputs","node"),
        ("test/js_code/insertionsort_js.js","codigosTeste/results/outputs","node"),
        ("test/js_code/bubblesort_js.js","codigosTeste/results/outputs","node")
        ]

    interface = Facade()

    interface.setPrograms(programs)
    interface.setConcurrentBatch()
    interface.runBatch(cpuTime= True)
    
    #print(interface.getResults())

    py, js = parse_sort_results(interface.getResults())
    plot_sort_benchmarks(py, js)


    interface.runBatch(captureOutput=True)
    results = interface.getResults()
    print(results)

    save_outputs_to_file(results, "outputs.txt")


if __name__ == "__main__":
    main()