# Program to copy contents from one file to another
# and count total number of words copied

try:
    # Open source file in read mode
    source = open("source.txt", "r")

    # Read content from source file
    content = source.read()

    # Open target file in write mode
    target = open("target.txt", "w")

    # Write content into target file
    target.write(content)

    # Count total words
    word_count = len(content.split())

    # Display total words copied
    print("Total Words Copied:", word_count)

    # Close files
    source.close()
    target.close()

except FileNotFoundError:
    print("Source file not found")

'''
output
Source file not found
'''
