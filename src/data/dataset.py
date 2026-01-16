"""
Module de chargement et preparation des donnees
"""
import os
import tensorflow as tf
from tensorflow.keras.preprocessing.image import ImageDataGenerator
import yaml


def load_config():
    """Charge la configuration"""
    config_path = os.path.join('config', 'config.yaml')
    with open(config_path, 'r', encoding='utf-8') as f:
        return yaml.safe_load(f)


def create_data_generators(config):
    """
    Cree les generateurs de donnees pour train/valid/test
    
    Args:
        config: Configuration du projet
        
    Returns:
        train_gen, valid_gen, test_gen
    """
    # Parametres
    img_size = tuple(config['model']['image_size'])
    batch_size = config['model']['batch_size']
    
    # Augmentation pour les donnees d'entrainement
    train_datagen = ImageDataGenerator(
        rescale=1./255,
        rotation_range=20,
        width_shift_range=0.2,
        height_shift_range=0.2,
        shear_range=0.2,
        zoom_range=0.2,
        horizontal_flip=True,
        fill_mode='nearest'
    )
    
    # Pas d'augmentation pour validation/test
    valid_test_datagen = ImageDataGenerator(rescale=1./255)
    
    # Verifier si les dossiers existent
    train_dir = config['data']['train_dir']
    valid_dir = config['data']['valid_dir']
    test_dir = config['data']['test_dir']
    
    if not os.path.exists(train_dir):
        raise FileNotFoundError(f"Le dossier {train_dir} n'existe pas!")
    
    # Creer les generateurs
    train_generator = train_datagen.flow_from_directory(
        train_dir,
        target_size=img_size,
        batch_size=batch_size,
        class_mode='categorical'
    )
    
    valid_generator = None
    if os.path.exists(valid_dir):
        valid_generator = valid_test_datagen.flow_from_directory(
            valid_dir,
            target_size=img_size,
            batch_size=batch_size,
            class_mode='categorical'
        )
    
    test_generator = None
    if os.path.exists(test_dir):
        test_generator = valid_test_datagen.flow_from_directory(
            test_dir,
            target_size=img_size,
            batch_size=batch_size,
            class_mode='categorical',
            shuffle=False
        )
    
    return train_generator, valid_generator, test_generator


def get_num_classes(data_dir):
    """Retourne le nombre de classes"""
    if not os.path.exists(data_dir):
        return 0
    return len([d for d in os.listdir(data_dir) 
                if os.path.isdir(os.path.join(data_dir, d))])


if __name__ == "__main__":
    # Test du module
    print("Test du module dataset...")
    try:
        config = load_config()
        print("Configuration chargee avec succes")
        print(f"Classes configurees: {config['classes']}")
    except Exception as e:
        print(f"Erreur: {e}")