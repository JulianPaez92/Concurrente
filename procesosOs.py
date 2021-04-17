import os

def hijo():
    print("Este es el proceso  \"hijo\" con PID= %d"%os.getpid())

def padre():
    print("Este es el proceso  \"padre\" con PID= %d"%os.getpid())

newRef=os.fork()

if newRef==0:
    hijo()

else:
    padre()

