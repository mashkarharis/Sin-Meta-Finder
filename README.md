# Sin-Meta-Finder
Metaphor Source Recommendation System For Sinhala Songs
## How To Run
1. Download and Install Elastic Search [link](https://www.elastic.co/downloads/elasticsearch)
2. Download and Install Kibana [link](https://www.elastic.co/downloads/kibana)
3. Install Plugin icu_analysis by running *bin\elasticsearch-plugin install analysis-icu*
4. Run *bin\elasticsearch.bat* to start Elastic Search
5. Run *bin\kibana.bat* to start Kibana
6. Make sure kibana running on [ http://localhost:5601](http://localhost:5601) 
7. Download this project
8. In project root folder create virtual environment by
    1. Run *python -m pip install virtualenv*
    2. Run *python -m venv env*
    3. Activate environment by running *env\Scripts\activate*
    4. Install requirements by running *python -m pip install -r requirements.txt*
    5. Verify installation by *python -m pip list*
9. Run *python initialize.py* to initialization
10. Run *python app.py* to start flask server
11. Now system is running
## How To Use
1. Go to [http://127.0.0.1:5000](http://127.0.0.1:5000), which is the home page of app




-> spell correction / auto complete
-> strip
-> special character removal
-> tokenization
-> stop word removal
-> boosting by keyword
    by artist
    by name
    meta target
    meta source
-> sorting by aluth, prasidhdha
-> limiting factors



find all songs
show


