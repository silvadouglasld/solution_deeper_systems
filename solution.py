import json
import numpy as np 

# Declare used variables

priorities= []
final_watchers = {}
final_managers = {}

# Opens the file
with open("source_file_2.json") as f:
    current_file = json.load(f)

# Iterates selecting the priorities as a auxiliry list
for i in range(0,len(current_file)):
    priorities.append(current_file[i]['priority'])
Np = len(priorities)

for i in range(0,Np):
    # Select the index of the minimum integer in the prority list
    index = np.argmin(priorities)
    manager_list = current_file[index]['managers']
    watcher_list = current_file[index]['watchers']
    for watcher in watcher_list:
        # Watchers
        if not watcher in final_watchers:
            final_watchers[watcher] = []
        else:
            final_watchers[watcher].append(current_file[index]["name"])
    for manager in manager_list:
        # Manager
        if not manager in final_managers:
            final_managers[manager] = []
        else:
            final_managers[manager].append(current_file[index]["name"])
    # Pops the used index from the list
    priorities.pop(index)


# Save both files


with open("managers.json", "w") as file_managers:# Append
    file_managers.write(json.dumps(final_managers))
    file_managers.close()

with open("watchers.json", "w") as file_watcher:# Append
    file_watcher.write(json.dumps(final_watchers))
    file_watcher.close()


    