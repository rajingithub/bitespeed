bitespeed assignment


API endpoint to hit:

(POST) http://127.0.0.1:8000/contacts/identify/   [ http://<host>:<port>/contacts/identify/]
with request body like :
{
"email":"george@hillvalley.edu",
"phoneNumber": "717171"
}

=== to run the project as Docker container===
<!-- to create the docker image -->
docker build -t bitespeed . 
<!-- to run the container frmo image -->
docker run bitespeed

== to run locally======
1. clone the repo
2. crate the virtual env and activate it and later install the requirement 
    a. python3 -m venv virtual
    b. source venv/bin/activate
    c. pip install -r requirements
3. make db migrations
    a. python manage.py makemigrations
    b. python manage.py migrate
4. then run the server
    python manage.py runserver
5. then hit the above give endpoint with the request body