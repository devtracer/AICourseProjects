import tkinter as tk
from tkinter import messagebox
import numpy as np
from numba import njit

@njit
def matrix_multiply(A: np.ndarray, B: np.ndarray) -> np.ndarray:
    rows_A, cols_A = A.shape
    rows_B, cols_B = B.shape
    if cols_A != rows_B:
        raise ValueError(f"Incompatible shapes for multiplication: {A.shape} and {B.shape}")
    product = np.zeros((rows_A, cols_B))
    for row in range(rows_A):
        for col in range(cols_B):
            sum_value = 0.0
            for k in range(cols_A):
                sum_value += A[row, k] * B[k, col]
            product[row, col] = sum_value
    return product

def collect_matrix(entries, rows, cols):
    """
    Collects the matrix values from the grid of entry widgets.
    """
    try:
        matrix = []
        for i in range(rows):
            row = []
            for j in range(cols):
                value = entries[i][j].get()
                row.append(int(value))
            matrix.append(row)
        return np.array(matrix)
    except ValueError:
        raise ValueError("All entries must be valid integers.")

def handle_calculation():
    try:
        # Collect matrices from entry widgets
        A = collect_matrix(entries_A, rows_A.get(), cols_A.get())
        B = collect_matrix(entries_B, rows_B.get(), cols_B.get())

        # Perform multiplication
        C = matrix_multiply(A, B)

        # Display result
        result_window = tk.Toplevel(root)
        result_window.title("Resulting Matrix C")
        result_label = tk.Label(result_window, text=f"Resulting Matrix C:\n{C}")
        result_label.pack(padx=10, pady=10)
    except ValueError as e:
        messagebox.showerror("Input Error", f"Error: {e}")
    except Exception as e:
        messagebox.showerror("Unexpected Error", f"An error occurred: {e}")

def create_matrix_inputs(frame, rows_var, cols_var, entries_var):
    """
    Creates a grid of entry widgets for the matrix input.
    """
    try:
        # Clear previous widgets
        for widget in frame.winfo_children():
            widget.destroy()

        rows = rows_var.get()
        cols = cols_var.get()

        entries_var.clear()
        for i in range(rows):
            row_entries = []
            for j in range(cols):
                entry = tk.Entry(frame, width=5)
                entry.grid(row=i, column=j, padx=5, pady=5)
                row_entries.append(entry)
            entries_var.append(row_entries)
    except Exception as e:
        messagebox.showerror("Error", f"An error occurred: {e}")

# GUI setup
root = tk.Tk()
root.title("Matrix Multiplication")

# Input for matrix A
frame_A = tk.LabelFrame(root, text="Matrix A", padx=10, pady=10)
frame_A.pack(padx=10, pady=10, fill="x")

rows_A = tk.IntVar(value=2)
cols_A = tk.IntVar(value=2)
entries_A = []

tk.Label(frame_A, text="Rows:").grid(row=0, column=0, sticky="w")
tk.Entry(frame_A, textvariable=rows_A, width=5).grid(row=0, column=1)
tk.Label(frame_A, text="Columns:").grid(row=0, column=2, sticky="w")
tk.Entry(frame_A, textvariable=cols_A, width=5).grid(row=0, column=3)
tk.Button(frame_A, text="Set Dimensions", command=lambda: create_matrix_inputs(frame_A_entries, rows_A, cols_A, entries_A)).grid(row=0, column=4)

frame_A_entries = tk.Frame(frame_A)
frame_A_entries.grid(row=1, column=0, columnspan=5)

# Input for matrix B
frame_B = tk.LabelFrame(root, text="Matrix B", padx=10, pady=10)
frame_B.pack(padx=10, pady=10, fill="x")

rows_B = tk.IntVar(value=2)
cols_B = tk.IntVar(value=2)
entries_B = []

tk.Label(frame_B, text="Rows:").grid(row=0, column=0, sticky="w")
tk.Entry(frame_B, textvariable=rows_B, width=5).grid(row=0, column=1)
tk.Label(frame_B, text="Columns:").grid(row=0, column=2, sticky="w")
tk.Entry(frame_B, textvariable=cols_B, width=5).grid(row=0, column=3)
tk.Button(frame_B, text="Set Dimensions", command=lambda: create_matrix_inputs(frame_B_entries, rows_B, cols_B, entries_B)).grid(row=0, column=4)

frame_B_entries = tk.Frame(frame_B)
frame_B_entries.grid(row=1, column=0, columnspan=5)

# Calculate Button
calculate_button = tk.Button(root, text="Multiply Matrices", command=handle_calculation)
calculate_button.pack(pady=10)

root.mainloop()
