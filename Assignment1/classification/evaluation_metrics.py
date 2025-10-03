import numpy as np

EPS = 1e-12  # 防分母零

def _binary_counts(y_true, y_pred):
    # remark: contigency table 混淆矩阵  
    """
    Compute contingency counts for a binary classification task with labels {0, 1}.

    Parameters
    ----------
    y_true : array-like of shape (n_samples,)
        Ground-truth binary labels (must be 0 or 1).
    y_pred : array-like of shape (n_samples,)
        Predicted binary labels (must be 0 or 1).；

    Returns
    -------
    tp : int
        True positives  (y_true == 1 and y_pred == 1).
    fp : int
        False positives (y_true == 0 and y_pred == 1).
    fn : int
        False negatives (y_true == 1 and y_pred == 0).
    tn : int
        True negatives  (y_true == 0 and y_pred == 0).
    """
    y_true = np.asarray(y_true).reshape(-1).astype(int)
    y_pred = np.asarray(y_pred).reshape(-1).astype(int)
    if y_true.shape[0] != y_pred.shape[0]:
        raise ValueError("y_true and y_pred must have the same length.")
    if not np.all(np.isin(y_true, (0, 1))) or not np.all(np.isin(y_pred, (0, 1))):
        raise ValueError("This template expects binary labels {0,1}.")
    # 这里用到了广播机制比较计算
    tp = int(np.sum((y_true == 1) & (y_pred == 1)))
    fp = int(np.sum((y_true == 0) & (y_pred == 1)))
    fn = int(np.sum((y_true == 1) & (y_pred == 0)))
    tn = int(np.sum((y_true == 0) & (y_pred == 0)))
    return tp, fp, fn, tn

def precision_score(y_true, y_pred):
    """Precision = TP / (TP + FP)"""
    tp, fp, _, _ = _binary_counts(y_true, y_pred)
    # =============== TODO (students) ===============
    precision = tp/(tp+fp)
    return precision
    # ===============================================
    # raise NotImplementedError("Implement precision_score")

def recall_score(y_true, y_pred):
    """Recall = TP / (TP + FN)"""
    tp, _, fn, _ = _binary_counts(y_true, y_pred)
    # =============== TODO (students) ===============
    recall = tp / (tp + fn)
    return recall
    # ===============================================
    # raise NotImplementedError("Implement recall_score")

def f1_score(y_true, y_pred):
    """F1 = 2 * (P * R) / (P + R)"""
    # =============== TODO (students) ===============
    precision = precision_score(y_true,y_pred)
    recall = recall_score(y_true,y_pred)
    f_one = (2*precision*recall) / (recall+precision)
    return f_one
    # ===============================================
    # raise NotImplementedError("Implement f1_score")
