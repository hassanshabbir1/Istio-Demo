## Python apps for Istio Routing and deployments demo


<h5>
Python Dash application to show a Mock Medical service portal .this prtal let sign in a hard coded user  ‘Betty wells’  (user betty , password wells). This app 
displays home and scheduled pages. All contents except Provider name and rating/reviews are static/stub content. 
</h5>


### Steps to run this app locally :

<ul>Front end service </ul>

<li> Clone this repository. </li>
<li> Switch to the folder  </li>
<li> Write : pip install -r requirements.txt  </li>
<li> Then write : python front_end_app.py (The app will start running on port 3000) </li>


<ul>Provider service </ul>

<li> Switch to the provider_service branch or write :  git clone https://github.com/hassanshabbir1/Istio-Demo/tree/provider_service  </li>
<li> Then write : python app.py (The app will start running on port 6000) </li>


<ul>Rating service V1 </ul>

<li> Switch to the rating_v1 branch or write :  git clone https://github.com/hassanshabbir1/Istio-Demo/tree/rating_v1  </li>
<li> Then write : python app.py (The app will start running on port 6001) </li>



<ul>Rating service V2 </ul>

<li> Switch to the rating_v1 branch or write :  git clone https://github.com/hassanshabbir1/Istio-Demo/tree/rating_v2  </li>
<li> Then write : python app.py (The app will start running on port 6002) </li>




<ul>Rating service V3 </ul>

<li> Switch to the rating_v1 branch or write :  git clone https://github.com/hassanshabbir1/Istio-Demo/tree/rating_v3  </li>
<li> Then write : python app.py (The app will start running on port 6003) </li>


<h5> Now redirect to http://127.0.0.1:3000/ in browser </h5>






