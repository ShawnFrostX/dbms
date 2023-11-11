from sqlcon import *

db_selector()

def activity_selector():
  res = querysender('select * from activity')
  return res

def spot_selector(ac,di):
  res = querysender(f"select place from place where district = '{di}' and act_id = (select act_id from activity where act_name = '{ac}');")
  return res

def district_selector():
  res = querysender('select distinct district from place')
  return res

def spec_dis_selector(ac):
  res = querysender(f"select distinct district from place where act_id = (select act_id from activity where act_name = '{ac}');")
  return res

def item_selector(ac):
  res = querysender(f"select item,item_id from item where act_id =(select act_id from activity where act_name = '{ac}');")
  return res

def spec_item_selector(ac,it):
  res = querysender(f"select item_id from item where item = '{it}' and act_id = (select act_id from activity where act_name = '{ac}');")
  return res
def shop_selector(it):
  res = querysender(f"select shop from shop where item_id = {it};")
  return res

def price_selector(it_id , sh):
  res = querysender(f"select price from shop where item_id = {it_id} and shop = '{sh}';")
  return res



