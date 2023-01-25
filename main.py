from sniffer import capture
from sklearn.feature_extraction.text import CountVectorizer
count_vectorizer = CountVectorizer(analyzer='word', min_df=10)



def main():
    traffic  = capture()
    for packet in traffic:
        ...
        

  

def convert_payload (packet) -> str:
    method = 0 if packet.method =='post' else 0
    if packet.body:
        pay_len = len(packet.body)
        payload = count_vectorizer.fit(packet.payload).transform(packet.payload).toarray()




    ...

if __name__== "__main__":
    main()