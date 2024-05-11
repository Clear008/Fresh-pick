# Architecture
##### *The end-to-end map for the data flowing through your system*

#### Diagram 1: Accessing Data in the Cloud
*This diagram showcases how a user retrieves data stored in the cloud.*
<img src="https://i.imgur.com/hnDrevg.png"/>

- User Request: The process starts with a user requesting a file on a website.
- DNS Lookup: The user's device contacts a DNS server to translate the website address into an IP address, locating the server that stores the data.
- Load Balancer: The DNS server directs the request to a load balancer, distributing traffic among web servers.
- Web Server: The load balancer forwards the request to a web server. This server retrieves the requested data from cloud storage.
- Content Delivery Network (CDN): (Optional) The data might be delivered through a CDN, a network of servers storing cached content closer to the user for faster loading.
- Delivery: Finally, the requested data is delivered back to the user's device.

<hr>

#### Diagram 2: Uploading and Storing Data in the Cloud
*This diagram illustrates how data is uploaded and stored in the cloud.*
<img src="https://i.imgur.com/yEDZctC.png"/>

- User Upload: The user uploads data through a web client or app.
- Store: The data is then stored in the cloud storage, visualized as a giant storage device.
- Database: A database might also be used to store information about the data, such as file names and locations within the cloud storage.
