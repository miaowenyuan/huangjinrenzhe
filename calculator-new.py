import tkinter
from functools import partial

def get_input(entry,argu):
    input_data = entry.get()

    if (input_data[-1:]=='+') and (argu == '+'):
        return

    if (input_data[-2:]=='+-') and (argu == '-'):
        return

    if (input_data[-2:]=='--') and (argu in ['-','+']):
        return

    if (input_data[-2:]=='**') and (argu in ['*','/']):
        return

    entry.insert('end',argu)

def backspace(entry):
    input_len=len(entry.get())
    entry.delete(input_len -1)

def clear(entry):
    entry.delete(0,'end')

def calc(entry):
    input_data = entry.get()
    if not input_data:
        return
    clear(entry)

    try:
        output_data=str(eval(input_data))
    except Exception:
        entry.insert('end','Calculation error')
    else:
        if len(output_data)>20:
            entry.insert('end','Value overflow')
        else:
            entry.insert('end',output_data)

if __name__=='__main__':

    root=tkinter.Tk()
    root.title('Calculator')

    root.resizable(True,True)

    button_bg='orange'
    math_sign_bg='DarkTurquoise'
    cal_output_bg='YellowGreen'
    button_active_bg='gray'

    entry=tkinter.Entry(root,justify='right',font=1)
    entry.grid(row = 0, column=0,columnspan=4, padx=10, pady=10)

    def place_button(text,func,func_params, bg=button_bg, **place_params):
        my_button= partial(tkinter.Button, root, bg=button_bg, padx=10,pady=3,activebackground=button_active_bg)
        button=my_button(text=text,bg=bg,command=lambda: func(*func_params))
        button.grid(**place_params)

    place_button('7',get_input,(entry,'7'),row=1,column=0,ipadx=5,pady=5)
    place_button('8',get_input,(entry,'8'),row=1,column=1,ipadx=5,pady=5)
    place_button('9',get_input,(entry,'9'),row=1,column=2,ipadx=5,pady=5)
    place_button('4',get_input,(entry,'4'),row=2,column=0,ipadx=5,pady=5)
    place_button('5',get_input,(entry,'5'),row=2,column=1,ipadx=5,pady=5)
    place_button('6',get_input,(entry,'6'),row=2,column=2,ipadx=5,pady=5)
    place_button('1',get_input,(entry,'1'),row=3,column=0,ipadx=5,pady=5)
    place_button('2',get_input,(entry,'2'),row=3,column=1,ipadx=5,pady=5)
    place_button('3',get_input,(entry,'3'),row=3,column=2,ipadx=5,pady=5)
    place_button('0',get_input,(entry,'0'),row=4,column=0,ipadx=8,pady=5,columnspan=2,sticky=tkinter.E + tkinter.W + tkinter.N + tkinter.S)
    place_button('.',get_input,(entry,'.'),row=4,column=2,ipadx=7,padx=5,pady=5)

    place_button('+',get_input,(entry,'+'),bg=math_sign_bg,row=1,column=3,ipadx=5,pady=5)
    place_button('-',get_input,(entry,'-'),bg=math_sign_bg,row=2,column=3,ipadx=5,pady=5)
    place_button('*',get_input,(entry,'*'),bg=math_sign_bg,row=3,column=3,ipadx=5,pady=5)
    place_button('/',get_input,(entry,'/'),bg=math_sign_bg,row=4,column=3,ipadx=5,pady=5)

    place_button('<-',backspace,(entry,),row=5,column=0,ipadx=5,padx=5,pady=5)
    place_button('C',clear,(entry,), row=5,column=1,pady=5,ipadx=5)
    place_button('=',calc,(entry,),bg=cal_output_bg,row=5,column=2,ipadx=5,padx=5,pady=5,columnspan=2, sticky=tkinter.E+tkinter.W+tkinter.N+tkinter.S)

    root.mainloop()

    
    
    
        
    
