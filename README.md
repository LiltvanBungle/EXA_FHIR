# FAO EXA:

My main experience has been with MySQL so my thought process was first to investigate the FHIR format and see what the structure was and explore the data with the intention to create an SQL schema for it. Very quickly I realised that an SQL schema would become very complicated, very quickly and would not only take longer than I had available to create, but it would not be very fast or effective if scaled. I knew about mongodb and what a document database was but I had not previously created a mongodb database and used it so I began to teach myself how to set it up. 

Upon success with Mongo I set about writing the script which I was confident I could do: create a list of filenames and iterate over them, validating then inserting into the database, this went mostly without a hitch save for one patient who had a ~ above the 'n' in his name which led me to research encoding, once set to 'utf-8' I was getting all files validated in my little test 'print' statement which I used at each stage to ensure that things were doing what they were told!

In my local environment I was then able to add each json file to the mongodb database, which then allowed me to use the MongoDB Compass app to filter the data as I pleased. Success!

However, I have not used Docker before and so had to research and understand it before I could try to containerize my little app, I came some of the way towards managing it before running out of time. Currently the app runs but it errors because I could not get mongodb to run in the container, further research suggests I should have mongo in a different container and make calls to it. I hope that you are either able to correct my error or that the github repo works in your environment, if not I'm happy to screen share running the app from my end however less impressive that might be.

Thank you for the opportunity to complete this task, I have enjoyed it and learned from it, I hope that my lack of docker success does not affect my application too much as I am incredibly keen on this position as it's exactly the kind of role I've been hoping to find.

Ramble over, 

Glen
