
# Mozio API

## Technologies Used

| Technology                | Version |
|---------------------------|---------|
| Python                    | 3.11.5  |
| Django                    | 4.2     |
| Django Rest Framework      | 3.15    |
| PostgreSQL                | 16      |
| PostGIS                   | 3.5       |

See more at requirements.txt file

---

# API Documentation

## Provider Endpoints

| Method | Endpoint            | Description                      | Request Body                        | Response                               |
|--------|---------------------|----------------------------------|-------------------------------------|----------------------------------------|
| GET    | `/providers/`       | List all providers               | None                                | 200 OK, List of providers              |
| POST   | `/providers/`       | Create a new provider            | `{ "name": "...", "email": "...", "phone_number": "...", "language": "...", "currency": "..." }` | 201 Created, Provider object           |
| GET    | `/providers/{id}/`  | Retrieve a provider by ID        | None                                | 200 OK, Provider object                |
| PUT    | `/providers/{id}/`  | Update a provider by ID          | `{ "name": "...", "email": "...", "phone_number": "...", "language": "...", "currency": "..." }` | 200 OK, Updated provider object        |
| DELETE | `/providers/{id}/`  | Delete a provider by ID          | None                                | 204 No Content                         |

## Service Area Endpoints

| Method | Endpoint                                     | Description                                | Request Body                                                                | Response                                   |
|--------|----------------------------------------------|--------------------------------------------|-----------------------------------------------------------------------------|--------------------------------------------|
| GET    | `/serviceareas/`                             | List all service areas                     | None                                                                        | 200 OK, List of service areas              |
| POST   | `/serviceareas/`                             | Create a new service area                  | `{ "name": "...", "price": "...", "geojson": "...", "provider": "..." }`    | 201 Created, ServiceArea object            |
| GET    | `/serviceareas/{id}/`                        | Retrieve a service area by ID              | None                                                                        | 200 OK, ServiceArea object                 |
| PUT    | `/serviceareas/{id}/`                        | Update a service area by ID                | `{ "name": "...", "price": "...", "geojson": "...", "provider": "..." }`    | 200 OK, Updated service area object        |
| DELETE | `/serviceareas/{id}/`                        | Delete a service area by ID                | None                                                                        | 204 No Content                             |
| GET    | `/serviceareas/search?lat={lat}&lng={lng}`   | Search service areas by latitude/longitude | None                                                                        | 200 OK, List of matching service areas     |

To test /search you should be logged "admin" and "admin".
---

## EC2 Setup

### Instance Details

| Key                            | Value                                                      |
|---------------------------------|------------------------------------------------------------|
| **Platform**                    | Ubuntu (Inferred)                                          |
| **AMI ID**                      | ami-0866a3c8686eaeeba                                      |
| **Monitoring**                  | Disabled                                                   |
| **Platform Details**            | Linux/UNIX                                                 |
| **AMI Name**                    | ubuntu/images/hvm-ssd-gp3/ubuntu-noble-24.04-amd64-server-20240927 |
| **Termination Protection**      | Disabled                                                   |
| **Stop Protection**             | Disabled                                                   |
| **Launch Time**                 | Thu Oct 17 2024 18:08:26 GMT-0300 (Horário Padrão de Brasília) |
| **AMI Location**                | amazon/ubuntu/images/hvm-ssd-gp3/ubuntu-noble-24.04-amd64-server-20240927 |
| **Instance Auto-Recovery**      | Default                                                    |
| **Lifecycle**                   | Normal                                                     |
| **Stop-Hibernate Behavior**     | Disabled                                                   |
| **AMI Launch Index**            | 0                                                          |
| **Key Pair Assigned at Launch** | aws-ec2-mozio                                              |
| **State Transition Reason**     | –                                                          |
| **Credit Specification**        | Standard                                                   |
| **Kernel ID**                   | –                                                          |
| **State Transition Message**    | –                                                          |
| **Usage Operation**             | RunInstances                                               |
| **RAM Disk ID**                 | –                                                          |
| **Enclaves Support**            | –                                                          |
| **Boot Mode**                   | uefi-preferred                                             |
| **Current Instance Boot Mode**  | Legacy BIOS                                                |
| **Allow Tags in Instance Metadata** | Disabled                                               |
| **Use RBN as Guest OS Hostname** | Disabled                                                  |
| **Answer RBN DNS Hostname IPv4** | Enabled                                                   |

### Host and Placement Group

| Key                            | Value                                                      |
|---------------------------------|------------------------------------------------------------|
| **Host ID**                     | –                                                          |
| **Affinity**                    | –                                                          |
| **Placement Group**             | –                                                          |
| **Host Resource Group Name**    | –                                                          |
| **Tenancy**                     | Default                                                    |
| **Placement Group ID**          | –                                                          |
| **Virtualization Type**         | HVM                                                        |
| **Reservation**                 | r-03af916081702e130                                        |
| **Partition Number**            | –                                                          |
| **Number of vCPUs**             | 1                                                          |

### Capacity Reservation

| Key                            | Value                                                      |
|---------------------------------|------------------------------------------------------------|
| **Capacity Reservation ID**     | –                                                          |
| **Capacity Reservation Setting** | Open                                                      |

### Accelerators

| Key                            | Value                                                      |
|---------------------------------|------------------------------------------------------------|
| **Elastic Graphics ID**         | –                                                          |

---

## Amazon RDS PostgreSQL Instance Details

| Attribute                        | Details                           |
|-----------------------------------|-----------------------------------|
| **Instance Class**                | db.t4g.micro                      |
| **vCPU**                          | 2                                 |
| **RAM**                           | 1 GB                              |
| **Master Username**               | postgres                          |
| **Master Password**               | *******                           |
| **IAM DB Authentication**         | Not enabled                       |
| **Multi-AZ**                      | No                                |
| **Secondary Zone**                | -                                 |
| **Encryption**                    | Enabled                           |
| **AWS KMS Key**                   | aws/rds                           |
| **Storage Type**                  | General Purpose SSD (gp3)         |
| **Storage**                       | 20 GiB                            |
| **Provisioned IOPS**              | 3000 IOPS                         |
| **Storage Throughput**            | 125 MiBps                         |
| **Storage Autoscaling**           | Enabled                           |
| **Maximum Storage Threshold**     | 1000 GiB                          |
| **Storage File System Configuration** | Current                      |
| **Performance Insights**          | Enabled                           |
| **AWS KMS Key for Performance**   | aws/rds                           |
| **Retention Period**              | 7 days                            |

Used mock_data.sql for initial and example data

---
