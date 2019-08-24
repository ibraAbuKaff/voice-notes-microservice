### Assumptions
A - Voice note should be short, and compressed(gzip) before it got sent to the server to make the uploading much faster.


B-  the scenario of listening to voice note will be as follows:
	
	1- User gets push notification about new update from pilot.
	
	2- Once the notification gets opened, there will be a long polling request against (receive endpoint), which will send list of voice notes in the response.
	
	3- Once the user clicks on one of the voice note, there will be a listen request to load that specific voice note , so the customer can listen to it.
	
==========

### Technology, Language and Framework choice :
   - **Python language with Flask framework** as it's is very suitable for building microservices with less  dependencies to external libraries. <br/>   
       -   The documentation and developer tools are excellent
       -   The Flask "core" is simple, but there are a large number of extensions which integrate with it very well
       -   Flask is actively maintained and developed
       -   It's based on Python, which is an excellent programming language for rapid high-level application development that offers useful libraries for many other things.

   - **For caching,  I used Redis** as it has the Persistence which allows you to treat **Redis** as a legitimate database rather than an unstable and temporary cache
   
   - **For Storing the physical voice note files , I used AWS S3**, as it's fully scalable, fast and reliable service provided by Amazon.
   
   - **Docker and docker-compose** to containerize the project

==========
   
### Service Architecture :
<a href="https://ibb.co/JzC9TbD"><img src="https://i.ibb.co/hKCSNn3/Screen-Shot-2019-08-24-at-9-43-38-AM.png" alt="Screen-Shot-2019-08-24-at-9-43-38-AM" border="0"></a>

We have the voice note component which does not implement everything in it. 
It delegates the work to other 3 sub-components (reference components), called Upload(exposing only `upload`  interface) , Listen (exposing only `listen` interface), and Receive (exposing `receive` interface)

By this way, any change we need to do in future, will not affect the other component business.

In the end the voice note component will expose/promote the service to the outside world to be used. 

==========

### Database & Data Store Technology and Architecture:
<a href="https://ibb.co/3YLbcSF"><img src="https://i.ibb.co/JFMTHrp/Screen-Shot-2019-08-24-at-9-54-10-AM.png" alt="Screen-Shot-2019-08-24-at-9-54-10-AM" border="0"></a>


==========

### Microservice explanation (Quick Developer On-boarding):

We have 3 main endpoints for the voice note microservice:

1- **Upload** , so when the pilot uploads the voice note, at the server side there are some steps to be achieved for the  intended functionality
 
 **voice note will be checked for its size in MB**
 
 **voice note will be uploaded to S3, then we generate a key to store a reference to it in MongoDb,**
  
 **last, the key will be stored in Redis cache(for a faster retrieval later on)**

2- **Receive**, so when the customer wants to browse all available voice notes which are sent from the pilot , the following things will happen in the server side for the retrieval:

**we search for the voice note keys(which are related to that specific pilot id) in Redis cache.**

**if Redis is out of service or it's broken , we load the voice note references(keys) from mongodb.**

**then we send the list of voice note keys as a response to the client side, so the user can list all available voice notes**


3- **Listen**, so when the customer clicks on one of the voice note, the client side sends a request to the server side to get/download that specific voice note.
at the server side:
 
**In the request data, we expect the pilot id, and voice note key, so we check if the voice note  already stored in our database for that specific pilot id, then we generate S3 downloadable link , then we send it back to the client side.**
 

### How to start MicroService docker containers.

Go to the root folder of this project and run 

1- ```docker-compose up --build```

2- Go to ```http://localhost:5000```  >> you should get a message "Voice note micro-service"", then you are all set!


==========

### HOW TO RUN API DOCS SERVER

- change directory to `api-docs-server`
- run the following:
    -   `docker build -t swagger_server .`
    -   `docker run -p 8080:8080 swagger_server`
    - Go to `http://localhost:8080/api/v1/ui/#!/default/get_retrive_voice_notes_for_specific_pilot`





