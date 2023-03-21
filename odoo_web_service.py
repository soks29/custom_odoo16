url = "http://localhost:8016"
db = "test"
username = 'soks'
password = 'ce045b42e6e30cc6d21adc24a41e0cf11a681982'

import xmlrpc.client

common = xmlrpc.client.ServerProxy('{}/xmlrpc/2/common'.format(url))
version = common.version()
print("detail ...", version)

# info = xmlrpc.client.ServerProxy('https://demo.odoo.com/start').start()
# url, db, username, password = info['host'], info['database'], info['user'], info['password']

uid = common.authenticate(db, username, password, {})
print("UID", uid)

models = xmlrpc.client.ServerProxy('{}/xmlrpc/2/object'.format(url))

# ids = models.execute_kw(db, uid, password, 'kzm.instance.request', 'search', [[]])
#
#
# partners_records = models.execute_kw(db, uid, password, 'kzm.instance.request', 'read', [ids], {'fields': ['name',
#                                                                                                            'treat_date',
#                                                                                                            'cpu']})

# partners_records = models.execute_kw(db, uid, password, 'kzm.instance.request', 'search_read', [[]],
#                                      {'fields': ['name', 'state', 'cpu']})
# for x in partners_records:
#     print(x)

# partners_ids = models.execute_kw(db, uid, password, 'kzm.instance.request', 'search', [[[]]])
# print("partners......", partners_ids)

# partners_count = models.execute_kw(db, uid, password,  'res.partner', 'search_count', [[]])
# print("partner count ...", partners_count)
#
# partners_rec = models.execute_kw(db, uid, password,  'res.partner', 'read', [[]])
# print("partner count ...", partners_rec)
#

""" Creation de données """

id_instance = models.execute_kw(db, uid, password, 'kzm.instance.request', 'create', [{'state': "Draft", 'cpu': '4', 'ram': '8'}])
print(id_instance)

""" Option de récupération des commandes par statut  """
# partners_records = models.execute_kw(db, uid, password, 'kzm.instance.request', 'search_read',
#                                      [[['state', '=', 'Draft']]],
#                                      {'fields': ['name', 'state', 'cpu']})
# print("Only Draft")
# for x in partners_records:
#     print(x)
