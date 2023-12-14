# Import the 'collections' module to use the 'defaultdict' class.
import collections

# Define a string 'str1' with a sentence.
str1 = input("Сложи текста тук, който да преброя тук: ")
str2 = str1.lower()
total_count = 0

# Create a defaultdict 'd' with integer values as the default type.
d = collections.defaultdict(int)

# Iterate through each character in the string 'str1'.
# Update the counts of each character in the 'd' dictionary.
for c in str2:
    if not c == " ":
        d[c] += 1
        total_count += 1

# Iterate through the characters in 'd' in descending order of their counts.
for c in sorted(d, key=d.get, reverse=True):
    # Check if the character occurs more than zero times
    if d[c] > 0:
        # Print the character and its count.
        print('%s %d' % (c, d[c]))

print(f"Общ брой букви: {total_count}")