from sklearn.metrics import classification_report, roc_auc_score, confusion_matrix
import matplotlib.pyplot as plt
import seaborn as sns

def print_classification_report(y_true, y_pred):
    print(classification_report(y_true, y_pred))

def print_roc_auc(y_true, y_probs):
    auc = roc_auc_score(y_true, y_probs)
    print(f"ROC AUC Score: {auc:.4f}")

def plot_confusion_matrix(y_true, y_pred):
    cm = confusion_matrix(y_true, y_pred)
    sns.heatmap(cm, annot=True, fmt='d', cmap='Blues')
    plt.xlabel("Predicted")
    plt.ylabel("Actual")
    plt.title("Confusion Matrix")
    plt.show()