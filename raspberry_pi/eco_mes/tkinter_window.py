import tkinter as tk
import tkinter.messagebox as tkms
import datetime

def insert_point():
    print("Count down T loss")
    ini_time = datetime.datetime.now()
    loss_type = "T Loss"
    returned_values['ini_time'] = ini_time
    returned_values['loss_type'] = loss_type
    tkms.showinfo("Message","Start to count down for T loss.")

def insert_end():
    print("Count down O loss")
    ini_time = datetime.datetime.now()
    loss_type = "O Loss"
    returned_values['ini_time'] = ini_time
    returned_values['loss_type'] = loss_type
    tkms.showinfo("Message","Start to count down for O loss.")
    
def reset():
    if returned_values['loss_type'] != "reset":
        print("Reset")
        ini_time_ = datetime.datetime.now()
        stopped_time = ini_time_ - returned_values["ini_time"]
        message = "{}: {} s.".format(returned_values['loss_type'],stopped_time.total_seconds())
        print(message) 
        tkms.showinfo("Message",message)
        returned_values['loss_type'] = "reset"
    else:
        tkms.showwarning("Warning", "Please click on T/O loss first.")
        
    
def do_job():
    print("3")
    

if __name__ == '__main__':
    
    loss_dic = {1:"T Loss", 2:"O Loss"}
    returned_values = {}
    
    window = tk.Tk()
    window.title('This is a trial version.')
    window.geometry('900x600')

    menubar = tk.Menu(window)
     
    # 第6步，创建一个File菜单项（默认不下拉，下拉内容包括New，Open，Save，Exit功能项）
    filemenu = tk.Menu(menubar, tearoff=0)
    # 将上面定义的空菜单命名为File，放在菜单栏中，就是装入那个容器中
    menubar.add_cascade(label='File', menu=filemenu)
     
    # 在File中加入New、Open、Save等小菜单，即我们平时看到的下拉菜单，每一个小菜单对应命令操作。
    filemenu.add_command(label='New', command=do_job)
    filemenu.add_command(label='Open', command=do_job)
    filemenu.add_command(label='Save', command=do_job)
    filemenu.add_separator()    # 添加一条分隔线
    filemenu.add_command(label='Exit', command=window.quit) # 用tkinter里面自带的quit()函数


    b1 = tk.Button(window, text='T loss', width=25,
                   height=5, bg = 'red', font = ("Time New Roman", 15), command=insert_point)
    b1.place(x=150, y=100, anchor='nw')


    b2 = tk.Button(window, text='O loss', width=25,
                   height=5, bg = 'orange',font = ("Time New Roman", 15), command=insert_end)
    b2.place(x=550, y=100, anchor='nw')

    b3 = tk.Button(window, text='reset', width=25,
                   height=5, bg = 'White', font = ("Time New Roman", 10), command=reset)
    b3.place(x=400, y=300, anchor='nw')

    window.config(menu=menubar)
