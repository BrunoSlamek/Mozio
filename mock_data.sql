INSERT INTO provider (name, email, phone_number, language, currency, created_at, updated_at)
VALUES
('ShuttleExpress', 'contact@shuttleexpress.com', '+12025550123', 'English', 'USD', NOW(), NOW()),
('CityTransfers', 'info@citytransfers.com', '+442071838888', 'English', 'GBP', NOW(), NOW()),
('FastTravel', 'support@fasttravel.com', '+33123456789', 'French', 'EUR', NOW(), NOW()),
('GoRide', 'service@goride.com', '+819012345678', 'Japanese', 'JPY', NOW(), NOW()),
('SkyLimo', 'hello@skylimo.com', '+61234567890', 'English', 'AUD', NOW(), NOW()),
('AirportShuttle', 'help@airportshuttle.com', '+498912345678', 'German', 'EUR', NOW(), NOW()),
('RapidTransit', 'sales@rapidtransit.com', '+14155552671', 'Spanish', 'USD', NOW(), NOW()),
('EasyTrans', 'contact@easytrans.com', '+5511998765432', 'Portuguese', 'BRL', NOW(), NOW()),
('SwiftRide', 'support@swiftride.com', '+911234567890', 'Hindi', 'INR', NOW(), NOW()),
('EcoMove', 'info@ecomove.com', '+27216543210', 'Afrikaans', 'ZAR', NOW(), NOW());

INSERT INTO service_area (name, price, geojson, provider_id, created_at, updated_at)
VALUES
('Downtown Area', 50.00, 'SRID=4326;POLYGON((30 10, 40 40, 20 40, 10 20, 30 10))', 1, NOW(), NOW()),
('Airport Zone', 75.00, 'SRID=4326;POLYGON((35 10, 45 45, 15 40, 10 20, 35 10))', 2, NOW(), NOW()),
('Suburban Ring', 40.00, 'SRID=4326;POLYGON((31 11, 41 41, 21 41, 11 21, 31 11))', 3, NOW(), NOW()),
('Central Business District', 100.00, 'SRID=4326;POLYGON((32 12, 42 42, 22 42, 12 22, 32 12))', 4, NOW(), NOW()),
('Tourist Zone', 60.00, 'SRID=4326;POLYGON((33 13, 43 43, 23 43, 13 23, 33 13))', 5, NOW(), NOW()),
('Residential Area', 30.00, 'SRID=4326;POLYGON((34 14, 44 44, 24 44, 14 24, 34 14))', 6, NOW(), NOW()),
('City Center', 90.00, 'SRID=4326;POLYGON((35 15, 45 45, 25 45, 15 25, 35 15))', 7, NOW(), NOW()),
('University District', 55.00, 'SRID=4326;POLYGON((36 16, 46 46, 26 46, 16 26, 36 16))', 8, NOW(), NOW()),
('Historic Area', 70.00, 'SRID=4326;POLYGON((37 17, 47 47, 27 47, 17 27, 37 17))', 9, NOW(), NOW()),
('Parkland Area', 45.00, 'SRID=4326;POLYGON((38 18, 48 48, 28 48, 18 28, 38 18))', 10, NOW(), NOW());

INSERT INTO service_area (name, price, geojson, provider_id, created_at, updated_at)
VALUES
('Brazil Area', 100.00, 
 'SRID=4326;POLYGON((-74.0 -33.7, -34.8 -7.2, -35.0 -9.6, -60.0 5.3, -65.0 -10.0, -74.0 -33.7))', 
 1, NOW(), NOW());
