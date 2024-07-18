# Cruise Ship Management

A web application for managing cruise ship operations, allowing voyagers to order catering items, book resort-movie tickets, schedule beauty salon appointments, book fitness center slots, and reserve party halls.

## Table of Contents
- [Features](#features)
- [Installation](#installation)
- [Usage](#usage)
- [Technologies Used](#technologies-used)
- [Contributing](#contributing)
- [License](#license)
- [Contact Information](#contact-information)

## Features
- **Order Catering Items:** Enable voyagers to order snacks, food, and beverages.
- **Order Stationery Items:** Allow voyagers to order gift items, chocolates, tale books, etc.
- **Book Resort-Movie Tickets:** Let voyagers choose movies, check seating availability, and book tickets.
- **Book Beauty Salon Appointments:** Enable voyagers to book appointments at the beauty salon.
- **Book Fitness Center:** Allow voyagers to select training equipment and schedule gym time.
- **Book Party Hall:** Let voyagers book different types of halls for various events.

- **Admin Module**
  - Add, edit, delete items
  - Maintain menu items
  - Voyager registration

- **Manager Module**
  - View booked Resort-Movie tickets
  - View booked beauty salon appointments
  - View booked fitness center reservations
  - View booked party hall reservations

- **Head-Cook Module**
  - View ordered catering items

- **Supervisor Module**
  - View ordered stationery items

## Technologies Used

- HTML
- CSS
- JavaScript
- Firebase (for authentication and database)
- Python (for backend and database management)

## Installation

1. Clone the repository:
    ```bash
    git clone https://github.com/yourusername/cruise-ship-management.git
    ```

2. Navigate to the project directory:
    ```bash
    cd cruise-ship-management
    ```

3. Install dependencies for the Python backend (make sure you have Python and pip installed):
    ```bash
    pip install -r requirements.txt
    ```

4. Set up Firebase:
    - Create a Firebase project in the [Firebase Console](https://console.firebase.google.com/).
    - Download the service account key JSON file and save it as `serviceAccountKey.json` in the project directory.
    - Replace the Firebase configuration in `index.html` with your own Firebase configuration.

5. Start the web server:
    ```bash
    python index.py
    ```

## Usage

- Open `index.html` in your web browser to access the application.
- Use the login and sign-up forms to create or access an account.
- Navigate through the various features using the navigation bar.

## Screenshots

![Login Page](screenshots/login.png)
![Movie Booking Page](screenshots/movie-booking.png)

## Contributing

1. Fork the repository
2. Create a new branch (`git checkout -b feature-branch`)
3. Make your changes
4. Commit your changes (`git commit -m 'Add some feature'`)
5. Push to the branch (`git push origin feature-branch`)
6. Create a new Pull Request

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## Contact

- **shriya** - [your-email@example.com](mailto:your-email@example.com)
- [GitHub](https://github.com/Shreya-V-H)
