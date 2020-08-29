import xlrd
from forms import AddForm
from adoption_site import db,Template
# Give the location of the file
loc = ("Meme_templates.xlsx")

# To open Workbook
wb = xlrd.open_workbook(loc)
sheet = wb.sheet_by_index(0)

row = 0
column = 0

list1 = ['Abhinav Gomatam', 'Akhil', 'Yash', 'Viva Harsha', 'Vishwak Sen', 'Vijay Devarakonda', 'Venu Madhav', 'Venkatesh', 'Tanikella Bharani', 'Siddharth', 'Sharwanand', 'Sayaji Shinde', 'Rana', 'Rajnikanth', 'Rahul Ramakrishna', 'Ram Charan', 'SJ Surya', 'Priyadarshee', 'Pradeep Rawat',
         'Prabhas', 'Posani', 'Pawan Kalyan', 'Nikhil Siddharth', 'Nagineedu', 'Nagarjuna', 'Motta Rajendran', 'Mahesh Babu', 'Jr artist Sanjay', 'Jr NTR', 'Ileana DCruz', 'Anushka Shetty', 'Dharmavarapu Subramanyam', 'Bramhanandam', 'Balakrishna', 'Raadhu Boy', 'Jaleel Khan', 'Chiyaan Vikram']

list2 = ['Abhinav Gomata', 'Akhil Akkineni', 'yash', 'Harsha Chemudu', 'Viswaksen Naidu', 'Vijay Devarakona', 'Venu Madhav and 2 others', 'Venkatesh Daggubati', 'Tanikela Bharani', 'Siddhart', 'Sharwanandh', 'Shiyaji Shinde', 'Rana Daggubati', 'Ram Charan Tej', 'Rajinikanth', 'Rahul Ramakrishnan', 'PriyaDarshe', 'SJ Suriya',
         'Pradeep Rawaat', 'Prabhas Raju', 'Posani Krishna Murali', 'Pawna Kalyan', 'RAADHU', 'Nikhil Siddhart', 'Naginedu', 'Mottai Rajendran', 'Akkineni Nagarjuna', 'Mahesh babu', 'Jr. artist Sanjay', 'JR NTR', 'Ileana DCruze', 'Jaleel khan', 'Dharamavarapu Subramanyam', 'Vikram', 'Brahmanandam', 'Bala Krishna', 'Anushka']

list1.sort()
list2.sort()

list2.insert(13, list2.pop(2))
list2.insert(5, list2.pop(34))
list2.insert(35, list2.pop(7))
list2.insert(8, list2.pop(9))


list3 = ['Najarjuna', 'Anuskha Shetty', 'balakrishna', 'Brahmanandham', 'Dharmavarupu Subramanyam', 'MaheshBabu', 'Rahul Ramakrsihna', 'RajiniKanth', 'Rana Daggupati', 'Siyyaji Shinde']

list4 = ['Nagarjuna', 'Anushka Shetty', 'Balakrishna', 'Bramhanandam', 'Dharmavarapu Subramanyam', 'Mahesh Babu', 'Rahul Ramakrishna', 'Rajnikanth', 'Rana', 'Sayaji Shinde']

for row in range(sheet.nrows):
    # template = {}
    name = sheet.cell_value(row, column)
    column += 1
    movie = sheet.cell_value(row, column)
    column += 1
    actor1 = sheet.cell_value(row, column)
    column += 1
    actor2 = sheet.cell_value(row, column)
    column += 1
    actor3 = sheet.cell_value(row, column)
    column += 1
    actor4 = sheet.cell_value(row, column)
    column += 1
    url = sheet.cell_value(row, column)
    column = 0
    row += 1

    if actor1 == 'JR. NTR' or actor1 == 'Jr. NTR' or actor1 == 'Jr.NTR':
        actor1 = 'Jr NTR'

    if actor1 in list2:
        actor1 = list1[list2.index(actor1)]

    if actor1 in list3:
        actor1 = list4[list3.index(actor1)]



    new_temp = Template(name, actor1, movie, url)
    db.session.add(new_temp)
    db.session.commit()



"""Use this only to delete all from the db, only use in the worst case"""
# Template.query.delete()
# db.session.commit()
 
