ingratos = []

with open("seguidores.txt", "r") as tf:
    seguidoresList = tf.read().split('\n')

with open("seguindo.txt", "r") as tf:
    seguindoList = tf.read().split('\n')



for seguindo in seguindoList:
    segue = False

    for seguidor in seguidoresList:
        if(seguindo==seguidor):
            segue = True
            break
    if (segue==False):
        ingratos.append(seguindo)

# for seguidor in seguidoresList:
#     if(seguindoList[7]==seguidor):
#         segue = True
#         break
# if (segue==False):
#     ingratos.append(seguindoList[7])

print(seguindoList)
print("")
print(ingratos)
print(segue)