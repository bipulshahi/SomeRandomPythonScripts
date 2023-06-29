#To find the collection of substrings within the string k and determine how many times each substring repeats, you can use a combination of loops and dictionaries. Here's an example:


k = 'abccghhjkijkabchjkkljhhhabcgvhjbjkklijkfgchvbabcgvhbjkijk'

substrings = {}
substring_length = 3  # Length of the substrings you want to search for

# Iterate over the string using a sliding window of the specified substring length
for i in range(len(k) - substring_length + 1):
    substring = k[i:i + substring_length]  # Extract the current substring
    
    # Check if the substring already exists in the dictionary
    if substring in substrings:
        substrings[substring] += 1  # Increment the count
    else:
        substrings[substring] = 1  # Add the substring to the dictionary

# Print the results
for substring, count in substrings.items():
    if count > 1:
        print(f"Substring '{substring}' repeats {count} times.")
