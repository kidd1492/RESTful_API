# Flask RESTful API

## Introduction
This repository contains a simple example of a Flask RESTful API that provides information about national parks and campsites. It’s designed to serve as both a web application and an API endpoint that returns JSON data. This is one part of a project that I am working on in order to understand how it all works. The project is outlined at https://cwwright1229.wordpress.com/2024/06/06/restful-api-http-server/.

I think I will add another blueprint to handle the API and use the auth.py file to handle the HTML side. I created a login I need to create a function  to issue the API key. https://cwwright1229.wordpress.com/2024/06/06/restful-api-development/

## Project Structure
- `instance/`
  - `database.db`: The SQLite database file.
- `app.py`: The main Flask application file.
- `park_api/`
  - `__init__.py`: Initializes the Flask app and the SQLAlchemy database.
  - `auth.py`: Defines routes for the web interface and the API.
  - `models.py`: Contains the SQLAlchemy models for Parks and Camps.
  - `templates/`: Holds HTML templates for rendering web pages.
  - `static/`: Holds css, javascript, images/.
  - `helper.py` : helper functions 

## Features

- Get a list of all parks
- Get details about a specific park
- Get a list of all campgrounds
- Get details about a specific campground
- Filter campgrounds by state

## Usage
- Access the web interface at the root URL: `http://localhost:5000/`

## Future Enhancements
- Implementing API key authentication to secure the API endpoints.
- Adding more API endpoints to provide additional functionality.

## Learning Journey
As a self-taught developer exploring RESTful APIs, this project serves as a practical application of my learning. I'm currently enhancing my understanding of API security and how to effectively manage user authentication. As well as api design and creation. I am still leaning what is invaoled in the design, creation of api what differnt api type are avalible.

## Contributing
Contributions are welcome! If you have suggestions or improvements, please feel free to fork the repository and submit a pull request.

## License
This project is open-sourced under the MIT License.

