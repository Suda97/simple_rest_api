# Simple REST API 
This application is a simple REST API made in Django.<br>
It's using HTTP methods to do various operations in database.<br>
To run it You have to install Django 4.0 and "requests" library.<br>
<b>App Name: Vehicle</b>
<h3>POST /cars</h3>
It will check if given model exists in external database https://vpic.nhtsa.dot.gov/api/ . <br>
<b>If exists:</b> The given model and maker will be saved in local database. <br>
<b>Else:</b> It will return an error (404). <br>
<b>Example:</b><br>
curl -X POST -H "Content-Type: application/json" -d '{"make":"Honda", "model":"del Sol"}' http://127.0.0.1:8000/vehicle/cars
<b>Heroku:</b><br>
curl -X POST -H "Content-Type: application/json" -d '{"make":"Honda", "model":"del Sol"}' https://simple-rest-api.herokuapp.com/vehicle/cars

<h3>DELETE /cars/{ id }/</h3>
It will check if vehicle with a given id exists in local database.<br>
<b>If exists:</b> Vehicle with a given id will be delete from database.<br>
<b>Else:</b> It will return an error (404).<br>
<b>Example:</b><br>
curl -X DELETE http://127.0.0.1:8000/vehicle/delete/15/
<b>Heroku:</b><br>
curl -X DELETE https://simple-rest-api.herokuapp.com/delete/15/


<h3>POST /rate</h3>
It will check if vehicle with a given id exists in local database.<br>
<b>If exists:</b> Number of rates will be incremented by one and average rating will be recalculated for new value.  <br>
<b>Else:</b> It will return an error (404).<br>
<b>Example:</b><br>
curl -X POST -H "Content-Type: application/json" -d '{"car_id":10, "rating":2}' http://127.0.0.1:8000/vehicle/rate
<b>Heroku:</b><br>
curl -X POST -H "Content-Type: application/json" -d '{"car_id":10, "rating":2}' https://simple-rest-api.herokuapp.com/vehicle/rate

<h3>GET /cars</h3>
It will return list of all cars from local database<br>
<b>Example:</b><br>
curl -X GET http://127.0.0.1:8000/vehicle/cars
<b>Heroku:</b><br>
curl -X GET https://simple-rest-api.herokuapp.com/vehicle/cars

<h3>GET /popular</h3>
It will return list of all cars from local database ordered by number of rates in descending order<br>
<b>Example:</b><br>
curl -X GET http://127.0.0.1:8000/vehicle/popular
<b>Heroku:</b><br>
curl -X GET https://simple-rest-api.herokuapp.com/vehicle/popular