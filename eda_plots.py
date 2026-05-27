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

    # Columns of interest
    cols_needed = [
        "Core Beam Power",
        "Laser Speed",
        "Tensile strength (Welds)",
        "Electrical resistance/conductivity"
    ]

    df = df[cols_needed]
    for col in cols_needed:
     df[col] = df[col].replace("-", np.nan)
     df[col] = pd.to_numeric(df[col], errors="coerce")

    for col in cols_needed:
        df[col] = pd.to_numeric(df[col], errors="coerce")

    df = df.dropna().reset_index(drop=True)

    print("Data used for plotting:", df.shape)

    # 1. Core Beam Power vs Tensile Strength
    plt.figure()
    plt.scatter(df["Core Beam Power"], df["Tensile strength (Welds)"])
    plt.xlabel("Core Beam Power")
    plt.ylabel("Tensile Strength")
    plt.title("Core Beam Power vs Tensile Strength")
    plt.tight_layout()
    plt.show()

    # 2. Core Beam Power vs Electrical Resistance
    plt.figure()
    plt.scatter(df["Core Beam Power"], df["Electrical resistance/conductivity"])
    plt.xlabel("Core Beam Power")
    plt.ylabel("Electrical Resistance / Conductivity")
    plt.title("Core Beam Power vs Electrical Resistance")
    plt.tight_layout()
    plt.show()

    # 3. Laser Speed vs Tensile Strength
    plt.figure()
    plt.scatter(df["Laser Speed"], df["Tensile strength (Welds)"])
    plt.xlabel("Laser Speed")
    plt.ylabel("Tensile Strength")
    plt.title("Laser Speed vs Tensile Strength")
    plt.tight_layout()
    plt.show()

    # 4. Laser Speed vs Electrical Resistance
    plt.figure()
    plt.scatter(df["Laser Speed"], df["Electrical resistance/conductivity"])
    plt.xlabel("Laser Speed")
    plt.ylabel("Electrical Resistance / Conductivity")
    plt.title("Laser Speed vs Electrical Resistance")
    plt.tight_layout()
    plt.show()


if __name__ == "__main__":
    main()
