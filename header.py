import os

def header(text):
    # Centering print text:
    # https://stackoverflow.com/questions/33594958/is-it-possible-to-align-a-print-statement-to-the-center-in-python
    def center (str):
      #os.get_terminal_size().columns
      return str.center(50)
    
    print(center("+-++-++-++-++-++-++-++-++-++-++-++-++-++-++-++-++-+"))
    print(center(f"{text}"))
    print(center("+-++-++-++-++-++-++-++-++-++-++-++-++-++-++-++-++-+"))
    print()