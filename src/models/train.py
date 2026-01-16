"""
Script d'entrainement du modele
"""
import os
import sys
import yaml
import mlflow
import mlflow.keras
from datetime import datetime
import tensorflow as tf

# Ajouter le repertoire parent au path
sys.path.append(os.path.dirname(os.path.dirname(os.path.dirname(__file__))))

from src.data.dataset import create_data_generators, load_config
from src.models.cnn_model import create_cnn_model, compile_model


def train_model():
    """
    Entraine le modele CNN sur les donnees
    """
    print("=" * 50)
    print("DEMARRAGE DE L'ENTRAINEMENT")
    print("=" * 50)
    
    # Charger la configuration
    print("\n1. Chargement de la configuration...")
    config = load_config()
    print("   Configuration chargee avec succes!")
    
    # Creer les generateurs de donnees
    print("\n2. Chargement des donnees...")
    try:
        train_gen, valid_gen, test_gen = create_data_generators(config)
        
        num_classes = len(train_gen.class_indices)
        print(f"   Nombre de classes: {num_classes}")
        print(f"   Classes: {list(train_gen.class_indices.keys())}")
        print(f"   Nombre d'images d'entrainement: {train_gen.samples}")
        if valid_gen:
            print(f"   Nombre d'images de validation: {valid_gen.samples}")
        
    except FileNotFoundError as e:
        print(f"   ERREUR: {e}")
        print("\n   INSTRUCTIONS:")
        print("   1. Organisez vos donnees dans data/train/, data/valid/, data/test/")
        print("   2. Chaque sous-dossier doit representer une classe")
        print("   Exemple:")
        print("      data/train/healthy/")
        print("      data/train/diseased/")
        return
    
    # Creer le modele
    print("\n3. Creation du modele CNN...")
    img_size = tuple(config['model']['image_size'])
    model = create_cnn_model(
        input_shape=(*img_size, 3),
        num_classes=num_classes
    )
    model = compile_model(model, config['model']['learning_rate'])
    print("   Modele cree avec succes!")
    
    # Afficher le resume du modele
    print("\n4. Architecture du modele:")
    model.summary()
    
    # MLflow tracking
    print("\n5. Configuration de MLflow...")
    mlflow.set_experiment(config['mlflow']['experiment_name'])
    
    with mlflow.start_run():
        # Logger les parametres
        mlflow.log_params({
            'image_size': img_size,
            'batch_size': config['model']['batch_size'],
            'epochs': config['model']['epochs'],
            'learning_rate': config['model']['learning_rate'],
            'num_classes': num_classes
        })
        
        # Callbacks
        callbacks = [
            tf.keras.callbacks.EarlyStopping(
                monitor='val_loss',
                patience=10,
                restore_best_weights=True
            ),
            tf.keras.callbacks.ReduceLROnPlateau(
                monitor='val_loss',
                factor=0.5,
                patience=5,
                min_lr=1e-7
            )
        ]
        
        # Entrainement
        print("\n6. Debut de l'entrainement...")
        print("-" * 50)
        
        history = model.fit(
            train_gen,
            epochs=config['model']['epochs'],
            validation_data=valid_gen,
            callbacks=callbacks,
            verbose=1
        )
        
        print("-" * 50)
        print("   Entrainement termine!")
        
        # Evaluation
        if valid_gen:
            print("\n7. Evaluation sur les donnees de validation...")
            val_loss, val_acc, val_prec, val_recall = model.evaluate(valid_gen)
            
            # Logger les metriques
            mlflow.log_metrics({
                'val_loss': val_loss,
                'val_accuracy': val_acc,
                'val_precision': val_prec,
                'val_recall': val_recall
            })
            
            print(f"   Validation Loss: {val_loss:.4f}")
            print(f"   Validation Accuracy: {val_acc:.4f}")
            print(f"   Validation Precision: {val_prec:.4f}")
            print(f"   Validation Recall: {val_recall:.4f}")
        
        # Sauvegarder le modele
        print("\n8. Sauvegarde du modele...")
        os.makedirs("models", exist_ok=True)
        model_path = os.path.join("models", "cnn_model.h5")
        model.save(model_path)
        print(f"   Modele sauvegarde dans: {model_path}")
        
        # Logger le modele dans MLflow
        mlflow.keras.log_model(model, "model")
        
    print("\n" + "=" * 50)
    print("ENTRAINEMENT TERMINE AVEC SUCCES!")
    print("=" * 50)
    
    return model, history


if __name__ == "__main__":
    train_model()