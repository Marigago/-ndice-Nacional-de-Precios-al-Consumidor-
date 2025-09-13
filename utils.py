import numpy as np

def calcular_mape(y_true, y_pred):
    """
    Calcula el MAPE (Mean Absolute Percentage Error).

    Parámetros:
    y_true : array-like
        Serie original (valores reales).
    y_pred : array-like
        Serie predicha (valores pronosticados).

    Retorna:
    float
        El MAPE en porcentaje.
    """
    y_true, y_pred = np.array(y_true), np.array(y_pred)
    
    # Evitar división por cero
    mask = y_true != 0
    mape = np.mean(np.abs((y_true[mask] - y_pred[mask]) / y_true[mask])) * 100
    
    return round(mape, 4)


def calcular_smape(y_true, y_pred):
    """
    Calcula el SMAPE (Symmetric Mean Absolute Percentage Error).

    Parámetros:
    y_true : array-like
        Serie original (valores reales).
    y_pred : array-like
        Serie predicha (valores pronosticados).

    Retorna:
    float
        El SMAPE en porcentaje.
    """
    y_true, y_pred = np.array(y_true), np.array(y_pred)
    
    # Calcular denominador como la media absoluta
    denominator = (np.abs(y_true) + np.abs(y_pred)) / 2
    
    # Evitar división por cero
    mask = denominator != 0
    smape = np.mean(np.abs(y_true[mask] - y_pred[mask]) / denominator[mask]) * 100
    
    return round(smape, 4)
