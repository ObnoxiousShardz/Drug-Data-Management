import time
from Fetcher import Fetcher
from DeleteEverything import DeleteEverything
from RemoveEntry import Clearer
from Writer import Writer
from ViewTable import Table

print("======================================================================================================="
      "\nWelcome to Drug Data Manager!\nYou can add, remove or fetch for drugs and their count with the help of this program.\n"
      "=======================================================================================================")
time.sleep(3)
choice = int(
    input("Available Options:\n1. Add New Entry (1)\n2. Remove An Entry (2)\n3. Fetch For Data (3)\n4. Delete All Records (4)\n5. See The Contents of the Table (5)\nYour Choice: "))
print("=======================================================================================================")
print("Processing Your Request to Server...")
print("=======================================================================================================")
time.sleep(1.5)

if choice == 1:
    Writer()
elif choice == 2:
    Clearer()
elif choice == 3:
    Fetcher()
elif choice == 4:
    DeleteEverything()
elif choice == 5:
    Table()
else:
    print("No such option available!")
