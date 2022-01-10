# Construção de uma interface gráfica utilizando python e a biblioteca kivy, para aquisição de dado de um sensor de velocidade 

### constrution of graphical interface using python and the kivy lib, for data aquisition via bluetooth from a velocity sensor

**Autor:** Gabriel G.R Castro

**Email:** gabriel.guitar@gmail.com

**Resumo:** O uso de interfaces gráficas (GUI) para interpretação e analise de dados é de extrema importância. Além de poder facilitar a leitura dos dados, ela também auxilia pesquisadores e estudantes que sem vasto conhecimento na área do trabalho dissertado, possam melhor interpreta-los e tirar suas conclusões. Dessa maneira esse trabalho propõe a construção de uma GUI para o sistema Android.Que apresentará de maneira didática os dados de um sensor de velocidade lidos por uma placa raspberrypi 3 model B e enviados,pela mesma, via bluetooth para o sistema Android.

**Abstract:** The use of graphical interfaces (GUI) for data interpretation and analysis is extremely important. In addition to facilitating the reading of data, it also allows researchers and students with not an extensive knowledge in a specific area of knowledge, to better understand and take their conclusions. In the light of these, this work proposes the construction of a GUI for the Android system. Wich will show, in a didactic way, the data from a speed sensor read by a raspberrypi 3 model B board and sent  via bluetooth to the Android system.
 

Esse trabalho será divido em duas partes.A primeira voltada para o computador que desenvolverá o aplicativo usando python em conjunto com kivy.
A segunda é o raspberry Pi (rpi3).

**Sumário** 

[1.Instalando Dependencias](#depencias)

[..1.1 PC](#dep_pc)
  
[..1.2 RPI](#dep_rpi)

[2.Exemplo2](## Preparando o Raspberrypi)

## 1 Instalando depêndencias <a name="depencias"></a>

### 1.1 PC <a name="dep_pc"></a>

É necessário ter instalado o python versão >3.3, caso não possua siga os próximos passos, ou clique no link para ser levado para a documentação oficial do python

> python -V **verifica a versão do python **

Caso seja inferior siga os comandos abaixo para instalar a versão 3.7 do python

> sudo apt update
>
> sudo apt install software-properties-common
>
> sudo add-apt-repository ppa:deadsnakes/ppa
>
> sudo apt update
>
> sudo apt install python3.7

**Instalar pacotes :** 

> python -m pip install --upgrade pip setuptools virtualenv
>
> python -m pip install kivy[base] kivy_examples
>
> pip3 install pandas 
>
> pip3 install numpy
>
> pip3 install kivy-garden
>
> pip3 install os
>
> pip3 install serial
>
> garden install matplotlib

### 1.2 RPI <a name="dep_rpi"></a>

> Primeiramente instale um sistema operacional no rpi, para isso basta seguir os passos encontrados no [link](https://www.raspberrypi.com/documentation/computers/getting-started.html#installing-images-on-linux). O sistema utilizado para os testes foi o Raspberry Pi OS.

Após o sistema ser implementado Instale os seguintes pacotes : 

> pip3 install serial
>
> pip3 install os
>
> sudo apt-get install rpi.gpio

## 2. Desenvolvimento das telas do aplicativo <a name="telas"></a>

Segundo  sua  [documentação](https://kivy.org/doc/stable/),  kivy ́é uma  biblioteca  para Python  construıda  em  código  aberto  e  voltada  para  o  de-senvolvimento  rápido  de  aplicativos  que  usam  interfaces gráficas,  como  por  exemplo  as  aplicações  multi-touch.A biblioteca Kivy pode ser executada em Linux, Windows, OSX, Android, iOS e Raspberry Pi, sem alteração no código. A estrutura mais básica do kivy são os Widgets, que nada mais são que classes que pertencem a biblioteca. Os mais simples e mais utilizados são Label,  BoxLayout,  Button  e GridLayout.

Antes de explicar o codigo app.kv que é encontrado nesse repositório, é preciso entender como funciona essa "linguagem". De maneira simples a tela do aplicativo chamada de canvas possui um layout dinânico. Sendo assim ao invés de atribuir um tamanho fixo aos widgets, será usado o conceito de size_hint e porcentagens.Por exemplo na [imagem](https://user-images.githubusercontent.com/43047212/148808058-6f205351-7e20-4c08-a51c-35c4938ebe7c.png) é possivel ver como os botãos são distribuidos no canvas, a partir do arquivo [exemplo.kv](https://user-images.githubusercontent.com/43047212/148808058-6f205351-7e20-4c08-a51c-35c4938ebe7c.png).  

![image](https://user-images.githubusercontent.com/43047212/148808058-6f205351-7e20-4c08-a51c-35c4938ebe7c.png)

Por boas práticas é sempre interessante criar um widget com 100% da tela, normalmente é utilizado o BoxLayout ou GridLayout com número de colunas igual a 1.Nesse exemplo foi usado o gridlayout (que possui a função de divir o espaço em grids)




