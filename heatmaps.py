import pandas as pd
import numpy as np
import matplotlib.pyplot as plt


def make_unique(cols):
    seen = {}
    new_cols = []
    for c in cols:
        if c not in seen:
            seen[c] = 0
            new_cols.append(c)
        else:
            seen[c] += 1
            new_cols.append(f"{c}_{seen[c]}")
    return new_cols


def main():
    file_path = r"C:\Users\hp\Downloads\DesignCredit\DesignCredit\LaserWelding dataset.xlsx"

    df_raw = pd.read_excel(file_path, header=1)
    df = df_raw.copy()
    df.columns = df.iloc[0]
    df = df.drop(index=0).reset_index(drop=True)
    df.columns = make_unique(df.columns)

    # Parameters used for heatmaps
    heatmap_cols = [
        "Core Beam Power",
        "Ring Beam Power",
        "Laser Speed",
        "Mat1_thickness",
        "Mat2_thickness",
        "Mat1_microhardness",
        "Mat2_microhardness",
        "Electrical resistance/conductivity",
        "Tensile strength (Welds)"
    ]

    df = df[heatmap_cols]

    for col in heatmap_cols:
        df[col] = df[col].replace("-", np.nan)
        df[col] = pd.to_numeric(df[col], errors="coerce")
    df = df.dropna().reset_index(drop=True)

    print("Data used for heatmaps:", df.shape)

    #heatmap_1: full correlation heatmap
    corr = df.corr()

    plt.figure(figsize=(10, 8))
    plt.imshow(corr)
    plt.colorbar(label="Correlation Coefficient")

    plt.xticks(range(len(corr.columns)), corr.columns, rotation=90)
    plt.yticks(range(len(corr.columns)), corr.columns)

    # Annotate values
    for i in range(len(corr.columns)):
        for j in range(len(corr.columns)):
            plt.text(j, i, f"{corr.iloc[i, j]:.2f}",
                     ha="center", va="center", fontsize=8)

    plt.title("Correlation Heatmap of Welding Parameters and Tensile Strength")
    plt.tight_layout()
    plt.show()

    #heatmap_2: process parametrs vs tensile strength 
    process_cols = [
        "Core Beam Power",
        "Ring Beam Power",
        "Laser Speed",
        "Electrical resistance/conductivity"
    ]

    corr_process = df[process_cols + ["Tensile strength (Welds)"]].corr()

    plt.figure(figsize=(6, 5))
    plt.imshow(corr_process.loc[process_cols, ["Tensile strength (Welds)"]])
    plt.colorbar(label="Correlation Coefficient")

    plt.xticks([0], ["Tensile strength"])
    plt.yticks(range(len(process_cols)), process_cols)

    for i in range(len(process_cols)):
        value = corr_process.loc[process_cols[i], "Tensile strength (Welds)"]
        plt.text(0, i, f"{value:.2f}", ha="center", va="center")

    plt.title("Process Parameters vs Tensile Strength")
    plt.tight_layout()
    plt.show()

