# Sin-Meta-Finder
Metaphor Source Recommendation System For Sinhala Songs
## How To Run
1. Download and Install Elastic Search [link](https://www.elastic.co/downloads/elasticsearch)
2. Download and Install Kibana [link](https://www.elastic.co/downloads/kibana)
3. Install Plugin icu_analysis by running *bin\elasticsearch-plugin install analysis-icu*
4. Run *bin\elasticsearch.bat* to start Elastic Search
5. Run *bin\kibana.bat* to start Kibana
6. Make sure kibana running on [ http://localhost:5601](http://localhost:5601) 
6. Download this project
7. In project root folder create virtual environment by
    1. Run *python -m pip install virtualenv*
    2. Run *python -m venv env*
    3. Activate environment by running *env\Scripts\activate*
    4. Install requirements by running *python -m pip install -r requirements.txt*
    5. Verify installation by *python -m pip list*
8. Run *python initialize.py* to initialization