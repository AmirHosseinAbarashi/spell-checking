
# A Dynamic Programming based Python program for edit
# distance problem

def calculateEditditDistDP(user_input, str2, m, n):
    # Create a table to store results of subproblems
    dp = [[0 for x in range(n + 1)] for x in range(m + 1)]

    # Fill d[][] in bottom up manner
    for i in range(m + 1):
        for j in range(n + 1):

            # If first string is empty, only option is to
            # insert all characters of second string
            if i == 0:
                dp[i][j] = j  # Min. operations = j

            # If second string is empty, only option is to
            # remove all characters of second string
            elif j == 0:
                dp[i][j] = i  # Min. operations = i

            # If last characters are same, ignore last char
            # and recur for remaining string
            elif user_input[i-1] == str2[j-1]:
                dp[i][j] = dp[i-1][j-1]

            # If last character are different, consider all
            # possibilities and find minimum
            else:
                dp[i][j] = 1 + min(dp[i][j-1],   # Insert
                                   dp[i-1][j],   # Remove
                                   dp[i-1][j-1])  # Replace

    return dp[m][n]


def calculateSimilarityWords(user_input):

    similar_size_words = []
    edit_distances_nums = []
    low_edit_distance_words = []
    low_edit_distance_nums = []

    for word in dictionary_list:
        if((len(word) >= len(user_input)-1) & (len(word) <= len(user_input)+1)):
            similar_size_words.append(word)

    for i in range(similar_size_words.__len__()):
        edit_distances_nums.append(calculateEditditDistDP(
            user_input, similar_size_words[i], len(user_input), len(similar_size_words[i])))

    for j in range(edit_distances_nums.__len__()):
        if(edit_distances_nums[j] < 2):
            low_edit_distance_words.append(similar_size_words[j])
            low_edit_distance_nums.append(edit_distances_nums[j])

    for k in range(low_edit_distance_nums.__len__()//2):
        print(low_edit_distance_words[k])


dictionary = open("dictionary.txt", "r")
dictionary_list = dictionary.read().split(" ")

user_input = input("Enter your Text: ")
print()

user_input_to_list = user_input.split(" ")

for word in user_input_to_list:
    if word not in dictionary_list:
        calculateSimilarityWords(word)
        print("")
