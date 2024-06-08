# Question Link: https://leetcode.com/problems/longest-substring-without-repeating-characters/

class Solution1:
    def lengthOfLongestSubstring(self, s):
        # extract the length of the string
        n = len(s)

        # initialize a variable to store the current maximum length of substring
        max_length = 0

        # initialize a variable to iterate throught the indices
        i = 0

        while i < n - max_length:
            # check for the longest substring starting with the char at index `i`
            j = i

            # initialize a set to store the char already in use for the substring
            char_set = set()

            curr_len = 0

            while j < n:
                if s[j] not in char_set:
                    curr_len += 1
                    
                    # add the current char to the set
                    char_set.add(s[j])
                    
                    # increment `j` to check the next char
                    j += 1
                else:
                    break
            
            # update the max_length
            max_length = max(max_length, curr_len)
            
            # increment `i` to start checking from the next position
            i += 1
        
        return max_length


class Solution2:
    def lengthOfLongestSubstring(self, s):
        # here, we use the fact that the largest substring with the required properties will always lie between 2 equal characters, so we only check the size of the such substrings by considering a sliding window using 2 pointers

        # initialize the left and right pointers of the sliding window
        l,r = 0,0

        # initialize a variable to store the current maximum length of substring
        max_length = 0

        # initialize a set to store the chars in the sliding window
        char_set = set()

        while r < len(s):
            if s[r] not in char_set:
                # add current char to set
                char_set.add(s[r])

                # move the right pointer
                r += 1

                # update the current window size and max_length
                max_length = max(max_length, r - l)
            
            else:
                # if the current char is in the set, remove chars until we can move the left pointer past the first occurrence of the repeated char
                char_set.remove(s[l])
                
                l += 1
        
        return max_length