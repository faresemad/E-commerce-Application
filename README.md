# E-commerce-Application

This project is a web application for e-commerce that utilizes the Django framework. The aim of this application is to provide a platform for selling products online securely and reliably.

## Table of Contents

- [Features](#features)
- [Requirements](#requirements)
- [Installation](#installation)
- [Usage](#usage)
- [Configuration](#configuration)
- [Folder Structure](#folder-structure)
- [Contributing](#contributing)
- [License](#license)


## Features

- Add new products and display them for sale.
- Create user accounts and manage login and logout.
- Add products to the shopping cart and complete the checkout process.
- Display details of previous orders for each user.
- Admin dashboard to manage products, users, and orders.

## Requirements

Ensure your system meets the following requirements before installing the application:

- Python 3.x
- Django
- Stripe
- PostgreSQL

## Installation

1. Clone the repository:

```bash
    git clone https://github.com/faresemad/E-commerce-Application.git
```

2. Build the application:

```bash
    make build
```

## Usage

1. Run the application:

```bash
    make up
```

2. Run the application in detached mode:

```bash
    make up-detached
```

## Configuration

The application can be configured by modifying the following files:

1. Configure Django settings in `/config/settings/base.py`.

2. Configure Django Environment settings in `/.envs/.django`.

3. Configure Postgres Environment settings in `/.envs/.postgres`.

3. Configure Stripe Environment settings in `/.envs/.stripe`.

## Folder Structure

The application is structured as follows:

- **\`.envs\`** - Environment variable files for Django and Postgres.
- **\`apps\`** - Application-specific files.
- **\`config\`** - Settings for the application
- **\`compose\`** - Docker Compose configuration files.
- **\`requirements\`** - Application requirements files.
- **\`manage.py\`** - Django's command-line utility for administrative tasks.

## Contributing

Contributions are welcome! Please feel free to submit a Pull Request.

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.
