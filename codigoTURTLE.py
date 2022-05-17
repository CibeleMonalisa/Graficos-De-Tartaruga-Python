#arquivo teste do gráfico de tartaruga com importação de arquivo externo
def file_read(fname):
    lista = []
    with open(fname) as f:
        for line in f:
            lista.append(line)
        #print(lista)
file_read('tartaruga.txt')


def remove_newlines(fname):
    with open(fname) as f:
        return f.read().replace("\n"," ")
l1=[]
l1.append(remove_newlines("tartaruga.txt"))
#print(l1)

l2=[]
l2=[(int(k)) if k.isdigit() else k for k in l1[0].strip().split(" ")]
#print(l2)

l3=[]
for n in range(len(l2)):
    if l2[n] == "CIMA" or l2[n]=="BAIXO":
      l3.append(l2[n])
    else:  
        l3.append(int(l2[n])) 
#print(l3)


#------------------------DESENHO---------------------------------
import turtle
touche = turtle.Turtle() # cria o objeto turtle touche
touche.shape("turtle") # forma do objeto
touche.color("green") # cor do objeto
touche.fillcolor("violet")
for b in range(len(l3)):
    if b < len(l3):
        if l3[b]=="CIMA":
            b+=1
            touche.penup()
            x=l3[b]
            y=l3[b+1]
            touche.setposition(x, y)
            b+=2
        elif l3[b]=="BAIXO" and b < len(l3):
            b+=1
            while l3[b] != "CIMA":
                if b < len(l3):
                    touche.pendown()
                    x=l3[b]
                    y=l3[b+1]
                    touche.setposition(x, y)
                    b+=2
                    if b >= len(l3):
                        break 
turtle.Screen().exitonclick()
            

          