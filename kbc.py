l1 = ['q1', 'q2', 'q3', 'q4', 'q5'] #List of questions
a1 = ['a1', 'a2', 'a3', 'a4', 'a5'] #List of corresponding answers
sum = 0
i = 0

for l in l1:
    print("\n",l)
    while i<len(a1):
        user = input("Enter your answer: ")
        if user==a1[i]:
            print("Correct Answer!")
            sum += 1000
            i += 1
            break
        else:
            print("Wrong Answer")
            i += 1
            break

print("\nTotal amount won: ", sum)

print("Thanks for playing!")