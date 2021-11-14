# pygame 

Algorithmic automated trading bot is implemented using python and mongodb with real time data analytics on Grafana to see the stock signals
Near real-time news feed from various sources is stored in the mongodb for faster access to find key positive signals

Highlights : 
1) Various market cap based strategies can be chosen as switches in the input to the program and is highly customizable with extensibility as the key factor in design
2) TDAmeritrade api's serve as the core price collector services
3) Rate of change in volume and Rate of change in price are the key strategies for ABCD and C point based implementations
4) Supports both simulation and live (realtime) account automated trading successfully tested over several months in realtime
5)  Several JSON key's are provided to control the customizability
6)  Millions of rows updated and retrieved through mongodb through a highly scalable plugin


Sample output screenshots : 

![image](https://user-images.githubusercontent.com/19297791/141664633-3e9cd720-8d29-4b6f-ac3f-da5afa79b6ca.png)

Grafana sample output : 

![image](https://user-images.githubusercontent.com/19297791/141664732-29aa5c0b-d8a4-47ac-b90b-ef3ca40cfacb.png)


Future consideration : 

Space based architecture 
