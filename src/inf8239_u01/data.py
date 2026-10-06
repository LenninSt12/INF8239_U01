from pathlib import Path
import pandas as pd
import kagglehub
import glob
import os

def download_csv(source: str = "ahmadrafiee/bank-personal-loan", destination: str = "data/raw/dataset.csv") -> Path:
    """
    Descarga el dataset utilizando la API de Kaggle y lo guarda localmente.
    Se encapsula el procedimiento de la API según los requerimientos del laboratorio.
    """
    path = Path(destination)
    # Crear la carpeta data/raw si no existe
    path.parent.mkdir(parents=True, exist_ok=True)
    
    print(f"Descargando dataset desde la API de Kaggle: {source}...")
    # Descarga a través de la API encapsulada
    cache_dir = kagglehub.dataset_download(source)
    csv_files = glob.glob(os.path.join(cache_dir, "*.csv"))
    
    if not csv_files:
        raise ValueError("No se encontró ningún archivo CSV en la descarga de Kaggle.")
        
    # Leer de la caché y guardar en nuestro directorio estructurado
    frame = pd.read_csv(csv_files[0])
    
    if frame.empty:
        raise ValueError("El dataset descargado está vacío.")
        
    frame.to_csv(path, index=False)
    print(f"Dataset guardado reproduciblemente en: {path}")
    
    return path