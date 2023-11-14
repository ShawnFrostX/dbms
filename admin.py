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
  id = actid_entry_option.get()
  aname = actname_entry_option.get()
  pname = place_entry_option.get()
  dname = dist_entry_option.get()
  k = activity_inserter(id,aname,pname,dname)
  del_final_label_option.set(k)
def remover():
  x=del_entry_option.get()
  k=deleter(x)
  del_final_label_option.set(k)

root = ttk.Window(themename='darkly')
root.geometry('1280x720')
root.attributes('-fullscreen',True)
f00 = ttk.Frame(master=root,width=640)

#!Activity part
act_label = ttk.Label(
  master=f00,
  text='INSERT ACTIVITY AND PLACE',
  font='Calibri 15'
)
act_label.pack(pady=30)
#*ID
factid = ttk.Frame(master=f00)
actid_label = ttk.Label(
  factid,
  text='Activity ID:',
  font='Calibri 12'
)
actid_label.pack(pady=10,side='left')

actid_entry_option = ttk.IntVar()
actid_entry = ttk.Entry(
  factid,
  textvariable=actid_entry_option
)
actid_entry.pack(side='left')
factid.pack()
#*ACTIVITY
factname = ttk.Frame(master=f00)
actname_label = ttk.Label(
  factname,
  text='Activity Name:',
  font='Calibri 12'
)
actname_label.pack(pady=10,side='left')

actname_entry_option = ttk.StringVar()
actname_entry = ttk.Entry(
  factname,
  textvariable=actname_entry_option
)
actname_entry.pack(side='left')
factname.pack()
#*PLACE
fplace = ttk.Frame(master=f00)
place_label = ttk.Label(
  fplace,
  text='Place Name:',
  font='Calibri 12'
)
place_label.pack(pady=10,side='left')

place_entry_option = ttk.StringVar()
place_entry = ttk.Entry(
  fplace,
  textvariable=place_entry_option
)
place_entry.pack(side='left')
fplace.pack()

#*DISTRICT
fdist = ttk.Frame(master=f00)
dist_label = ttk.Label(
  fdist,
  text='District Name:',
  font='Calibri 12'
)
dist_label.pack(pady=10,side='left')

dist_entry_option = ttk.StringVar()
dist_entry = ttk.Entry(
  fdist,
  textvariable=dist_entry_option
)
dist_entry.pack(side='left')
fdist.pack()

act_insert_button = ttk.Button(
  f00,
  text='INSERT',
  command=insert_act
)
act_insert_button.pack(pady=10,padx=10)

#!ITEM PART
item_label = ttk.Label(
  master=f00,
  text='INSERT ITEM DETAILS',
  font='Calibri 15'
)
item_label.pack(pady=30)
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
shop_label.pack(pady=30)
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



