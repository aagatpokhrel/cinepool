
# Cinepool

Web application that uses search analytics on current movies/shows.





## Introduction
Everyday new movies and shows are being released, which can be hectic process for movie people to find and search according to their needs. Cinepool is a system where users can find new movies/shows according to their description and taste.



## Features

- Easy to use web application UI
- Automated & user defined scheduled pipeline
- Complex search analytics


## Tech Stack

**Client:** React, VanillaCSS

**Server:** Flask

**Database:** Mongo DB (Atlas for cloud host)

**Pipeline:** Python

**Language Model:** BERT (bert-base-nli)


##  Structure

Overall project structure

    .
    ├── frontend     
    |   ├──public/
    |   ├──package.json  #Contains modules to be installed
    |   └──src/          #Our main code lies here
    |       ├── index.js    #no need to touch this
    |       ├── index.css   #no need to touch this
    |       ├── App.css 
    |       └── App.js      #code here for all UI
    ├── backend      
    |   ├── main.py      #Starting point of backend
    |   ├── requirements.txt #All the modules to be installed
    |   └── app/
    |       ├── __init__.py #Initialization of flask app
    |       ├── routes.py   #Routes for apis (api reference below)
    |       └── search.py   # main functionality for search analytics
    ├── pipeline   
    |   ├── main.py     #Starting point of piepline execution
    |   ├── requirements.txt
    |   └── core/
    |       ├── __init__.py #Initialization 
    |       ├── extract.py  #crawling and extracting data
    |       ├── transform.py    #transformation of data (LLMs are employed)
    |       └── load.py     #load data to mongodb 
    ├── automate.py     #automation script for pipeline
    └── README.md
## Installation

Clone the project

```bash
  git clone https://github.com/aagatpokhrel/cinepool.git
```

Go to the project directory

```bash
  cd cinepool
```

For backend dependencies

```bash
  cd backend
  pip install -r requirements.txt
```

For frontend dependencies
```bash
  cd frontend
  npm install
```

For pipeline dependencies
```bash
  cd pipeline
  pip install -r requirements.txt
```


    
## How to Use

First set the automation according to needs in `automate.py`
```python
def create_task_scheduler_job():
    # Change the script to include your time here. Right now it runs the script at 3:00 am every day
    start_date = datetime.now() + timedelta(days=1)
    start_time = time(hour=3, minute=0)

    # Build the task scheduler command
    path_to_script = os.path.join(os.getcwd(),"/pipeline/main.py")
    task_command = "python {}".format(path_to_script)
    task_name = "My Script"
    # Create the task scheduler job
    subprocess.run(["schtasks.exe", "/Create", "/TN", task_name, "/TR", task_command,"/SC", "Daily", "/ST", start_time.strftime('%H:%M'), "/SD", start_date.strftime('%m/%d/%Y'), "/F"])
```
Then run the command for the first time.
```bash
python automate.py
```

After this the job is scheduled according to the time you mention.
Now to run the frontend and backend. We do the following

For running backend
```bash
cd backend
python main.py
```

For running frontend
```bash
cd frontend
npm start
```
## Implementation Details

#### Pipeline Implementation

Firstly the pipeline was implemented (crawl for extraction and loading into the database). For this tasks we perform three crucial tasks i.e, extract, transform and load. The task is broken into:

*  **Extract :**
    - First we crawl through imdb sites using beatifulsoup library. 
    - After that we find relevant details such as date and title href (title href gives movie/show links)
    - For each title href we find in the page, we crawl to find out information such as genres and plot.
    - We only take the information details of the information date that matches current date (today). Because the task has to run every time. So we only take only today's date's movies/shows

* **Trasform :** 
    - After extraction, the data is in the form of movie_dictionary and show_dictionary. So we need to combine the two.
    - We first transform the sentences in plot to 1 or 2 sentences max to avoid space issues.
    - We then employ our language model to convert the plot into embedding list, which would be required later on during search analytics.
    - After all this, the data is transformed and merged to form a list of dictionaries.

* **Load :** 
    - To load into database, we first setup the mongodb. Good practice is to store user credentials and uri for client in `.env` file inside pipeline.
    - We load the today's data into the collection
    - We then delete the data that is stale (i.e, data longer than 7days time) so that we only keep new shows/movies in our database

#### Backend Implementation
Flask is used in Backend to create backend app. We fetch the data from the mongodb and then perform search analytics using large language models. We compare the search description sent from the user to the description from each data entries. (remember we stored embeddings to make our life easier for faster access). API Reference will be mentioned in the section below.

#### Frontend Implementation
React is used for frontend. Contains a simple UI that sends axios post request to the backend service and retrieves relevant results.

## How Analytics Works

The language model (LM) is first used to transform the plot description into embedding list. Then the user's search description is also transformed into embedding list. Then we use cosine similarity to find the similarity between the two embedding lists. The higher the similarity, the more relevant the movie/show is to the user's search description. We then sort the results according to the similarity score and return the top 10 results.

## API Reference

#### Test the backend

```http
  GET /
```

#### Get all movies in DB

```http
  GET /get_movies
```

#### Search

```http
  POST /search
```

| Parameter | Type     | Description                       |
| :-------- | :------- | :-------------------------------- |
| `description`      | `string` | **Optional**. Plot description that you want to search |
| `type` | `boolean` | **Optional**. Either movies(0) or shows(1)  |
| `genres` |	`string` |	**Optional**. What genre of movies
| `date` |	`string` |	**Optional**. Search according to date released |



## Environment Variables

To run this project, you will need to add the following environment variables to your .env file in pipeline and in backend

`MONGO_USERNAME`

`MONGO_PASSWORD`


## Screenshots

![Screenshot]()

