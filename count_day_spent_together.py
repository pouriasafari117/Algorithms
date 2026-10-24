# Intro : 
# Alice and Bob are traveling to Rome for separate business meetings.
# You are given 4 strings arriveAlice, leaveAlice, arriveBob, and leaveBob. Alice will be in the city from the dates arriveAlice to leaveAlice (inclusive), while Bob will be in the city from the dates arriveBob to leaveBob (inclusive). Each will be a 5-character string in the format "MM-DD", corresponding to the month and day of the date.
# Return the total number of days that Alice and Bob are in Rome together.
# You can assume that all dates occur in the same calendar year, which is not a leap year. Note that the number of days per month can be represented as: [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31].
# Example 1:
arriveAlice = "08-15"
leaveAlice = "08-18"
arriveBob = "08-16"
leaveBob = "08-19"
# Output: 3
# Explanation: Alice will be in Rome from August 15 to August 18. Bob will be in Rome from August 16 to August 19. They are both in Rome together on August 16th, 17th, and 18th, so the answer is 3.

# Example 2:
# arriveAlice = "10-01"
# leaveAlice = "10-31"
# arriveBob = "11-01"
# leaveBob = "12-31"
# Output: 0
# Explanation: There is no day when Alice and Bob are in Rome together, so we return 0.

arriveAlice ="02-14"
leaveAlice ="12-06"
arriveBob ="09-25"
leaveBob ="10-31"

arriveAlice = arriveAlice.split('-')
arriveAlice[0] = int(arriveAlice[0])
arriveAlice[1] = int(arriveAlice[1])

arriveBob = arriveBob.split('-')
arriveBob[0] = int(arriveBob[0])
arriveBob[1] = int(arriveBob[1])

leaveAlice = leaveAlice.split('-')
leaveAlice[0] = int(leaveAlice[0])
leaveAlice[1] = int(leaveAlice[1])

leaveBob = leaveBob.split('-')
leaveBob[0] = int(leaveBob[0])
leaveBob[1] = int(leaveBob[1])

def main():
    if (leaveBob[0] < arriveAlice[0]) or (leaveAlice[0] < arriveBob[0]):
        return 0
    elif (leaveBob[0] == arriveAlice[0] and leaveBob[1] < arriveAlice[1]) or (leaveAlice[0] == arriveBob[0] and leaveAlice[1] < arriveBob[1]):
        return 0
    
    if arriveAlice[0] > arriveBob[0]:
        s_m = arriveAlice[0]
        s_d = arriveAlice[1]

    elif arriveAlice[0] < arriveBob[0]:
        s_m = arriveBob[0]
        s_d = arriveBob[1]
    
    elif arriveAlice[1] <= arriveBob[1]:
        s_m = arriveBob[0]
        s_d = arriveBob[1]
    
    elif arriveAlice[1] >= arriveBob[1]:
        s_m = arriveAlice[0]
        s_d = arriveAlice[1]

    
    if leaveAlice[0] < leaveBob[0]:
        e_m = leaveAlice[0]
        e_d = leaveAlice[1]

    elif leaveAlice[0] > leaveBob[0]:
        e_m = leaveBob[0]
        e_d = leaveBob[1]
    
    elif leaveAlice[1] >= leaveBob[1]:
        e_m = leaveBob[0]
        e_d = leaveBob[1]
    
    elif leaveAlice[1] <= leaveBob[1]:
        e_m = leaveAlice[0]
        e_d = leaveAlice[1]

    months = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
    print(s_d , s_m , e_d , e_m)

    counter = 0
    while s_m != e_m or s_d != e_d:
        print(s_m , s_d)
        if s_d == months[s_m-1]:
            s_m += 1
            s_d = 1
            counter += 1
            continue
        s_d += 1
        counter += 1

    # with this condition we lost the last case counting. so we add 1 to res.
    return counter + 1

print(main())