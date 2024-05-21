# MicroserviceA
Microservice to convert speeds

<ins>
How to programmatically REQUEST data:
</ins>

  Data should be requested from the user in the format **source unit, target unit, speed value** (ex: "mph, km/h, 50") and written to text file speedConv_service.txt. 

**Example Call:**
```
conversion_input = "mph, km/h, 50"
with open('speedConv_service.txt', 'w') as input_file:
    input_file.write(str(conversion_input))
```

<ins>
how to programmatically RECEIVE data:
</ins>

  Data should should be received from the text file speedConv_service.txt. The request data will be overwritten in this file.
```
with open('speedConv_service.txt', 'r') as output_file:
    speed_output = output_file.read().strip()
```

![Model](https://github.com/binghreb/MicroserviceA/blob/main/UML.png)
