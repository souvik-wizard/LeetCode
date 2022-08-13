def titleToNumber(self, title: str) -> int:
        res=0        
        for i in range(len(title)):
            # as we all know that there are 26 alphabets in English thats why 26.
            # why pre-multiply 26 with res?
            #if there is given only one single alphabet ["A" -> 1] then we first multiply 26 with 0 and that will be 0 itself.
            # And after that res will be updated  with its actual value and the loop ends. 
            # Why multiply with 26 only?
            #if it is lets say ("BAD") then we'll multiply B's value with 26 -->26 * 2(B's value) 
            res*=26

            # Why ASCII?  Bcz of that we dont need to use any extra space such as hash table to store A-Z value individually.
            # we are adding the Value of that particular character [ord(title[i]))] with our res.
            # Why substract with Ord("A")?  cz we need the exact value for our character [title[i])].
            # And we can get that if and only if we substarct that value with "A"s value.
            # Why Then add +1 at last?
            # If [title[i]] is "A" itself then A will be 0 , And we know "A" is 1.
            res+=ord(title[i])-ord("A")+1



            # Instead of writing {ord("A")+1} in previous expression we can write this.That will do the same for us.
            # res+=ord(title[i])-64

        return res