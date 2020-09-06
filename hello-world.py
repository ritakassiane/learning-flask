from flask import Flask
import os
app = Flask(__name__) # Essa variável é criada toda vez que o programa é executado com o intuito de identificar qual o arquivo esta sendo executado. Se é a main ou uma arquivo secundário. Se for o arquivo principal __name__ = main

@app.route("/") # Isso é um decorator. Um decorator serve para aplicarmos uma funçao em cima de outra.Nesse caso, a função "route" [que permite que possamos definir uma rota] em cima da função index.
def index():
    return 'Hello World'

if __name__ == '__main__':
    app.run()
    


os.system('pause')