
# Step - 1
## Database setup (postgres)
CREATE DATABASE warehouse;
CREATE ROLE warehouse WITH  PASSWORD "bird";

GRANT ALL PRIVILEGES ON DATABASE "warehouse" to warehouse;

# Step - 2 
## create needed tables and indexes
### go to root folder of a project and run
python models.py

# Step -3 
## Host the Service
### go to root folder of a project and run
python api.py

Use postman for verifying endpoints
get it from https://www.getpostman.com/apps
