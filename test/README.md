```markdown
# Predicción de Aceptación de Préstamos Personales (SVM)

**Autor:** Lennen Santos Mejía  
**Programa:** Maestría en Ciencia de Datos e Inteligencia Artificial  

## 1. Descripción del Proyecto
Proyecto de Machine Learning diseñado para predecir si un cliente bancario aceptará una oferta de préstamo personal, estructurado mediante un pipeline reproducible, evaluación de controles preventivos y validación de calidad de datos. El objetivo es optimizar el esfuerzo de telemarketing y el retorno de inversión (ROI) de la campaña institucional.

## 2. Instalación y Configuración
Se requiere un entorno de Python (recomendado 3.10+) y la instalación de las dependencias base definidas en el proyecto:

```bash
pip install -r requirements.txt
pip install pytest kagglehub

```

## 3. Procedencia y Extracción de Datos

La obtención del dataset está encapsulada para garantizar la reproducibilidad del entorno sin exponer los datos crudos en el repositorio.

* **Origen:** API de Kaggle (`ahmadrafiee/bank-personal-loan`)
* **Licencia:** CC0: Public Domain
* **Extracción:** Ejecuta el módulo de descarga con el siguiente comando:

```bash
python src/inf8239_u01/data.py

```

El archivo se estructurará automáticamente en la ruta local `notebooks/data/raw/dataset.csv`.

## 4. Target, Métricas y Pruebas (Data Contract)

* **Variable Objetivo:** `Personal Loan` (1 = Acepta el préstamo, 0 = Rechaza).
* **Métrica Principal:** Macro F1-Score y Recall. Seleccionadas estratégicamente para penalizar los falsos negativos ante el severo desbalanceo de clases (solo 9.6% de aceptación histórica), mitigando el costo de oportunidad de omitir a un prospecto viable.
* **Auditoría de Datos:** Antes del entrenamiento, el pipeline valida la integridad de la base de datos (ausencia de nulos y existencia de variables críticas) mediante pruebas automatizadas. Para ejecutar el control, utiliza:

```bash
$env:PYTHONPATH="src"
python -m pytest -q

```

---

## 5. Ficha del Dataset y Matriz de Selección

| Criterio | Candidato A: Bank Personal Loan (Seleccionado) | Candidato B: Credit Card Fraud |
| --- | --- | --- |
| **Procedencia** | Kaggle (`ahmadrafiee`) | Kaggle (`jacklizhi`) |
| **Dominio** | Analítica de Retail Banking y Propensión | Detección de Anomalías |
| **Filas/columnas** | 5,000 filas / 14 columnas | 284,807 filas / 31 columnas |
| **Target y clases** | `Personal Loan` (1: Acepta, 0: Rechaza) | `Class` (1: Fraude, 0: Genuina) |
| **Riesgo de fuga** | Bajo (Variables independientes previas) | Bajo (Variables transformadas por PCA) |

---

## 6. Diccionario de Datos y Matriz de Riesgos

| Variable | Significado | Unidad / Tipo | Fuente | Transformación Prevista | Riesgo Operacional |
| --- | --- | --- | --- | --- | --- |
| **Personal Loan** | (Target) Si el cliente aceptó el préstamo | Binario (0/1) | CRM | Ninguna | Riesgo de desbalanceo (9.6% positivos). |
| **Income** | Ingresos anuales del cliente | Dólares ($000) | BBDD | Escalar (`StandardScaler`). | Asimetría derecha (outliers de altos ingresos). |
| **CCAvg** | Gasto promedio mensual en tarjetas | Texto / `str` | Transaccional | Reemplazar `/` por `.` y convertir a `float`. | Fallo de tipo de dato (Type error) en el pipeline. |
| **Age / Experience** | Edad y años de experiencia | Años (Entero) | BBDD | Escalar (`StandardScaler`). | Colinealidad alta esperada. |
| **Education** | Nivel educativo (1: Grado, 2: Post, 3: Avanzado) | Categórica | BBDD | Evaluar variables dummy. | Datos desactualizados si el perfil cambió. |
| **ZIP Code** | Código postal del domicilio | Numérico | BBDD | Eliminar (`drop`). | Ruido algorítmico y sobreajuste geográfico. |
| **ID** | Identificador único del cliente | Numérico | Core | Eliminar (`drop`). | Fuga de información o memorización del modelo. |

---

## 7. Ejecución del Modelado

Ejecuta secuencialmente las celdas del archivo `notebooks/02_svm_prestamos.ipynb` para aplicar el preprocesamiento definido (limpieza de `CCAvg`, eliminación de identificadores y escalado) y entrenar los pipelines comparativos (Baseline Dummy Classifier vs. Support Vector Machine).

---

## 8. Conclusión Ejecutiva

El presente proyecto de laboratorio abordó la predicción de aceptación de préstamos personales estructurando un pipeline analítico integral bajo estrictos estándares de reproducibilidad. El objetivo central consistió en identificar prospectos de clientes optimizando el esfuerzo de marketing, donde el modelo debe maximizar la captación de la clase positiva minimizando el desperdicio operativo y el costo de oportunidad asociado a un bajo rendimiento predictivo.

Durante la fase de auditoría de esquema, se aplicaron evaluaciones de control interno para perfilar y mitigar riesgos en los datos crudos. El hallazgo de mayor impacto fue la variable `CCAvg` (gasto mensual en tarjetas), registrada originalmente con un formato de texto fraccionario. De no haberse intervenido, esta estructura habría generado un error de tipificación o una severa explosión de dimensionalidad durante la codificación categórica en el `ColumnTransformer`, representando un riesgo operacional clásico en la ingesta de sistemas de machine learning. Su saneamiento garantizó una matriz limpia de 5,000 registros, reforzada por la exclusión de identificadores (`ID`) y variables de ruido (`ZIP Code`) para prevenir fugas de información transaccional.

En la etapa de modelado, la ejecución de un `DummyClassifier` expuso la vulnerabilidad inherente del dataset: un desbalanceo extremo del 9.6% hacia la clase minoritaria, arrojando un F1-Score macro de 0.47. Al introducir una Máquina de Vectores de Soporte (SVM) con un kernel RBF, el rendimiento general se elevó a un F1-Score macro de 0.93. Aunque la precisión de la clase 1 alcanzó un 0.97, el recall de 0.79 en la iteración inicial refleja la necesidad algorítmica de integrar esquemas de optimización (`GridSearchCV`) y pesos compensatorios para alinear la sensibilidad del modelo a las metas de conversión de la gerencia de negocios.

Finalmente, el despliegue de un contrato de datos automatizado mediante `pytest` institucionalizó una capa de control preventivo dentro del flujo de trabajo. Validar estructuralmente la base de datos antes del paso de inferencia asegura que el ecosistema analítico sea resiliente y auditable, demostrando que el rigor en la gobernanza y control de los datos es tan crítico para el éxito corporativo como la sofisticación matemática del algoritmo predictivo.

```

```