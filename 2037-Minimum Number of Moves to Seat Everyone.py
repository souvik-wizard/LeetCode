def minMovesToSeat(seats, students):
        seats.sort()
        students.sort()
        if len(seats) == len(students):
            moves = 0                     
            for i, j in zip(seats, students):
                if i!= j:
                    moves += abs(i-j)
            return moves
            
seats=[4,1,5,9]
students=[1,3,2,6]

print(minMovesToSeat(seats,students))