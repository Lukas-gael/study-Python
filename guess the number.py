secret_number = 777
guess =-99
print(
"""
+================================+
| Welcome to my game, muggle!    |
| Enter an integer number        |
| and guess what number I've     |
| picked for you.                |
| So, what is the secret number? |
+================================+
""")
guess = int(input())

while guess != secret_number:
    print("ha ha, you're stucked in my loop, tente novamente")
    guess = int(input())
print ("well done muggle, you're free now")
