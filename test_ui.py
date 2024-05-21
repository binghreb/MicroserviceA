import time

# test program to make request from microservice
while True:
    # inform user of format
    print("Please enter your conversion request in the following format: 'km/h, mph, 50'")
    conversion_input = input("Speed Conversion: ")

    # once the user has entered request - write this to the file
    if conversion_input:
        with open('speedConv_service.txt', 'w') as input_file:
                input_file.write(str(conversion_input))

        time.sleep(9)
        # Open and read the input file
        with open('speedConv_service.txt', 'r') as output_file:
            speed_output = output_file.read().strip()
            if speed_output:
                print(speed_output)

                # clear the file
                open('speedConv_service.txt', 'w').close()
                print("")

    

