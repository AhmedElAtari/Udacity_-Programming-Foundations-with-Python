import urllib

def read_text():
    file = open(r"C:\OOP\movie_quotes.txt") # Open the message file
    file_content=file.read() # Get the message file content
    file.close() # Close the file
    check_profanity(file_content) # Check if the file contains any curs word


def check_profanity(text):
    # Start Connection
    connection = urllib.urlopen("http://www.wdylike.appspot.com/?q="+text)
    # Read the response & Get the content
    output = connection.read()
    # Close the connection
    connection.close()
    # Check if the response is negative or the opposite
    if "true" in output:
        print 'Profanity detected'
    elif "false" in output:
        print 'Safe msg'
    else:
        print "Could not scan the doc "

# Function Call
read_text()
