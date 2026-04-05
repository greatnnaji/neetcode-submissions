class Solution:
    def isPalindrome(self, s: str) -> bool:
        cleaned_s = ""

        for string in s:
            if string.isalnum():
                cleaned_s += string.lower()
        
        # print(cleaned_s)

        start_pointer = 0
        end_pointer = len(cleaned_s) - 1

        if len(cleaned_s) % 2 == 0:
            print("even length...")
            midpoint = len(cleaned_s) / 2

            while start_pointer < midpoint:
                print("start_value: ")
                print(cleaned_s[start_pointer])
                print("end_value")
                print(cleaned_s[end_pointer])

                if cleaned_s[start_pointer] != cleaned_s[end_pointer]:
                    print("False")
                    return False
                start_pointer += 1
                end_pointer -= 1

        else:
            print("odd length...")
            while start_pointer != end_pointer:
                print("start_value: ")
                print(cleaned_s[start_pointer])
                print("end_value")
                print(cleaned_s[end_pointer])

                if cleaned_s[start_pointer] != cleaned_s[end_pointer]:
                    print("False")
                    return False
                start_pointer += 1
                end_pointer -= 1

        return True
