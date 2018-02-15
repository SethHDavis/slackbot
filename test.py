from get_sprint import scrape

username = raw_input("What is your username? ")
password = raw_input("What is your password? ")
company = raw_input("What company are you from? ")
board = raw_input("What board do you want to access? ")

print scrape(username, password, company, board)