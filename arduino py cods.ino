int gelenByte; 

void setup() {
  Serial.begin(9600);
  pinMode(8, OUTPUT);

   
}

void Yak()
{
  digitalWrite(8, HIGH);
}

void Sondur()
{
  digitalWrite(8, LOW);
}

void loop() {
  
  if (gelenByte == '1') {
    Yak();
  } 
    
  if (gelenByte == '2') {
    Sondur();
  }
  
  
  if (Serial.available() > 0) {
    gelenByte = Serial.read();
    if (gelenByte == '1') {
      Yak();
    } 

    if (gelenByte == '2') {
      Sondur() ;
    }
    
  }
}
