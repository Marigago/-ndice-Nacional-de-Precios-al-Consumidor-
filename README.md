
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

> **Nota:** Aquí se deben incluir imágenes y explicar las decisiones tomadas.

---

## 🤖 Modelo SARIMA

Se utilizó un modelo SARIMA porque:
- La serie presenta **estacionalidad mensual clara**.
- Permite capturar tanto patrones **cíclicos** como **tendenciales**.

**Ecuación general:**
\[
SARIMA(p,d,q)(P,D,Q,s)
\]

**Parámetros seleccionados:**
| Parámetro | Valor | Justificación |
|------------|-------|---------------|
| p          | ?     | Basado en PACF |
| d          | ?     | Basado en pruebas ADF/KPSS |
| q          | ?     | Basado en ACF |
| P          | ?     | Estacionalidad detectada |
| D          | ?     | Estacionalidad y KPSS |
| Q          | ?     | Basado en ACF estacional |
| s          | 12    | Mensualidad |

---

## 📊 Resultados de la Predicción

Gráfica generada con **Plotly** mostrando:
- Datos históricos.
- Predicciones para los próximos 12 meses.

> Aquí se incluye el gráfico interactivo.

---

## 🧮 Evaluación del Modelo

Se calculó el **MAPE (Mean Absolute Percentage Error)** utilizando los últimos 12 valores como datos de validación:

\[
MAPE = \frac{100\%}{n} \sum_{t=1}^{n} \left| \frac{y_t - \hat{y}_t}{y_t} \right|
\]

| Métrica  | Valor |
|-----------|-------|
| MAPE (%)  | ??    |

---

## 📌 Conclusiones
- Resumen de la calidad del modelo.
- Posibles causas de error, como:
  - Volatilidad en el mercado.
  - Shocks externos (políticos, económicos, etc.).
  - Limitaciones del modelo SARIMA.

---

## 🏆 Criterios de Evaluación

| Criterio             | Descripción                                         | Peso |
|----------------------|-----------------------------------------------------|------|
| Ejecución del código | Flujo completo sin errores, gráficas y predicciones | 40%  |
| Explicación          | Justificación de parámetros y claridad en README    | 50%  |
| Desempeño MAPE       | Precisión en la predicción                          | 20%  |
