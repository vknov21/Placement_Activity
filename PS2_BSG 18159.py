vertex=["/"]
edge=[]
f=open("outputPS2.txt","a+")
p=open("promptsPS2.txt","a+")

def readActMovFile(fileName):
    global vertex
    global edge
    e1=[]
    movie=[]
    actor=[]
    fp=open(fileName,"r")

    if(fp==''):
        print("File Not Found")
        exit()
    line="h"
    while(not line==''):
        line=fp.readline()
        word=[]
        word=line.split('/')
        if(len(word)>3):
            print("Only Maximum of two actors allowed")
            exit()
        k=len(word)
        movie=movie+[(word[0].strip()).upper()]
        i=1
        while(i<k):
            word[i]=word[i].upper()
            word[i]=word[i].strip()
            if word[i] in actor:
                e1=e1+[actor.index(word[i])]
            else:
                e1=e1+[len(actor)]
                actor=actor+[word[i]]
            i=i+1
        edge.append(e1)
        e1=[]
    del edge[-1]
    del movie[-1]
    for i in range(0,len(edge)):
        for j in range(0,len(edge[i])):
            edge[i][j]=edge[i][j]+len(movie)+1
    vertex=movie+['/']+actor

def displayActMov():
    global vertex
    f.write("\n\n                  /-------------------------------\\")
    f.write("\n-----------------(    Display Actors and Movies    )-----------------\n")
    f.write("                  \\-------------------------------/")
    f.write("\n\nTotal no. of Movie = %d" %(vertex.index('/')))
    f.write("\n\nTotal no. of Actors = %d\n" %(len(vertex)-vertex.index('/')-1))
    f.write("\n.----------------.\n|     Movies     |\n'----------------'")
    for i in range(0,vertex.index('/')):
        f.write("\n  %s" %vertex[i])
    f.write("\n\n.----------------.\n|     Actors     |\n'----------------'")
    for i in range(vertex.index('/')+1,len(vertex)):
        f.write("\n  %s" %vertex[i])

def displayMoviesOfActor(actor):
    global vertex
    global edge
    p.write("\n searchActor : %s" %actor)
    f.write("\n\n                  /-----------------------------\\")
    f.write("\n-----------------(    Display Movies of Actor    )----------------\n")
    f.write("                  \\-----------------------------/")
    f.write("\n\n  Actor Name : %s" %actor)
    f.write("\n.----------------.\n| List of Movies |\n'----------------'")
    for i in range(0,len(edge)):
        if vertex.index(actor) in edge[i]:
            f.write("\n  %s" %vertex[i])

def displayActorsOfMovie(movie):
    global vertex
    global edge
    p.write("\n searchMovie : %s" %movie)
    f.write("\n\n                  /-----------------------------\\")
    f.write("\n-----------------(    Display Actors in Movie    )----------------\n")
    f.write("                  \\-----------------------------/")
    f.write("\n\n  Movie Name : %s" %movie)
    f.write("\n.----------------.\n| List of Actors |\n'----------------'")
    for i in range(0,len(edge[vertex.index(movie)])):
        f.write("\n  %s" %vertex[edge[vertex.index(movie)][i]])

def findMovieRelation(movA,movB):
    global vertex
    global edge
    p.write("\n RMovies : %s : %s" %(movA,movB))
    f.write("\n\n                  /-------------------------------\\")
    f.write("\n-----------------(    Relation between 2 Movies    )----------------\n")
    f.write("                  \\-------------------------------/")
    f.write("\n\n  Movie A : %s\n  Movie B : %s" %(movA,movB))
    for i in range (0,len(edge[vertex.index(movA)])):
        if edge[vertex.index(movA)][i] in edge[vertex.index(movB)]:
            f.write("\n  Yes, %s" %vertex[edge[vertex.index(movA)][i]])
            return
    f.write("\n  No relation between %s and %s" %(movA,movB))


def findMovieTransRelation(movA,movB):
    global vertex
    global edge
    b={}
    t=[]
    p.write("\n TMovies : %s : %s" %(movA,movB))
    a=edge[vertex.index(movA)]+edge[vertex.index(movB)]
    c=[edge[vertex.index(movA)]]+[edge[vertex.index(movB)]]
    for i in range(0,len(a)):
    	b[a[i]]=i
    a=b.keys()
    for i in range(0,len(a)):
        if(len(a)>1):
            for j in range(i+1,len(a)):
                t=t+[[a[i],a[j]]]
        else:
            t=[a[i]]
    a=t
    f.write("\n\n                  /------------------------------------------\\")
    f.write("\n-----------------(    Transitive Relation between 2 Movies    )----------------\n")
    f.write("                  \\------------------------------------------/")
    f.write("\n\n  Movie A : %s\n  Movie B : %s" %(movA,movB))
    for i in range(0,len(c)):
        if c[i] in a:
            a.remove(c[i])
    for i in range(0,len(a)):
        if a[i] in edge:
            f.write("\n  Yes,  %s > %s > %s > %s > %s" %( movA, vertex[a[i][0]], vertex[edge.index(a[i])], vertex[a[i][1]], movB ))
            return
    f.write("\n  No Transitive relation between %s and %s" %(movA,movB))

if __name__=="__main__":
    filename="inputPS2.txt"
    readActMovFile(filename)
    print("\n Choose an integral option from below : \n\t1. Display total list of Movies and Actors\n\t2. Display Movie(s) of an Actor\n\t3. Display Actor(s) in a Movie\n\t4. Display Relation between Movies\n\t5. Display Transitive Relation of Movie\n\t6. Exit\n")
    option=input(" Option (1-6) : ")
    f.write("\n")

    if(option==1):
        displayActMov()

    elif(option==2):
        while(1):
            actor=raw_input("  Enter name of Actor : ")
            actor=actor.strip()
            actor=actor.upper()
            if not actor in vertex:
                print("Actor not present")
                continue
            displayMoviesOfActor(actor)
            break

    elif(option==3):
        while(1):
            movie=raw_input("  Enter name of Movie : ")
            movie=movie.strip()
            movie=movie.upper()
            if not movie in vertex:
                print("Movie not present")
                continue
            displayActorsOfMovie(movie)
            break

    elif(option==4):
        while(1):
            movA=raw_input("  Enter name of Movie A : ")
            movA=movA.strip()
            movA=movA.upper()
            if not movA in vertex:
                print("Movie Not Present\n")
                continue
            movB=raw_input("  Enter name of Movie B : ")
            movB=movB.strip()
            movB=movB.upper()
            if not movB in vertex:
                print("Movie Not Present\n")
                continue
            findMovieRelation(movA,movB)
            break

    elif(option==5):
        while(1):
            movA=raw_input("  Enter Movie A : ")
            movA=movA.strip()
            movA=movA.upper()
            if not movA in vertex:
                print("  Movie Not present\n")
                continue
            movB=raw_input("  Enter Movie B : ")
            movB=movB.strip()
            movB=movB.upper()
            if not movB in vertex:
                print("  Movie Not present\n")
                continue
            findMovieTransRelation(movA,movB)
            break
    else:
        exit()
