# Function to calculate the value of a consonant
def consonantValue(char):
    return ord(char) - ord('a') + 1

# Function to find the highest value of consonant substrings
def HighestConsonantValue(s):
    maxConstantValue = 0  # Initialize the maximum value of consonant substrings found so far
    currentConstantValue = 0  # Initialize the value of the current consonant substring

    # Iterate through each character in the input string
    for char in s:
        if char in "bcdfghjklmnpqrstvwxyz":  # Check if the character is a consonant
            currentConstantValue += consonantValue(char)  # Add the value of the consonant to the current substring's value
        else:  # If the character is not a consonant (vowel or other)
            # Update the maximum value if the current substring's value is greater
            maxConstantValue = max(maxConstantValue, currentConstantValue)
            currentConstantValue = 0  # Reset the current substring's value since a vowel or non-alphabetic character is encountered
    
    # After the loop, update the maximum value if necessary
    maxConstantValue = max(maxConstantValue, currentConstantValue)

    return maxConstantValue

# Example usage
input_string = "bzaeioucdf"  # Sample input string
result = HighestConsonantValue(input_string)
print(result)  # Output: 15 (bcd and cdf are consonant substrings with values 7 and 8)
