device_names = {1: 'cpu0', 2: 'mem_bank0', 3: 'mem_bank1'}
device_models = {1: 'Xeon', 2: 'Corsair', 3: 'Corsair'}

devices = []

for dev_id, name in device_names.items():
    devices.append({'id': dev_id, 'name': name, 'model': device_models[dev_id]})

print(devices)

#druga część zadania


model_map = {}

for id, model in device_models.items():
    name = device_names[id]
    if model in model_map:
        model_map[model].append(name)
    else:
        model_map[model] = [name]

print(model_map)


[{'id': 1, 'name': 'cpu0', 'model': 'Xeon'},
 {'id': 2, 'name': 'mem_bank0', 'model': 'Corsair'}]

{'Xeon': ['cpu0'], 'Corsair': ['mem_bank0', 'mem_bank1']}
