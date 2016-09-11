#include <dht.h>
#define dht_apin A0 // Analog Pin sensor is connected to
 
dht DHT;
int led = 13;

void setup(){
  pinMode(led , OUTPUT);
  Serial.begin(9600);
  
  delay(1000);//Wait before accessing Sensor
 
}//end "setup()"
 
void loop(){
  //Start of Program 
  //Serial.println("hi");
    int i = 0;
    DHT.read11(dht_apin);
    
    if(Serial.available()){
      char ch = Serial.read();
      
      if(ch == '1'){
        Serial.println(DHT.humidity);
        
      }
      if(ch == '2'){
        Serial.println(DHT.temperature);  
      }
      digitalWrite(led , ch=='3' ? HIGH : LOW );
    }
    delay(3000);
 
}// end loop() 

