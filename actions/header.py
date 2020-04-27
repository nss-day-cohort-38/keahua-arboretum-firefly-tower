# import os

def header(text):
    # Centering print text:
    # https://stackoverflow.com/questions/33594958/is-it-possible-to-align-a-print-statement-to-the-center-in-python
    def center (str):
        #if we wanted to center based on the os terminal size,
        # replace 50 with: os.get_terminal_size().columns
        return str.center(50)
      
    #https://www.geeksforgeeks.org/python-split-string-into-list-of-characters/
    def split(word): 
      return [char for char in word]  
      
    def space_out(str):
        # Start with a double space,
        # split the string into an array of characters, 
        # then rejoin it with double spaces between each letter
        spaced_str = "  " + "  ".join(split(str))
        return spaced_str
    
    print(center("+-++-++-++-++-++-++-++-++-++-++-++-++-++-++-++-++-+"))
    print(space_out(text))
    print(center("+-++-++-++-++-++-++-++-++-++-++-++-++-++-++-++-++-+"))
    print()