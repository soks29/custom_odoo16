# custom_odoo16
## Repositories de deux modules odoo creer a base de la v16, afin de simuler la creation des models, vues, controllers ...
## heritage des vues, models, methodes ... 

### Creez un fichier python et copier-coller ces lignes de code:
=> url= ip_address:8016
##### exemple: http://127.0.0.1:8016 (adresse du serveur odoo)
=> db= name_db
##### exemple: db = "test"
=> username = 'admin'

=> password = 'admin'
##### username & password sont vos identifiants au serveur odoo
=> import xmlrpc.client

=> common = xmlrpc.client.ServerProxy('{}/xmlrpc/2/common'.format(url))
=> version = common.version()

=> uid = common.authenticate(db, username, password, {})

### Récupération de toutes les demandes d'instance:
=> models = xmlrpc.client.ServerProxy('{}/xmlrpc/2/object'.format(url))
=> ids = models.execute_kw(db, uid, password, 'kzm.instance.request'', 'search', [[]])
=> partners_records = models.execute_kw(db, uid, password, 'kzm.instance.request', 'read', [ids],
                                     {'fields': ['name', 'treat_date', 'cpu']})

### Option de creation des demandes:
=> id_instance = models.execute_kw(db, uid, password, 'kzm.instance.request', 'create',
                                [{'state': "Submissive", 'cpu': 3, 'ram': 16}])


### Pour la recuperation des demandes par statut:
=> partners_records = models.execute_kw(db, uid, password, 'kzm.instance.request', 'search_read',
                                     [[['state', '=', 'Processed']]],
                                     {'fields': ['name', 'state', 'cpu']})
