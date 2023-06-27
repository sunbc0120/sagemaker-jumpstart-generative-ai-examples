import sagemaker
import boto3
from sagemaker import script_uris
from sagemaker import image_uris 
from sagemaker import model_uris
from sagemaker.jumpstart.notebook_utils import list_jumpstart_models

session = sagemaker.Session()

def get_sagemaker_uris(model_id,instance_type,region_name):
    
    
    MODEL_VERSION = "*"  # latest
    SCOPE = "inference"

    inference_image_uri = image_uris.retrieve(region=region_name, 
                                          framework=None,
                                          model_id=model_id, 
                                          model_version=MODEL_VERSION, 
                                          image_scope=SCOPE, 
                                          instance_type=instance_type)
    
    inference_model_uri = model_uris.retrieve(
                                          region=region_name,
                                          model_id=model_id, 
                                          model_version=MODEL_VERSION, 
                                          model_scope=SCOPE)
    
    inference_source_uri = script_uris.retrieve(
                                            region=region_name,
                                            model_id=model_id, 
                                            model_version=MODEL_VERSION, 
                                            script_scope=SCOPE)

    model_bucket_name = inference_model_uri.split("/")[2]
    model_bucket_key = "/".join(inference_model_uri.split("/")[3:])
    model_docker_image = inference_image_uri

    return {"model_bucket_name":model_bucket_name, "model_bucket_key": model_bucket_key, \
            "model_docker_image":model_docker_image, "instance_type":instance_type, \
                "inference_source_uri":inference_source_uri, "region_name":region_name}