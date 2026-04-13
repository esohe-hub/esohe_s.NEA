import tkinter as tk

def launch_app():
    window = tk.Tk()
    window.title("Movie Recommendation System")
    window.geometry("600x400")
    window.resizable(False, False)

    # --- Button functions ---
    def browse_movies():
        print("Browse Movies clicked")

    def search_movies():
        print("Search Movies clicked")

    def filter_movies():
        print("Filter Movies clicked")

    def rate_movies():
        print("Rate Movies clicked")

    def get_recommendations():
        print("Get Recommendations clicked")

    # --- Title label ---
    title_label = tk.Label(window, text="Movie App", font=("Georgia", 20))
    title_label.pack(pady=20)

    # --- Buttons ---
    tk.Button(window, text="Browse Movies", command=browse_movies).pack(pady=5)
    tk.Button(window, text="Search Movies", command=search_movies).pack(pady=5)
    tk.Button(window, text="Filter Movies", command=filter_movies).pack(pady=5)
    tk.Button(window, text="Rate Movies", command=rate_movies).pack(pady=5)
    tk.Button(window, text="Get Recommendations", command=get_recommendations).pack(pady=5)

    window.mainloop()