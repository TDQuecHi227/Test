import tkinter as tk
from tkinter import font
from tkinter import simpledialog
import pandas as pd
# from draw_chart import draw_bar_chart, draw_pie_chart, draw_line_chart

window = tk.Tk()
window.title("Oscar Movie")
window.configure(bg='#1E1E1E')
window.state("zoomed")

title_font = font.Font(family="Helvetica", size=22, weight="bold")
button_font = font.Font(family="Helvetica", size=10, weight="bold")

title_label = tk.Label(window, text="Tác Phẩm Điện Ảnh Được Vinh Danh Tại Oscar", font=title_font, fg="#FFD700", bg="#1E1E1E")
title_label.pack(pady=10)

button_frame = tk.Frame(window, bg='#1E1E1E')
button_frame.pack(side="left", fill="y", padx=20, pady=10, expand=False)

def on_enter(e):
    e.widget['bg'] = "#FFD700"

def on_leave(e):
    e.widget['bg'] = "#2E2E2E"

def print_chart():
    file_path = 'oscar.csv'
    data = pd.read_csv(file_path)
    
    for widget in display_area.winfo_children():
        widget.destroy()
    
    chart_type = tk.simpledialog.askstring("Chọn Biểu Đồ", "Nhập loại biểu đồ muốn vẽ:\n1. Biểu đồ cột\n2. Biểu đồ tròn\n3. Biểu đồ đường")
    if chart_type == '1':
        draw_bar_chart(data, display_area)
    elif chart_type == '2':
        draw_pie_chart(data, display_area)
    elif chart_type == '3':
        draw_line_chart(data, display_area)
    else:
        print("Lựa chọn không hợp lệ!")

def add_movie():
    add_window = tk.Toplevel(window)
    add_window.title("Thêm Phim")
    add_window.configure(bg="#1E1E1E")

    #Nhãn và ô nhập ID phim
    tk.Label(add_window, text="ID Phim:", fg="#FFD700", bg="#1E1E1E").grid(row=0, column=0, padx=10, pady=10)
    movie_id_entry = tk.Entry(add_window, width=30)
    movie_id_entry.grid(row=0, column=1, padx=10, pady=10)
    
    # Nhãn và ô nhập tên phim
    tk.Label(add_window, text="Tên Phim:", fg="#FFD700", bg="#1E1E1E").grid(row=1, column=0, padx=10, pady=10)
    movie_title_entry = tk.Entry(add_window, width=30)
    movie_title_entry.grid(row=1, column=1, padx=10, pady=10)

    # Nhãn và ô nhập năm phim
    tk.Label(add_window, text="Năm:", fg="#FFD700", bg="#1E1E1E").grid(row=2, column=0, padx=10, pady=10)
    movie_year_entry = tk.Entry(add_window, width=30)
    movie_year_entry.grid(row=2, column=1, padx=10, pady=10)
    
    #Nhãn và ô nhập số giải thưởng của phim
    tk.Label(add_window, text="Giải Thưởng: ", fg="#FFD700", bg="#1E1E1E").grid(row=3, column=0, padx=10, pady=10)
    movie_award_entry = tk.Entry(add_window, width=30)
    movie_award_entry.grid(row=3, column=1, padx=10, pady=10)
    
    #Nhãn và ô nhập số lần đề cử cúa phim
    tk.Label(add_window, text="Đề cử:", fg="#FFD700", bg="#1E1E1E").grid(row=4, column=0, padx=10, pady=10)
    movie_nomination_entry = tk.Entry(add_window, width=30)
    movie_nomination_entry.grid(row=4, column=1, padx=10, pady=10)
    

    # Hàm xử lý khi nhấn nút "Thêm"
    def save_movie():
        # Lấy giá trị từ các ô nhập
        movie_id = movie_id_entry.get()
        movie_title = movie_title_entry.get()
        movie_year = movie_year_entry.get()
        moive_award = movie_award_entry.get()
        movie_nomination = movie_nomination_entry.get()

        # Kiểm tra dữ liệu hợp lệ
        if not movie_title or not movie_year.isdigit() or not movie_id.isdigit() or not moive_award.isdigit() or not movie_nomination.isdigit():
            tk.messagebox.showerror("Lỗi", "Vui lòng nhập tên phim, năm, ID, giải thưởng, đề cử không hợp lệ")
            return

        # Đọc dữ liệu hiện tại từ file CSV
        file_path = 'oscar.csv'
        try:
            data = pd.read_csv(file_path)
        except FileNotFoundError:
            data = pd.DataFrame(columns=['ID', 'Film', 'Year', 'Award', 'Nomination'])

        # Thêm dữ liệu mới vào DataFrame
        new_row = {'ID': movie_id, 'Film': movie_title, 'Year': int(movie_year), 'Award' : int(moive_award), 'Nomination' : int(movie_nomination)}
        data = pd.concat([data, pd.DataFrame([new_row])], ignore_index=True)

        # Ghi dữ liệu trở lại file CSV
        data.to_csv(file_path, index=False)

        # Thông báo thành công và đóng cửa sổ thêm phim
        tk.messagebox.showinfo("Thành công", "Phim đã được thêm thành công!")
        add_window.destroy()

    # Nút "Thêm"
    add_button = tk.Button(add_window, text="Thêm", command=save_movie, bg="#2E2E2E", fg="#FFD700", width=15)
    add_button.grid(row=5, column=0, columnspan=2, pady=10)


def delete_movie():
    delete_window = tk.Toplevel(window)
    delete_window.title("Xóa Phim")
    delete_window.configure(bg="#1E1E1E")
    
    #Nhãn và ô nhập ID phim
    tk.Label(delete_window, text="ID Phim:", fg="#FFD700", bg="#1E1E1E").grid(row=0, column=0, padx=10, pady=10)
    movie_id_entry = tk.Entry(delete_window, width=30)
    movie_id_entry.grid(row=0, column=1, padx=10, pady=10)
    
    def delete_selected_movie():
        movie_id = movie_id_entry.get()
        
        if not movie_id.isdigit():
            tk.messagebox.showerror("Lỗi", "Vui lòng nhập ID hợp lệ")
            return

        # Đọc dữ liệu từ file CSV
        file_path = 'oscar.csv'
        try:
            data = pd.read_csv(file_path)
        except FileNotFoundError:
            tk.messagebox.showerror("Lỗi", "Không tìm thấy file dữ liệu.")
            return
        
        data = data[data['ID'] != int(movie_id)]
        
        if movie_id and data.empty:
            tk.messagebox.showerror("Lỗi", "Không tìm thấy phim với ID này.")
            return
        
        if not data.empty:
            data.to_csv(file_path, index=False)
            tk.messagebox.showinfo("Thành công", "Phim đã được xóa thành công!")
        else:
            tk.messagebox.showerror("Lỗi", "Không có phim nào để xóa.")
        
        delete_window.destroy()
        
    add_button = tk.Button(delete_window, text="Xóa", command=delete_selected_movie, bg="#2E2E2E", fg="#FFD700", width=15)
    add_button.grid(row=5, column=0, columnspan=2, pady=10)

def edit_movie():
    print("Edit")

def search_movie():
    print("Search")

buttons = [
    ("Add", add_movie),
    ("Delete", delete_movie),
    ("Chart", print_chart),
    ("Edit", edit_movie),
    ("Search", search_movie)
]

for text, command in buttons:
    button = tk.Button(button_frame, text=text, font=button_font, bg="#2E2E2E", fg="#FFD700",
                    width=15, height=2, bd=0, relief="solid", cursor="hand2",
                    activebackground="#FFD700", activeforeground="#1E1E1E", command=command)
    button.pack(pady=5, fill="x")
    button.bind("<Enter>", on_enter)
    button.bind("<Leave>", on_leave)

display_area = tk.Frame(window, bg="#333333", relief="solid", borderwidth=1)
display_area.pack(pady=10, padx=10, fill="both", expand=True)

window.mainloop()