# Sign Language Recognition System

## Problem Statement
Dumb people use hand signs to communicate, hence normal people face problem
in recognizing their language by signs made. Hence there is a need of the systems
which recognizes the different signs and conveys the information to the normal
people.

## Scope of Project
Sign language recognition system could be used at reception desks or during
video conferences to allow signing people to speak with people who don't know
Sign Language.

Potential Use Cases:
- Hotels
- Hospitals
- Clinics
- Offices

## Solution
The main point of this application is to use camera to recognize gestures from the
sign language to offer a new means of communication. The program will be able
to transcribe gestures done by dumb people into written words printed on the
screen.

## Project Structure
```
Sign Language Recognition/
├── data/                          # Directory for storing data files
├── signLanguage/                  # Main package directory
│   ├── components/               # Core components of the system
│   │   ├── data_ingestion.py    # Data collection and loading
│   │   ├── data_validation.py   # Data validation and verification
│   │   ├── model_trainer.py     # Model training logic
│   │   └── model_pusher.py      # Model deployment
│   ├── configuration/           # Configuration management
│   │   └── s3_operations.py     # AWS S3 operations
│   ├── constant/                # Constants and configurations
│   │   ├── application.py       # Application constants
│   │   └── training_pipeline/   # Training pipeline constants
│   ├── entity/                  # Data entities and models
│   │   ├── artifacts_entity.py  # Artifact definitions
│   │   └── config_entity.py     # Configuration entities
│   ├── exception/               # Custom exception handling
│   ├── logger/                  # Logging configuration
│   ├── pipeline/                # Pipeline implementations
│   │   └── training_pipeline.py # Training workflow
│   └── utils/                   # Utility functions
│       └── main_utils.py        # Common utility functions
├── template/                     # HTML templates
│   └── index.html              # Main web interface
├── app.py                       # Main application entry point
├── Dockerfile                   # Docker configuration
├── requirements.txt             # Python dependencies
├── setup.py                     # Package setup configuration
└── .dockerignore               # Docker ignore rules
```

## Setup Instructions
1. Clone the repository
2. Install dependencies:
   ```
   pip install -r requirements.txt
   ```
3. Run the application:
   ```
   python app.py
   ```

## Technologies Used
- Python
- OpenCV (for image processing)
- Deep Learning (for gesture recognition)
- Flask (for web interface)
- Docker (for containerization)

## Contributing
Feel free to submit issues and enhancement requests.

## License
[MIT License](LICENSE) 