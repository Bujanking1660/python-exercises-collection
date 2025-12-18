#Progaram Pohon Biner dari Data Masukkan
#I.S : pengguna memasukkan sejumlah nama 
#F.S : menampilkan isi pohon biner per level
import os

#Konstanta maksimal elemen queue
MAKSNAMA = 30

#1) Membuat class untuk simpul
class Simpul:
    def __init__(self,Info):
        self.LS = None
        self.Nama = Info
        self.RS = None

#2) Membuat class untuk pohon biner
class PohonBiner:
    #Inisialisasi
    def __init__(self):
        self.Head = None
        self.Front = -1
        self.Rear = -1
        self.Queue = [' '] * MAKSNAMA

        #Stack
        self.Top = -1
        self.Stack = [' '] * MAKSNAMA

    #Method membuat pohon biner
    def BuatPohon(self,NamaBaru):
        if(self.Head is None):
            self.Head = Simpul(NamaBaru)
        else:
            self.BuatNodeBaru(NamaBaru,self.Head)
    
    #Method membuat node baru selain root
    def BuatNodeBaru(self,NamaBaru,NodeParent):
        if(NamaBaru >= NodeParent.Nama):
            if(NodeParent.RS is None):
                NodeParent.RS = Simpul(NamaBaru)
            else:
                self.BuatNodeBaru(NamaBaru,NodeParent.RS)
        
        if(NamaBaru < NodeParent.Nama):
            if(NodeParent.LS is None):
                NodeParent.LS = Simpul(NamaBaru)
            else:
                self.BuatNodeBaru(NamaBaru,NodeParent.LS)

    #Method mengecek queue kosong atau tidak
    def Kosong(self):
        return self.Rear == -1

    #Method memasukkan satu data ke dalam queue(Enqueue)
    def Enqueue(self, NamaBaru):
        if(self.Kosong()):
            self.Front = 0
            self.Rear  = 0
        else:
            self.Rear += 1
        self.Queue[self.Rear] = NamaBaru
        
    #Method mengeluarkan satu data dari queue(Dequeue)
    def Dequeue(self):
        item = self.Queue[self.Front]
        if(self.Front == self.Rear):
            self.Queue[self.Rear] = ' '
            self.Front = -1
            self.Rear  = -1
        else:
            for i in range(self.Rear):
                self.Queue[i] = self.Queue[i+1]
            self.Queue[self.Rear] = ' '
            self.Rear -= 1

        return item

    #Method menampilkan isi pohon biner
    def TampilPohonBiner(self,Root):
        if(self.Head is None):
            print('Pohon Biner Kosong!')
        else:
            self.Enqueue(Root)
            print('| ',end='')
            while(not self.Kosong()):
                Node = self.Dequeue()
                print(Node.Nama,end=' | ')

                if(Node.LS):
                    self.Enqueue(Node.LS)
                if(Node.RS):
                    self.Enqueue(Node.RS)

    #Method menampilkan isi pohon biner per level
    def TampilPerLevel(self,Root):
        if(self.Head is None):
            print('Pohon Biner Kosong!')
        else:
            self.Enqueue(Root)
            Level = 1
            while(not self.Kosong()):
                PanjangQueue = self.Rear - self.Front+1
                print(f'Level {Level} : ',end='')
                for i in range(PanjangQueue):
                    Node = self.Dequeue()
                    print(Node.Nama,end='')
                    if(i != PanjangQueue-1):
                        print(', ',end='')

                    if(Node.LS):
                        self.Enqueue(Node.LS)
                    if(Node.RS):
                        self.Enqueue(Node.RS)

                Level += 1
                print()
        
    #Method Mengahapus Cabang Pohon (subTree)
    def HapusCabang(self,Node):
        if(Node is not None):
            return
        
        self.HapusCabang(Node.LS)
        self.HapusCabang(Node.RS)
        Node.LS = None
        Node.RS = None

        del Node

    #Method Menghapus seluruh node di pohon biner
    def Penghancuran(self,Node):
        if(Node is not None):
            self.HapusCabang(self.Head)
            del Node
            self.Head = None

    #Method Penelusuran Pohon Biner Secara Preorder (Rekursif)
    def Preorder(self,Node): # (NLR)
        if(Node):
            print(Node.Nama,end='|') #Node
            self.Preorder(Node.LS) #Left
            self.Preorder(Node.RS) #Right

    #Method Mengecek Stack Kosong Atau Tidak
    def StackKosong(self):
        return self.Top == -1 
    
    #Method Memasukkan Satu Data Ke Stack (Push)
    def Push(self, NamaBaru):
        self.Top += 1
        self.Stack[self.Top] = NamaBaru

    #Method Mengeluarkan Satu Data Dari Stack (Pop)
    def Pop(self):
        item = self.Stack[self.Top]
        self.Stack[self.Top] = ' '
        self.Top -= 1

        return item

    #Method Penelusuran Preorder Menggunakan Stack
    def PreorderStack(self,Node):
        while(not self.StackKosong()) or (Node is not None):
            print(Node.Nama,end='|') 
            if(Node.LS is not None) :
                if(Node.RS is not None):
                    self.Push(Node.RS)

                Node = Node.LS
            elif(Node.RS is not None):
                Node = Node.RS
            else:
                #Jika tidak punya anak
                if(not self.StackKosong()):
                    Node = self.Pop()
                else:
                    Node = None

    #Method Penelusuran Pohon Biner Secara Inorder
    def Inorder(self,Node): # (LNR)
        if(Node):
            self.Preorder(Node.LS) #Left
            print(Node.Nama,end='|') #Node
            self.Preorder(Node.RS) #Right

    #Method Penelusuran Inorder Menggunakan Stack
    def InorderStack(self,Node):
        while(not self.StackKosong()) or (Node is not None):
            if(Node.LS is not None):
                self.Push(Node)
                Node = Node.LS
            elif(Node.RS is not None):
                print(Node.Nama,end='|')
                Node = Node.RS
            else:
                #Tidak punya anak
                print(Node.Nama,end='|')
                if(not self.StackKosong()):
                    simpul = self.Pop()
                    print(simpul.Nama,end='|')
                    while(simpul.RS is not None) and (not self.StackKosong()):
                        simpul = self.Pop()
                        print(simpul.Nama,end='|')
                    if(simpul.RS is not None):
                        Node = simpul.RS
                    else:
                        Node = None
                else:
                    Node = None

    #Method Penelusuran Pohon Biner Secara Postorder
    def Postorder(self,Node): # (LRN)
        if(Node):
            self.Preorder(Node.LS) #Left
            self.Preorder(Node.RS) #Right
            print(Node.Nama,end='|') #Node

    #Method Penelusuran Postorder Menggunakan Stack
    def PostorderStack(self,Node):
        while(not self.StackKosong()) and (Node is not None):
            if(Node.LS is not None):
                if(Node.RS is not None):
                    self.Push(Node)
                    Node = Node.LS
                    self.Push(Node.RS)

                self.Push(Node) 
                Node = Node.LS 

            elif(Node.RS is not None):
                self.Push(Node) 
                Node = Node.RS 

            else:
                print('anu')



#Badan Program Utama
Pohon = PohonBiner()

Root = str(input('Nama Pertama (Root/Akar) : ')).upper()
Pohon.BuatPohon(Root)

NamaBaru = str(input('Nama Berikutnya : ')).upper()
while(NamaBaru != 'STOP'):
    Pohon.BuatPohon(NamaBaru)
    NamaBaru = str(input('Nama Berikutnya : ')).upper()

print()
os.system('cls')
print('<< Isi Pohon Biner >>')
Pohon.TampilPohonBiner(Pohon.Head)

print()
print()

print('<< Isi Pohon Biner >>')
Pohon.TampilPerLevel(Pohon.Head)

print()

print('<< Penelusuran Pohon Biner Secara Rekursif >>')

print('Preorder (Rekursif)  :',end='')
Pohon.Preorder(Pohon.Head)
print()

print('Preorder Stack  :',end='')
Pohon.PreorderStack(Pohon.Head)
print()

print('Inorder (Rekursif)   :',end='')
Pohon.Inorder(Pohon.Head)
print()

print('Inorder Stack   :',end='')
Pohon.InorderStack(Pohon.Head)
print()

print('Postorder (Rekursif) :',end='')
Pohon.Postorder(Pohon.Head)
print()

print('Postorder Stack :',end='')
Pohon.PostorderStack(Pohon.Head)
print()

print()
os.system('pause')
Pohon.Penghancuran(Pohon.Head)
Pohon.TampilPohonBiner(Pohon.Head)
print()
