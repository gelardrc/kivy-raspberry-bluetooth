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

[2.Desenvolvimento das telas do aplicativo](#telas)

[..2.1 Explicando Posicionamento dos Widgets](#pos_wid)

[..2.2 Projeto das telas](#proj_telas)

[..2.3 Implementando multiplas telas no kivy ](#proj_telas)

[..2.4 Construindo MainWindow](#proj_telas)

[..2.5 Construindo SecondWindow](#proj_telas)

[..2.6 Construindo ThirdWindow](#proj_telas)

[..2.7 Construindo a Fourth Window](#proj_telas)

[3 Bluetooth](#proj_telas)

[..3.1 Bluetooth Raspberry/PC](#proj_telas)

[4 Controle e leitura Raspberry](#proj_telas)




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

### 2.1 Explicando Posicionamento dos Widgets <a name="pos_wid"></a>

Segundo  sua  [documentação](https://kivy.org/doc/stable/),  kivy ́é uma  biblioteca  para Python  construıda  em  código  aberto  e  voltada  para  o  de-senvolvimento  rápido  de  aplicativos  que  usam  interfaces gráficas,  como  por  exemplo  as  aplicações  multi-touch.A biblioteca Kivy pode ser executada em Linux, Windows, OSX, Android, iOS e Raspberry Pi, sem alteração no código. A estrutura mais básica do kivy são os Widgets, que nada mais são que classes que pertencem a biblioteca. Os mais simples e mais utilizados são Label,  BoxLayout,  Button  e GridLayout.

Antes de explicar o codigo app.kv que é encontrado nesse repositório, é preciso entender como funciona essa "linguagem". De maneira simples a tela do aplicativo chamada de canvas possui um layout dinânico. Sendo assim ao invés de atribuir um tamanho fixo aos widgets, será usado o conceito de size_hint e porcentagens.Por exemplo na [imagem](https://user-images.githubusercontent.com/43047212/148808058-6f205351-7e20-4c08-a51c-35c4938ebe7c.png) é possivel ver como os botãos são distribuidos no canvas, a partir do arquivo [exemplo.kv](https://user-images.githubusercontent.com/43047212/148808058-6f205351-7e20-4c08-a51c-35c4938ebe7c.png).  

![image](https://user-images.githubusercontent.com/43047212/148808058-6f205351-7e20-4c08-a51c-35c4938ebe7c.png)

Por boas práticas é sempre interessante criar um widget com 100% da tela, normalmente é utilizado o BoxLayout ou GridLayout com número de colunas igual a 1.Nesse exemplo foi usado o gridlayout (que possui a função de dividir o espaço em grids), com cols:1 e size_hint: 100,100. Para inserir outros widgets dentro do grid basta ser escrito de maneira identada. No exemplo é utilizado mais um GridLayout, porém dessa vez com cols:2 e size_hint : 1.0.6 ou sejá o grid ocupará 100% da largura da tela e terá 60% altura da tela. Por último é utilizado agora dentro da identação do primeiro GridLayout com size_hint : 1,.4.

### 2.2 Projeto das telas <a name="proj_telas"></a>

O projeto inicial de qualquer interface gráfica, passa primeiro por uma faze de rascunho, para só depois ser implementado. Dessa maneira o rascunho do aplicativo aqui proposto foi obtido utilizando o libreoffice writer para gerar as telas. A [imagem](https://user-images.githubusercontent.com/43047212/148819782-e89567cc-0d3f-4885-be63-d7efabde727f.png) mostra a ultima versão desses rascunhos. 

![1111](https://user-images.githubusercontent.com/43047212/148819782-e89567cc-0d3f-4885-be63-d7efabde727f.png)

### 2.3 Implementando multiplas telas no kivy <a name="proj_telas"></a>


Para utilizar varias telas no kivy, é necessário importar o screen manager no arquivo app.py. Para fazer isso basta adicionar a seguinte linha no arquivo:

> from kivy.uix.screenmanager import ScreenManager, Screen

Após isso basta criar uma classe para cada tela que se deseja criar e mais uma para gerenciar elas. As primeiras herdam a classe Screen e a ultima a classe ScreenManager, como visto na [imagem](https://user-images.githubusercontent.com/43047212/148821431-32879d04-6b4a-479c-8792-c502389ecd47.png) abaixo. Na imagem também é possivel ver como essas classes são utilizadas no arquivo app.kv.  

![image](https://user-images.githubusercontent.com/43047212/148821431-32879d04-6b4a-479c-8792-c502389ecd47.png)

Cada clase recebe um nome, name:"primeira"..."segunda"..."main", para que o usuário possa navegar entre elas.

### 2.4 Construindo MainWindow <a name="proj_telas"></a>


Para construir a MainWindow, é bem simples, basta seguir o que foi discutido no [item](#pos_wid), e aplicar a ideia do posicionamentos do widgets no canvas da MainWindow. A imagem abaixo mostra o arquivo app.kv além das funções do aquivo app.py acionadas por cada botão do menu.

![image](https://user-images.githubusercontent.com/43047212/148822965-4066c211-c9ee-465f-ab8d-4885b0a062a7.png)

### 2.5 Construindo SecondWindow <a name="proj_telas"></a>


Essa janela também não utiliza nenhuma função diferente das já discutidas anteriormente, a exceção é somente no arquivo app.py que dessa vez envia informações via bluetooth para o raspberry via serial bluetooth. A imagem abaixo mostra o trecho dos arquivos app.kv e app.py

![image](https://user-images.githubusercontent.com/43047212/148823376-1c1875b8-2e7b-489f-ba87-5bfc1ba11bee.png)

### 2.6 Construindo ThirdWindow <a name="proj_telas"></a>


A terceira janela possui uma peculiaridade, a construção de um gráfico online. A maneira de implementar esse gráfico é dividida em três partes. A primeira e determinar o local que se deseja inserir o gráfico, para isso basta criar um BoxLayout do tamanho e no local que se deseja no arquivo app.kv, depois dar a ele uma id (id : graph_online). A segunda parte é criar uma função no arquivo app.py para construir o gráfico a partir da leitura do sensor. A ultima parte e criar uma função que atualizara o gráfico a cada intervalo de tempo. Para realizar essas três funções deve-se primeiro adicionar as seguintes linhas no arquivo app.py.

> from kivy.garden.matplotlib.backend_kivyagg import FigureCanvasKivyAgg ## utilizada para usar a função matplolib em conjunto com o graden
>
> from kivy.clock import Clock  ## Essa classe serve para criar um clock, e atualizar o gráfico

![image](https://user-images.githubusercontent.com/43047212/148825106-b443c8a0-f25e-4622-b29c-2b994e124742.png)

![image](https://user-images.githubusercontent.com/43047212/148825188-8c72ae50-616c-4640-b85b-5857d4858c4d.png)

![image](https://user-images.githubusercontent.com/43047212/148825268-3d322940-03e4-45d6-84a8-226c1e770cb2.png)


### 2.7 Construindo a Fourth Window <a name="proj_telas"></a>

A última janela usa o mesmo conceito de atualização de gráfico da terceira janela.Porém sem a necessidade de atualizar a cada intervalo de tempo, visto que os dados já estão salvos. Nesse caso o widget chamado de spinner é quem da o gatilho para limpar o gráfico antigo e aplicar um novo no local indicado no arquivo app.kv. O spinner funciona parecido com uma dropDown list, porém cada termo da lista não aciona um evento e sim retorna para um função o texto selecionado. O que nos permite explorar arquivos de maneira bem simples. A implementação foi realizada como na imagem abaixo : 

![image](https://user-images.githubusercontent.com/43047212/148827337-13531666-8821-4723-9b82-ec6bc19f13f6.png)

![image](https://user-images.githubusercontent.com/43047212/148827387-4e588c24-5dd8-411d-a1f1-bd000f60ffab.png)


