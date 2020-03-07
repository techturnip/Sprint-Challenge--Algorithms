'''
Your function should take in a single parameter (a string `word`)
Your function should return a count of how many occurences of ***"th"*** occur within `word`. Case matters.
Your function must utilize recursion. It cannot contain any loops.
'''
def count_th(word):

    # TBC

    # base case:
    if word == '':
        # no word, obviously the count is 0
        return 0

    else:
        # check 'th'
        if word[0:2] == 'th':
            print('FOUND TH:', word[0:2])

            # found th, return 1 and recurse adding to the 1
            # until the count is achieved
            return 1 + count_th(word[2:])
        else:
            print('NO TH:', word[0:2])

            # recurse, moving through the index of the word
            return count_th(word[1:])
