#!/usr/bin/env python
# coding: utf-8

# # Anagram Check
# 
# ## Problem
# 
# Given two strings, check to see if they are anagrams. An anagram is when the two strings can be written using the exact same letters (so you can just rearrange the letters to get a different phrase or word). 
# 
# For example:
# 
#     "public relations" is an anagram of "crap built on lies."
#     
#     "clint eastwood" is an anagram of "old west action"
#     
# **Note: Ignore spaces and capitalization. So "d go" is an anagram of "God" and "dog" and "o d g".**
# 
# ## Solution
# 
# Fill out your solution below:

# In[40]:


def anagram(s1,s2):
    Arr1 = s1.replace(' ', '').lower()
    Arr2 = s2.replace(' ', '').lower()
    return sorted(Arr1) == sorted(Arr2)


# In[62]:


def anagram2(s1, s2):
    Arr1 = s1.replace(' ', '').lower()
    Arr2 = s2.replace(' ', '').lower()
    
    if len(Arr1) != len(Arr2):
        return False
    count = {}
    
    for letter in Arr1:
        if letter in count:
            count[letter] += 1
        else:
            count[letter] = 1
            
    
    for letter in Arr2:
        if letter in Arr2:
            count[letter] -= 1
        else:
            count[letter] = 1
#     print('count', count.d)
    for letter in count:
        if count[letter] !=0:
            return False
        
    return True
            
    


# In[63]:


anagram2('dog', 'odg')


# In[55]:


anagram('dog','god')


# In[107]:


anagram('clint eastwood','old west action')


# In[108]:


anagram('aa','bb')


# # Test Your Solution
# Run the cell below to test your solution

# In[64]:


"""
RUN THIS CELL TO TEST YOUR SOLUTION
"""
from nose.tools import assert_equal

class AnagramTest(object):
    
    def test(self,sol):
        assert_equal(sol('go go go','gggooo'),True)
        assert_equal(sol('abc','cba'),True)
        assert_equal(sol('hi man','hi     man'),True)
        assert_equal(sol('aabbcc','aabbc'),False)
        assert_equal(sol('123','1 2'),False)
        print("ALL TEST CASES PASSED")

# Run Tests
t = AnagramTest()
t.test(anagram)


# In[65]:


t.test(anagram2)


# # Good Job!
