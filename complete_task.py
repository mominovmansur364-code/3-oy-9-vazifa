import csv

def complete_tasks(id):
    qatorlar=[]
    found=False

    with open("tasks.csv","r",encoding="UTF-8") as f:
        data=csv.DictReader(f)

        for qator in data:
            if qator['id']==str(id):
                qator['status']="bajarilgan"
                found=True
            qatorlar.append(qator)
    if found==True:
        with open("tasks.csv","w",newline="") as f:
            writer = csv.DictWriter(f, fieldnames=["id", "name", "status"])
            writer.writeheader()
            writer.writerows(qatorlar)
        print("Vazifa bajarildi deb ozgartirildi")
    else:
        print("Bunday ID li oquvchi topilmadi")

almashtirish=int(input("Id kiriting: "))
complete_tasks(almashtirish)
