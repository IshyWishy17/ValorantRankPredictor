# ValorantRankPredictor

VALORANT Rank predictor! VALORANT is a game that I enjoy and I’ve always wanted to do a project where I build a rank predictor (based on certain factors of your gameplay). The game offers a competitive mode where you compete for a rank (ELO-based system). Here are the ranks along with their distribution of players -

Source: Valorant Leaderboard - North America Competitive Ranked Rating for Episode 9 - Act 2

Here is what a typical player profile looks like (showing mine as reference) -

I basically want to be able to predict a player’s rank, given their stats as shown above. The stats include damage/round, K/D ratio, Headshot %, Win %, ACS, DD/Round, KAST, etc (I haven’t really decided which stats I will use yet). It’s important to know that people of higher ranks could have somewhat similar stats as people with lower ranks - (Ascendant > Platinum)

It isn’t obvious what stats have a higher weight in determining a player’s rank and what stats don’t matter as much, the correlation isn’t clear at all. I want to build a DL model to figure this out. But gathering the data isn’t so easy. I’m going to have to scrape every single player’s data from their respective tracker page, until I have enough data (ex - https://tracker.gg/valorant/profile/riot/IshyWishy17%237495/overview). The page URL format is https://tracker.gg/valorant/profile/riot/<username>/overview. Unfortunately getting a list of usernames isn’t easy at all, especially for players of lower ranks (of course it isn’t). Here is a list of the top-rank players (Radiant rank), whose usernames and respective pages can be found easily -

Source-Valorant Leaderboard - North America Competitive Ranked Rating for Episode 9 - Act 2

So how do I gather data on noob players like myself? Well, I make use of the fact that the matchmaking system pits players of similar ranks against each other! Here is a report of a single match -

You can clearly see that all the players' ranks are in the Platinum 3 - Diamond 2 range. So I just need to pick one seed player from every rank, and effectively carry out a Breadth-first search to find other players in the same rank! I can do so by pulling up the match history of every player and then I’ll eventually have enough players of each rank to add to my dataset.

After scraping all the data and creating the dataset comes training the model, and deciding which features to use, the details of which will be decided soon! I will also do an analysis / breakdown of the average of each stat per rank, etc. as a way of visualisation. This will give a holistic view of what stats matter. So the project will include collecting all the data via scraping (no API to provide us with the results directly unfortuantely), the rank predictor plus basic visualization graphs stat-rank wise. A nice collection of insights will be presented.

# Execution Plan

Sure! Here’s a concise summary for each week:

Week 1: Research and Data Collection Planning
Research relevant player stats for rank prediction and devise a scraping strategy to collect data from player profiles and match histories.

Week 2: Data Scraping
Implement a web scraping tool to gather data from top-ranked players and use a breadth-first search to collect stats from players in similar ranks.

Week 3: Data Cleaning and Preparation
Clean the gathered dataset to handle missing values and duplicates, then conduct exploratory data analysis to understand feature distributions and correlations with rank.

Week 4: Model Development
Split the dataset for training and testing, train various machine learning models, and evaluate their performance to identify the best rank prediction approach.

Week 5: Visualization and Reporting
Create visualizations to summarize insights from the data and model performance, then compile a report detailing your methodology and findings.
