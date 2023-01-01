from tkinter import * # type: ignore
from haberlerApi import news
from time import sleep,strftime
from PIL import Image,ImageTk
import webbrowser

class Pencere(Tk):
    def __init__(self):
        super().__init__()
        Tk.resizable(self,width=False,height=False)
        self.img=ImageTk.PhotoImage(Image.open("fotolar\\sondakika.jpg"))  # type: ignore
        self.width,self.height = self.img.width(),self.img.height()
        self.canvas1=Canvas(width=self.width,height=self.height)
        self.canvas1.pack()
        self.canvas1.create_image((0,0),anchor=NW,image=self.img)
        self.title('Haberler')
        self.eval("tk::PlaceWindow . center")
        self.canvas1.create_text((self.width / 2, self.height/2), text='Hoşgeldiniz hangi haberleri görmek istersiniz?',font=("Helvetica 12 bold",20), anchor="center",fill="yellow")
        
        button1_img= (Image.open("fotolar\\lira.png"))  # type: ignore
        resized_button1_image= button1_img.resize((50,50), Image.Resampling.LANCZOS)  # type: ignore
        new_button1_image= ImageTk.PhotoImage(resized_button1_image)
        self.buton1=Button(text="Ekonomi",command=businessWindow,bg="yellow",padx=10,pady=10,cursor="hand2",image=new_button1_image)
        self.buton1.image=new_button1_image  # type: ignore
        self.canvas1.create_window((self.width / 2, self.height/3.75), window=self.buton1, anchor="center")
        self.canvas1.create_text((self.width / 2, self.height/2.6), text='Ekonomi',font=("Helvetica 12 bold",15), anchor="center",fill="white")


        button2_img= (Image.open("fotolar\\eglence.png"))  # type: ignore
        resized_button2_image= button2_img.resize((50,50), Image.Resampling.LANCZOS)  # type: ignore
        new_button2_image= ImageTk.PhotoImage(resized_button2_image)
        self.buton2=Button(text="Eğlence",command=entertainmentWindow,bg='yellow',padx=10,pady=10,cursor="hand2",image=new_button2_image)
        self.buton2.image=new_button2_image  # type: ignore
        self.canvas1.create_window((self.width / 1.5, self.height/3.75), window=self.buton2, anchor="center")
        self.canvas1.create_text((self.width / 1.5, self.height/2.6), text='Eğlence',font=("Helvetica 12 bold",15), anchor="center",fill="white")
        
        button3_img= (Image.open("fotolar\\saglik.png"))  # type: ignore
        resized_button3_image= button3_img.resize((50,50), Image.Resampling.LANCZOS)  # type: ignore
        new_button3_image= ImageTk.PhotoImage(resized_button3_image)
        self.buton3=Button(text="Sağlık",command=healthWindow,bg='yellow',padx=10,pady=10,cursor="hand2",image=new_button3_image)
        self.buton3.image=new_button3_image  # type: ignore
        self.canvas1.create_window((self.width / 3, self.height/3.75), window=self.buton3, anchor="center")
        self.canvas1.create_text((self.width / 3, self.height/2.6), text='Sağlık',font=("Helvetica 12 bold",15), anchor="center",fill="white")
        
        button4_img= (Image.open("fotolar\\bilim.png"))  # type: ignore
        resized_button4_image= button4_img.resize((50,50), Image.Resampling.LANCZOS)  # type: ignore
        new_button4_image= ImageTk.PhotoImage(resized_button4_image)
        self.buton4=Button(text="Bilim",command=scienceWindow,bg='yellow',padx=10,pady=10,cursor="hand2",image=new_button4_image)
        self.buton4.image=new_button4_image  # type: ignore
        self.canvas1.create_window((self.width / 3, self.height/1.25), window=self.buton4, anchor="center")
        self.canvas1.create_text((self.width / 3, self.height/1.5), text='Bilim',font=("Helvetica 12 bold",15), anchor="center",fill="white")
        
        button5_img= (Image.open("fotolar\\ball.png"))  # type: ignore
        resized_button5_image= button5_img.resize((50,50), Image.Resampling.LANCZOS)  # type: ignore
        new_button5_image= ImageTk.PhotoImage(resized_button5_image)        
        self.buton5=Button(text="Spor",command=sportsWindow,bg="yellow",padx=10,pady=10,cursor="hand2",image=new_button5_image) 
        self.buton5.image=new_button5_image   # type: ignore
        self.canvas1.create_window((self.width / 2, self.height/1.25), window=self.buton5, anchor="center")
        self.canvas1.create_text((self.width / 2, self.height/1.5), text='Spor',font=("Helvetica 12 bold",15), anchor="center",fill="white")
        
        button6_img= (Image.open("fotolar\\teknoloji.png"))  # type: ignore
        resized_button6_image= button6_img.resize((50,50), Image.Resampling.LANCZOS)  # type: ignore
        new_button6_image= ImageTk.PhotoImage(resized_button6_image) 
        self.buton6=Button(text="Teknoloji",command=technologyWindow,bg='yellow',padx=10,pady=10,cursor="hand2",image=new_button6_image)
        self.buton6.image=new_button6_image  # type: ignore
        self.canvas1.create_window((self.width / 1.5, self.height/1.25), window=self.buton6, anchor="center")
        self.canvas1.create_text((self.width / 1.5, self.height/1.5), text='Teknoloji',font=("Helvetica 12 bold",15), anchor="center",fill="white")
        
        closeButton_img= (Image.open("fotolar\\kapat.png"))  # type: ignore
        resized_closeButton_image= closeButton_img.resize((50,50), Image.Resampling.LANCZOS)  # type: ignore
        new_closeButton_image= ImageTk.PhotoImage(resized_closeButton_image)
        self.closeButton=Button(text='Kapat',command=self.kapat,bg='yellow',padx=10,pady=10,cursor="hand2",image=new_closeButton_image)
        self.closeButton.image=new_closeButton_image  # type: ignore
        self.canvas1.create_window((self.width , self.height), window=self.closeButton, anchor="se")
        

        saat = Label(font=("ds-digital", 15), background="#800020", foreground="yellow")
        saat.place(relx=0.1025,rely=0.05,anchor='center')
        
        def time():
            string = strftime('%H:%M:%S: %p')
            saat.config(text=string)
            saat.after(1000, time)
        time()
        
    def business(self):
        news.get_business()
            
    def entertainment(self):
        news.get_entertainment()
        
    def health(self):
        news.get_health()
       
    def science(self):
        news.get_science()
            
    def sports(self):
        news.get_sports()
        
    def technology(self):
        news.get_technology()
       
    def callback(self,url):
            webbrowser.open_new_tab(url)

    def kapat(self):        
        self.closeButton['state']='disabled'
        self.after(1000,self.destroy)    
    
class entertainmentWindow():
    def __init__(self):
        a.entertainment()
        self.acilan_pencere = Toplevel()
        self.acilan_pencere.resizable(width=False,height=False)
        self.img=ImageTk.PhotoImage(Image.open("fotolar\\entertainment.jpg"))  # type: ignore
        self._width,self._height = self.img.width(),self.img.height()
        self.acilan_pencere.title("Eğlence Haberleri")
        self.canvas=Canvas(self.acilan_pencere,width=self._width,height=self._height)
        self.canvas.pack()
        self.canvas.image=self.img  # type: ignore
        self.canvas.create_image((0,0),anchor=NW,image=self.img)
        a.eval(f"tk::PlaceWindow {str(self.acilan_pencere)} center")
        
        def callback(url):
            webbrowser.open_new(url)

        i=0
        k=0
        j=0
        self.button = []
        for x in news.entertainmentList:

            self.button.append(Button(self.canvas, text=news.entertainmentList[i],font=("Helvetica 12 bold",13),padx=5,pady=8,bg="#800020",fg="white",command=lambda k=k: callback(news.entertainmentList[k+1])))
            self.button[j].grid(column=0, row=j,sticky=W)

            i+=2
            k+=2
            j+=1
            if k ==20:
                break
            
class healthWindow():
    def __init__(self):
        a.health()
        self.acilan_pencere = Toplevel()
        self.acilan_pencere.resizable(width=False,height=False)
        self.img=ImageTk.PhotoImage(Image.open("fotolar\\health.jpg"))  # type: ignore
        self._width,self._height = self.img.width(),self.img.height()
        self.acilan_pencere.title("Sağlık Haberleri")
        self.canvas=Canvas(self.acilan_pencere,width=self._width,height=self._height)
        self.canvas.pack()
        self.canvas.image=self.img  # type: ignore
        self.canvas.create_image((0,0),anchor=NW,image=self.img)
        a.eval(f"tk::PlaceWindow {str(self.acilan_pencere)} center")
        
        def callback(url):
            webbrowser.open_new(url)

        i=0
        k=0
        j=0
        self.button = []
        for x in news.healthList:

            self.button.append(Button(self.canvas, text=news.healthList[i],font=("Helvetica 12 bold",13),padx=3,pady=3,bg="white",fg="red",command=lambda k=k: callback(news.healthList[k+1])))
            self.button[j].grid(column=0, row=j,sticky=W)

            i+=2
            k+=2
            j+=1
            if k ==20:
                break 
            
class scienceWindow():
    def __init__(self):
        a.science()
        self.acilan_pencere = Toplevel()
        self.acilan_pencere.resizable(width=False,height=False)
        self.img=ImageTk.PhotoImage(Image.open("fotolar\\science.jpg"))  # type: ignore
        self._width,self._height = self.img.width(),self.img.height()
        self.acilan_pencere.title("Bilim Haberleri")
        self.canvas=Canvas(self.acilan_pencere,width=self._width,height=self._height)
        self.canvas.pack()
        self.canvas.image=self.img  # type: ignore
        self.canvas.create_image((0,0),anchor=NW,image=self.img)
        a.eval(f"tk::PlaceWindow {str(self.acilan_pencere)} center")
            
        def callback(url):
            webbrowser.open_new(url)

        i=0
        k=0
        j=0
        self.button = []
        for x in news.scienceList:

            self.button.append(Button(self.canvas, text=news.scienceList[i],font=("Helvetica 12 bold",12),padx=3,pady=3,bg="blue",fg="white",command=lambda k=k: callback(news.scienceList[k+1])))
            self.button[j].grid(column=0, row=j,sticky=W)

            i+=2
            k+=2
            j+=1
            if k ==20:
                break 
                  
class sportsWindow():
    def __init__(self):
        a.sports()
        self.acilan_pencere = Toplevel()
        self.acilan_pencere.resizable(width=False,height=False)
        self.img=ImageTk.PhotoImage(Image.open("fotolar\\sports.jpg"))  # type: ignore
        self._width,self._height = self.img.width(),self.img.height()
        self.acilan_pencere.title("Spor Haberleri")
        self.canvas=Canvas(self.acilan_pencere,width=self._width,height=self._height)
        self.canvas.pack()
        self.canvas.image=self.img  # type: ignore
        self.canvas.create_image((0,0),anchor=NW,image=self.img)
        a.eval(f"tk::PlaceWindow {str(self.acilan_pencere)} center")
            
        def callback(url):
            webbrowser.open_new(url)

        i=0
        k=0
        j=0
        self.button = []
        for x in news.sportsList:

            self.button.append(Button(self.canvas, text=news.sportsList[i],font=("Helvetica 12 bold",13),padx=3,pady=3,bg="green",fg="black",command=lambda k=k: callback(news.sportsList[k+1])))
            self.button[j].grid(column=0, row=j,sticky=E)

            i+=2
            k+=2
            j+=1
            if k ==20:
                break 
        
class technologyWindow():
    def __init__(self):
        a.technology()
        self.acilan_pencere = Toplevel()
        self.acilan_pencere.resizable(width=False, height=False)
        self.img=ImageTk.PhotoImage(Image.open("fotolar\\technology.jpg"))  # type: ignore
        self._width,self._height = self.img.width(),self.img.height()
        self.acilan_pencere.title("Teknoloji Haberleri")
        self.canvas=Canvas(self.acilan_pencere,width=self._width,height=self._height)
        self.canvas.pack()
        self.canvas.image=self.img  # type: ignore
        self.canvas.create_image((0,0),anchor=NW,image=self.img)
        a.eval(f"tk::PlaceWindow {str(self.acilan_pencere)} center")
            
        def callback(url):
            webbrowser.open_new(url)

        i=0
        k=0
        j=0
        self.button = []
        for x in news.technologyList:

            self.button.append(Button(self.canvas, text=news.technologyList[i],font=("Helvetica 12 bold",12),padx=3,pady=3,bg="white",fg="blue",command=lambda k=k: callback(news.technologyList[k+1])))
            self.button[j].grid(column=0, row=j,sticky=E)

            i+=2
            k+=2
            j+=1
            if k ==20:
                break 
        
class businessWindow():
    def __init__(self):
        a.business()
        self.acilan_pencere = Toplevel()
        self.acilan_pencere.resizable(width=False, height=False)
        self.img=ImageTk.PhotoImage(Image.open("fotolar\\business2.jpg"))  # type: ignore
        self._width,self._height = self.img.width(),self.img.height()
        self.acilan_pencere.title("Ekonomi Haberleri")
        self.canvas=Canvas(self.acilan_pencere,width=self._width,height=self._height)
        self.canvas.pack()
        self.canvas.image=self.img  # type: ignore
        self.canvas.create_image((0,0),anchor=NW,image=self.img)
        a.eval(f"tk::PlaceWindow {str(self.acilan_pencere)} center")
            
        def callback(url):
            webbrowser.open_new(url)

        i=0
        k=0
        j=0
        self.button = []
        for x in news.businessList:

            self.button.append(Button(self.canvas, text=news.businessList[i],font=("Helvetica 12 bold",12),padx=3,pady=3,bg="grey",fg="black",command=lambda k=k: callback(news.businessList[k+1])))
            self.button[j].grid(column=0, row=j,sticky=E)

            i+=2
            k+=2
            j+=1
            if k ==20:
                break 
           
a=Pencere()
a.mainloop()