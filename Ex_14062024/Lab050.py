# range can be negative
for counter in range(10, 0, -1): #10 to 1
    print(counter)
    if counter == 5:
        print("Loop ended at counter =", counter)
        break # exit the loop when counter is 5
    