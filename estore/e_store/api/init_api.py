from sre_compile import isstring
import frappe , json
from datetime import datetime
import requests
import requests.exceptions
from frappe.utils import getdate
from frappe.core.doctype.sms_settings.sms_settings import send_sms
from frappe.desk.search import search_link

# http://127.0.0.1:8000/api/method/estore.e_store.api.init_api.get_categorys

@frappe.whitelist(allow_guest=True)
def get_categorys():
    message=''
    resp_code=500
    data=frappe.db.get_all('Category',['category','image'])
    print(data)
    return {"message": message, "response_code": resp_code, "data": data}

@frappe.whitelist(allow_guest=True)
def get_products():
    message=''
    resp_code=500
    data=frappe.db.get_all('Products',['name','price','description','image1'])
    print(data)
    return {"message": message, "response_code": resp_code, "data": data}

