# Perplexity_Automation
# Perplexity_Automation
Automating the research process with Perplexity without spending on the API. 

I created this with the intention of making it easier to utilize generative ai models like perplexity for doing research that involves asking repeat prompts about
many data points. For example, asking perplexity what the birthdate, political party, and 3 most important achievements of all US presidents are and exporting its responses in csv form for research. It was fun getting to use selenium and hunting 
through perplexity's DOM to find where different information is stored. 

Admittedly, it would be infinitely faster to just use perplexity's API, however I (and others as well based on my online search) have found the responses given by Perplexity when using its online UI are much better than the API for research purposes. 

My best advice would be to run this in headless mode in the background while you work --> to run it for 10 presidnets (30 prompts total) took about 5 minutes, though there are shortcuts you can implement to make it quicker based on how detailed a response you want. While you can load directly into perplexity's response page by adding your prompt to the url I found that navigating the site as a person would, by first entering in your prompt returned a better result and doesn't take that much more time. 

Details of use: 
the key function is GetPerplexityResponse ==> its arguments are (prompt, chrome_driver_path, max_retries=1, waitTime=10, fullSentence=True, headless=True)
prompt => the prompt you want to ask perplexity 
chrome_driver_path => the path to your chromedriver on your computer. You can download it from here https://sites.google.com/chromium.org/driver/ and find plenty of tutorials online 
max_retries => how many times perplexity will retry if it cannot get an answer the first time 
waitTime => how long (in seconds) perplexity has to generate a response 
fullSentence => this was my attempt at making this more efficient. Basically, the idea is that the function pulls text from perplexity and exits as soon as it detects punctuation, indicating that atleast 1 full sentence has been produced. Perplexity tends to drone on much longer than necessary and the first sentence often has 95% of useful information, so for large files this could save a lot of time. I have not worked out all its kinks yet, though. 
headless => makes the webdriver run in headless mode. I recommend leaving this as false for your first few times using the program so you can really see how it works.

Words of Warning: 
this will only work as is until Perplexity puts up a Captcha. Message me when that happens or feel free to contribute. If you have ideas on how to make thsi more efficient timewise, please contribute. 
