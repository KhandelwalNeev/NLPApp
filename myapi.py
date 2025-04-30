import nlpcloud
class API:
    def __init__(self):
        self.client = nlpcloud.Client("distilbert-base-uncased-emotion", "fdb150394173113fe99b5609a9f806bdab084fa2",
                                 gpu=False)

    def sentiment_analysis(self,text):
        response = self.client.sentiment(text)
        return response


