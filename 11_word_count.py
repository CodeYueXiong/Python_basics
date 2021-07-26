from collections import Counter


## Task; Word count
# For the text below,
# a) Clean punctuation and transform all words to lower case.
# b) Output a list of word count pairs sorted from highest to lowest count.
Text = """
bands which have connected them with another, and to assume among the
powers of the earth, the separate and equal station to which the Laws
of Nature and of Nature's God entitle them, a decent respect to the
opinions of mankind requires that they should declare the causes which
impel them to the separation.  We hold these truths to be
self-evident, that all men are created equal, that they are endowed by
their Creator with certain unalienable Rights, that among these are
Life, Liberty and the pursuit of Happiness.--That to secure these
rights, Governments are instituted among Men, deriving their just
powers from the consent of the governed, --That whenever any Form of
Government becomes destructive of these ends, it is the Right of the
People to alter or to abolish it, and to institute new Government,
laying its foundation on such principles and organizing its powers in
such form, as to them shall seem most likely to effect their Safety
and Happiness. """
# Solution 1
# 1). Cleaning text and lower casing all words
for char in '-.,\n':
    Text = Text.replace(char, ' ')
Text = Text.lower()
print(f"after cleaning the text and lower casing all words:\n {Text}")

# 2). Text splitting
word_list = Text.split()
print(f"after text splitting:\n {word_list}")

# 3). Counting the numbers for word occurrence
d = {}
for word in word_list:
    d[word] = d.get(word, 0) + 1
print(f"word counting:\n {d}")

# 4). Reverse the key and values using tuples
word_freq = []
for key, value in d.items():
    word_freq.append((value, key))
print(f"after sorting, the formatting is like:\n {word_freq}")

# Solution 2: Not using the get method
d = {}
for word in word_list:
    if word not in d:
        d[word] = 0
    d[word] += 1
print(f"solution 2: \n {d}")

# Solution 3: using in-built method
d = {}
for key in word_list:
    d[key] = d.get(key,0)+1

sort_list = sorted(d.items(), key=lambda x: x[1], reverse=True)
print(f"solution 3:\n {sort_list}")

# Solution 4: using counter method from the collections package
print(f"Solution 4:\n {Counter(word_list).most_common()}")
