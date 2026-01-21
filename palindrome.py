def is_palindrome(word):
    def palindrome_util(l, r):
        if l == r:
            return True
        if word[l] != word[r]:
            return False
        return palindrome_util(l+1, r-1)
    return palindrome_util(0, len(word)-1)



if __name__ == "__main__":
    words = ["abracadabra", "nitin", "palindrome", "abcdcba"]
    for word in words:
        if is_palindrome(word):
            print(word + " is a palindrome")
        else:
            print(word + " is not a paldindrome")