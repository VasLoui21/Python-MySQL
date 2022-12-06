#THEMA 1o
#eisagw ton server MariaDB
import mariadb
#dhmiourgw ti sundesh me th vash dedomenwn
connection = mariadb.connect(host = "localhost", user= "root", password = "", database = "test")

#dhmiourgia tou cursor gia na mporw na ktelesw queries (erwtimata)
mycursor = connection.cursor()

#dhmiourgia toy zhtoumenou pinaka me id, biologiki akolouthia, eidos allhlouxias kai etos
mycursor.execute("CREATE TABLE NucleoTBL (id INT, sequence VARCHAR(50), seq_type VARCHAR(3), year INT)")

#OPTIONAL: eisagwgh 2 eggrafwn ston pinaka
mycursor.execute("INSERT INTO NucleoTBL (id, sequence, seq_type, year) VALUES (%s,%s,%s,%s)", (1,"ATTTGCA", "DNA", 1963))
mycursor.execute("INSERT INTO NucleoTBL (id, sequence, seq_type, year) VALUES (%s,%s,%s,%s)", (2,"AUUUGCA", "RNA", 2000))
connection.commit()

#THEMA 2o: dhmiourgia tis zhtoumenhs klasis
class NucleoCLS:
    #dhmiourgia tou kataskeuasth me orismata ta pedia tou prwtou thematos
    def __init__(self, id, sequence, seq_type, year):
        self.id = id
        self.sequence = sequence
        self.seq_type = seq_type.upper() #to seq.type na metatrepetai panta se kefalaia grammata
        self.year = year
#dhmiourgia sunartisis pou deixnei olh tin plhroforia mias eggrafis
    def show_info(self):
        print(str(self.id), self.sequence, self.seq_type, str(self.year))
#dhmiourgia sunartisis pou an to seq_type tis allhlouxias einai DNA h RNA epistrefei TRUE kai emfanizei antistoixo mnm
#enw an den einai DNA h RNA epistrefei False kai ektypwnei to antistoixo mhnyma
    def validate_seq(self):
        if self.seq_type == "DNA" or self.seq_type == "RNA":
            print("It's biological sequence!" + ":" + self.seq_type)
            return True

        else:
            print("Not a biological sequence!")
            return False

#dhmiourgia enos antikeienou kai elegxos tou mesw tis sunartisis "validate_seq"
SEQ=NucleoCLS(1,"ATTTGCA", "DNA", 1963)
SEQ.validate_seq()


#ΤΗΕΜΑ 3: enfanish twn 4 epilogwn ston xrhsth mazi me tis plhrofories tis kathe epilogis
try:
 x=int(input("To insert a record, please press:1 \nTo delete a record please press:2 \nTo print arecord please press:3 \nTo see the table and exit please press:4 \n"))

#an o xrhsths epileksei tin prwti epilogi tote prepei na eisagei mia eggrafi
 if x==1:
        id=int(input("Please provide the id of the sequence\n")) #prepei na dwsei to id tis eggrafis
        sequence=str(input("Please provide the sequence\n")) #prepei na dwsei tin allhlouxia
        seq_type=str(input("Please provide the sequence type\n")) #prepei na dwsei ton tupo allhlouxias
        year=int(input("Please provide the year of registration\n")) #prepei na dwsei to etos kataxwrisis
        #afou mas dwsei ola ta stoixeia tote ta pername mesa apo tin klasi NucleoCLS kai ti sunartisi validate_seq
        #kai an to programma epistrepsei true tote ginetai eisagwgi tis eggafis ston pinaka alliws vgazei mhnuma lathous
        My_seq = NucleoCLS(id,  sequence, seq_type, year)
        if My_seq.validate_seq() == True:
           mycursor.execute("INSERT INTO NucleoTBL (id, sequence, seq_type, year) VALUES (%s,%s,%s,%s)", (id,sequence , seq_type,  year))
           connection.commit() #apothikeusi tis allagis
           print("The SeQUENCE HAS BEEN ADDED TO THE DATABASE")
        else:
            print("This is not a valid sequence, cannot proceed")

#an o xrhsths epileksei tin deuteri epilogi tote prepei na dwsei to id tis eggrafis pou thelei na diagrapsei
 if x==2:
        id=int(input("Please provide the id of the sequence you want to delete\n"))
        while id == True: #oso to id uparxei ston pinaka
         mycursor.execute("DELETE from NucleoTBL where id='%s'"%id) #diegrapse tin eggrafi
         connection.commit() #kai apothikeuse tin allahagi
         print("The record has been deleted") #kai enhmerwse ton xrhsth me katallhlo mhnuma
         break
        else: #alliws enhmerwse ton xrhsth oti den uparxei h eggrafi pou epelekse
            print("There is no record with this id")

#an o xrhsths epileksei tin trith epilogi tote prepei na dwsei to id tis eggrafis pou thelei na dei
 try:
    if x==3:
        id=int(input("Please provide the id of the sequence you want to see\n"))
        mycursor.execute("SELECT id, sequence, seq_type, year from NucleoTBL where id='%s'" % id) #epelekse tin aggrafi
        id, sequence, seq_type, year=mycursor.fetchone()  #apothikeuse tin
        # kai mesw tis sunartisis show_info deikse mou oles tis plhrofories auths ths eggrafis
        My_seq = NucleoCLS(id, sequence, seq_type, year)
        My_seq.show_info()
 except:
     #an den uparxei tetoio id epestrepse mhnuma lathous
     print("There is no record with this id")

#telos an o xrhsths epileksei tin tetarth epilogi
 if x==4:
          mycursor.execute("SELECT * FROM nucleotbl") #epelekse oles tis eggrafes tou pinaka
          records=mycursor.fetchall() #apothikeuse tes
          for row in records:
              print(row,"\n") #kai epestrepse tes ston xrhsth

#se periptwsh pou kati den paei kala me to prwto "try" epestrepse mhnuma lathous
except:
  print("Something went wrong")

#telos kleise tin sundesh me ton server kai ektupwse to katallhlo munhma
finally:
      mycursor.close()
      print("MySql cursor closed")
