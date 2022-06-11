
# A Dynamic Programming based Python program for edit
# distance problem

def calculateEditDistanceBetweenTwoWords(word1, word2):
    m = len(word1)
    n = len(word2)

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
            elif word1[i-1] == word2[j-1]:
                dp[i][j] = dp[i-1][j-1]

            # If last character are different, consider all
            # possibilities and find minimum
            else:
                dp[i][j] = 1 + min(dp[i][j-1],   # Insert
                                   dp[i-1][j],   # Remove
                                   dp[i-1][j-1])  # Replace

    return dp[m][n]


def compareTwoWords(word, word_len, similarFoundWords):
    # پیمایش در کلمات دیکشنری با اندازه دیشکنری دریافتی
    for wordToCompare in opened_dic_files[word_len]:
        edit_distance = calculateEditDistanceBetweenTwoWords(
            word, wordToCompare)  # (edit distance) محاسبه تعداد عملیات تغییر در ترتیب حروف کلمات
        # از مقدار درخواستی edit distance بررسی کمتر یا برابر بودن
        if (edit_distance <= requested_edit_distance):
            # قرار دادن کلمه دیکشنری در لیست کلمات مشابه برای کلمه اشتباه
            similarFoundWords.append(wordToCompare)
            if (len(similarFoundWords) == requested_number_of_suggestions):
                break


def findSimilarWordsFor(word):
    word_len = len(word)
    similarFoundWords = []  # لیست کلمات مشابه برای کلمه اشتباه

    # بررسی کلمات مشابه برای کلمه اشتباه
    compareTwoWords(word, word_len, similarFoundWords)
    # اگر تعداد کلمات مشابه برای کلمه اشتباه برابر با تعداد کلمات پیشنهادی کاربر باشد لیست را بر میگرداند
    if (len(similarFoundWords) == requested_number_of_suggestions):
        similarFoundWords_str = ' '.join(str(item)
                                         for item in similarFoundWords)  # تبدیل لیست به رشته
        return word + ' : ' + similarFoundWords_str

    for i in range(requested_edit_distance + 1):
        if i != 0:
            compareTwoWords(word, word_len - i, similarFoundWords)
            if (len(similarFoundWords) == requested_number_of_suggestions):
                break
            compareTwoWords(word, word_len + i, similarFoundWords)
            if (len(similarFoundWords) == requested_number_of_suggestions):
                break


    similarFoundWords_str = ' '.join(
        str(item) for item in similarFoundWords)  # تبدیل لیست به رشته
    return word + ' : ' + similarFoundWords_str


def openNecessaryDictionaries():

    for i in range(count_of_words):
        for j in range(len(words[i]) - requested_edit_distance, len(words[i]) + requested_edit_distance + 1):
            # وارد شده توسط کاربر edit distance باز کردن دیکشنری های مورد نیاز با توجه به

            # prevent j index from being out of our dictionaries range
            # because the value of current_word_len - requested_edit_distance could be negative
            # and similar for current_word_len + requested_edit_distance + 1

            # که edit distance از محدوده دیکشنری خارج نمیشه و اون باگ مربوط به اندازه j تو کامنت بالا منظورم همین بود که
            # بزرگتر از اندازه کوچیک ترین کلمه متن هست و خطا میده اینجا به وجود میاد
            if (j < 0 or j > 31):
                continue

            # بررسی اینکه لیست دیکشنری با تکرار کلمات با اندازه یکسان چندین بار باز نشود
            if (opened_dic_files[j] == None):
                dic_file = open("d_w_length_" + str(j) + ".txt", "r")
                # تبدیل دیکشنری به لیست و قرار دادن در لیست دیکشنری های باز شده
                opened_dic_files[j] = dic_file.read().split(" ")


def isWrongWord(word):
    if word not in opened_dic_files[len(word)]:
        return True
    return False


def calculateSimilarWordsForEachWrongWords():
    # لیستی از لیست کلمه های مشابه برای هر کلمه اشتباه
    similar_words_for_each_wrong_words = []
    for i in range(count_of_words):  # پیمایش بر روی لیست کلمات
        word = words[i]
        if (isWrongWord(word)):  # بررسی اشتباه بودن کلمه
            similar_words_for_each_wrong_words.append(
                findSimilarWordsFor(word))  # قرار دادن لیست کلمات مشابه برای هر کلمه اشتباه

    similar_words_for_each_wrong_words_str = '\n\n'.join(
        str(item) for item in similar_words_for_each_wrong_words)  # تبدیل لیست به رشته
    return similar_words_for_each_wrong_words_str


if __name__ == "__main__":

    # openes_dic_files برای قرار دادن لیست دیکشنری های مورد نیاز در هر عنصر لیست
    opened_dic_files = [None] * 31

    words = input("Enter your Text: ").split(" ")
    requested_edit_distance = int(input("Enter edit distance: "))
    requested_number_of_suggestions = int(
        input("Enter number of suggestions: "))
    count_of_words = len(words)  # تعداد کل کلمات در متن دریافت شده

    openNecessaryDictionaries()  # باز کردن دیکشنری های مورد نیاز
    print()
    # نمایش کلمات مشابه برای هر کلمه اشتباه
    print(calculateSimilarWordsForEachWrongWords())
