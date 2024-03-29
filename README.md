﻿# SearchEngineIR
 ## _Search Engine for the metaphors of the Tamil Songs_
 
 ## Setup the SearchEngine4TamilSongs
 
 - [Installation and SetUp of ElasticSearch](https://www.elastic.co/guide/en/elasticsearch/reference/current/install-elasticsearch.html)
 - [Installation and SetUp of Kibana](https://www.elastic.co/guide/en/kibana/current/install.html)
 - Setup the Environment 
 
 ## Setup the Environment 
 
 - Clone the repository 
 - Navigate to the Directory (../SearchEngine4TamilSongs/)
 - Creating the [python virtual environment](https://docs.python.org/3/library/venv.html)
  ```sh
python -m venv myenv
```
  - Activate the [virtual environment](https://docs.python.org/3/library/venv.html#how-venvs-work)
  - Replace your key and username credential in the `searchquery.py` 
  - Change the `app.py` and `results.html` according to your corpus 
  - Run the app
  ```sh
flask --app app --debug run
```
  - Navigate to ```http://127.0.0.1:5000/search```
 
 ## Search 
 
  - Choose: `"இசையமைப்பாளர்" **(OR/AND)** "பாடலாசிரியர்" **(OR/AND)** "நாயகன்" **(OR/AND)** "START YR - END YR` and to get the results for your preference select the `வரிசைப்படுத்தப்பட்ட தரவுகளுக்கு` Option and Search 
  - Provide any word that you want to search and select the `முழுமையான தேடலுக்கு` option to get the basic search results for your word
  - Provide any word that you want to search and select the `சந்தங்களை அறிய` option to get the rhyming words for the respective input 
