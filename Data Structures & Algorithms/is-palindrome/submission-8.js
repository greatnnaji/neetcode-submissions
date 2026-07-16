class Solution {
    /**
     * @param {string} s
     * @return {boolean}
     */
    isPalindrome(s) {
        let l = 0;
        let r = s.length - 1;

        while (l < r){
            while ((!this.isAlphaNum(s[l])) && (l < r)) l += 1;
            while ((!this.isAlphaNum(s[r])) && (l < r)) r -= 1;

            if (s[l].toLowerCase() != s[r].toLowerCase()) return false;

            l += 1;
            r -= 1
        }

        return true;
    }

    isAlphaNum(char) {
        if (!char) return false;
    
        return (
                (char >= 'A' && char <= 'Z') ||
                (char >= 'a' && char <= 'z') ||
                (char >= '0' && char <= '9')
            );  
    } 
}
