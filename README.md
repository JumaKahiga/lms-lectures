# lms-lectures

[![Build Status](https://travis-ci.com/JumaKahiga/lms-lectures.svg?token=WppzFusXpymh1phyCxmF&branch=ch-setup-CI-CD-169231552)](https://travis-ci.com/JumaKahiga/lms-lectures)

## How to install locally
1. Create a local folder and then navigate inside it.
2. Open a terminal in this location and then initialize git using `git init`
3. Clone the online repository using the following command `git clone https://github.com/JumaKahiga/lms-lectures.git`
4. Create a virtual environment using the following command `python3 -m venv lms_env`
5. Activate the virtual environment using `source lms_env/bin/activate`
6. Navigate inside the project using `cd lms-lectures` and then install required modules using `pip install -r requirements.txt`
7. Create a `.env` file following the format outlined in the `env_example` file.
8. Install Docker using the packages and instructions provided [here](https://docs.docker.com/v17.09/engine/installation/)
9. Build the app's Docker containers using `make install` and then run it using `docker-compose up`. If successful, you will see API server running on your terminal. Please note that this build automatically loads seed data into the database. 
10. On Postman, Insomnia, or your preferred API client, visit the endpoints listed below.

## Endpoints
A. Index page. Exposes a random lecture at every instance `http://0.0.0.0:5000/`
B. All lectures. Fetches all lectures based on pagination params provided `http://0.0.0.0:5000/lectures/<start_page>/<items_per_page>`
C. To ten lectures. Fetches highest rated lectures `http://0.0.0.0:5000/lectures/top-10`
D. Filter lectures. Currently, filters lectures based on provided author name. `http://0.0.0.0:5000/lectures/filter/<author_name>`

