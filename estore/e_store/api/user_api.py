from sre_compile import isstring
import frappe , json
from datetime import datetime
import requests
import requests.exceptions
from frappe.utils import getdate
from frappe.core.doctype.sms_settings.sms_settings import send_sms
from frappe.desk.search import search_link

# http://127.0.0.1:8000/api/method/estore.e_store.api.user_api.set_user

@frappe.whitelist(allow_guest=True)
def login_user():
    print(frappe.request.method)
    if frappe.request.data:
        data=json.loads(frappe.request.data)
    print(data)
    auth=frappe.db.get_value('Customer login',{'customer_id':data['customer_id'],'password':data['password']},['customer_id'])
    message=''
    resp_code=500
    return {"message": message, "response_code": resp_code, "data": auth}

@frappe.whitelist(allow_guest=True)
def set_user():
    print(frappe.request.method)
    if frappe.request.data:
        data=json.loads(frappe.request.data)
    data["doctype"]="Customer"
    data["customer_id"]='@'+data["name1"]
    customer=frappe.get_doc(data)
    customer.insert(ignore_permissions=True)
    customer.submit()
    message='ok'
    resp_code=500
    return {"message": message, "response_code": resp_code, "data": data}

# Dummy user data
# {
#   "name1":"rushil",
#   "password":"1234",
#   "email":"krupalvora789@gmail.com",
#   "contact":"8104409285",
#   "address":"A6 kalpakchs"
# }