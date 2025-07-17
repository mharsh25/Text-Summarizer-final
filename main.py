from TextSummarizer.pipeline.stage_01_data_ingestion import DataIngestionTrainingPipeline
from TextSummarizer.logging import logger
from TextSummarizer.pipeline.stage_01_data_ingestion import DataIngestionTrainingPipeline
from TextSummarizer.pipeline.stage_02_data_validation import DataValidationTrainingPipeline
from TextSummarizer.pipeline.stage_03_data_transformation import DataTransformationTrainingPipeline
from TextSummarizer.pipeline.stage_04_model_trainer import ModelTrainerTrainingPipeline
from TextSummarizer.pipeline.stage_05_model_evaluation import ModelEvaluationTrainingPipeline
STAGE_NAME01="Data Ingestion Stage"
try:
    logger.info(f">>>>Stage {STAGE_NAME01} started<<<<")
    data_ingestion=DataIngestionTrainingPipeline()
    data_ingestion.main()
    logger.info(f">>>>Stage {STAGE_NAME01} completed<<<<")
except Exception as e:
    logger.exception(e)
    raise e

STAGE_NAME02="Data Validation Stage"
try:
    logger.info(f">>>>Stage {STAGE_NAME02} started<<<<")
    data_validation=DataValidationTrainingPipeline()
    data_validation.main()
    logger.info(f">>>>Stage {STAGE_NAME02} completed<<<<")
except Exception as e:
    logger.exception(e)
    raise e

STAGE_NAME03="Data Transformation Stage"
try:
    logger.info(f">>>>Stage {STAGE_NAME03} started<<<<")
    data_transformation=DataTransformationTrainingPipeline()
    data_transformation.main()
    logger.info(f">>>>Stage {STAGE_NAME03} completed<<<<")
except Exception as e:
    logger.exception(e)
    raise e


STAGE_NAME04="Model Training Stage"
try:
    logger.info(f">>>>Stage {STAGE_NAME04} started<<<<")
    model_training=ModelTrainerTrainingPipeline()
    model_training.main()
    logger.info(f">>>>Stage {STAGE_NAME04} completed<<<<")
except Exception as e:
    logger.exception(e)
    raise e


STAGE_NAME05="Model Evaluation Stage"
try:
    logger.info(f">>>>Stage {STAGE_NAME05} started<<<<")
    model_evaluation=ModelEvaluationTrainingPipeline()
    model_evaluation.main()
    logger.info(f">>>>Stage {STAGE_NAME05} completed<<<<")
except Exception as e:
    logger.exception(e)
    raise e