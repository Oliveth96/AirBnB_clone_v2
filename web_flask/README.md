<h1> 0x04. AirBnB clone - Web framework </h1>
<br>
<h4>Learning Objectives</h4>
<hr>
<p>At the end of this project, you are expected to be able to explain to anyone, without the help of Google</p>
<br>
<ul></ul>
<li>What is a Web Framework</li>
<li>How to build a web framework with Flask</li>
<li>How to define routes in Flask</li>
<li>What is a route</li>
<li>How to handle variables in a route</li>
<li>What is a template</li>
<li>How to create a HTML response in Flask by using a template</li>
<li>How to create a dynamic template (loops, conditions…)</li>
<li>How to display in HTML data from a MySQL database</li>
<br>

| TASKS | FILES | DESCRIPTION |
| ----- | ----- | ----------- |
| 0. Hello Flask! | <li>[0-hello_route.py](https://github.com/Oliveth96/AirBnB_clone_v2/web_flask/0-hello_route.py)</li><li>[__init__.py](https://github.com/Oliveth96/AirBnB_clone_v2/web_flask/__init__.py)</li> | <ul>Write a script that starts a Flask web application:</ul><li>Your web application must be listening on 0.0.0.0, port 5000</li><li>Routes: /: display “Hello HBNB!”</li> |
| 1. HBNB | [1-hbnb_route.py](https://github.com/Oliveth96/AirBnB_clone_v2/web_flask/1-hbnb_route.py)| <ul>Write a script that starts a Flask web application:</ul><li>Your web application must be listening on 0.0.0.0, port 5000</li><li>Routes: /: display “Hello HBNB!”</li><li>Routes: /hbnb: display “HBNB”</li> |
| 2. C is fun! | [2-c_route.py](https://github.com/Oliveth96/AirBnB_clone_v2/web_flask/2-c_route.py) | <ul>Write a script that starts a Flask web application:</ul><li>Your web application must be listening on 0.0.0.0, port 5000</li><li>Routes: /: display “Hello HBNB!”</li><li>Routes: /hbnb: display “HBNB”</li><li>/c/<text>: display “C ” followed by the value of the text variable (replace underscore _ symbols with a space )</li> |
| 3. Python is cool! | [3-python_route.py](https://github.com/Oliveth96/AirBnB_clone_v2/web_flask/3-python_route.py) | <ul>Write a script that starts a Flask web application:</ul><li>Your web application must be listening on 0.0.0.0, port 5000</li><li>Routes: /python/(<text>): display “Python ”, followed by the value of the text variable (replace underscore _ symbols with a space )</li> The default value of text is “is cool”|
| 4. Is it a number? | [4-number_route.py](https://github.com/Oliveth96/AirBnB_clone_v2/web_flask/4-number_route.py) | <ul>Write a script that starts a Flask web application:</ul><li>Your web application must be listening on 0.0.0.0, port 5000</li><li>Routes: /number/<n>: display “n is a number” only if n is an integer</li> |
| 5. Number template | <li>[5-number_template.py](https://github.com/Oliveth96/AirBnB_clone_v2/web_flask/5-number_template.py)</li><li>[templates/5-number.html](https://github.com/Oliveth96/AirBnB_clone_v2/web_flask/5-number_template.html)</li>| <ul>Write a script that starts a Flask web application:</ul><li>Your web application must be listening on 0.0.0.0, port 5000</li><li>Routes: /number_template/<n>: display a HTML page only if n is an integer</li> |
| 6. Odd or even? | <li>[6-number_odd_or_even.py](https://github.com/Oliveth96/AirBnB_clone_v2/web_flask/6-number_odd_or_even.py)</li><li>[templates/6-number_odd_or_even.html](https://github.com/Oliveth96/AirBnB_clone_v2/web_flask/templates/6-number_odd_or_even.html)</li>| Write a script that starts a Flask web application: <ul>Routes:</ul><li>/number_odd_or_even/<n>: display a HTML page only if n is an integer: H1 tag: “Number: n is even|odd” inside the tag BODY</li> |
| 7. Improve engines |<li>[file_storage.py](https://github.com/Oliveth96/AirBnB_clone_v2/models/engine/file_storage.py)</li><li>[db_storage.py](https://github.com/Oliveth96/AirBnB_clone_v2/models/engine/db_storage.py)</li><li>[state.py](https://github.com/Oliveth96/AirBnB_clone_v2/models/state.py)</li>| Before using Flask to display our HBNB data, you will need to update some part of our engine: <ul>Update FileStorage: (models/engine/file_storage.py)</ul><li>Add a public method def close(self):: call reload() method for deserializing the JSON file to objects</li><ul>Update DBStorage: (models/engine/db_storage.py)</ul><li>Add a public method def close(self):: call remove() method on the private session attribute (self.__session) tips or close() on the class Session</li><ul>Update State: (models/state.py) - If it’s not already present</ul><li>If your storage engine is not DBStorage, add a public getter method cities to return the list of City objects from storage linked to the current State</li> |
| 8. List of states | <li>[7-states_list.py](https://github.com/Oliveth96/AirBnB_clone_v2/web_flask/7-states_list.py)</li><li>[templates/7-states_list.html](https://github.com/Oliveth96/AirBnB_clone_v2/web_flask/templates/7-states_list.html)</li> | <p>After updating the Db, You must use storage for fetching data from the storage engine (FileStorage or DBStorage) => from models import storage and storage.all. Routes:</p> <li>/states_list: display a HTML page: (inside the tag BODY) </li><li>H1 tag: “States”</li><li>UL tag: with the list of all State objects present in DBStorage sorted by name (A->Z) tip</li><li>LI tag: description of one State</li> |
| 9. Cities by states |<li>[8-cities_by_states.py](https://github.com/Oliveth96/AirBnB_clone_v2/web_flask/8-cities_by_states.py)<li>[templates/8-cities_by_states.html](https://github.com/Oliveth96/AirBnB_clone_v2/web_flask/templates/8-cities_by_states.html)</li>|<p>In Addendum</p><li>To load all cities of a State: If your storage engine is DBStorage, you must use cities relationship</li><li>Otherwise, use the public getter method cities</li><li>LI tag: description of one city</li> |
| 10. States and State |<li>[9-states.py](https://github.com/Oliveth96/AirBnB_clone_v2/web_flask/9-states.py)</li><li>[templates/9-states.html](https://github.com/Oliveth96/AirBnB_clone_v2/web_flask/templates/9-states.html)</li>| <p>description of one State</p><li>Declare a method to handle @app.teardown_appcontext</li><li>Call in this method storage.close()</li><p>Routes:</p><li>/states/<id>: display a HTML page: (inside the tag BODY)</li><li>If a State object is found with this id</li><li>H1 tag: “States”, "Cities"</li><li>UL tag: with the list of all State objects present in DBStorage sorted by name (A->Z)</li><li>LI tag: description of one City</li><l>Otherwise: display h1 tag:"not found"</l>|
| 11. HBNB filters |<li>[templates/100-hbnb.html](https://github.com/Oliveth96/AirBnB_clone_v2/web_flask/templates/100-hbnb.html)</li><li>[](https://github.com/Oliveth96/AirBnB_clone_v2/web_flask/)</li><li>[100-hbnb.py](https://github.com/Oliveth96/AirBnB_clone_v2/web_flask/100-hbnb.py)</li><li>[web_flask/static/](https://github.com/Oliveth96/AirBnB_clone_v2/web_flask/static/)</li>| <span>Routes:</span><li>/hbnb_filters: display a HTML page like [6-index.html](https://github.com/Oliveth96/AirBnB_clone_v2/web_static/6-index.html)</li><li>State, City and Amenity objects must be loaded from DBStorage and sorted by name (A->Z)</li> |
<br>

AUTHOR
<hr>

[Oliveth Ndubuka](https://github.com/Oliveth96)