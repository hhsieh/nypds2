import lxml.etree as ET
import sqlite3

def insert_program(db_conn, id, programID, orchestra, season, concertInfo):
    curs = db_conn.cursor()
    curs.execute("insert into program values (?,?,?,?,?,?)", (id, programID, orchestra, season, concertInfo, worksInfo))
    db_conn.commit()

def program_data_from_element(element):
    id = element.find("id")
    programID = element.find("programID")
    orchestra = element.find("orchestra")
    season = element.find("season")
    concertInfo = element.find("concertInfo")
    worksInfo = element.find("worksInfo")

    return id, programID, orchestra, season, concertInfo, worksInfo

def insert_work(db_conn, programID, season, workID, composerName, workTitle, movement, conductorName):
    curs = db_conn.cursor()
    curs.execute("insert into work values (?,?,?,?,?,?,?)", (programID, season, workID, composerName, workTitle, movement, conductorName))
    db_conn.commit()

def work_data_from_element(element):
    programID = element.find("programID").text
    season = element.find("season").text
    workID = element.find("workID").text
    composerName = element.find("composerName").text
    workTitle = element.find("workTitle").text
    movement = element.find("movement").text
    conductorName = element.find("conductorName").text

    return programID, season, workID, composerName, workTitle, movement, conductorName

def insert_soloist(db_conn, programID, season, composerName, workTitle, movement, conductorName, soloistName, soloistInstrument, soloistRole):
    curs = db_conn.cursor()
    curs.execute("insert into soloist values (?,?,?,?,?,?,?,?,?)", (programID, season, composerName, workTitle, movement, conductorName, soloistName, soloistInstrument, soloistRole))
    db_conn.commit()

def soloist_data_from_element(element):
    soloistName = element.find("soloistName").text
    soloistInstrument = element.find("soloistInstrument").text
    soloistRole = element.find("soloistRole").text
    composerName = element.find("composerName").text
    workTitle = element.find("workTitle").text
    movement = element.find("movement").text
    conductorName = element.find("conductorName").text
    programID = element.find("programID").text
    season = element.find("season").text

    return programID, season, composerName, workTitle, movement, conductorName, soloistName, soloistInstrument, soloistRole


def insert_s2(db_conn, programID, season, composerName, workTitle, movement, conductorName, soloistName, soloistInstrument, soloistRole):
    curs = db_conn.cursor()
    curs.execute("insert into s2 values (?,?,?,?,?,?,?,?,?)", (programID, season, composerName, workTitle, movement, conductorName, soloistName, soloistInstrument, soloistRole))
    db_conn.commit()

def s2_data_from_element(element):
    soloistName = element.find("soloistName").text
    soloistInstrument = element.find("soloistInstrument").text
    soloistRole = element.find("soloistRole").text
    programID = element.find("programID").text
    season = element.find("season").text
    composerName = element.find("composerName").text
    workTitle = element.find("workTitle").text
    movement = element.find("movement").text
    conductorName = element.find("conductorName").text

    return programID, season, composerName, workTitle, movement, conductorName, soloistName, soloistInstrument, soloistRole


if __name__ == "__main__":    
    conn1 = sqlite3.connect("/Users/achimnyswallow/Documents/Data_Incubator/Capstone project/test/test2/program.sqlite3")
    conn2 = sqlite3.connect("/Users/achimnyswallow/Documents/Data_Incubator/Capstone project/test/test2/work.sqlite3")
    conn3 = sqlite3.connect("/Users/achimnyswallow/Documents/Data_Incubator/Capstone project/test/test2/soloist.sqlite3")
    conn4 = sqlite3.connect("/Users/achimnyswallow/Documents/Data_Incubator/Capstone project/test/test2/s2.sqlite3")
    xml = ET.parse("/Users/achimnyswallow/Documents/Data_Incubator/Capstone project/complete.xml")

    # PROGRAM PARSE - transform xml to xsl
    xslt = ET.parse("program.xsl")
    transform = ET.XSLT(xslt)
    newdom = transform(xml)
    program = newdom.xpath("//program")

    for index, element in enumerate(program):
        id, programID, orchestra, season, concertInfo, worksInfo = program_data_from_element(element)
        insert_program(conn1, id, programID, orchestra, season, concertInfo)

    # WORK PARSE
    xslt = ET.parse("work.xsl")
    transform = ET.XSLT(xslt)
    newdom = transform(xml)
    work = newdom.xpath("//work")    

    # SOLOIST PARSE
    xslt = ET.parse("soloist.xsl")
    transform = ET.XSLT(xslt)
    newdom = transform(xml)
    soloist = newdom.xpath("//work")

    # S2 PARSE
    xslt = ET.parse("s2.xsl")
    transform = ET.XSLT(xslt)
    newdom = transform(xml)
    s2 = newdom.xpath("//soloist")

    for index, element in enumerate(work):
        programID, season, workID, composerName, workTitle, movement, conductorName = work_data_from_element(element)
        insert_work(conn2, programID, season, workID, composerName, workTitle, movement, conductorName)

    for index, element in enumerate(soloist):
        programID, season, composerName, workTitle, movement, conductorName, soloistName, soloistInstrument, soloistRole  = soloist_data_from_element(element)
        insert_soloist(conn3, programID, season, composerName, workTitle, movement, conductorName, soloistName, soloistInstrument, soloistRole)

    for index, element in enumerate(s2):
        programID, season, composerName, workTitle, movement, conductorName, soloistName, soloistInstrument, soloistRole  = s2_data_from_element(element)
        insert_s2(conn4, programID, season, composerName, workTitle, movement, conductorName, soloistName, soloistInstrument, soloistRole)
   
