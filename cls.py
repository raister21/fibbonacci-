Days = ["sunday","monday","tuesday","wednesday","thursday","friday"]
Subjects = ["Info Systems", "Hardware&System", "Logic&Problem","Programming"]
Tipe = ["Lecture","Tutorial","Lab"]
Locations = ["Kenshington","Buckhingham","Piccadilly circus","Patan","Lumbini","Cambridge","Bristol"]

class subjects():
    def __init__(self, subject, tipe, time, location, subject2, tipe2, time2, location2, subject3, tipe3, time3, location3):
        self.subject = subject
        self.tipe = tipe 
        self.time = time
        self.location = location
        self.subject2 = subject2
        self.tipe2 = tipe2
        self.time2 = time2
        self.location2 = location2
        self.subject3 = subject3
        self.tipe3 = tipe3
        self.time3 = time3
        self.location3 = location3

def main():
    tdy = input("what day is it?")
    if tdy == Days[0]:
        print(sunday.subject)
        print(sunday.tipe)
        print(sunday.time)
        print(sunday.location)
        print("")
        print(sunday.subject2)
        print(sunday.tipe2)
        print(sunday.time2)
        print(sunday.location2)

    if tdy == Days[1]:
        print(monday.subject)
        print(monday.tipe)
        print(monday.time)
        print(monday.location)
        print("")
        print(monday.subject2)
        print(monday.tipe2)
        print(monday.time2)
        print(monday.location2)
        print("")
        print(monday.subject3)
        print(monday.tipe3)
        print(monday.time3)
        print(monday.location3)

    if tdy == Days[2]:
        print(tuesday.subject)
        print(tuesday.tipe)
        print(tuesday.time)
        print(tuesday.location)

    if tdy == Days[3]:
        print(wednesday.subject)
        print(wednesday.tipe)
        print(wednesday.time)
        print(wednesday.location)
        print("")
        print(wednesday.subject2)
        print(wednesday.tipe2)
        print(wednesday.time2)
        print(wednesday.location2)

    if tdy == Days[4]:
        print(thursday.subject)
        print(thursday.tipe)
        print(thursday.time)
        print(thursday.location)
        print("")
        print(thursday.subject2)
        print(thursday.tipe2)
        print(thursday.time2)
        print(thursday.location2)

    if tdy == Days[5]:
        print(friday.subject)
        print(friday.tipe)
        print(friday.time)
        print(friday.location)
        print("")
        print(friday.subject2)
        print(friday.tipe2)
        print(friday.time2)
        print(friday.location2)





            


sunday = subjects(Subjects[3],Tipe[0],"11:30am to 1:00pm:",Locations[0],Subjects[1],Tipe[0],"1:00pm to 2:30pm",Locations[1],"empty","empty","empty","empty")
monday = subjects(Subjects[0],Tipe[0],"9:00am to 10:30am:",Locations[0],Subjects[2],Tipe[0],"12:00pm to 1:30pm",Locations[0],Subjects[1],Tipe[1],"1:30pm to 2:30pm",Locations[2])
tuesday = subjects(Subjects[3],Tipe[1],"10:00am to 11:30am:",Locations[3],"empty","empty","empty","empty","empty","empty","empty","empty")
wednesday = subjects(Subjects[0],Tipe[1],"7:30am to 8:30am:",Locations[2],Subjects[2],Tipe[1],"10:00am to 11:30am",Locations[4],"empty","empty","empty","empty")
thursday = subjects(Subjects[3],Tipe[2],"8:30am to 10:00am:",Locations[5],Subjects[1],Tipe[2],"10:00am to 11:30am",Locations[6],"empty","empty","empty","empty")
friday = subjects(Subjects[0],Tipe[2],"7:00am to 8:30am:",Locations[5],Subjects[2],Tipe[1],"8:30am to 9:30am",Locations[3],"empty","empty","empty","empty")

main()


            

    

