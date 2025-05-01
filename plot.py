import matplotlib.pyplot as plt
import matplotlib.colors as mcolors
import pandas as pd
import numpy as np

data = {
    'Model': ['Logistic Regression', 'Decision Tree', 'Random Forest'],
    'F1 Score (yes)': [0.54, 0.53, 0.56],
    'Recall (yes)': [0.45, 0.48, 0.48],
    'Accuracy': [0.92, 0.91, 0.91]
}

df_metrics = pd.DataFrame(data)

cyan_light = mcolors.to_rgba("#ccf2f4")  # 浅青
cyan_mid = mcolors.to_rgba("#66cfd6")    # 中青
cyan_dark = mcolors.to_rgba("#2baeb7")   # 深青
cyan_colors = [cyan_light, cyan_mid, cyan_dark]

fig, ax = plt.subplots(figsize=(8, 6))
bar_width = 0.25
x = np.arange(len(df_metrics))

plt.bar(x - bar_width, df_metrics['F1 Score (yes)'], width=bar_width, color=cyan_colors[0], label='F1 Score (yes)')
plt.bar(x, df_metrics['Recall (yes)'], width=bar_width, color=cyan_colors[1], label='Recall (yes)')
plt.bar(x + bar_width, df_metrics['Accuracy'], width=bar_width, color=cyan_colors[2], label='Accuracy')

plt.xlabel('Model')
plt.ylabel('Score')
plt.title('Model Comparison: F1 Score, Recall, and Accuracy')
plt.xticks(ticks=x, labels=df_metrics['Model'], rotation=15)
plt.ylim(0, 1)
plt.legend()
plt.tight_layout()

plt.show()


data_rf = {
    'Model': ['Random Forest 1', 'Random Forest 2'],
    'F1 Score (yes)': [0.56, 0.64],
    'Recall (yes)': [0.48, 0.72],
    'Accuracy': [0.91, 0.91]
}

df_rf = pd.DataFrame(data_rf)

cyan_light = mcolors.to_rgba("#ccf2f4")
cyan_mid = mcolors.to_rgba("#66cfd6")
cyan_dark = mcolors.to_rgba("#2baeb7")
cyan_colors = [cyan_light, cyan_mid, cyan_dark]

fig, ax = plt.subplots(figsize=(7, 6))
bar_width = 0.25
x = np.arange(len(df_rf))

plt.bar(x - bar_width, df_rf['F1 Score (yes)'], width=bar_width, color=cyan_colors[0], label='F1 Score (yes)')
plt.bar(x, df_rf['Recall (yes)'], width=bar_width, color=cyan_colors[1], label='Recall (yes)')
plt.bar(x + bar_width, df_rf['Accuracy'], width=bar_width, color=cyan_colors[2], label='Accuracy')

plt.xlabel('Model')
plt.ylabel('Score')
plt.title('Random Forest vs. Tuned Random Forest (RF2)')
plt.xticks(ticks=x, labels=df_rf['Model'], rotation=15)
plt.ylim(0, 1)
plt.legend()
plt.tight_layout()

plt.show()

