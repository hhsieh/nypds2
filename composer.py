import sqlite3
import pandas as pd

def insert_composer(db_conn, composer, era):
    curs = db_conn.cursor()
    curs.execute("insert into composer values (?,?)", (composer, era))
    db_conn.commit()

if __name__ == "__main__":
    conn = sqlite3.connect("/Users/achimnyswallow/Documents/Data_Incubator/Capstone project/test/test2/composer.sqlite3")

composers = pd.read_csv("complete_composers_list.txt", sep = ",")


for i in range(len(composers)):
    insert_composer(conn, composers.ix[i][0].decode('utf-8'), composers.ix[i][1].decode('utf-8'))




#import lxml.etree as ET
#xml = ET.parse("/Users/achimnyswallow/Documents/Data_Incubator/Capstone project/complete.xml")
#xslt = ET.parse("s2.xsl")
#transform = ET.XSLT(xslt)
#newdom = transform(xml)
#s2 = newdom.xpath("//soloist")

#for item in s2:
#    print item[0].text, item[1].text, item[2].text, item[3].text
 



