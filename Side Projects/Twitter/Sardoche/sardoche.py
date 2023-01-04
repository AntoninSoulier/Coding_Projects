from matplotlib.pyplot import text
import tweepy
import twitter

def answer():
    auth = tweepy.OAuthHandler("aaY1e536Lp44Apytesb7ZJ9L6","xNgN1d9dg6U7MORfyF3ZAMOPISR2sGutZtU0K3obMK5gO1qGHB")
    auth.set_access_token("1485564928169857024-eEa2vMvp49B2Ej4bbCad6nVboA1q67","LkFPD43ultdOqT7tlI1v2Nslw0fDdH2Cj4uQTXsH7s1eX")

    api = tweepy.API(auth)

    try:
        api.verify_credentials()
        print("ok")
    except:
        print("Erreur de connexion")
    
    max_t = 100
    tweets = api.search_tweets(q="@Sardoche_Lol")
    
    for tweet in tweets:
        try:
            api.update_status("Allez Sardo", tweet.id_str, auto_populate_reply_metadata=True)
            print(tweet.text + " | Allez Sardo")
        except:
            print("Tweet déjà répondu")
answer()
