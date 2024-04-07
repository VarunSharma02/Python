toll_records = []
while True:
 print("\n1. Record Toll Transaction\n2. Display Toll Records\n3. Calculate Total Revenue\n4. Search Toll Record by Vehicle Number\n5. Remove Toll Record by Vehicle Number\n6. Exit")
 choice = int(input("Enter your choice: "))
 if choice == 1:
  toll_record = {}
  toll_record['Vehicle Number'] = input("Enter Vehicle Number: ")
  toll_record['Date'] = input("Enter Date (MM/DD/YYYY): ")
  toll_record['Amount'] = float(input("Enter Toll Amount: "))
  toll_records.append(toll_record)
  print("Toll transaction recorded successfully.")
 elif choice == 2:
  print("\nToll Records:")
  for record in toll_records:
   print(f"Vehicle Number: {record['Vehicle Number']}")
   print(f"Date: {record['Date']}")
   print(f"Amount: ${record['Amount']:.2f}\n")
 elif choice == 3:
  total_revenue = 0
  for record in toll_records:
   total_revenue += record['Amount']
  print(f"\nTotal Revenue: ${total_revenue:.2f}")
 elif choice == 4:
  search_vehicle_number = input("\nEnter Vehicle Number to Search: ")
  found_record = None
  for record in toll_records:
   if record['Vehicle Number'] == search_vehicle_number:
    found_record = record
    break
  if found_record:
   print("\nToll Record:")
   print(f"Vehicle Number: {found_record['Vehicle Number']}")
   print(f"Date: {found_record['Date']}")
   print(f"Amount: ${found_record['Amount']:.2f}")
  else:
   print("Toll record not found.")
 elif choice == 5:
  remove_vehicle_number = input("\nEnter Vehicle Number to Remove: ")
  found = False
  for i in range(len(toll_records)):
   if toll_records[i]['Vehicle Number'] == remove_vehicle_number:
    del toll_records[i]
    print("Toll record removed.")
    found = True
    break
  if not found:
   print("Toll record not found.")
 elif choice == 6:
  print("\nExiting the Bridge Toll Management System.")
  break
 else:
  print("\nInvalid choice. Please enter a valid option.")
