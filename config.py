# This is the configuration class for the Implmentation
# You can modify the LOG level and messaging type
# You can modify the weights directory
# You can modify the characters that shouldn't be removed during the postprocessing
import logging


class CFG:
    encoder_decoder_weights = 'weights/AutoEncoderModelBestLoss.h5' ## for photos denoising
    chars = '[^a-zA-Z0-9\n\.#@?/&\'\"_-]'
    
class LOG:
    logging.basicConfig(
    format="%(asctime)s %(message)s",
    datefmt="%Y-%m-%d,%H:%M:%S",
    level=logging.INFO,
    )
    logger = logging.getLogger(__name__)