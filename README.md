# Cheap Flight Deal

Welcome to the "Cheap Flight Deal" project! This application is designed to help you find and monitor flight deals to your favorite destinations, sending notifications when a lower price is found.

## Overview

This project utilizes the Amadeus API for flight search, Sheety API for managing destination data, and Twilio for sending notifications. The main components include:

- **Data Manager**: Handles interactions with the Sheety API to fetch and update destination data.
- **Flight Search**: Queries flight data from the Amadeus API.
- **Flight Data**: Contains logic to determine the cheapest flight from the available options.
- **Notification Manager**: Sends notifications via WhatsApp using the Twilio API.

## Features

- Fetch and update destination data with IATA codes.
- Search for flight offers based on specified criteria.
- Notify users via WhatsApp when a lower flight price is detected.

## Installation

1. **Clone the repository:**

    ```bash
    git clone https://github.com/nares10/cheap-flight-deal.git
    ```

2. **Navigate into the project directory:**

    ```bash
    cd cheap-flight-deal
    ```

3. **Create a virtual environment and activate it:**

    ```bash
    python -m venv venv
    source venv/bin/activate  # On Windows use `venv\Scripts\activate`
    ```

4. **Install the required dependencies:**

    ```bash
    pip install -r requirements.txt
    ```

5. **Set up your environment variables:**

    Create a `.env` file in the root directory and add your API keys and credentials:

    ```plaintext
    SHEETY_USRERNAME="your_sheety_username"
    SHEETY_PASSWORD="your_sheety_password"
    AMADEUS_API_KEY="your_amadeus_api_key"
    AMADEUS_SECRET="your_amadeus_secret"
    TWILIO_SID="your_twilio_sid"
    TWILIO_AUTH_TOKEN="your_twilio_auth_token"
    TWILIO_WHATSAPP_NUMBER="your_twilio_whatsapp_number"
    TWILIO_VERIFIED_NUMBER="your_verified_whatsapp_number"
    ```

## Usage

1. **Run the application:**

    ```bash
    python main.py
    ```

    This script will:
    - Fetch destination data.
    - Update the destination codes with IATA codes.
    - Search for flights and check for lower prices.
    - Send WhatsApp notifications if a lower price is found.

## Dependencies

- `requests==2.28.1`
- `python-dotenv==1.0.0`
- `twilio==7.12.0`

## Contributing

Feel free to fork the repository. For any issues or feature requests, please open an issue on the GitHub repository.
