import datetime

class ReadingTracker:
    def __init__(self, goal):
        self.goal = goal
        self.current_book = None
    
    def set_goal(self, goal):
        self.goal = goal
        
    def add_book(self, title, total_pages, start_date=datetime.date.today(), current_page=0):
        self.current_book = {'title': title, 'total_pages': total_pages, 'start_date': start_date, 'current_page': current_page}
        
    def update_progress(self, pages_read):
        if self.current_book is not None:
            self.current_book['current_page'] += pages_read
    
    def days_to_finish(self):
        if self.current_book is not None:
            days = (self.current_book['total_pages'] - self.current_book['current_page']) / self.goal
            finish_date = datetime.date.today() + datetime.timedelta(days=days)
            return finish_date.strftime('%Y-%m-%d')
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
    
    def on_track(self):
        if self.current_book is not None:
            days = (self.current_book['total_pages'] - self.current_book['current_page']) / self.goal
            finish_date = datetime.date.today() + datetime.timedelta(days=days)
            if finish_date > datetime.date.today():
                return 'On schedule!'
            else:
                return 'Behind schedule!'
        else:
            return 'No current book'
