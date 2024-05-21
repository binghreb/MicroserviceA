import time

while True:
    # Open and read the input file
    with open('speedConv_service.txt', 'r') as input_file:
        speed_request = input_file.read().strip()

    # Check if there is a conversion request in the file
    if speed_request:
        print("Received data: " +speed_request)
        # Parse the input (expected format: source_unit,target_unit,value)
        try:
            source_unit, target_unit, value = speed_request.split(',')
        except:
            converted_value = "Invalid units. Please try again."
        else:
            # Remove any whitespace for proper string comparison
            source_unit = source_unit.strip()
            target_unit = target_unit.strip()
            value = value.strip()

            # Perform the conversion
            if source_unit == "km/h" and target_unit == "mph":
                converted_value = str(float(value) * 0.621371) + " mph"
            elif source_unit == "mph" and target_unit == "km/h":
                converted_value = str(float(value) / 0.621371) + " km/h"
            else:
                converted_value = "Invalid units. Please try again."

        # Write the conversion result to the output file
        with open('speedConv_service.txt', 'w') as output_file:
            output_file.write(str(converted_value))

    # Sleep for a short time before checking the input file again
    time.sleep(8)
