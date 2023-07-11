from Tweet import Tweet
import pickle as cPickle
tweets = []

def makeTweet():
    author = input("What is your name?")
    while(True):
        text = input("What would you like to tweet?")
        if(len(text) > 140):
            print("Tweets can only be 140 characters!")
            continue
        else:
            break
    twit = Tweet(author,text)
    tweets.append(twit)
    print(author, ", your tweet has been saved.")

def viewTweet():
    if not tweets:
        print("No Recent Tweets")
        return
    print("Recent Tweets\n-------")
    for tweet in tweets:
        print(tweet.getAuthor(), " - ", tweet.getAge(), "\n", tweet.getText())

def searchTweet():
    x = 0
    if not tweets:
        print("No Tweets to Search")
        return
    search = input("What would you like to search for?")
    print("Search Results\n-------")
    for tweet in tweets:
        if search in tweet.getText():
            print(tweet.getAuthor(), " - ", tweet.getAge(), "\n", tweet.getText())
            x = x + 1
    if(x == 0):
        print("No tweets contained ",search)
        
def saveTweet():
    with open('Tweet.pickle','wb') as file:
        cPickle.dump(tweets,file)
    
try:
    pikle = []
    with open('Tweet.pickle','rb') as file:
        tweets = cPickle.load(file)
        print(tweets)
except:
    print("No tweets in file.")
while(True):
    print("Tweet Menu\n------")
    print("1.Make a Tweet")
    print("2.View Recent Tweets")
    print("3.Search Tweets")
    print("4.Quit")
    try:
        choice = int(input("What would you like to do?"))
    except:
        print("Please enter numeric value.")
        continue
    if(int(choice) < 1 or int(choice) > 4):
        print("Please enter valid option")
    if(int(choice) == 1):
        makeTweet()
        continue
    if(int(choice) == 2):
        viewTweet()
        continue
    if(int(choice) == 3):
        searchTweet()
        continue
    if(int(choice) == 4):
        print("Thank you for using the Tweet Manager!")
        saveTweet()
        break
    
