from updater import *
import tkinter as tk
import ttkbootstrap as ttk

def insert_shop():
  iid = shop_itemid_entry_option.get()
  sname = shop_shopname_entry_option.get()
  sid = shop_shopid_entry_option.get()
  pr = shop_price_entry_option.get()
  k=shop_inserter(iid,sname,sid,pr)
  del_final_label_option.set(k)

def insert_item():
  aid = item_actid_entry_option.get()
  iid = item_itemid_entry_option.get()
  iname = item_itemname_entry_option.get()
  k=item_inserter(aid,iid,iname)
  del_final_label_option.set(k)

def insert_act():
  idd = act_actid_entry_option.get()
  aname = act_actname_entry_option.get()
  k = activity_inserter(idd,aname,)
  del_final_label_option.set(k)
def insert_place():
  idd = place_actid_entry_option.get()
  pname = place_place_entry_option.get()
  dname = place_dist_entry_option.get()
  k = place_inserter(idd,pname,dname)
  del_final_label_option.set(k)
def remover():
  x=del_entry_option.get()
  k=deleter(x)
  del_final_label_option.set(k)

root = ttk.Window(themename='darkly')
root.geometry('1280x720')
root.title('ADMIN')
root.attributes('-fullscreen',True)
main_label = ttk.Label(
  master=root,
  text='ADMINISTRATOR PRIVILEGE',
  font='Calibri 20'
)
main_label.pack(pady=10)
separator = ttk.Frame(
  master=root,
  bootstyle = 'primary',
  height=2
)
separator.pack(fill=tk.X)

f00 = ttk.Frame(master=root,width=640)

#!Activity part
act_label = ttk.Label(
  master=f00,
  text='INSERT ACTIVITY',
  font='Calibri 15'
)
act_label.pack(pady=5)
#*ID

act_actid = ttk.Frame(master=f00)
act_actid_label = ttk.Label(
  act_actid,
  text='Activity ID:',
  font='Calibri 12'
)
act_actid_label.pack(pady=10,side='left')

act_actid_entry_option = ttk.IntVar()
act_actid_entry = ttk.Entry(
  act_actid,
  textvariable=act_actid_entry_option
)
act_actid_entry.pack(side='left')
act_actid.pack()

#*ACTIVITY

act_actname = ttk.Frame(master=f00)
act_actname_label = ttk.Label(
  act_actname,
  text='Activity Name:',
  font='Calibri 12'
)
act_actname_label.pack(pady=10,side='left')

act_actname_entry_option = ttk.StringVar()
act_actname_entry = ttk.Entry(
  act_actname,
  textvariable=act_actname_entry_option
)
act_actname_entry.pack(side='left')
act_actname.pack()


act_insert_button = ttk.Button(
  f00,
  text='INSERT',
  command=insert_act
)
act_insert_button.pack(pady=10,padx=10)

#!place

place_label = ttk.Label(
  master=f00,
  text='INSERT PLACE',
  font='Calibri 15'
)
place_label.pack(pady=5)

#*PLACE act id

place_actid = ttk.Frame(master=f00)
place_actid_label = ttk.Label(
  place_actid,
  text='Activity ID:',
  font='Calibri 12'
)
place_actid_label.pack(pady=10,side='left')

place_actid_entry_option = ttk.IntVar()
place_actid_entry = ttk.Entry(
  place_actid,
  textvariable=place_actid_entry_option
)
place_actid_entry.pack(side='left')
place_actid.pack()

#*place place

place_place = ttk.Frame(master=f00)
place_place_label = ttk.Label(
  place_place,
  text='Place:',
  font='Calibri 12'
)
place_place_label.pack(pady=10,side='left')

place_place_entry_option = ttk.StringVar()
place_place_entry = ttk.Entry(
  place_place,
  textvariable=place_place_entry_option
)
place_place_entry.pack(side='left')
place_place.pack()

#*DISTRICT

place_dist = ttk.Frame(master=f00)
place_dist_label = ttk.Label(
  place_dist,
  text='District:',
  font='Calibri 12'
)
place_dist_label.pack(pady=10,side='left')

place_dist_entry_option = ttk.StringVar()
place_dist_entry = ttk.Entry(
  place_dist,
  textvariable=place_dist_entry_option
)
place_dist_entry.pack(side='left')
place_dist.pack()

place_insert_button = ttk.Button(
  f00,
  text='INSERT',
  command=insert_place
)
place_insert_button.pack(pady=10,padx=10)

#!ITEM PART
item_label = ttk.Label(
  master=f00,
  text='INSERT ITEM DETAILS',
  font='Calibri 15'
)
item_label.pack(pady=5)
#*item actid
item_actid = ttk.Frame(master=f00)
item_actid_label = ttk.Label(
  item_actid,
  text='Activity ID:',
  font='Calibri 12'
)
item_actid_label.pack(pady=10,side='left')

item_actid_entry_option = ttk.IntVar()
item_actid_entry = ttk.Entry(
  item_actid,
  textvariable=item_actid_entry_option
)
item_actid_entry.pack(side='left')
item_actid.pack()

#*item itemid
item_itemid = ttk.Frame(master=f00)
item_itemid_label = ttk.Label(
  item_itemid,
  text='Item ID:',
  font='Calibri 12'
)
item_itemid_label.pack(pady=10,side='left')

item_itemid_entry_option = ttk.IntVar()
item_itemid_entry = ttk.Entry(
  item_itemid,
  textvariable=item_itemid_entry_option
)
item_itemid_entry.pack(side='left')
item_itemid.pack()

#*item name
item_itemname = ttk.Frame(master=f00)
item_itemname_label = ttk.Label(
  item_itemname,
  text='Item Name:',
  font='Calibri 12'
)
item_itemname_label.pack(pady=10,side='left')

item_itemname_entry_option = ttk.StringVar()
item_itemname_entry = ttk.Entry(
  item_itemname,
  textvariable=item_itemname_entry_option
)
item_itemname_entry.pack(side='left')
item_itemname.pack()

item_insert_button = ttk.Button(
  f00,
  text='INSERT',
  command=insert_item
)
item_insert_button.pack(pady=10,padx=10)

#!SHOP
shop_label = ttk.Label(
  master=f00,
  text='INSERT SHOP DETAILS',
  font='Calibri 15'
)
shop_label.pack(pady=5)
#*shop itemid
shop_itemid = ttk.Frame(master=f00)
shop_itemid_label = ttk.Label(
  shop_itemid,
  text='Item ID:',
  font='Calibri 12'
)
shop_itemid_label.pack(pady=10,side='left')

shop_itemid_entry_option = ttk.IntVar()
shop_itemid_entry = ttk.Entry(
  shop_itemid,
  textvariable=shop_itemid_entry_option
)
shop_itemid_entry.pack(side='left')
shop_itemid.pack()

#*shop shopname
shop_shopname = ttk.Frame(master=f00)
shop_shopname_label = ttk.Label(
  shop_shopname,
  text='Shop Name:',
  font='Calibri 12'
)
shop_shopname_label.pack(pady=10,side='left')

shop_shopname_entry_option = ttk.StringVar()
shop_shopname_entry = ttk.Entry(
  shop_shopname,
  textvariable=shop_shopname_entry_option
)
shop_shopname_entry.pack(side='left')
shop_shopname.pack()

#*shop shopid
shop_shopid = ttk.Frame(master=f00)
shop_shopid_label = ttk.Label(
  shop_shopid,
  text='Shop ID:',
  font='Calibri 12'
)
shop_shopid_label.pack(pady=10,side='left')

shop_shopid_entry_option = ttk.IntVar()
shop_shopid_entry = ttk.Entry(
  shop_shopid,
  textvariable=shop_shopid_entry_option
)
shop_shopid_entry.pack(side='left')
shop_shopid.pack()

#*shop price
shop_price = ttk.Frame(master=f00)
shop_price_label = ttk.Label(
  shop_price,
  text='Price:',
  font='Calibri 12'
)
shop_price_label.pack(pady=10,side='left')

shop_price_entry_option = ttk.IntVar()
shop_price_entry = ttk.Entry(
  shop_price,
  textvariable=shop_price_entry_option
)
shop_price_entry.pack(side='left')
shop_price.pack()

shop_insert_button = ttk.Button(
  f00,
  text='INSERT',
  command=insert_shop
)
shop_insert_button.pack(pady=10,padx=10)

f00.pack(side=tk.LEFT,fill=tk.BOTH,expand=True)

#####################################################################################


sep_frame = ttk.Frame(master=root,bootstyle = 'primary',width=2)
sep_frame.pack(side=tk.LEFT,fill=tk.Y)


#####################################################################################

f001 = ttk.Frame(master=root,width=640)
f01 = ttk.Frame(master=f001)
del_frame = ttk.Frame(master=f01)

del_label = ttk.Label(
  del_frame,
  text='Activity ID:',
  font='Calibri 12'
)
del_label.pack(pady=10,side='left')
del_entry_option = ttk.IntVar()
del_entry = ttk.Entry(
  del_frame,
  textvariable=del_entry_option
  )
del_entry.pack(side='left')
del_frame.pack()

del_button = ttk.Button(
  f01,
  text='DELETE',
  command=remover
)
del_button.pack(pady=10,padx=10)
f01.pack(fill=tk.BOTH,pady=100)

f0s = ttk.Frame(master=f001,bootstyle = 'primary',height=2)
f0s.pack(fill=tk.X)

f02 = ttk.Frame(master=f001)
del_final_label_option = ttk.StringVar()
del_final_label = ttk.Label(
  f02,
  text='sds',
  textvariable=del_final_label_option,
  font='Calibri 15'
)
del_final_label.pack()
f02.pack(pady=200)
f001.pack(side=tk.RIGHT,fill=tk.BOTH,expand=True)

root.mainloop()



