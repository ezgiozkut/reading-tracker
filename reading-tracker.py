import datetime

# Set your yearly reading goal
yearly_goal = int(input("What is your yearly reading goal? "))

# Set today's date
today = datetime.date.today()

# Set a starting point for the tracker
tracker = {'total_pages_read': 0, 'current_book': None, 'book_start_date': None, 'book_end_date': None}

# Function to update the tracker with the number of pages read
def update_tracker(pages_read):
    tracker['total_pages_read'] += pages_read
    days_elapsed = (today - tracker['book_start_date']).days
    days_remaining = (tracker['book_end_date'] - today).days
    pages_remaining = tracker['current_book']['pages'] - tracker['current_book']['pages_read']
    daily_goal = (yearly_goal - tracker['total_pages_read']) / (365 - days_elapsed)
    if daily_goal < 0:
        daily_goal = 0
    if pages_remaining > 0:
        tracker['current_book']['pages_read'] += pages_read
    else:
        tracker['current_book'] = None
        tracker['book_start_date'] = None
        tracker['book_end_date'] = None
    return daily_goal, days_remaining

# Function to start reading a new book
def start_book(title, pages):
    tracker['current_book'] = {'title': title, 'pages': pages, 'pages_read': 0}
    tracker['book_start_date'] = today
    days_remaining = (year_end - today).days
    pages_remaining = pages
    daily_goal = pages_remaining / days_remaining
    tracker['book_end_date'] = today + datetime.timedelta(days=round(pages_remaining / daily_goal))
    return daily_goal, days_remaining

# Main loop of the program
year_end = datetime.date(today.year, 12, 31)
daily_goal, days_remaining = start_book(input("What is the title of the book you are starting? "), int(input("How many pages does the book have? ")))
print(f"Your daily reading goal to finish {tracker['current_book']['title']} by {tracker['book_end_date']} is {round(daily_goal)} pages per day.")
while True:
    pages_read = int(input("How many pages did you read today? "))
    daily_goal, days_remaining = update_tracker(pages_read)
    if tracker['current_book'] is None:
        print(f"Congratulations! You have finished {yearly_goal} pages of reading for the year!")
        break
    print(f"Your daily reading goal to finish {tracker['current_book']['title']} by {tracker['book_end_date']} is {round(daily_goal)} pages per day.")
    print(f"You have {days_remaining} days remaining to finish {tracker['current_book']['title']}.")
    if daily_goal == 0:
        print("You have already met your yearly reading goal!")
    elif daily_goal < 1:
        print("You are behind your yearly reading goal.")
    else:
        print("You are ahead of your yearly reading goal.")
