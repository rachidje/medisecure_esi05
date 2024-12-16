class MissingPatientConsentException(Exception):
    def __init__(self):
        super().__init__("Patient consent is required")