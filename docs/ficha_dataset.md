# Ficha del dataset

- **Dominio:** Analítica de Retail Banking y Propensión de Compra.
- **Unidad de análisis:** El perfil individual de un cliente captador del banco.
- **Decisión:** Determinar si los recursos de una campaña de telemarketing deben invertirse en un cliente de pasivos específico para ofrecerle un producto de crédito personal, optimizando así el presupuesto.
- **Target:** `Personal Loan` (1 = Acepta el préstamo personal, 0 = Rechaza la oferta).
- **Error más costoso:** Un falso positivo. Gastar esfuerzo operativo, costo de llamadas y tiempo de analistas contactando a un cliente que no tiene probabilidad matemática de conversión, reduciendo el retorno de inversión (ROI) de la campaña.
- **Usuario:** Departamento de Marketing Retail y Gerencia de Negocios.

---

## Matriz de Selección

| Criterio | Candidato A: Bank Personal Loan | Candidato B: Credit Card Fraud |
| :--- | :--- | :--- |
| **Procedencia** | Kaggle (`ahmadrafiee`) | Kaggle (`jacklizhi`) |
| **Licencia** | CC0: Public Domain | Database Contents License (DbCL) |
| **Filas/columnas** | 5,000 filas / 14 columnas | 284,807 filas / 31 columnas |
| **Target y clases** | `Personal Loan` (1: Acepta, 0: Rechaza) | `Class` (1: Fraude, 0: Genuina) |
| **Ausentes** | 0 valores nulos[cite: 23] | 0 valores nulos |
| **Riesgo de fuga** | Bajo (Variables independientes previas al préstamo) | Bajo (Variables transformadas por PCA) |

---

## Diccionario de Datos y Auditoría

| Variable | Significado | Unidad / Tipo | Fuente | Momento de Disponibilidad | Transformación Prevista | Riesgo Operacional |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| **Personal Loan** | (Target) Si el cliente aceptó el préstamo | Binario (0/1) | CRM del Banco | Post-Campaña | Ninguna (Target) | Riesgo de desbalanceo (Solo 9.6% de casos positivos). |
| **Income** | Ingresos anuales del cliente | Dólares ($000) | BBDD Clientes | Pre-Campaña | Escalar (`StandardScaler`). | Posible asimetría derecha (outliers de altos ingresos). |
| **CCAvg** | Gasto promedio mensual en tarjetas | Texto / `str` (formato fraccionario)[cite: 21, 23] | Transaccional | Pre-Campaña | Reemplazar `/` por `.` y convertir a `float64`. Escalar. | Fallo de tipo de dato (`Type error`) en el pipeline si no se limpia. |
| **Age / Experience** | Edad y años de experiencia profesional | Años (Entero) | BBDD Clientes | Pre-Campaña | Escalar (`StandardScaler`). | Colinealidad alta esperada entre edad y experiencia. |
| **Education** | Nivel educativo (1: Grado, 2: Postgrado, 3: Avanzado) | Categórica (Ordinal) | BBDD Clientes | Pre-Campaña | Evaluar necesidad de variables dummy. | Datos desactualizados si el cliente mejoró su perfil académico. |
| **ZIP Code** | Código postal del domicilio | Numérico[cite: 23] | BBDD Clientes | Pre-Campaña | Eliminar (`drop`). | Ruido algorítmico y sobreajuste geográfico. |
| **ID** | Identificador único del cliente | Numérico[cite: 23] | Sistema Core | Pre-Campaña | Eliminar (`drop`). | Fuga de información o memorización del modelo. |