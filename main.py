import tkinter as tk
import ttkbootstrap as ttk
from functions import *
import os

def empty_tree():
  for item in tree.get_children():
    tree.delete(item)

def click(x):
  global total_cost
  act_option.set(x)
  dist_label.pack(side='left')
  empty_tree()
  total_cost =0
  res = spec_dis_selector(x)
  dists = []
  for d in res:
    dists.append(d[0])
  
  dist_menu_button = ttk.Menubutton(f2,text='d',width=20)
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

def ok_button_fun():
  output_frame.pack(fill=tk.BOTH,pady=150)

  f3.pack(pady=10)
  f7.pack(pady=10)

  act = act_option.get()
  dis = dist_option.get()

  spots = spot_selector(act,dis)
  sp = []
  for s in spots:
    sp.append(s[0])
  
  output_var.set('\n'.join(sp))
  title_var.set(f'TOP SPOTS')

  act = act_option.get()
  items = item_selector(act)
  
  it =[]
  id = []
  for i in items:
    it.append(i[0])
    id.append(i[1])
  
  item_menu_button = ttk.Menubutton(f3,text='nothing',width=20)
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

def ok_button_fun3():
  global l
  act = act_option.get()
  ite = item_option.get()
  item = spec_item_selector(act,ite)

  item_id = item[0][0]

  shop = shop_selector(item_id)

  shops =[]
  for i in shop:
    price = price_selector(item_id,i[0])
    pr = price[0][0]
    t = str(item_id)+'#'+i[0]+'-'+str(pr)
    shops.append(t)

  f5 = ttk.Frame(master=f4)
  
  def shop_check(j):
    data = []
    t = (item_option.get(),(j.split('-')[0]).split('#')[1],j.split('-')[1])
    data.append(t)
    global total_cost,l
    co = j.split('-')[1]
    if j not in l:
      l.append(j)
      tree.insert('','end',value=t)
      total_cost+=int(co)
    else:
      l.remove(j)
      re = tree.get_children()
      for child in re:
        it = tree.item(child)
        shop_name = it['values'][1]
        item_name = it['values'][0]
        act_name = act_option.get()
        it_id = spec_item_selector(act_name,item_name)[0][0]
        final_name = str(it_id)+'#'+shop_name
        if final_name ==j.split('-')[0]:
          tree.delete(child)
          break
      total_cost-=int(co)
    print(l)
    cost_option.set(total_cost)

  c=ttk.BooleanVar(value=True)
  for j in shops:
    shop_checkbox = tk.Checkbutton(
        master=f5,
        text=j.split('#')[1],
        font= 'Calibri 12',
        command=lambda j=j:shop_check(j)
    )
    if j in l:
      print('in')
      shop_checkbox.select()
    else:
      print('out')
    shop_checkbox.pack(anchor='w',pady=5)

  

  if (len(f4.winfo_children())>1):
    f4.winfo_children()[0].destroy()
  f4.pack()
  f5.pack(pady=5)
  f6.pack(pady=10,fill=tk.BOTH,anchor='se')

def update():
 win.destroy()
 os.system('python main.py')

win = ttk.Window(themename='darkly')
win.attributes('-fullscreen',True)
win.title('OAR')
win.geometry('1600x800')
style = ttk.Style()


f00 = ttk.Frame(master=win,width=800)
f001 = ttk.Frame(master=f00)
main_label = ttk.Label(
  master=f001,
  text='OAR',
  font='Calibri 48'
)
main_label.pack()

#*ACTIVITY
f1 = ttk.Frame(master=f001)

act_label = ttk.Label(
  master=f1,
  text='Select Activity:',
  font='Calibri 12'
)
act_label.pack(side='left')

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

for x in act:
  menu.add_radiobutton(label= x, command=lambda x=x: click(x))
menu_button.config(textvariable=act_option)

menu.add_separator()
f1.pack()

#*DISTRICT 
f2 = ttk.Frame(master=f001)

dist_label = ttk.Label(
  master=f2,
  text='Select District:',
  font='Calibri 12'
)

dist_option = ttk.StringVar()
f2.pack()

#*OUTPUT
ok_button_2 = ttk.Button(
  master=f001,
  text='OK',
  command=ok_button_fun,
  width=5,
  bootstyle = 'primary outline'
)
ok_button_2.pack(pady=10)

f001.pack(pady=100,fill=tk.BOTH)

# SEPARATOR
sep = ttk.Frame(f00,bootstyle = 'primary',)
sep.pack(fill='x')

output_frame = ttk.Frame(master=f00)
output_var = ttk.StringVar()
title_var = ttk.StringVar()
output_title = ttk.Label(
  master=output_frame,
  text="Spots",
  font="Calibre 20",
  textvariable=title_var,
)
output_title.pack(pady=5)
output_label = ttk.Label(
  master=output_frame,
  text='Output',
  font='Calibri 15',
  textvariable=output_var,
)
output_label.pack(pady=20,padx=20)

# SEPARATOR
sep2 = ttk.Separator(f00,bootstyle = 'primary')
f00.pack(side=tk.LEFT,fill=tk.BOTH,expand=True)

#####################################################
sep_main = ttk.Frame(win,bootstyle = 'primary')
sep_main.pack(side=tk.LEFT,fill=tk.Y)
#####################################################

f01 = ttk.Frame(master=win,width=800)
f3 = ttk.Frame(master=f01)
item_option = ttk.StringVar()

item_label = ttk.Label(
  master=f3,
  text='Select Item:',
  font='Calibri 12'
)
item_label.pack(side='left')


total_cost =0
l=[]
  
f7 = ttk.Frame(master=f01)
ok_button_3 = ttk.Button(
  master=f7,
  text='Find Shops',
  command=ok_button_fun3,
  width=10,
  bootstyle = 'primary outline'
)
ok_button_3.pack(pady=5)

f4 = ttk.Frame(master=f01)

f6 = ttk.Frame(master=f01)
tree = ttk.Treeview(
  master=f6,
  columns=('ITEM','SHOP','PRICE'),
  show='headings'
)
tree.column('ITEM',anchor='center')
tree.column('SHOP',anchor='center')
tree.column('PRICE',anchor='center')
tree.heading('ITEM', text='ITEM')
tree.heading('SHOP', text='SHOP')
tree.heading('PRICE', text='PRICE')
tree.pack(expand=tk.YES)

cost_option = ttk.StringVar()
cost_title = ttk.Label(
  master=f6,
  text='TOTAL COST:',
  font='Calibri 12'
)
cost_title.pack()
cost_label = ttk.Label(
  master=f6,
  text=':',
  textvariable=cost_option,
  font='Calibri 12'
)
cost_label.pack()
f01.pack(side=tk.RIGHT,fill=tk.BOTH,expand=True,pady=230)

refresh = ttk.Button(win,text="Refresh",command=update)
refresh.pack()

win.mainloop()