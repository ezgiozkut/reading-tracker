import datetime

class ReadingTracker:
    def __init__(self, goal):
        self.goal = goal
        self.current_book = None
    
    def set_goal(self, goal):
        self.goal = goal
        
    def add_book(self, title, total_pages, start_date=datetime.date.today(), current_page=0):
        self.current_book = {'title': title, 'total_pages': total_pages, 'start_date': start_date, 'current_page': current_page}
        
    def update_progress(self, pages_read, date=datetime.date.today()):
        if self.current_book is not None:
            self.current_book['current_page'] += pages_read
            if date > self.current_book['start_date']:
                days_since_start = (date - self.current_book['start_date']).days
                pages_per_day = self.current_book['current_page'] / days_since_start
                days_left = (self.current_book['total_pages'] - self.current_book['current_page']) / pages_per_day
                finish_date = date + datetime.timedelta(days=days_left)
                if finish_date < date:
                    return f"Behind schedule! You should have finished the book by {finish_date.strftime('%b %d')}."
                else:
                    return f"On schedule! According to your daily reading goal, you should finish the book by {finish_date.strftime('%b %d')}."
        else:
            return 'No current book'
    
    def days_to_finish(self):
        if self.current_book is not None:
            days = (self.current_book['total_pages'] - self.current_book['current_page']) / self.goal
            finish_date = datetime.date.today() + datetime.timedelta(days=days)
            return finish_date.strftime('%b %d')
        else:
            return 'No current book'
    
    def pages_left(self):
        if self.current_book is not None:
            return self.current_book['total_pages'] - self.current_book['current_page']
        else:
            return 'No current book'
    
    def percent_complete(self):
        if self.current_book is not None:
            return round(self.current_book['current_page'] / self.current_book['total_pages'] * 100, 2)
        else:
            return 'No current book'
    
    def on_track(self, date=datetime.date.today()):
        if self.current_book is not None:
            days_since_start = (date - self.current_book['start_date']).days
            pages_per_day = self.current_book['current_page'] / days_since_start
            days_left = (self.current_book['total_pages'] - self.current_book['current_page']) / pages_per_day
            finish_date = date + datetime.timedelta(days=days_left)
            if finish_date < date:
                return f"Behind schedule! You should have finished the book by {finish_date.strftime('%b %d')}."
            else:
                return f"On schedule! According to your daily reading goal, you should finish the book by {finish_date.strftime('%b %d')}."
        else:
            return 'No current book'
    
    def start_date(self):
        if self.current_book is not None:
            return self.current_book['start_date'].strftime('%b %d')
        else:
            return 'No current book'
