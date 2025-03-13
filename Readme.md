# Flask Ticket Distribution App

This is a simple Flask web application that distributes tickets in a round-robin manner. Users can claim a ticket by providing their email address. Each user can only get one ticket, and the tickets are limited and expire after a certain period. This project is done for the completion of the assignment for Internship of Full stack development by The Sales Studio

## Features

- Users can claim a ticket by providing their email address.
- Each user can only get one ticket based on their email and IP address.
- Tickets expire after a specified period (5 minutes for testing).
- After expiry of the existing ticket. The same user can claim another ticket.
- Tickets are limited and managed in a separate table. One ticket can only be assigned once.

## Development Workflow

This project is developed using Flask and SQLite. On each claim request. Two tables are managed. One table named 'ticket_ids' contains all the limited available ticket IDs with their status as assigned or not. Another table is maintained named 'tickets' which holds the information of user's IP and EMAIL along with their expiry time. On each request the 'tickets' table is checked first to ensure if theres any entry with the user's IP and EMAIL ID. If so the expiry time is verified. Then if the user is eligable. A ticket will be assigned with current IP email and expiry date. To maintain ticket limitation and even distribution. The 'ticket_ids' table is used. On a valid request, This table is checked for next available ticket. If available the ID of the ticket is retrived and stored into the other table. Also the status of that ticked is updated as true. This is done to ensure one ticket is only distributed once. Minimal UI is created with proper feedbacks for ticket assignment, not availabe or invalid attempt

## Abuse Prevention

- Used two saperate databases and asked for email for ticket verification
- Use of Email is done in order to prevent IP attacks as hackers can use VPN like services to modify their IP and can bypass the IP verification.
- Cookie verification is avoided as hackers can also modify cookie data to bypass security. Also cookie data can be stolen further leading to ticket stealing.
- Server sided protection is used to verify that no client side change affects the security
- A rate limiting and email verification can be added to maintain authenticity and server load security.

## Requirements

- Python 3.x
- Flask
- SQLite

## Setup

1. Create a virtual enviromnent and activate it ( Optional ):

```sh
python -m venv venv
source venv/bin/activate  # On Windows, use `venv\Scripts\activate`
```

2. Install the required pakages:

```sh
pip install -r requirements.txt
```

3. Initialize the database:

```sh
python init_db.py
```

4. Run the Flask application

```sh
python app.py
```