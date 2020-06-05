import time
import uuid
from datetime import datetime
from reports.bill import GenerateBill

current_date = datetime.today().strftime('%Y-%m-%d')
current_time = time.strftime("%H:%M:%S", time.localtime())
bill_number = str(uuid.uuid1())

a = GenerateBill()
bill_list = [a.add_item_to_bill("Bizuteria i zegarki", "Dla kobiet", 1, 3),
                a.add_item_to_bill("Bizuteria i zegarki", "Dla mezczyzn", 0, 1),
                a.add_item_to_bill("Delikatesy", "Napoje wody soki", 0, 13),
                a.add_item_to_bill("Delikatesy", "Alkohol", 1, 5),
                a.add_item_to_bill("Sprzet RTV", "Telewizory 4k UHD", 1, 1)]

overall_net = []
overall_gross = []
for item in bill_list:
    overall_net.append(item[1]*item[2])
for item in bill_list:
    overall_gross.append((item[1]*item[3]+item[1])*item[2])

print(overall_net)

with open('example_bill.txt') as f:
    with open("output_bill.txt", "w", encoding='utf-8') as f1:
        for line in f:
            f1.write(line)
        f1.write(f'\n\t\t{current_date} {current_time}    {bill_number}')
        f1.write(f'\n\t\t-----------------------------------------------------------\n')
        for item in bill_list:
            f1.write(f"\t\t{item[0]}\n")
        f1.write(f'\t\t-----------------------------------------------------------\n')
        f1.write(f'\t\tSUMA netto:                        {sum(overall_net)}')
        f1.write(f'\n\t\tSUMA brutto:                       {sum(overall_gross)}')
        f1.write(f'\n\t\t-----------------------------------------------------------\n')



