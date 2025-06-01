from ..models.registry import MODELS, ModelBackendEnum
from ..models.base import PromptModelBase

_model_instance_cache = {}
def is_ollama_model(model_key):
    return MODELS[model_key]["backend"] == ModelBackendEnum.OLLAMA

class ModelManager:
    @classmethod
    def get_model(cls, model_key, keep_model_alive=False, **kwargs) -> PromptModelBase:
        if model_key not in MODELS:
            raise ValueError(f"Model {model_key} not registered.")

        if is_ollama_model(model_key):
            # Always create new wrapper; let Ollama handle keep_alive internally
            model_cls = MODELS[model_key]["model_class"]
            return model_cls(**kwargs)

        if keep_model_alive and model_key in _model_instance_cache:
            return _model_instance_cache[model_key]

        model_cls = MODELS[model_key]["model_class"]
        model_instance = model_cls(**kwargs)

        if keep_model_alive:
            for key, instance in _model_instance_cache.items():
                if hasattr(instance, "unload"):
                    instance.unload()
            _model_instance_cache.clear()
            _model_instance_cache[model_key] = model_instance

        return model_instance
