import csv

def add_task():
    task_name = input("Yangi vazifa nomini kiriting: ")
    
    qatorlar = []
    max_id = 0

    with open("tasks.csv", "r", encoding="utf-8") as f:
        data = csv.DictReader(f)
        
        for qator in data:
            qatorlar.append(qator)
            id_raqam = int(qator['id'])
            if id_raqam > max_id:
                max_id = id_raqam

    new_id = max_id + 1
    
    yangi_vazifa = {
        'id': str(new_id),
        'name': task_name,
        'status': 'bajarilmagan'
    }
    
    qatorlar.append(yangi_vazifa)

    with open("tasks.csv", "w", encoding="utf-8", newline="") as f:
        writer = csv.DictWriter(f, fieldnames=["id", "name", "status"])
        writer.writeheader()
        writer.writerows(qatorlar)

    print("Yangi vazifa muvaffaqiyatli qo'shildi!")

add_task()