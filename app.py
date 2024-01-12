import csv_update as csv
from ttkbootstrap import *
from ttkbootstrap.toast import ToastNotification

class App:
    def __init__(self,root):
        self.root = root

        Button(self.root,text="Update Data",command=lambda:self.update_data()).grid(row=0,column=0,padx=10,pady=10)
        self.date = DateEntry(self.root,bootstyle="info")
        self.date.grid(row=0,column=1,padx=10,pady=10)
        Button(self.root,command=self.search,text="Search").grid(row=0,column=2,padx=10,pady=10)

        self.results = Label(root,text='''1. open : ???\n\n2. high : ???\n\n3. low : ???\n\n4. close : ???\n\n5. volume : ???''')
        self.results.grid(row=1,column=1,padx=10,pady=30)

    def search(self):
        try:
            #changing the date mode from 1/12/2024 to 2024-1-12 . like a csv file
            date_get = self.date.entry.get()
            date_list = date_get.split("/")
            date_list.reverse()
            year, day , month =  date_list
            if int(month)<10:
                month = f"0{month}"
            if int(day)<10:
                day = f"0{day}"
            
            data = csv.csv_read()
            date = f"{year}-{month}-{day}"

            result=data[date]

            self.results.configure(text=f'''1. open : {result['1. open']} \n\n2. high : {result['2. high']}\n\n3. low : {result['3. low']}\n\n4. close : {result['4. close']}\n\n5. volume : {result['5. volume']}''')
        except:
            toast = ToastNotification(title="Error !",message="This date is not available \nUpdate data \nIf you encounter an error again, then this date is not available in the API!",duration=3000)
            toast.show_toast()

    def update_data(self):
        csv.updata_csv()
        toast = ToastNotification(title="Updated!",message="The information was updated \n(Daily)",duration=3000)
        toast.show_toast()
        
if "__main__" == __name__:
    app = Window(themename="darkly",title= "IBM")
    App(app)
    app.mainloop()
