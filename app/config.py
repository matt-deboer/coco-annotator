import os

from .util.version_util import get_tag


class Config:

    NAME = "COCO Annotator"
    VERSION = get_tag()

    # Flask instance
    SWAGGER_UI_JSONEDITOR = True
    MAX_CONTENT_LENGTH = 1 * 1024 * 1024 * 1024  # 1GB
    MONGODB_HOST = os.getenv("MONGODB_HOST", "mongodb://database/flask")
    SECRET_KEY = os.getenv('SECRET_KEY', '<--- YOUR_SECRET_FORM_KEY --->')

    TESTING = os.getenv("TESTING", False)

    # Dataset Options
    DATASET_DIRECTORY = os.getenv("DATASET_DIRECTORY", "/datasets/")
    INITIALIZE_FROM_FILE = os.getenv("INITIALIZE_FROM_FILE")
    LOAD_IMAGES_ON_START = os.getenv("LOAD_IMAGES_ON_START", False)


    # Autoannotator options
    AUTOANNOTATOR_ENABLED = os.getenv("AUTOANNOTATOR_ENABLED", False)
    AUTOANNOTATOR_VERBOSE = os.getenv("AUTOANNOTATOR_VERBOSE", False)
    AUTOANNOTATOR_MAX_WORKERS = int(
        os.getenv("AUTOANNOTATOR_MAX_WORKERS", 4))
    AUTOANNOTATOR_QUEUE_SIZE = int(
        os.getenv("AUTOANNOTATOR_QUEUE_SIZE", 32))
    AUTOANNOTATOR_MAX_MISMATCHED = int(
        os.getenv("AUTOANNOTATOR_MAX_MISMATCHED", 5))
    AUTOANNOTATOR_DIFF_THRESHOLD = float(
        os.getenv("AUTOANNOTATOR_DIFF_THRESHOLD", 0.0035))

    # Coco Importer Options
    COCO_IMPORTER_VERBOSE = os.getenv("COCO_IMPORTER_VERBOSE", False)
    COCO_IMPORTER_MAX_WORKERS = int(os.getenv("COCO_IMPORTER_MAX_WORKERS", 4))
    COCO_IMPORTER_IMAGE_BATCH_SIZE = int(
        os.getenv("COCO_IMPORTER_IMAGE_BATCH_SIZE", 1000))
    COCO_IMPORTER_ANNOTATION_BATCH_SIZE = int(
        os.getenv("COCO_IMPORTER_ANNOTATION_BATCH_SIZE", 1000))

    # Autoexporter Options
    AUTOEXPORTER_ENABLED = os.getenv("AUTOEXPORTER_ENABLED", False)
    AUTOEXPORTER_VERBOSE = os.getenv("AUTOEXPORTER_VERBOSE", False)
    AUTOEXPORTER_EXTENSION = os.getenv("AUTOEXPORTER_EXTENSION", ".coco.json")


    # User Options
    LOGIN_DISABLED = os.getenv('LOGIN_DISABLED', False)
    ALLOW_REGISTRATION = True
