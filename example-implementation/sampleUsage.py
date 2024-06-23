# assuming your path starts in the example-implementation folder 
import sys
sys.path.append('../API')

from PerplexitySearcher import GetPerplexityResponse
import pandas as pd

# replace with the path to your own chromedriver - see ReadMe for help
chromedriverPath = "/Users/ajcaesar/Downloads/chromedriver"

# import this df - it has 1 row for each US president, currently with 1 column with just their name
presidents_df = pd.read_csv("exampleInput.csv")


#it's up to you to make the prompt. This is often the trickiest part. For help 
# look up 'prompt engineering' or ask chatgpt or another model to help you format
# your questions to best extract the information that you need
def datePrompt(name):
    return (f"""Provide the birthdate of US President {name} in YYYY-MM-DD format. return just the date""")

def achievementPrompt(name):
    return (f"""what are considered the three most important achievements of President {name}. Return
            the three achievements in list format""")

def partyPrompt(name):
    return (f"""to what political party did President ${name} belong? Return just the party and no 
            other text""")

for index, row in presidents_df.iterrows():
    # I am only doing the first 10 entries as an example
    if (index < 10):
       name = row["Name"]
       print(name)
       
       #provide the prompt and path to chromedriver as well as any customizations - see readme
       presidents_df.loc[index, "DOB"] = GetPerplexityResponse(datePrompt(name), chromedriverPath, fullSentence = False)
       presidents_df.loc[index, "Party"] = GetPerplexityResponse(partyPrompt(name), chromedriverPath)
       presidents_df.loc[index, "notable_achievements"] = GetPerplexityResponse(achievementPrompt(name), chromedriverPath)
    

presidents_df.to_csv("exampleOutput.csv", index=False)