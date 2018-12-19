import math

# 1. Intro and naive search algorithm
with open('AviationData.txt') as f:
    aviation_data = f.readlines()

aviation_list = [event.split(' | ') for event in aviation_data]

headers = aviation_list.pop(0)
aviation_data.pop(0)

def first(aviation_list):
    lax_code = []
    for event in aviation_list:
        for field in event:
            if "LAX94LA336" == field :
                lax_code.append(event)
                break
    print("\nBrute Force:\n",lax_code)

first(aviation_list)

# 2. Linear and Logarithmic Time Algorithms
def linear(aviation_list):
    lax_code = []
    for event in aviation_list:
        if event[2] == "LAX94LA336":
            lax_code.append(event)
            break
    print("\nLinear:\n",lax_code)
    
def sort_list(aviation_list):
    # Sorts aviation_list on column 3
    return sorted(aviation_list, key=lambda x: x[2])
    
def logarithmic(sorted_aviation_list):
    # Given a sorted list this works in log(n) time
    search_code = "LAX94LA336"
    lax_code = []
    upper_limit = len(sorted_aviation_list) - 1
    lower_limit = 0
    while upper_limit >= lower_limit:
        index = lower_limit + math.floor((upper_limit - lower_limit)/2)
        target = sorted_aviation_list[index]
        if target[2] > search_code:
            upper_limit = index - 1
        elif target[2] < search_code:
            lower_limit = index + 1
        else:
            lax_code.append(target)
            break
    print("\nLogarithmic:\n",lax_code)
    
linear(aviation_list)
logarithmic(sort_list(aviation_list))


# 3. Hash Tables
aviation_dict_list = []

for line in aviation_data:
    event_dict = {}
    event_list = line.split(" | ")
    for i, header in enumerate(headers):
        event_dict[header] = event_list[i]
    aviation_dict_list.append(event_dict)
    
lax_dict = []
for event in aviation_dict_list:
    if "LAX94LA336" in event.values():
        lax_dict.append(event)
        break

print("\nHash Table:\n",lax_dict)


# 4. Accidents by U.S. State
state_accidents = {}
for accident in aviation_dict_list:
    if accident["Country"] == "United States":
        if ',' not in accident["Location"]:
            pass
        else:
            accident_state = accident["Location"].split(',')[-1].strip()
            if accident_state in state_accidents:
                state_accidents[accident_state] += 1
            else:
                state_accidents[accident_state] = 1
        
sorted_states = sorted(state_accidents,key =    state_accidents.__getitem__,reverse=True)
        
print("\nState with most accidents:\n",
      sorted_states,
      "\n",
      sorted_states[0],state_accidents[sorted_states[0]]
     )


# 5. Fatalities and Injuries by Month

monthly_injuries = {}
for accident in aviation_dict_list:
    accident_month = accident["Event Date"].split('/')[0]
    injury_count = 0
    if accident["Total Fatal Injuries"] != '':        
        injury_count += int(accident["Total Fatal Injuries"])
    if accident["Total Serious Injuries"] != '':
        injury_count += int(accident["Total Serious Injuries"])
    if accident_month in monthly_injuries:
        monthly_injuries[accident_month] += injury_count
    else:
        monthly_injuries[accident_month] = injury_count

month_map = {'01':'Jan',
             '02':'Feb',
             '03':'Mar',
             '04':'Apr',
             '05':'May',
             '06':'Jun',
             '07':'Jul',
             '08':'Aug',
             '09':'Sep',
             '10':'Oct',
             '11':'Nov',
             '12':'Dec',
             '':"None"}

for month in sorted(month_map.keys()):
    print(month_map[month],monthly_injuries[month])
