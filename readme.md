## Python app for Istio Routing and deployments demo


<h5>
Python Dash application to show a Mock Medical service portal .this prtal let sign in a hard coded user  ‘Betty wells’  (user betty , password wells). This app 
displays home and scheduled pages. All contents except Provider name and rating/reviews are static/stub content. 
</h5>


### Steps to run this app locally :

<ul>Front end service </ul>


<li> docker pull hpcllc/front-end:latest  </li>
<li> docker run hpcllc/front-end:latest </li>
<li> (The app will start running on localhost port 3000) </li>
 
<br><br><br>



<ul>Provider service </ul>

<li> docker pull hpcllc/provider-service:latest  </li>
<li> docker run hpcllc/provider-service:latest </li>
<li> (The app will start running on localhost port 6000) </li>
 
<br><br><br>



<ul>Rating service V1 </ul>

<li> docker pull hpcllc/rating-v1:latest  </li>
<li> docker run hpcllc/rating-v1:latest </li>
<li> (The app will start running on localhost port 6001) </li>
 
<br><br><br>

<ul>Rating service V2 </ul>

<li> docker pull hpcllc/rating-v2:latest  </li>
<li> docker run hpcllc/rating-v2:latest </li>
<li> (The app will start running on localhost port 6002) </li>
 


<br><br><br>

<ul>Rating service V3 </ul>



<li> docker pull hpcllc/rating-v3:latest  </li>
<li> docker run hpcllc/rating-v3:latest </li>
<li> (The app will start running on localhost port 6003) </li>
 
 
<br><br><br>

<h5> Now redirect to http://0.0.0.0:3000/ in browser </h5>






