import customtkinter as ctk
from PIL import Image,ImageTk
from tkinter import ttk
default_color='white'
default_font=('calibri',45,'italic')

initial_start=0
initial_start_2=0
global entry_user
global database_frame

#items in the root
root=ctk.CTk()
root.title('POS MANAGEMENT SYSTEM')
screen_height=root.winfo_screenheight()
screen_width=root.winfo_screenwidth()

initial_start_3=0
total_sales = 0.0
initial_start=0
initial_start_2=0
combination=0
initial_start_2=0
Qty1=0
def btn_beef():
    global Price1
    global Food_item1
    global Qty1
    
    Food_item1 = 'BEEF STEW'
    Price1 = '$ 1.50'
    while True:
        Qty1=Qty1+1
        break
    table.insert('', ctk.END, values=(Food_item1, Price1, Qty1))
    global initial_start
    global initial_end
    while True:
        initial_start = initial_start + 1.50
        combination=initial_start+initial_start_2+initial_start_3
        label_total_price.configure(text=f'$ {combination} ' )
        break
Qty2=0

def btn_roast_chick():
    global Price2
    global Food_item2
    global Qty2
    global btn_beef_clicked
    btn_beef_clicked = True
    Food_item2 = 'ROASTED CHICKEN'
    Price2 = '$ 1.50'
    while True:
        Qty2=Qty2+1
        break
    table.insert('', ctk.END, values=(Food_item2, Price2, Qty2))
    global initial_start
    global initial_end
    while True:
        initial_start = initial_start + 1.50
        combination=initial_start+initial_start_2+initial_start_3
        label_total_price.configure(text=f'$ {combination} ' )
        break
Qty3=0

def btn_chick_stew():
    global Price3
    global Food_item3
    global Qty3
    Food_item3 = 'CHICKEN STEW'
    Price3 = '$ 1.50'
    while True:
        Qty3=Qty3+1
        break
    table.insert('', ctk.END, values=(Food_item3, Price3, Qty3))
    global initial_start
    global initial_end
    while True:
        initial_start = initial_start + 1.50
        combination=initial_start+initial_start_2+initial_start_3
        label_total_price.configure(text=f'$ {combination} ' )
        break
Qty4=0

def btn_chick_stir():
    global Price4
    global Food_item4
    global Qty4
    Food_item4 = 'CHICKEN STIR FRY'
    Price4 = '$ 1.50'
    while True:
        Qty4=Qty4+1
        break
    table.insert('', ctk.END, values=(Food_item4, Price4, Qty4))
    global initial_start
    global initial_end
    while True:
        initial_start = initial_start + 1.50
        combination=initial_start+initial_start_2+initial_start_3
        label_total_price.configure(text=f'$ {combination} ' )
        break
Qty5=0

def btn_chick_curry():
    global Price5
    global Food_item5
    global Qty5
    Food_item5 = 'CHICKEN CURRY'
    Price5 = '$ 1.50'
    while True:
        Qty5=Qty5+1
        break
    table.insert('', ctk.END, values=(Food_item5, Price5, Qty5))
    global initial_start
    global initial_end
    while True:
        initial_start = initial_start + 1.50
        combination=initial_start+initial_start_2+initial_start_3
        label_total_price.configure(text=f'$ {combination} ' )
        break

Qty6=0

def btn_chips():
    global Price6
    global Food_item6
    global Qty6
    Food_item6 = 'CHIPS'
    Price6 = '$ 1.00'
    while True:
        Qty6=Qty6+1
        break
    table.insert('', ctk.END, values=(Food_item6, Price6, Qty6))
    global initial_start_2
    while True:
        initial_start_2 = initial_start_2 + 1.00
        combination=initial_start+initial_start_2+initial_start_3
        label_total_price.configure(text=f'$ {combination} ' )
        break

Qty7=0

def btn_burger():
    global Price7
    global Food_item7
    global Qty7
    Food_item7 = 'BURGERS'
    Price7 = '$ 1.00'
    while True:
        Qty7=Qty7+1
        break
    table.insert('', ctk.END, values=(Food_item7, Price7, Qty7))
    global initial_start_3
    global initial_end_3
    while True:
        initial_start_3 = initial_start_3 + 1.00
        combination=initial_start+initial_start_2+initial_start_3
        label_total_price.configure(text=f'$ {combination} ' )
        break
Qty8=0

def btn_russian_sausage():
    global Price8
    global Food_item8
    global Qty8
    Food_item8 = 'RUSSIAN SAUSAGES'
    Price8 = '$ 2.00'
    while True:
        Qty8=Qty8+1
        break
    
    table.insert('', ctk.END, values=(Food_item8, Price8, Qty8))
    global initial_start_3
    global initial_end_3
    while True:
        initial_start_3 = initial_start_3 + 2.00
        combination=initial_start+initial_start_2+initial_start_3
        label_total_price.configure(text=f'$ {combination} ' )
        break
Qty9=0
def btn_pork_chops():
    global Price9
    global Food_item9
    global Qty9
    Food_item9 = 'PORK CHOPS'
    Price9 = '$ 2.00'
    while True:
        Qty9=Qty9+1
        break
    
    table.insert('', ctk.END, values=(Food_item9, Price9, Qty9))

    global initial_start_3
    global initial_end_3
    while True:
        initial_start_3 = initial_start_3 + 2.00
        combination=initial_start+initial_start_2+initial_start_3
        label_total_price.configure(text=f'$ {combination} ' )
        break

def pay_button():
    global receipt_item
    global balance_total

    data = ""
    for item in table.get_children():
        item_data = table.item(item)
        values = item_data['values']
        data += f"{values[0]} \t {values[1]} \t {values[2]}\n"

    cash_payed=float(entry_user.get())
    combination=initial_start+initial_start_2+initial_start_3
    balance_total=float(cash_payed)-(combination)
    balance_price.configure(text=balance_total)
    label_total_price.configure(text=f'$ {combination} ' )
    receipt_item.configure(text=f'''
Bulawayo 
Selborne Park 
Mountain Road 
Plot 16 
----------------------------------------------------------------
Food item                 Price                      Qty
----------------------------------------------------------------
{data}
----------------------------------------------------------------
Total:         {combination}
Money Payed:  {cash_payed}
Balance:       {balance_total}
======================================================
BEST MEAL EVER!!!!
________________________________________________________________
POWERED BY GROUP 2 :) 

                ''')

def print_button():
    global initial_start_3
    global initial_start
    global initial_start_2
    global Qty9, Qty8, Qty7, Qty6, Qty5, Qty4, Qty3, Qty2, Qty1
    Qty9=0 
    Qty8=0 
    Qty7=0 
    Qty6=0 
    Qty5=0 
    Qty4=0 
    Qty3=0
    Qty2=0
    Qty1=0
    initial_start_3=0
    initial_start=0
    initial_start_2=0
    combination=0
    initial_start_2=0
    Qty1=0
    combination=initial_start+initial_start_2+initial_start_3
    label_total_price.configure(text=f'$ {combination} ' )
    entry_user.delete(0,'end')
    balance_total='$ 0'
    balance_price.configure(text=balance_total)
    table.delete(*table.get_children())
    data = []
    for item in table.get_children():
        item_data = table.item(item)
        item_text = item_data["text"]
        item_values = item_data["values"]
        data.append((item_text, item_values[0]))
    saved_data.extend(data)

    

def save_data():
    data = []
    for item in table.get_children():
        item_data = table.item(item)
        item_values = item_data["values"]
        data.append(item_values)
    saved_data.extend(data)  

def open_data():
    global total_sales
    global items_sold
    for item in table.get_children():
        table.delete(item)  
    
    for item_values in saved_data:
        table.insert("", "end", values=item_values)
    total_sales +=(initial_start+initial_start_2+initial_start_3)
    table.insert('', ctk.END, values=('TOTAL',f'$ {total_sales}'))


entry_var=ctk.DoubleVar()
root.geometry(f'{screen_width}x{screen_height}+0+0')
root.configure(fg_color='black')
comp_name=ctk.CTkLabel(root,text='TCZ POS MANAGEMENT SYSTEM',text_color='red',font=('jokerman',38,'bold'))
comp_name.place(relx=0.01,rely=0.02)
food_frame=ctk.CTkFrame(root,corner_radius=10,fg_color='red',border_color='yellow',border_width=3,width=660,height=580)
food_frame.place(rely=0.128,relx=0.01)
database_frame=ctk.CTkFrame(root,corner_radius=10,fg_color='white',border_color='yellow',border_width=3,width=350,height=453)
database_frame.pack_propagate(False)
database_frame.place(rely=0.02,relx=0.501)
label_total=ctk.CTkLabel(root,text='Total',text_color=default_color,padx=3,bg_color='transparent',font=default_font)
label_cash=ctk.CTkLabel(root,text='Cash:',text_color=default_color,font=default_font)
entry_user=ctk.CTkEntry(root,font=('calibri',23),width=175,border_color='yellow',border_width=2,height=35)
label_balance=ctk.CTkLabel(root,text='Balance:',text_color=default_color,font=default_font)
label_total_price=ctk.CTkLabel(root,text='$ 0',text_color=default_color,font=default_font)
balance_price=ctk.CTkLabel(root,text='$ 0',text_color=default_color,font=default_font)

table = ttk.Treeview(database_frame, columns=('Food item', 'Price', 'Qty'), show='headings',height=400)
table.heading('Food item', text='Food item')
table.heading('Price', text='Price')
table.heading('Qty', text='Qty')
table.pack(pady=5)

table.column('#0', width=100)
table.column('#1', width=130)
table.column('#2', width=100)
table.column('#3', width=100)

saved_data = []

label_total_price.place(relx=0.628,rely=0.70)
label_cash.place(relx=0.501,rely=0.77)
label_balance.place(relx=0.501,rely=0.85)
label_total.place(relx=0.501,rely=0.70)
entry_user.place(rely=0.795,relx=0.628)
balance_price.place(relx=0.628,rely=0.85)


receipt_frame=ctk.CTkFrame(root,corner_radius=10,fg_color='white',border_color='yellow',border_width=3,width=300,height=565)
receipt_frame.pack_propagate(False)
receipt_frame.place(rely=0.02,relx=0.77)

pay=ctk.CTkButton(root,text='PAY',width=140,height=100,command=pay_button)
pay.place(relx=0.77,rely=0.85)

print_reciept=ctk.CTkButton(root,text='PRINT',width=140,height=100,command=print_button)
print_reciept.place(relx=0.88,rely=0.85)

receipt_item=ctk.CTkLabel(receipt_frame,padx=5,corner_radius=10,text='Welcome to your favourite Canteen',anchor='center')
receipt_item.pack(padx=5,pady=5)


food_1=ctk.CTkFrame(food_frame,fg_color=default_color,width=200,height=567)
food_1.pack_propagate(False)
food_1.place(relx=0.015,rely=0.01)
food_2=ctk.CTkFrame(food_frame,fg_color=default_color,width=200,height=567)
food_2.pack_propagate(False)
food_2.place(relx=0.35,rely=0.01)
food_3=ctk.CTkFrame(food_frame,fg_color=default_color,width=200,height=567)
food_3.pack_propagate(False)
food_3.place(relx=0.68,rely=0.01)
global light_image


save_button = ctk.CTkButton(root, text="Save", command=save_data)
save_button.place(relx=0.501,rely=0.65)

open_button = ctk.CTkButton(root, text="Open", command=open_data)
open_button.place(relx=0.64,rely=0.65)

#frame 1
resize=(203,150)
beef_stew_image=Image.open('C:/Users/mwale/Documents/POS_AT_TCZ/beef stew.jpg')
resized_beef=beef_stew_image.resize(resize)
photo1=ImageTk.PhotoImage(resized_beef)
beef_stew=ttk.Button(food_1,image=photo1,command=btn_beef)
beef_stew_price=ctk.CTkLabel(food_1,text='$ 1.50')
beef_stew.pack(expand=False,fill='both')
beef_stew_price.pack(fill='x',padx=5)


roasted_chick_image=Image.open('c:/Users/mwale/Documents/POS_AT_TCZ/roasyed chic.jpg')
resized_roast=roasted_chick_image.resize(resize)
photo2=ImageTk.PhotoImage(resized_roast)
roasted_chick=ttk.Button(food_1,image=photo2,command=btn_roast_chick)
roasted_chick_price=ctk.CTkLabel(food_1,text='$ 1.50')
roasted_chick.pack(fill='both')
roasted_chick_price.pack(fill='x',padx=5)


chick_stew_image=Image.open('c:/Users/mwale/Documents/POS_AT_TCZ/chic stew.jpg')
resized_roast=chick_stew_image.resize(resize)
photo3=ImageTk.PhotoImage(resized_roast)
chick_stew=ttk.Button(food_1,image=photo3,command=btn_chick_stew)
chick_stew_price=ctk.CTkLabel(food_1,text='$ 1.50')
chick_stew.pack(fill='both')
chick_stew_price.pack(fill='x',padx=5)

#frame 2
beef_chick_stir_fry_image=Image.open('c:/Users/mwale/Documents/POS_AT_TCZ/stir fry.jpg')
resized_roast=beef_chick_stir_fry_image.resize(resize)
photo4=ImageTk.PhotoImage(resized_roast)
chick_stew=ttk.Button(food_1,image=photo4)
beef_chick_stir_fry=ttk.Button(food_2,image=photo4,command=btn_chick_stir)
beef_chick_stir_fry_price=ctk.CTkLabel(food_2,text='$ 1.50')
beef_chick_stir_fry.pack(fill='both')
beef_chick_stir_fry_price.pack(fill='x',padx=5)




beef_chick_curry_image=Image.open('c:/Users/mwale/Documents/POS_AT_TCZ/curry chic.jpg')
resized_roast=beef_chick_curry_image.resize(resize)
photo5=ImageTk.PhotoImage(resized_roast)
beef_chick_curry=ttk.Button(food_2,image=photo5,command=btn_chick_curry)
beef_chick_curry_price=ctk.CTkLabel(food_2,text='$ 1.50')
beef_chick_curry.pack(expand=True,fill='both')
beef_chick_curry_price.pack(fill='x',padx=5)


chips_image=Image.open('c:/Users/mwale/Documents/POS_AT_TCZ/chips.jpg')
resized_roast=chips_image.resize(resize)
photo6=ImageTk.PhotoImage(resized_roast)
chips=ttk.Button(food_2,image=photo6,command=btn_chips)
chips_price=ctk.CTkLabel(food_2,text='$ 1.00')
chips.pack(fill='both')
chips_price.pack(fill='x',padx=5)

#frame 3
burger_image=Image.open('c:/Users/mwale/Documents/POS_AT_TCZ/burger.jpg')
resized_roast=burger_image.resize(resize)
photo7=ImageTk.PhotoImage(resized_roast)
burger=ttk.Button(food_3,image=photo7,command=btn_burger)
burger_price=ctk.CTkLabel(food_3,text='$ 1.00')
burger.pack(fill='both')
burger_price.pack(fill='x',padx=5)



russian_sas_image=Image.open('c:/Users/mwale/Documents/POS_AT_TCZ/russian sausage.jpg')
resized_roast=russian_sas_image.resize(resize)
photo8=ImageTk.PhotoImage(resized_roast)
russian_sas=ttk.Button(food_3,image=photo8,command=btn_russian_sausage)
russian_sas_price=ctk.CTkLabel(food_3,text='$ 2.00')
russian_sas.pack(fill='both')
russian_sas_price.pack(fill='x',padx=5)


pork_chops_image=Image.open('c:/Users/mwale/Documents/POS_AT_TCZ/OIP.jfif')
resized_roast=pork_chops_image.resize(resize)
photo9=ImageTk.PhotoImage(resized_roast)
pork_chops=ttk.Button(food_3,image=photo9,command=btn_pork_chops)
pork_chops_price=ctk.CTkLabel(food_3,text='$ 2.00')
pork_chops.pack(fill='both')
pork_chops_price.pack(fill='x',padx=5)

root.mainloop()