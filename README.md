# My Weather Forecast Web Application
My Weather is a Django-based web application that provides a 4-day weather forecast for any given city. The application fetches real-time weather data and displays it in a user-friendly format. Additionally, it showcases an image of the city queried to enhance the user experience.

## Features
- Real-time 4-day weather forecast.
- Dynamic city images based on the queried location.
- Simple and user-friendly interface.

## Tech Stack and Tools
- **Web Framework**: Django
- **IDE**: PyCharm
- **Languages**: Python, HTML
- **APIs**: WeatherAPI, Unsplash

## Examples of the Final Product
![image](https://github.com/cvoutselas/Weather-Forecast-App/assets/130950618/6e45d405-7d48-4e19-8559-88217509cdbe)
![image](https://github.com/cvoutselas/Weather-Forecast-App/assets/130950618/1e9e1ad2-5389-4ebc-9b4c-f53ef2522e4f)
![image](https://github.com/cvoutselas/Weather-Forecast-App/assets/130950618/1f02d582-53a2-402d-8210-fa5da4cf1fc8)


## Getting Started
### Prerequisites
- Python (version 3.10 or higher recommended).
- PyCharm (Not needed but recommended).
- Django (latest version recommended).
- An API key for WeatherAPI.
- An API key for Unsplash.

## Installation & Setup
1. Clone the repository:

git clone https://github.com/cvoutselas/Weather-Forecast-App

2. Navigate to the project directory:

cd myweather

3. Install required packages:

pip install -r requirements.txt

4. Set up your API keys:

- Create a file named weather_key.py inside the forecast directory.
- Inside this file, add the following lines:

weather_api_key = '*YOUR WEATHER API KEY*'

unsplash_api_key = '*YOUR UNSPLASH API KEY*'

5. Set up the database:

Since the db.sqlite3 file isn't provided in the repository, you'll need to set up the database yourself.

- Run migrations:

python manage.py migrate

6. Start the development server:


python manage.py runserver

7. Visit http://127.0.0.1:8000/ in your web browser to access the application.

## Notes for Missing Files
- **Database (db.sqlite3):** The database file is not included in the repository. You'll need to set up your own database using Django's migrations.
- **API Key file (weather_key.py):** This file contains the API keys for both WeatherAPI and Unsplash. You need to set up your own keys as instructed in the setup section.
- **.pyc files:** These are compiled Python files and are generated automatically when the project is run. They are not necessary for the functioning of the application and are therefore excluded.
- **IDE-specific files:** Files related to specific IDE settings (like those for PyCharm or VSCode) are excluded. If you're using an IDE, you might need to configure some settings again.

## Contributing
If you'd like to contribute, please fork the repository and make changes as you'd like. Pull requests are warmly welcome.

## License
This project is open-sourced and is available under the MIT License.
