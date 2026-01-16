"""
Tests pour le module d'entrainement
"""
import pytest
import os
import sys

# Ajouter le repertoire parent au path
sys.path.append(os.path.dirname(os.path.dirname(__file__)))

from src.data.dataset import load_config, get_num_classes
from src.models.cnn_model import create_cnn_model, compile_model


def test_load_config():
    """Teste le chargement de la configuration"""
    config = load_config()
    assert config is not None
    assert 'model' in config
    assert 'data' in config
    print("Test load_config: OK")


def test_create_model():
    """Teste la creation du modele"""
    model = create_cnn_model(num_classes=4)
    assert model is not None
    assert len(model.layers) > 0
    print("Test create_model: OK")


def test_compile_model():
    """Teste la compilation du modele"""
    model = create_cnn_model(num_classes=4)
    model = compile_model(model)
    assert model.optimizer is not None
    assert model.loss is not None
    print("Test compile_model: OK")


def test_config_values():
    """Teste les valeurs de la configuration"""
    config = load_config()
    assert config['model']['batch_size'] > 0
    assert config['model']['epochs'] > 0
    assert len(config['model']['image_size']) == 2
    print("Test config_values: OK")


if __name__ == "__main__":
    print("Lancement des tests...")
    print("-" * 50)
    test_load_config()
    test_create_model()
    test_compile_model()
    test_config_values()
    print("-" * 50)
    print("Tous les tests sont passes avec succes!")