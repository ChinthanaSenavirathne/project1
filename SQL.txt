CREATE TABLE Users (
    userID INT PRIMARY KEY AUTO_INCREMENT,
    username VARCHAR(50) NOT NULL UNIQUE,
    password VARCHAR(100) NOT NULL,
    role ENUM('admin', 'staff', 'customer') NOT NULL
);

CREATE TABLE Reservations (
    reservationID INT PRIMARY KEY AUTO_INCREMENT,
    userID INT,
    reservationDate DATE NOT NULL,
    reservationTime TIME NOT NULL,
    guests INT NOT NULL,
    status ENUM('pending', 'confirmed', 'cancelled') DEFAULT 'pending',
    FOREIGN KEY (userID) REFERENCES Users(userID)
);

CREATE TABLE Queries (
    queryID INT PRIMARY KEY AUTO_INCREMENT,
    userID INT,
    queryText TEXT NOT NULL,
    response TEXT,
    FOREIGN KEY (userID) REFERENCES Users(userID)
);
