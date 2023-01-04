import twitter

def sendTweet():
    auth = twitter.OAuth(consumer_key="aaY1e536Lp44Apytesb7ZJ9L6",
                         consumer_secret="xNgN1d9dg6U7MORfyF3ZAMOPISR2sGutZtU0K3obMK5gO1qGHB",
                         token="1485564928169857024-eEa2vMvp49B2Ej4bbCad6nVboA1q67",
                         token_secret="LkFPD43ultdOqT7tlI1v2Nslw0fDdH2Cj4uQTXsH7s1eX"
                        )
    tweet = twitter.Twitter(auth=auth)

    alert = "Spencer"

    #Publish
    tweet.statuses.update(status=alert)

API_key = "jxd0sijy7xObcUHQ7Xz5HARZ5"
API_key_secret = "A5xSrrmkkbChoX02nVVqUVUNkXubeeazamfANl5Tmf9I6eRsoy"
Bearer_Token = "AAAAAAAAAAAAAAAAAAAAAEUNiAEAAAAANhJfe02kYwp90MTqxhkaXEvvUD8%3D193OcQuWoWwHvHd0KKE2Bhd5Ix4yw8woBiyDnXvrZ5JYnicd7y"

sendTweet()