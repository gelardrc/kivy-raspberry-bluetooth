import kivy
from kivy.app import App

import datetime

from kivy.lang import Builder
from kivy.uix.widget import Widget
from kivy.properties import ObjectProperty
from kivy.uix.label import Label
from kivy.uix.gridlayout import GridLayout
from kivy.uix.boxlayout import BoxLayout
from kivy.clock import Clock
from kivy.uix.screenmanager import ScreenManager, Screen
import numpy as np
from os import walk
import os
import pandas as pd

####### parte grafica ##########
from kivy.garden.matplotlib.backend_kivyagg import FigureCanvasKivyAgg
import matplotlib.pyplot as plt
################################

import serial
import time

print("Start")
port = "/dev/rfcomm0"
bluetooth = serial.Serial(port,9600,timeout=0.050)
print("Conected")
bluetooth.flushInput()

class WindowManager(ScreenManager):
    pass

class MainWindow(Screen):
    def button1(self):
        #print("enviei 0 para o bluetooth")
        bluetooth.write(b"0")
        time.sleep(1)
    def button2(self):
        print("enviei 1 para o bluetooth")
        bluetooth.write(b"1")
        time.sleep(1)
    def button3(self):
        print("enviei 2 para o bluetooth")
# controle    
class SecondWindow(Screen):
    def on_enter(self):
        velocidade_antiga = 0
        dire = True    
    
    def aumenta(self):
        bluetooth.write(str(10).encode())
    def diminui(self):
        bluetooth.write(str(11).encode())
    def hora(self):
        bluetooth.write(str(20).encode())
    def anti(self):
        bluetooth.write(str(21).encode())
# velocidade atual
class ThirdWindow(Screen):
    lido = ObjectProperty(None)

    def on_enter(self):
        bluetooth.flushInput()
        self.clocky = Clock.schedule_interval(self.leitura, .1)
        self.x_online = []
        self.y_online = []
        self.x_on = 0
        self.y_on = 0
        plt.cla()
        self.ids.graph_online.clear_widgets()
        self.fig2 = ThirdWindow.constroi_grafico(self)
        self.ids.graph_online.add_widget(FigureCanvasKivyAgg(self.fig2))
        
    def constroi_grafico(self):

        plt.plot(self.x_online,self.y_online)
        plt.ylabel(" Velocidade (RPM)")
        plt.xlabel(" Tempo (s)")
        plt.title("Velocidade atual do Motor ")
        if self.x_online:
            plt.xlim([0,max(self.x_online)+20])
            plt.ylim([min(self.y_online)-10,max(self.y_online)+10])
        else:
            plt.xlim([0,2])
            plt.ylim([0,2])
        self.fig2 = plt.gcf()
        
        return self.fig2

    def on_leave(self):
        ## Somente para parar o clock
        self.clocky.cancel()
        

    def atualiza_grafico(self):
        plt.cla()
        self.ids.graph_online.clear_widgets()
        self.fig2 = ThirdWindow.constroi_grafico(self)
        self.ids.graph_online.add_widget(FigureCanvasKivyAgg(self.fig2))

    
    def leitura(self,*args):
        
       if bluetooth.in_waiting>0:
            var = bluetooth.read(size=8).decode()
            bluetooth.flushInput()
            self.lido.text = "Velocidade do motor: "+str(var)+"rpm"
            self.y_online.append(float(var))
            self.x_online.append(self.x_on)
            self.x_on = self.x_on+10
            self.y_on = self.x_on*2
            ThirdWindow.atualiza_grafico(self)
            print(self.y_online)
       
       # else: 
       #self.lido.text = "Aguardando comunicação com o bluetooth..."
    def pausa(self):
        self.clocky.cancel()
    def continua(self):
        self.clocky = Clock.schedule_interval(self.leitura, 1)
    def salva_grafico(self):
        now = datetime.datetime.now()
        local = {   'x' : self.x_online,
                    'y' : self.y_online
                }

        df = pd.DataFrame(  data=local,    # values
                            columns=['x',  'y'])  # 1st row as the column names

        df.to_csv('/home/gelo/codes/raspberry_project/data/leitura_'+str(now)+'.csv', index=False)

# leituras antigas
class ForthWindow(Screen):

    def varredura(self):
        lista = os.listdir('/home/gelo/codes/raspberry_project/data')
        self.ids.mainbutton.values = []
        for i in lista:self.ids.mainbutton.values.append(i)
        
    def spinner(self,value):

        self.ids.mainbutton.text = value
        self.dataset = pd.read_csv("/home/gelo/codes/raspberry_project/data/"+str(value))
        self.x_graf = self.dataset.x.tolist()
        self.y_graf = self.dataset.y.tolist()
        self.zoom_att = max(self.x_graf)
        self.zoom_y_att = max(self.y_graf)
        plt.cla()
        self.ids.graph.clear_widgets()
        self.fig = ForthWindow.grafico(self,x_zoom = max(self.x_graf)+20,y_zoom = max(self.y_graf)+20)
        self.ids.graph.add_widget(FigureCanvasKivyAgg(self.fig))

    def grafico(self,x_zoom,y_zoom):
        plt.plot(self.x_graf,self.y_graf,color='y')
        plt.xlim([0,x_zoom])
        plt.ylim([0,y_zoom])
        plt.ylabel(" Velocidade (RPM)")
        plt.xlabel(" Tempo (s)")
        plt.title("Velocidade atual do Motor ")
        self.fig = plt.gcf()
        return self.fig
    def on_leave(self):
        plt.cla()
        self.ids.graph.clear_widgets()
    def on_enter(self):
        self.on_off = 0
        ForthWindow.varredura(self)
        self.x_graf = []
        self.y_graf= []
        self.zoom_att = 10
        self.zoom_y_att = 10
        self.fig = ForthWindow.grafico(self,x_zoom=self.zoom_att,y_zoom=self.zoom_y_att)
        self.ids.graph.add_widget(FigureCanvasKivyAgg(self.fig))
    def button_zoom_x(self,zoom):
        self.zoom_att = self.zoom_att + zoom
        plt.cla()
        self.ids.graph.clear_widgets()
        self.fig = ForthWindow.grafico(self,x_zoom = self.zoom_att,y_zoom = self.zoom_y_att)
        print(self.zoom_att)
        self.ids.graph.add_widget(FigureCanvasKivyAgg(self.fig))
       
    def button_zoom_y(self,zoom):
        
        self.zoom_y_att = self.zoom_y_att + zoom
        plt.cla()
        self.ids.graph.clear_widgets()
        self.fig = ForthWindow.grafico(self,x_zoom = self.zoom_att,y_zoom = self.zoom_y_att)
        self.ids.graph.add_widget(FigureCanvasKivyAgg(self.fig))
        
    def grid(self,n):
        if (self.on_off + n)%2 != 0: 
            plt.cla()
            self.ids.graph.clear_widgets()
            plt.grid(color='b', linestyle='-', linewidth=1)
            self.fig = ForthWindow.grafico(self,x_zoom = self.zoom_att,y_zoom = self.zoom_y_att)
            self.ids.graph.add_widget(FigureCanvasKivyAgg(self.fig))
        else :
            plt.cla()
            self.ids.graph.clear_widgets()
            plt.grid(color='r', linestyle='-', linewidth=0)
            self.fig = ForthWindow.grafico(self,x_zoom = self.zoom_att,y_zoom = self.zoom_y_att)
            self.ids.graph.add_widget(FigureCanvasKivyAgg(self.fig))
        self.on_off = self.on_off + n
        print(self.on_off) 

class appApp(App):
    def build(self):
        return Builder.load_file("app.kv")


if __name__ == "__main__":
   appApp().run()