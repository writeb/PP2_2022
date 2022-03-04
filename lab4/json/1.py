import json
print("Interface Status")
print("================================================================================")
print("DN                                                 Description           Speed    MTU  ")
print("-------------------------------------------------- --------------------  ------  ------")

data = open('sample-data.json', 'r')
data = data.read()
data = json.loads(data)

c = len(data['imdata'][0]['l1PhysIf']['attributes']['dn'])
for i in data['imdata']:
    res = len(i['l1PhysIf']['attributes']['dn'])
    i['l1PhysIf']['attributes']['dn'] += ' ' * (c - res)

for i in data['imdata']:
    print("{}                              {}   {}".format(i['l1PhysIf']['attributes']['dn'], i['l1PhysIf']['attributes']['speed'], i['l1PhysIf']['attributes']['mtu']))