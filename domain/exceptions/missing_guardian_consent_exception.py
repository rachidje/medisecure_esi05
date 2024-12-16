class MissingGuardianConsentException(Exception):
    def __init__(self):
        super().__init__("Guardian consent is required")