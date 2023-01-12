import re

class Processor:

    def strip(self,term):
        return term.strip()
    
    def special_char_remove(self,term):
        text = ""
        for chr in str(term):
            if chr not in "[!@#$%^&*()[];:,./<>?\|`~-=_+]":
                text+=chr
        return text
    
    def tokenize(self,term):
        return term.split()

    def stop_word_remove(self,tokens):
        with open("stop words.txt","r",encoding="UTF-8") as f:
            stop_words = [i.strip() for i in f.readlines()]
            tokens = [token for token in tokens if token not in stop_words]
            return tokens

    def get_boosters(self,tokens):
         heuristics = {}
         heuristics["artist"] = ['ගායකයා', 'ගයනවා', 'ගායනා', 'ගැයු', 'ගයන', 'ගයපු', 'කියපු', 'කියන']
         heuristics["name"] = ["නම","ගීතය","නාමය"]
         heuristics["source"] = ["මෙන්","සේ","වැනි","බඳු","වන්","අයුරු","අයුරින්","ලෙස","උපමේය"]
         heuristics["targets"] = ["උපමා","උපමාවක්","රූපක","රූපකයක්"] 

         boosts={}
         boosts["artist"]=1
         boosts["name"]=1
         boosts["source"]=1
         boosts["targets"]=1

         for token in tokens:
            for field in heuristics.keys():
                if token in heuristics[field]:
                   boosts[field] +=4

         boosters=[
                "name^"+str(boosts["name"]),
                "singers^"+str(boosts["artist"]),
                "metaphors.source^"+str(boosts["source"]),
                "metaphors.targets^"+str(boosts["targets"])
         ]

         return boosters

    def get_sorter(self,tokens):

        by_date=0
        by_popularity=0

        date =["නවතම", "අලුත්", "නව", "අලුත්ම" ]
        popularity = ['ජනප්‍රිය', 'ප්‍රචලිත', 'ප්‍රසිද්ධ', 'ජනප්‍රියම', 'ප්‍රචලිතම' 'ප්‍රචලිතම']

        for token in tokens:
            if token in date:
                by_date+=1
            if token in popularity:
                by_popularity+=1
        
        return {"view_count":"desc"} if by_popularity>by_date else {"published_on":"desc"}

    def get_range(self,tokens):
        range = 10
        for token in tokens:
            if str(token).isdigit():
                range = int(token)
        return range
        
    def query_text(self,tokens):
        return " ".join(tokens)