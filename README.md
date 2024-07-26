
# Smart Parking Car IoT Challenge 2024

## Introduction

The Smart Parking Car IoT Challenge 2024 is an innovative project aimed at revolutionizing the parking experience by leveraging IoT technology. This project focuses on developing a smart parking system that can detect available parking spaces, recognize license plates, and control access using servo mechanisms. Additionally, it includes a fire detection feature to enhance safety.

## Features

- **Parking Space Detection**: Identifies and monitors available parking spots using computer vision.
- **License Plate Recognition**: Recognizes and logs vehicle license plates for access control and monitoring.
- **Servo Control**: Manages access control using servo mechanisms to open and close barriers.
- **Fire Detection**: Detects fire within the parking area to ensure safety.
- **LED Matrix Display**: Shows the status of parking slots on an LED matrix.
- **MQTT Gateway**: Handles communication between the IoT devices and the central server.

## Project Structure

```
Smart_Parking_Car_IOT_Challenge_2024/
│
├── Computer_Vision/
│   ├── license-plate-recognition/
│   │   └── main_webcam.py
│   ├── predict_space/
│   │   └── test_customtkinter.py
│
├── Python_Server/
│   ├── gateway_pi.py
│   ├── led_matrix_parking_slot.py
│   └── servo_control.py
│
└── README.md
```

## Prerequisites

- Python 3.x
- OpenCV
- NumPy
- MySQL
- MQTT
- CustomTkinter
- Raspberry Pi (or any other compatible device)

## Installation

1. **Clone the repository:**

    ```bash
    git clone https://github.com/BKG-Robocon-team/Smart_Parking_Car_IOT_Challenge_2024.git
    ```

2. **Navigate to the project directory:**

    ```bash
    cd Smart_Parking_Car_IOT_Challenge_2024
    ```

3. **Install the required Python packages:**

    ```bash
    pip install -r requirements.txt
    ```

## Usage

### Running the Python Scripts

To run the main scripts, you can use the following commands on your Raspberry Pi:

1. **Gateway Script:**

    ```bash
    python3 Python_Server/gateway_pi.py
    ```

2. **LED Matrix Parking Slot Script:**

    ```bash
    python3 Python_Server/led_matrix_parking_slot.py
    ```

3. **Servo Control Script:**

    ```bash
    python3 Python_Server/servo_control.py
    ```

### Running the Computer Vision Scripts

1. **License Plate Recognition:**

    ```bash
    python3 Computer_Vision/license-plate-recognition/main_webcam.py
    ```

2. **Parking Space Detection:**

    ```bash
    python3 Computer_Vision/predict_space/test_customtkinter.py
    ```

### Automated Script Execution

You can automate the execution of these scripts using a shell script. Create a `run_scripts.sh` file with the following content:

```bash
#!/bin/bash
echo "Running gateway_pi.py"
python3 /path/to/Smart_Parking_Car_IOT_Challenge_2024/Python_Server/gateway_pi.py &

echo "Running led_matrix_parking_slot.py"
python3 /path/to/Smart_Parking_Car_IOT_Challenge_2024/Python_Server/led_matrix_parking_slot.py &

echo "Running servo_control.py"
python3 /path/to/Smart_Parking_Car_IOT_Challenge_2024/Python_Server/servo_control.py &

wait
```

Replace `/path/to/Smart_Parking_Car_IOT_Challenge_2024/` with the actual path to your project directory.

Make the script executable and run it:

```bash
chmod +x run_scripts.sh
./run_scripts.sh
```

## Contributing

We welcome contributions! Please read our [Contributing Guidelines](CONTRIBUTING.md) for more information on how to contribute to this project.

## License

This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for more details.

## Acknowledgments

- Special thanks to the BKG Robocon team for their continuous support and contributions.
- Thanks to all contributors and participants of the Smart Parking Car IoT Challenge 2024.

# Smart Parking Car IoT Challenge 2024

## Introduction

The Smart Parking Car IoT Challenge 2024 is an innovative project aimed at revolutionizing the parking experience by leveraging IoT technology. This project focuses on developing a smart parking system that can detect available parking spaces, recognize license plates, and control access using servo mechanisms. Additionally, it includes a fire detection feature to enhance safety.

## Features

- **Parking Space Detection**: Identifies and monitors available parking spots using computer vision.
- **License Plate Recognition**: Recognizes and logs vehicle license plates for access control and monitoring.
- **Servo Control**: Manages access control using servo mechanisms to open and close barriers.
- **Fire Detection**: Detects fire within the parking area to ensure safety.
- **LED Matrix Display**: Shows the status of parking slots on an LED matrix.
- **MQTT Gateway**: Handles communication between the IoT devices and the central server.

## Project Structure

```
Smart_Parking_Car_IOT_Challenge_2024/
│
├── Computer_Vision/
│   ├── license-plate-recognition/
│   │   └── main_webcam.py
│   ├── predict_space/
│   │   └── test_customtkinter.py
│
├── Python_Server/
│   ├── gateway_pi.py
│   ├── led_matrix_parking_slot.py
│   └── servo_control.py
│
└── README.md
```

## Prerequisites

- Python 3.x
- OpenCV
- NumPy
- MySQL
- MQTT
- CustomTkinter
- Raspberry Pi (or any other compatible device)

## Installation

1. **Clone the repository:**

    ```bash
    git clone https://github.com/BKG-Robocon-team/Smart_Parking_Car_IOT_Challenge_2024.git
    ```

2. **Navigate to the project directory:**

    ```bash
    cd Smart_Parking_Car_IOT_Challenge_2024
    ```

3. **Install the required Python packages:**

    ```bash
    pip install -r requirements.txt
    ```

## Usage

### Running the Python Scripts

To run the main scripts, you can use the following commands on your Raspberry Pi:

1. **Gateway Script:**

    ```bash
    python3 Python_Server/gateway_pi.py
    ```

2. **LED Matrix Parking Slot Script:**

    ```bash
    python3 Python_Server/led_matrix_parking_slot.py
    ```

3. **Servo Control Script:**

    ```bash
    python3 Python_Server/servo_control.py
    ```

### Running the Computer Vision Scripts

1. **License Plate Recognition:**

    ```bash
    python3 Computer_Vision/license-plate-recognition/main_webcam.py
    ```

2. **Parking Space Detection:**

    ```bash
    python3 Computer_Vision/predict_space/test_customtkinter.py
    ```

### Automated Script Execution

You can automate the execution of these scripts using a shell script. Create a `run_scripts.sh` file with the following content:

```bash
#!/bin/bash
echo "Running gateway_pi.py"
python3 /path/to/Smart_Parking_Car_IOT_Challenge_2024/Python_Server/gateway_pi.py &

echo "Running led_matrix_parking_slot.py"
python3 /path/to/Smart_Parking_Car_IOT_Challenge_2024/Python_Server/led_matrix_parking_slot.py &

echo "Running servo_control.py"
python3 /path/to/Smart_Parking_Car_IOT_Challenge_2024/Python_Server/servo_control.py &

wait
```

Replace `/path/to/Smart_Parking_Car_IOT_Challenge_2024/` with the actual path to your project directory.

Make the script executable and run it:

```bash
chmod +x run_scripts.sh
./run_scripts.sh
```

## Contributing

We welcome contributions! Please read our [Contributing Guidelines](CONTRIBUTING.md) for more information on how to contribute to this project.

## License

This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for more details.

## Acknowledgments

- Special thanks to the BKG Robocon team for their continuous support and contributions.
- Thanks to all contributors and participants of the Smart Parking Car IoT Challenge 2024.
