from typing import List
from datetime import date
from ....base import catch_vector_errors
from ....doc_utils import ModelDefinition
from ....import_utils import *
from ....models_dict import MODEL_REQUIREMENTS
from ..base import BaseTextText2Vec
from .use_qa import USEQA2Vec
if is_all_dependency_installed(MODEL_REQUIREMENTS['text-bi-encoder-tfhub-use-qa']):
    import bert
    import numpy as np
    import tensorflow as tf
    import tensorflow_hub as hub
    import tensorflow_text

USEMultiQAModelDefinition = ModelDefinition(markdown_filepath='bi_encoders/text_text/tfhub/use_multi_qa')

class USEMultiQA2Vec(USEQA2Vec):
    definition = USEMultiQAModelDefinition
    def __init__(self):
        self.model_url = "https://tfhub.dev/google/universal-sentence-encoder-multilingual-qa/3"
        self.model = hub.load(self.model_url)
        self.model_name = self.model_url.replace(
            'https://tfhub.dev/google/', '').replace('/', '_')
        self.vector_length = 512