# Example for Arduino

```cpp
Serial.begin(115200);

# Note ON
Serial.write(0x99);
Serial.write(60);
Serial.write(100);

# Note OFF
Serial.write(0x89);
Serial.write(60);
Serial.write(0);
```
