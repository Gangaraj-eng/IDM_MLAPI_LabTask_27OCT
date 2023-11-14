# <p align='center'>IT496 - Introduction to Data Mining</p>
### <p align='center'>ICC Cricket World Cup 2023 ML Challange</p>
**Course Project**: 3 <br/>
**Lab Group**: T06<br />
##### Table of Contents  
[1.Project Overview](#project-overview) <br/>
[2.Web Application](#web-application) <br/>
[3.Dataset scraping](#dataset-scraping) <br/>
[4.Tasks and Implementation](#tasks-and-implementation) <br/>
[5.Results and Conclusion](#results-and-conclusion) <br/>
## <p align='center'>Project Overview</p>
In this project we have worked on the ICC Cricket World Cup 2023 prediction, which involves building and deploying machine learning models to make informative predictions related to the tournament. As a part of it, we have did the following tasks<br/>
**Task 1**:
* decid the task
* decide the taks

**Task 2**:
*  Predicting the Finalist Teams and Players
  
**Task 3**:
* Predicting the winner of ICC World cup 2023
## <p align='center'>Web Application</p>
This application demonstrates the Match winner prediction model that was built as a part of this project.<br/>
To run this Application follow these steps:
### 1. Clone the repository and navigate to project folder:
```bash
git clone https://github.com/Gangaraj-eng/IT496_CP3_T06
cd .\IT496_CP3_T06
```

### 2. Install the required packages:
```bash
pip install -r requirements.txt
```
In case if there are any version issues, please install these packages manually - Flask, Numpy, Pandas, tensorFlow, scikit-learn
### 3. Navigate to the App folder and run server.py file
```
cd .\App
python server.py
```
The application will be accessible at http://127.0.0.1:8000/

### 4. Make predictions by giving inputs
* Select the two playing teams and Venue
* Click on the predict button
* Predict results for winner and the respective team composition prediction(playing 11) of each team will be displayed<br/>

![image](https://github.com/Gangaraj-eng/IDM_MLAPI_LabTask_27OCT/assets/77287821/3fa8c772-781b-47d9-861c-2297ab8b4e2b)
## <p align='center'>Dataset Scraping</p>
To carry out proper predictions, comprehensive and reliable data is essential. We have collected the data related to the past cricket matches, team performance and players statistics from various websites.The collected dataset files can be found [here](https://github.com/Gangaraj-eng/IT496_CP3_T06/tree/main/Dataset). These dataset includes the following files
1. ICC_Player_Stats.csv - Individual player statistics in ODI’s
2. ICC_Matches_Stats.csv - Data related to all the matches played in ICC world cup for the last 7 seasons from 1999, 2003, 2007, 2011, 2015, 2019, 2023
3. ODI_Matches.csv - Data related to all the ODI Matches from 2017-2023
4. ICC_Team_Stats.csv - Team wise statistics which includes data like ODI ranking of the team, number of matches played by team and some average statistics of team players.
5. Matches_Stats.csv - combined matches data of ICC world cup and ODI data collected.
6. ICC_TeamComposition.csv - Composition of batter, bowlers and all rounders of the team for the ICC world cup 2023
7. ICC_Venues_List.csv - List of all the venues used for ICC and ODI Matches
8. ICC 2023 Kaggle: Data of ICC 2023 collected from kaggle
    * deliveries.csv - ball wise data for each match
    * matches.csv  - matches wise teams and winners data
    * points_table.csv - data related to points table

**Individual player statistics in ODI**
The individual statistics of each player of all time from the day of debut till date were scraped. The data includes attributes like matches played, runs scored, batting average, not-outs, boundaries scored, and centuries and half-centuries.The players participating in the current World Cup are only included in the team.Only the team of 15 players declared before the World Cup are included.<br/>
Source: [ESPN cricketing website](https://www.espncricinfo.com/records/most-runs-in-career-83548) <br/>
![image](https://github.com/Gangaraj-eng/IDM_MLAPI_LabTask_27OCT/assets/77287821/2e471e7a-b97d-4711-991f-62904fc12fe3)
<br/>

**Head to Head statistics of each country in ODI**
The head-to-head data of each match played in the past 8 years in the ODI is collected in this sheet. The attributes present in it are the names of two teams in that particular match, the venue, the margin of victory, and the winner.<br/>
Source: [ESPN cricketing website](https://www.espncricinfo.com/records/year/team-match-results/2016-2016/one-day-internationals-2)<br/>

![image](https://github.com/Gangaraj-eng/IDM_MLAPI_LabTask_27OCT/assets/77287821/ac1c7870-3d6a-4f38-b78a-9c062aee7e6a)



**Head to Head statistics of each team in the past World Cups**
This is very similar to the above dataset, but the only difference here is that the matches held during the past World Cups are included, example:1999,2003,2007.This data is scraped from the cricbuzz website using python with BeautifulSoap.The code used for scrapping can be found in this [file](https://github.com/Gangaraj-eng/IT496_CP3_T06/blob/main/Models/DataPreparation.ipynb)<br/>
Source: [Cricbuzz](https://www.cricbuzz.com/cricket-series/2810/indian-premier-league-2019/matches)<br/>

**Team Composition**
The Dataset contains a number of Batsmen, Bowlers and All-Rounders for each team given the match venue.
Source: EPSN cricketing website<br/>

![image](https://github.com/Gangaraj-eng/IDM_MLAPI_LabTask_27OCT/assets/77287821/54e592be-0698-4d36-8624-b7c5882afaec) <br/>




## <p align='center'>Tasks and Implementation</p>
## <p align='center'>Results and Conclusion</p>

**Contributions**:
| Name | ID | Contribution|
| --- | --- | ---|
| Saineni Rohit Rao | 202001003 | Attribute summary: 18-34 <br/> Data Preprocessing <br/> Documentation | 
| Rohan Reddy Patlolla | 202001076 | Attribute summary: 52-68 <br/> Exploratory data analysis <br/> Train test splitting and model defining |
| Nipun Shah | 202001096 | Attribute summary: 35-51 <br/> Data Preprocessing <br/> Documentation |
| Gangaraju Bopparam | 202001107 | Attribute summary: 1-17 <br/> Training, Hyperparameter tuning <br/> and Evaluation |
| Rishit Shah | 202001411 | Attribute summary: 68-87 <br/> Exploratory Data Analysis <br/> Documentation |
