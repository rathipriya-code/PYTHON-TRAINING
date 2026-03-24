from sentence_transformers import SentenceTransformer
#from azure.identity import ClientSecretCredential
#from azure.storage.fileshare import ShareFileClient
#from cdpFunctionApp.constants import CROSS_ENCODER_MODEL_PATH, SENTENCE_MODEL_PATH
#from cdpFunctionApp.config import Config
#from cdpFunctionApp.utils import timeit
import os
import logging
import zipfile
logging.basicConfig(level=logging.INFO)


# === GLOBAL CACHE ===
_model_cache = {}
#_credential = None

'''def _get_credential():
    """Lazy-load Azure credential."""
    global _credential
    if _credential is None:
        _credential = ClientSecretCredential(
            Config.AZURE_ML_TENANT_ID,
            Config.AZURE_ML_CLIENT_ID,
            Config.AZURE_ML_CLIENT_SECRET,
        )
    return _credential
'''
def download_and_extract_zip_from_file_share(
    share_name: str, 
    file_name: str, 
    local_dir: str
):
    """
    Download a ZIP file from Azure File Share and extract its contents.

    Args:
        share_name (str): The name of the Azure File Share.
        file_name (str): Path to the ZIP file inside the share.
        local_dir (str): Local directory to save and extract contents.
    """
    os.makedirs(local_dir, exist_ok=True)

    # Local temp path for the downloaded zip
    local_zip_path = file_name 

    # Skip if already extracted
    extracted_dir = os.path.join(local_dir, os.path.splitext(os.path.basename(file_name))[0])
    if os.path.exists(extracted_dir) and os.listdir(extracted_dir):
        logging.info(f"Model already exists at: {extracted_dir}")
        return

    logging.info(f"Extracting local zip :{file_name} ")

    # Connect to file in Azure File Share
    '''file_client = ShareFileClient.from_connection_string(
        conn_str=Config.AZURE_ML_STORAGE_CONNECTION_STRING,
        share_name=share_name,
        file_path=file_name
    )'''

    '''try:
        # Download the file
        file=zre.zipfile.ZipFile(os.path.join(local_dir, file_name), 'w')
        stream = file.download_file()
        with open(local_zip_path, "wb") as f:
            data = stream.readall()
            f.write(data)
            f.flush()
        logging.info(f" Downloaded to: {local_zip_path}")

        # Extract the ZIP
        logging.info(f" Extracting to: {local_dir}")
        with zipfile.ZipFile(local_zip_path, "r") as zip_ref:
            zip_ref.extractall(local_dir)
        logging.info(" Extracted successfully")

        # Clean up ZIP file
        os.remove(local_zip_path)
        logging.info(f"🧹 Removed temporary file: {local_zip_path}")

    except Exception as e:
        logging.error(f" Failed to download/extract model: {e}")
        # Clean up partial files on error
        if os.path.exists(local_zip_path):
            os.remove(local_zip_path)
        raise
       '''
    with zipfile.ZipFile(local_zip_path, "r") as zip_ref:
        zip_ref.extractall(local_dir)

    logging.info("Extracted successfully")
#@timeit

def _load_model(model_str: str, model_class, cache_dir: str =  "/tmp/model_cache", device: str = "cpu"):

    """
    Load model from Azure File Share.

    Expected format: "<share_name>/<remote_path>"
    Example: "f6b61e86-4e81-4e1c-8c63-e11184c28c6a-code/zre_cross_encoder.zip"

    Args:
        model_str (str): Path in format "share_name/file_name.zip"
        model_class: SentenceTransformer or CrossEncoder class
        cache_dir (str): Local directory to cache models
        device (str): Device to load model on ("cpu" or "cuda"). Defaults to "cpu"

    Returns:
        Loaded model instance
    """
    # Strip any accidental version suffix
    model_str = model_str.strip()
    if ":" in model_str:
        model_str = model_str.split(":")[0]

    # Parse share name and file path
    parts = model_str.split("/", 1)
    if len(parts) != 2:
        raise ValueError(
            f"Invalid model_str format: '{model_str}'. Expected '<share_name>/<file_path.zip>'"
        )

    share_name, file_name = parts

    # Ensure cache directory exists
    os.makedirs(cache_dir, exist_ok=True)

    # Download and extract if not already cached
    download_and_extract_zip_from_file_share(share_name, file_name, cache_dir)

    # Load the model from extracted directory
    model_dir_name = os.path.splitext(os.path.basename(file_name))[0]
    model_path = os.path.join(cache_dir, model_dir_name)

    logging.info(f"Loading model from: {model_path} on device: {device}")
    model = model_class(model_path, device=device)
    logging.info(" Model loaded successfully")

    return model



def get_models():
    """
    Return shared instances of the models (lazy-load).
    
    Note: Cross encoder model is now loaded from Azure Model Endpoint.

    Returns:
        tuple: (None, sentence_model) - cross_encoder is None
    """
    # Cross encoder model is now served via Azure Model Endpoint
    # if "cross_encoder" not in _model_cache:
    #     logging.info("Loading cross encoder model...")
    #     _model_cache["cross_encoder"] = _load_model(
    #         CROSS_ENCODER_MODEL_PATH, 
    #         CrossEncoder
    #     )

    if "sentence_model" not in _model_cache:
        logging.info("Loading sentence transformer model...")
        _model_cache["sentence_model"] = _load_model(
             "dummy/zeiss-re-1757443344.zip",
              SentenceTransformer
        )

    return None, _model_cache["sentence_model"] 

if __name__ == "__main__":
    print("Starting model loading...")
    get_models()
_, sentence_model = get_models() 


query1 = "Hello world"
query_emb1 = sentence_model.encode([query1], convert_to_tensor=True)
print(query_emb1)

    
model = SentenceTransformer("jagadeesh/zeiss-re-1757443344")
query2 = "Hello World"

query_emb2 = model.encode([query2], convert_to_tensor=True)
print(query_emb2)
os.makedirs("outputfiles", exist_ok=True)
with open("outputfiles/output_1.txt","w",encoding="utf-8")as f:
    f.write(str(query_emb1))
    
with open("outputfiles/output_2.txt", "w", encoding="utf-8")as f1:
    f1.write(str(query_emb2))