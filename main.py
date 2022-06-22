import tkinter as tk
from tkinter import *
import random
from pandas import DataFrame
import matplotlib.pyplot as plt
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg

click=False
running=False
#plot3=False
x=0

class Content:
    def __init__(self, root):
        global click
        global lf
        global lf2

        def count():
            #print('10 new values clicked')
            global running
            running = True
            #print(f'running = {running}')
            def app():
                #try:
                if running:
                    global x
                    if x ==0:
                        change()
                        #print('change() called')
                        x=1
                    root.after(1000, app)
                    #print('app called')
                    x-=1
            app()

        def stop():
            global running
            running = False

        btn3=Button(text='10 new values', command=count).pack()
        btn4=Button(text='stop', command=stop).pack()

        label=Label()
        label.pack(side=LEFT, padx=10)

        lf = LabelFrame(text='graph')

        def change():
            #print(f'running = {running}')
            global click
            global lf
            global lf2
            r =[]
            p=[]
            N=11
            for i in range(N):
                b=random.randint(1, 10)
                r.append(b)
                p.append(i)

            if click==False:
                #print(f'click = {click}')
                # if plot3 ==True:
                #     lf3.destroy()
                # else:
                #     pass
                lf.destroy()
                #print('lf destroyed')
                lf2=LabelFrame(text='graph')

                lf2.pack()
                #print('lf2 created')

                d = {'dx': p[1:11],
                     'dy': r[1:11]}
                dfd = DataFrame(d, columns=['dx', 'dy'])
                #figure_d = plt.Figure(dpi=100)
                figure_d = plt.Figure(dpi=100)
                ax1=figure_d.add_subplot(111)#one row, one column, first plot
                bar2=FigureCanvasTkAgg(figure_d, lf2)
                bar2.get_tk_widget().pack(fill=X)
                dfd=dfd[['dx', 'dy']].groupby('dx').sum()
                dfd.plot(kind='line', grid=True, ax=ax1)
                label['text']=dfd[0:10]
                click=True
            else:
                # if plot3 ==True:
                #     lf3.destroy()
                # else:
                #     pass
                lf2.destroy()
                lf=LabelFrame(text='graph')
                lf.pack()
                d={'dx': p[1:11],
                   'dy': r[1:11]}
                dfd=DataFrame(d, columns=['dx', 'dy'])
                figure_d=plt.Figure(dpi=100)
                ax1=figure_d.add_subplot(111)
                bar1=FigureCanvasTkAgg(figure_d, lf)
                bar1.get_tk_widget().pack(fill=X)
                dfd=dfd[['dx', 'dy']].groupby('dx').sum()
                dfd.plot(kind='line', grid=True, ax=ax1)
                label['text']=dfd[0:11]
                click=False
                #plt.axis()

        change()



def main():
    root=Tk()
    root.title('Pandas Dataframe GUI')
    root.geometry('730x600+400+300')
    root.resizable(0,0)
    cnt = Content(root)
    root.mainloop()

if __name__ == '__main__':
    main()
