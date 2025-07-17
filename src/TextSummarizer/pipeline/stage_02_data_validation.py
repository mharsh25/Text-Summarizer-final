from TextSummarizer.config.configuration import ConfigurationManager
from TextSummarizer.components.data_validation import DataValidation
from TextSummarizer.logging import logger

class DataValidationTrainingPipeline:
    def __init__(self):
            pass
    
    def main(self):
        try:
            config=ConfigurationManager()
            data_validation_config= config.get_data_validation_config()
            data_validation= DataValidation(config= data_validation_config)
            data_validation.validate_all_files_exist()
            data_validation.config
            ##data_validation.extract_zip_file()

        except Exception as e:
            raise e 