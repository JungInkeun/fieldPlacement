from datetime import datetime, timedelta
class DateExtractor:
    def __init__(self):
        self.now = datetime.now()
        self.target_date_to = self.now.strftime("%Y-%m-%d")
        self.today_date = self.now.strftime("%Y%m%d")
        self.now = self.now - timedelta(days=1)
        self.target_date_from = self.now.strftime("%Y-%m-%d")
        self.days_ago = self.now - timedelta(days=2)
        self.registered_date_from = self.days_ago.strftime("%Y-%m-%d")

    def get_target_date_from(self):
        return self.target_date_from

    def get_target_date_to(self):
        return self.target_date_to

    def get_registered_date_from(self):
        return self.registered_date_from
    
    def get_today_date(self):
        return self.today_date



class IndexCreator:
    def __init__(self) -> None:
        self.today_index = DateExtractor().get_today_date()
    
    def get_today_index_name(self):
        return self.today_index
    
    def grant_opensearch_index_name(self):
        today = IndexCreator().get_today_index_name()
        index_name = f"opensearch_name_{today}"
        return index_name



class RequestURL:
    def __init__(self, pathway) -> None:
        self.pathway = pathway
        self.url = "rc2-ai...." if "rc2" in pathway else "dev-ai ..."
    
    def get_url(self):
        return self.url