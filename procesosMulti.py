import multiprocessing
import time

def tarea():
    nombre = multiprocessing.current_process().name
    procId = multiprocessing.current_process().pid
    print(f"Este es el proceso {nombre} con PID = {str(procId)}")
    time.sleep(10)

if __name__ == '__main__':

    proceso_1 = multiprocessing.Process( name="tarea 1", target=tarea)
    proceso_2 = multiprocessing.Process( name="tarea 2", target=tarea)
    currentId = multiprocessing.current_process().pid
    print(f"Este es el proceso principal con PID = {str(currentId)}")
    proceso_1.start()
    proceso_2.start()
    