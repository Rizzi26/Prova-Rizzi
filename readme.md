# Configuração

&emsp;Clone em sua maquina meu repo `git clone https://github.com/Rizzi26/Prova-Rizzi`

&emsp;Ative o venv em sua maquina, para fazer isso execute `pytho3 -m venv venv` na raiz do repo, depois rode o requirements.txt e ative a venv com o comando `source venv/bin/activate`

&emsp;Agora na pasta meu_workspace voce vai rodar o seguinte comando `colcon build` e depois `source install/local_setup.bash`

# Rodadndo

&emsp;Em um terminal voce vai rodar sua tartaruga cm o seguinte comando `ros2 run turtlesim turtlesim_node`

&emsp;Agora com o outro terminal voce vai navegar ate a pasta **meu_workspace** e digitar `ros2 run prova prova`. Ao rodar esse comando a CLI será emulada no terminal e você irá digitar na seguinte ordem os comando para a tartaruga: `VX, VY, VTHETA, TEMPO_EM_SEGUNDOS` é necessário que você separe por virgulas cada comando.

### Code da CLI:

```python 
def show(interface):
    questions = [
        {
            "type": "input",
            "name": "action",
            "message": "Digite o seu input na seguinte ordem: [vx (velocidade x), vy (velocidade em y), vtheta (velocidade angular), tempo_em_segundos]",
        }
    ]
    prompt_response = prompt(questions)["action"]
    prompt_list.append(prompt_response)
    interface.send_command(prompt_response)
```

&emsp;A CLI armazena o prompt enviado pelo user e so libera o proximo prompt quando o comando enviado anteriormente acabar de ser executado.

### Função publisher:

```python 
    def send_command(self, command):
        msg = Twist()
        msg.linear.x, msg.linear.y, msg.angular.z, duration = map(float, command.split(','))
        msg.linear.x = float(msg.linear.x)
        msg.linear.y = float(msg.linear.y)
        msg.angular.z = float(msg.angular.z)
        print("toki", msg.linear.x, msg.linear.y, msg.angular.z, duration)
        duration = float(duration)
        self.publisher_.publish(msg)
        time.sleep(duration)
        self.stop()
```

&emsp;Quando o user envia os comandos pela CLI é acionado a função `def send_command():` essa função separa o prompt a cada vírgula e armazena para cada variavel respectiva o seu valor. Após fazer essa divisão, a função publica os comandos a serem realizados para a tartaruga e ela se move.

# Prints 

![CLI](../../fotos/print1.png)

![CLI](../../fotos/print2.png)

![CLI](../../fotos/print3.png)


