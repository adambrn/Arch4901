CREATE TABLE IF NOT EXISTS `users` (
  `id` int NOT NULL PRIMARY KEY,
  `user_type_id` int NOT NULL,
  `parse_id` varchar NOT NULL,
  `email` varchar NOT NULL,
  `password` varchar NOT NULL,
  `logged_in` boolean NOT NULL
);

CREATE TABLE IF NOT EXISTS `doctors` (
  `id` int NOT NULL PRIMARY KEY,
  `user_id` int NOT NULL,
  `specialization` varchar NOT NULL,
  `position` varchar NOT NULL
);

CREATE TABLE IF NOT EXISTS `patients` (
  `id` int NOT NULL PRIMARY KEY,
  `user_id` int NOT NULL,
  `date_of_birth` date NOT NULL,
  `gender` varchar NOT NULL
);

CREATE TABLE IF NOT EXISTS `departments` (
  `id` int NOT NULL PRIMARY KEY,
  `name` varchar NOT NULL
);

CREATE TABLE IF NOT EXISTS `cabinets` (
  `id` int NOT NULL PRIMARY KEY,
  `department_id` int NOT NULL,
  `number` int NOT NULL
);

CREATE TABLE IF NOT EXISTS `doctor_schedules` (
  `id` int NOT NULL PRIMARY KEY,
  `doctor_id` int NOT NULL,
  `day_of_week` varchar NOT NULL,
  `start_time` time NOT NULL,
  `end_time` time NOT NULL
);

CREATE TABLE IF NOT EXISTS `registrator` (
  `id` int NOT NULL PRIMARY KEY,
  `department_id` int NOT NULL,
  `responsible_user_id` int NOT NULL
);

CREATE TABLE IF NOT EXISTS `appointments` (
  `id` int NOT NULL PRIMARY KEY,
  `doctor_id` int NOT NULL,
  `patient_id` int NOT NULL,
  `appointment_record` int NOT NULL,
  `purpose` varchar NOT NULL,
  `is_confirmed` boolean NOT NULL,
  `registrator_id` int NOT NULL
);

CREATE TABLE IF NOT EXISTS `patient_medical_records` (
  `id` int NOT NULL PRIMARY KEY,
  `patient_id` int NOT NULL,
  `doctor_id` int NOT NULL,
  `appontment` int NOT NULL,
  `diagnosis` varchar NOT NULL,
  `prescription` varchar NOT NULL
);

CREATE TABLE IF NOT EXISTS `user_types` (
  `id` int NOT NULL PRIMARY KEY,
  `type` varchar NOT NULL
);

CREATE TABLE IF NOT EXISTS `user_addresses` (
  `id` int NOT NULL PRIMARY KEY,
  `user_id` int NOT NULL,
  `title` varchar NOT NULL
);