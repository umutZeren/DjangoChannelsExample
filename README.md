# DjangoChannelsExample
Self Notes and Documentation
It is template for a Django project with channels,live data streaming and graphing with chart.js
Django Realtime  
-Only good alternative is Django-channels  
o	Django only works at http normally  
o	Will use Websockets and IoT protocols  
o	ASGI  specification  
o	Integration with Django auth is easy ,  
o	-Groups and scopes for consumer should subscript to channel.  
o	-print(self.scope )at consumer.py will show the necessary data about scope for debug.  
o	-redis channel layer is an option CHECK_LATER  
o	-default channel layer for now.  
•	-For sendMockData.py  if not in current env pip install websocket-client  	
•	-consumer.py need as_asgı() now updateded library  
•	Simulation of the data stream django  
o	Run server with python manage.py runserver  
o	For subscriping to socket python -m websockets ws://localhost:8000/ws/polData (ws/polData part is written in Django routing.py change accordingly )  
o	After subscription run python sendMockData.py  
o	Inspect changing graphs at http://127.0.0.1:8000/   

-Realtime data charts available.  
	-implement an basic demo  
	-If success look for auth and chart library performance tests.  
