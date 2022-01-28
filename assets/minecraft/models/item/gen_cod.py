f=open("cod.json","w")
write='''{
    "parent": "item/generated",
    "textures": {
        "layer0": "item/cod"
    },
    "display": {
        "head": {
            "rotation": [ 0, 90, -60 ],
            "translation": [ -7, -4, -7],
            "scale":[ 0.8, 0.8, 0.8]
        }
    },
    "overrides": [\n'''
f.write(write)
for i in range(1,81):
    f.write('        {"predicate": {"custom_model_data": %d}, "model": "sct:skadi2/%d"},\n'%(130000+i,i))
f.write('    ]\n}')