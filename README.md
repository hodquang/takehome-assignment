
## Evaluation
Submit a Github repo (fork this one) via email to lilly@contenda.co. Please include a README that has the following:

1. Any additional setup required outside of the ones I wrote so that I can run your app
    Not really, you just need to do "pip3 install" on the modules being called on top of main.py
2. What your code does and why
    So I assume from the input/output that what we need in the end is a timezone array. I simplified the problem from "optimal time" to target time. The solution I came up with is basically a feature that allows the user to select a time that the user wants to tweet out their tweets in their followers' timezone. In that sense, the system will gather a array of time in the user's timezone and write each timestamp accordingly. For example, I live in NY timezone and want to have my tweet to post at 9AM in Tokyo and London that means the array of time will contains 4am and 8pm in New York timezone to tweet. I will also ask the user to input their location and the target time for their tweet. The code itself takes awhile to run since there is a nested loop, so I made a test.json to run it to make the code works.

    I do feel that it's quite unrealistic since twitter is worldwide and not region based so the idea of some accounts can view the tweet before it goes out to them seems strange. More reasons to use VPN, like how people used that to watch Netflix movies blocked in some regions.

4. Stuff you'd like to get to but didn't have the time
    "Optimal time" makes me think of performing data analysis on the followers' twitter usage data to find the time that they used twitter the most every day of the week.
5. A rough estimate of how you spent your time
    3 hours total but not all in one sitting. The first hour is spent understanding the problem, brainstorming solutions, as well as googling some of the needed python libraries. I had to understand the how the datetime library works, how the timezone are converted. 

    The code itself is not that difficult to write, so I spent the next 1 hour and a half writing it. Trying to keep it as simple as possible. Most of the time is actually me waiting for the code to finish running in order to see the output. I do recommend you to just run it on the test.json

    Last 30 minutes are spent writing this write up.

When I read your code, I'll be asking myself the following:

- Does this solve the business problem?
- Is this code efficient?
- Is this code understandable? 
- Did you use your time well?

If it makes sense, we'll organize a video call for our engineering team to ask you a few questions live and walk through the code together. 

Can't wait to see what you come up with! As always, if you have any feedback on this particular assignment, please let me know. 
