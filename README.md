# 📈 Pronóstico INPP (excluyendo petróleo) - SARIMA
 
## 📝 Descripción del Proyecto
Este proyecto tiene como objetivo **predecir la evolución del Índice Nacional de Precios Productor (INPP) excluyendo petróleo** en México durante los próximos 12 meses.
 
Utilizamos datos abiertos obtenidos mediante la **API de INEGI** y construimos un modelo **SARIMA** para realizar los pronósticos.
 
**Serie utilizada:**
- **Nombre:** Índice Nacional de Precios Productor excluyendo petróleo  
- **ID:** 910493  
- **Frecuencia:** Mensual  
- **Pregunta guía:** *"¿Cómo se comportará el INPP excluyendo petróleo en los próximos 12 meses?"*
 
---
 
## 📂 Estructura del Proyecto
```
├── equipo2.ipynb         # Notebook con el desarrollo completo
├── README.md              # Documento de explicación y resultados
└── data/                  # Carpeta con datos descargados (opcional)
```
 
---
 
## ⚙️ Requerimientos
 
Para ejecutar este proyecto, instala las siguientes librerías:
 
```bash
pip install pandas numpy statsmodels plotly requests
```
 
---
 
## 🔗 Conexión a la API de INEGI
 
Se utilizó la API de INEGI para descargar la serie **910493**.  
El flujo de conexión incluye:
 
1. Conexión vía `requests` utilizando el token proporcionado por INEGI.
2. Procesamiento de la respuesta JSON para convertirla en un DataFrame.
3. Limpieza y preparación de la serie para el modelo.
 
---
 
## 🔍 Análisis Exploratorio
 
1. **Visualización inicial** de la serie para identificar tendencias y estacionalidad.
2. **Pruebas de estacionariedad:**
   - ADF (Augmented Dickey-Fuller)
   - KPSS (Kwiatkowski–Phillips–Schmidt–Shin)
3. **Gráficas ACF y PACF** para definir órdenes iniciales de:
   - (p, d, q) → Componente ARIMA
   - (P, D, Q, s) → Componente estacional
### Insights
- Algunos gráficos se abren en el navegador.
- Se utilizarán sólo datos de la serie a partir del año 2018, debido a que al hacer una descomposición STL es el punto en donde los picos cambian de forma en la parte de estacionalidad.
 
** gráfica de descomposición STL en el notebook
 
- Tanto ADF como KPSS dieron resultados de que la serie no es estacionaria, por lo que se diferenciará una vez y se realizarán ambas pruebas otra vez.
##### === Prueba ADF (desde 2018) ===
- Estadístico: -0.5484
- p-valor: 0.8822
- Hipótesis nula: La serie NO es estacionaria
 
##### === Prueba KPSS (desde 2018) ===
- Estadístico: 1.5786
- p-valor: 0.0100
- Hipótesis nula: La serie SÍ es estacionaria
 
** gráfica de serie diferenciada en el notebook
 
##### === Prueba ADF (serie diferenciada) ===
Estadístico: -6.0498
p-valor: 0.0000
 
##### === Prueba KPSS (serie diferenciada) ===
Estadístico: 0.0838
p-valor: 0.1000
 
> **Nota:** Después de diferenciar, hacemos las pruebas estadísticas y la serie ya es estacionaria.
 
- Con las gráficas ACF y PACF elegimos p, q y P,Q:
   - La ACF cae rápido después del rezago 1, con un pico significativo al rezago 1. Esto sugiere la presencia de un componente de media móvil (q=1).
   - La PACF también muestra un pico significativo en el rezago 1 y luego cae dentro de las bandas. Esto indica un componente autorregresivo simple (p=1).
   - No se ven rezagos largos dominantes que obliguen a meter un AR estacional evidente.
   - Modelo sugerido: (p,d,q) = (1,1,1) como punto de partida.
 
---
 
## 🤖 Modelo SARIMA
 
Se utilizó un modelo SARIMA porque:
- La serie presenta **estacionalidad mensual clara**.
- Permite capturar tanto patrones **cíclicos** como **tendenciales**.
 
**Ecuación general:**
\[
SARIMA(p,d,q)(P,D,Q,s)
\]
 
- Se probaron distintos modelos, cambiando únicamente los componentes (P,D,Q):
   - order=(1, 1, 1) seasonal_order=(0, 1, 1, 12)  AIC=431.0
   - order=(1, 1, 1) seasonal_order=(1, 1, 1, 12)  AIC=439.0
   - order=(1, 1, 1) seasonal_order=(0, 0, 0, 12)  AIC=455.6
   - order=(1, 1, 1) seasonal_order=(1, 1, 0, 12)  AIC=526.2
   - order=(1, 1, 1) seasonal_order=(0, 1, 0, 12)  AIC=586.9
 
**Parámetros seleccionados:**
| Parámetro | Valor | Justificación |
|------------|-------|---------------|
| p          | 1     | Basado en PACF |
| d          | 1     | Basado en pruebas ADF/KPSS |
| q          | 1     | Basado en ACF |
| P          | 0     | Estacionalidad detectada |
| D          | 1     | Estacionalidad y KPSS |
| Q          | 1     | Basado en ACF estacional |
| s          | 12    | Mensualidad |
 
---
 
## 🧮 Evaluación del Modelo
 
Se calculó el **MAPE (Mean Absolute Percentage Error)** utilizando los últimos 12 valores como datos de validación:
 
\[
MAPE = \frac{100\%}{n} \sum_{t=1}^{n} \left| \frac{y_t - \hat{y}_t}{y_t} \right|
\]
 
Entrenamiento: 2018-01 → 2024-08
Prueba: 2024-09 → 2025-08
 
Tamaño train: 80  | Tamaño test: 12
 
| Métrica  | Valor |
|-----------|-------|
| MAPE (%)  | 2.32  |
 
---
 
## 📌 Conclusiones
- Con MAPE=2.32%, la exactitud ≈ 97.7%. ✅
 
---
 
## 🏆 Criterios de Evaluación
 
| Criterio             | Descripción                                         | Peso |
|----------------------|-----------------------------------------------------|------|
| Ejecución del código | Flujo completo sin errores, gráficas y predicciones | 40%  |
| Explicación          | Justificación de parámetros y claridad en README    | 50%  |
| Desempeño MAPE       | Precisión en la predicción                          | 20%  |
