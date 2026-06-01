# Measurements of Infineon IGOT60R070D1 GIT device.

Project filename format

```
igot_{diodesensecurrent}\_{channelsense}\_{channeldrive}
```

Channels:

* Ch0 - the Shottky diode voltage
* Ch1 - measured near to the device
* Ch2 - measured at the edge of the board
* Ch3 - measured on the external resistance



`extractor.py` will extract power and voltage information from the files.
