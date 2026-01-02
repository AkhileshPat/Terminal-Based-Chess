# text = input("Enter a string: ")
# result = []

# for char in text:
#     if char.lower() in 'abcdefgh':
#         result.append(str(ord(char.lower()) - ord('a') + 1))

# print(' '.join(result))

move = input("")

def square_to_index(move) :

    col = [ord(char.lower()) - ord('a') + 1 for char in move if char.lower() in 'abcdefgh']

    print(col)

    return col

square_to_index(move)