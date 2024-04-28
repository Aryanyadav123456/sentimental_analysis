import streamlit as st
import pickle

# Loading the model outside the route to avoid loading it every time the route is called
with open("sentimentanalysis.pkl", "rb") as f:
    model = pickle.load(f)

def predict_sentiment(text):
    prediction = model.predict([text])[0]
    return prediction

def main():
    st.title('Sentiment Analysis Web App')
    text = st.text_area("Enter Text Here", "")
    if st.button('Predict'):
        if text == "":
            st.error("Please Enter Text")
        else:
            prediction = predict_sentiment(text)
            st.write("Predicted Sentiment:", prediction)
            if prediction == 'Positive':
                st.image('https://m.media-amazon.com/images/I/318lGxWI-GL._AC_UF1000,1000_QL80_.jpg')
            elif prediction == 'Negative':
                st.image("https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcQAb0RqZahdmcKJmBCigq1Dt9yRPCMfc6URAg&s", caption='Negative Sentiment Image')
            else : 
                st.image("https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcQ3dciRP34yl85KkeO6PbED0O29jkoMwUT_CQ&s", caption='Neutral Sentiment Image')

if __name__ == '__main__':
    main()
