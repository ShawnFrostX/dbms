import tkinter as tk
import ttkbootstrap as ttk
from functions import *

win = ttk.Window(themename='darkly')
win.geometry('800x1000')

main_label = ttk.Label(
  master=win,
  text='OAR',
  font='Calibri 48'
)
main_label.pack()


#*ACTIVITY
f1 = ttk.Frame()

act_label = ttk.Label(
  master=f1,
  text='Select Activity:',
  font='Calibri 12'
)
act_label.pack(side='left')

# ttk.Style().configure('custom.TButton',foreground='white',background='#007bff')
menu_button = ttk.Menubutton(f1,text='something',width=20)
menu_button.pack(pady=10)

activity = activity_selector()
act = []
for a in activity:
  act.append(a[1])

menu = ttk.Menu(menu_button)
menu_button['menu']=menu

act_option = ttk.StringVar()
act_option.set(act[0])

def click(x):
  act_option.set(x)

  res = spec_dis_selector(x)
  dists = []
  for d in res:
    dists.append(d[0])
  print(dists)
  
  dist_menu_button = ttk.Menubutton(f2,text='dsaf',width=20)
  dist_menu_button.pack()
  if (len(f2.winfo_children())>2):
    f2.winfo_children()[1].destroy()
  
  dist_menu = ttk.Menu(dist_menu_button)
  dist_menu_button['menu']=dist_menu

  dist_option.set(dists[0])

  def click2(x):
    dist_option.set(x)

  for y in dists:
    dist_menu.add_radiobutton(label=y,command=lambda z=y:click2(z))
  dist_menu_button.config(textvariable=dist_option)


for x in act:
  menu.add_radiobutton(label= x, command=lambda x=x: click(x))
menu_button.config(textvariable=act_option)

menu.add_separator()
f1.pack()

#*DISTRICT 
f2 = ttk.Frame()

dist_label = ttk.Label(
  master=f2,
  text='Select District:',
  font='Calibri 12'
)
dist_label.pack(side='left')

dist_option = ttk.StringVar()
f2.pack()

#*OUTPUT
def ok_button_fun():
  act = act_option.get()
  dis = dist_option.get()

  spots = spot_selector(act,dis)
  sp = []
  for s in spots:
    sp.append(s[0])
  
  output_var.set('\n'.join(sp))
  title_var.set(f'Spots in {dis} for {act}')

  act = act_option.get()
  items = item_selector(act)
  
  it =[]
  id = []
  for i in items:
    it.append(i[0])
    id.append(i[1])
  
  
  item_menu_button = ttk.Menubutton(f3,text='ss',width=20)
  item_menu_button.pack()

  if (len(f3.winfo_children())>2):
    f3.winfo_children()[1].destroy()


  item_menu = ttk.Menu(item_menu_button)
  item_menu_button['menu']=item_menu

  item_option.set(it[0])

  

  def item_adder(x):
    item_option.set(x)
    

  for x in it:
    item_menu.add_radiobutton(label= x, command=lambda x=x: item_adder(x))
  item_menu_button.config(textvariable=item_option)

ok_button_2 = ttk.Button(
  master=win,
  text='OK',
  command=ok_button_fun,
  width=5,
  bootstyle = 'primary outline'
)
ok_button_2.pack(pady=10)

# SEPARATOR
sep = ttk.Separator(win,bootstyle = 'primary')
sep.pack(pady=5,fill='x',padx=10)
style = ttk.Style()

output_var = ttk.StringVar()
title_var = ttk.StringVar()
output_title = ttk.Label(
  master=win,
  text="Spots",
  font="Calibre 15",
  textvariable=title_var,
)
output_title.pack(pady=5)
output_label = ttk.Label(
  master=win,
  text='Output',
  font='Calibri 12',
  textvariable=output_var,
  
  # compound=tk.CENTER,
  # anchor='center'
)
output_label.pack(pady=20,padx=20)

# SEPARATOR
sep2 = ttk.Separator(win,bootstyle = 'primary')
sep2.pack(pady=5,fill='x',padx=10)


f3 = ttk.Frame()
item_option = ttk.StringVar()

item_label = ttk.Label(
  master=f3,
  text='Select Item:',
  font='Calibri 12'
)
item_label.pack(side='left')
f3.pack(pady=10)

total_cost =0
l=[]
def ok_button_fun3():
  act = act_option.get()
  ite = item_option.get()
  item = spec_item_selector(act,ite)

  item_id = item[0][0]

  shop = shop_selector(item_id)
  print(shop)

  shops =[]
  for i in shop:
    price = price_selector(item_id,i[0])
    pr = price[0][0]
    t = i[0]+'-'+str(pr)
    print(t)
    shops.append(t)

  f5 = ttk.Frame(master=f4)
  
  def shop_check(j):
    global total_cost,l
    co = j.split('-')[1]
    if j not in l:
      l.append(j)
      total_cost+=int(co)
      print(l)
    else:
      l.remove(j)
      total_cost-=int(co)

    
    cost_option.set(total_cost)

      


  shop_select_var = ttk.BooleanVar()
  for j in shops:
    shop_checkbox = ttk.Checkbutton(
      master=f5,
      text=j,
      # variable=shop_select_var,
      command=lambda j=j:shop_check(j)
    )
    shop_checkbox.pack(anchor='w',pady=5)

  if (len(f4.winfo_children())>1):
    f4.winfo_children()[0].destroy()
  f5.pack(pady=10)
  

ok_button_3 = ttk.Button(
  master=win,
  text='Find Shops',
  command=ok_button_fun3,
  width=10,
  bootstyle = 'primary outline'
)
ok_button_3.pack(pady=10)
# SEPARATOR
sep3 = ttk.Separator(win,bootstyle = 'primary')
sep3.pack(pady=5,fill='x',padx=10)

f4 = ttk.Frame(master=win)
f4.pack()

f6 = ttk.Frame(master=win)
cost_option = ttk.StringVar()
cost_title = ttk.Label(
  master=f6,
  text='TOTAL COST:',
  font='Calibri 12'
)
cost_title.pack(side='left')
cost_label = ttk.Label(
  master=f6,
  text=':',
  textvariable=cost_option,
  font='Calibri 12'
)
cost_label.pack(side='left')
f6.pack(pady=10)


win.mainloop()