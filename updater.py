from sqlcon import *

db_selector()

def deleter(id):
  try:
    querytaker(f"delete from activity where act_id = {id};")
    # querytaker(f"delete from place where act_id = {id};")
  except mysql.connector.Error as error:
    return error
  return f'All correspondence of activity id {id} deleted from all tables'

def activity_inserter(act_id,act_name):
  try:
    querytaker(f"insert into activity values({act_id},'{act_name}');")
  except mysql.connector.Error as error:
    return error
  return f"Inserted act_id:{act_id}, act_name:{act_name} to Activity Table."

def place_inserter(act_id,place_name,place_dist):
  try:
    querytaker(f"insert into place values({act_id},'{place_name}','{place_dist}')")
  except mysql.connector.Error as error:
    return error
  return f"Inserted act_id:{act_id}, Place_name:{place_name}, District:{place_dist} to Place Table"

def shop_inserter(item_id,shop_name,shop_id,price):
  try:
    querytaker(f"insert into shop values({item_id},'{shop_name}',{shop_id},{price});")
  except mysql.connector.Error as error:
    return error
  return f"Inserted item_id{item_id}, shop_name:'{shop_name}', shop_id:{shop_id}, price:{price} to Shop Table"

def item_inserter(act_id,item_id,item_name):
  try:
    querytaker(f"insert into item values({act_id},{item_id},'{item_name}');")
  except mysql.connector.Error as error:
    return error
  return f"Inserted act_id:{act_id}, item_id:{item_id}, item_name:{item_name} to Item Table"


