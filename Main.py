import tkinter as tk
from tkinter import messagebox
import pandas as pd
from Film import Film

# Danh sách chứa các đối tượng Film
film_list = []

# Hàm đọc dữ liệu từ file CSV
def load_data_from_csv():
    try:
        df = pd.read_csv('oscar.csv')
        for _, row in df.iterrows():
            film = Film(str(row['ID']), row['Film'], str(row['Year']), str(row['Award']), str(row['Nomination']))
            film_list.append(film)
            listbox_film.insert(tk.END, f"ID: {film.id} | {film.name} ({film.year}) - Giải thưởng: {film.award}, Đề cử: {film.nomination}")
        messagebox.showinfo("Thông báo", "Dữ liệu đã được tải thành công từ file CSV!")
    except Exception as e:
        messagebox.showerror("Lỗi", f"Đã xảy ra lỗi khi tải dữ liệu: {e}")

# Hàm thêm phim vào danh sách
def add_film():
    iD = entry_id.get()
    name = entry_name.get()
    year = entry_year.get()
    award = entry_award.get()
    nomination = entry_nomination.get()
    
    if not (iD and name and year and award and nomination):
        messagebox.showerror("Lỗi", "Vui lòng điền đầy đủ thông tin!")
        return
    
    film = Film(iD, name, year, award, nomination)
    film_list.append(film)
    listbox_film.insert(tk.END, f"ID: {film.id} | {film.name} ({film.year}) - Giải thưởng: {film.award}, Đề cử: {film.nomination}")
    
    clear_entries()
    update_csv()
    messagebox.showinfo("Thông báo", "Phim đã được thêm vào danh sách!")

# Hàm xóa phim khỏi danh sách dựa trên ID
def delete_film():
    selected_index = listbox_film.curselection()
    if not selected_index:
        messagebox.showwarning("Cảnh báo", "Vui lòng chọn một phim để xóa!")
        return

    selected_film = listbox_film.get(selected_index)
    film_id = selected_film.split(" | ")[0].split(": ")[1]

    for film in film_list:
        if film.id == film_id:
            film_list.remove(film)
            break

    listbox_film.delete(selected_index)
    update_csv()
    messagebox.showinfo("Thông báo", "Phim đã được xóa thành công!")

# Hàm cập nhật file CSV
def update_csv():
    update_data = {
        'ID': [film.id for film in film_list],
        'Film': [film.name for film in film_list],
        'Year': [film.year for film in film_list],
        'Award': [film.award for film in film_list],
        'Nomination': [film.nomination for film in film_list]
    }
    
    update_df = pd.DataFrame(update_data)
    update_df.to_csv('oscar.csv', index=False)

# Hàm xóa nội dung nhập liệu
def clear_entries():
    entry_id.delete(0, tk.END)
    entry_name.delete(0, tk.END)
    entry_year.delete(0, tk.END)
    entry_award.delete(0, tk.END)
    entry_nomination.delete(0, tk.END)

# Tạo cửa sổ chính
window = tk.Tk()
window.title("Quản lý Phim - Oscar Awards")
window.geometry("500x700")
window.config(bg="#343a40")

# Nhãn và hộp nhập liệu
def create_label_entry(window, text, entry_var):
    label = tk.Label(window, text=text, fg="#f8f9fa", bg="#343a40", font=("Arial", 12))
    label.pack()
    entry = tk.Entry(window, textvariable=entry_var, font=("Arial", 12), width=25)
    entry.pack(pady=5)
    return entry

entry_id = create_label_entry(window, "ID Phim:", tk.StringVar())
entry_name = create_label_entry(window, "Tên Phim:", tk.StringVar())
entry_year = create_label_entry(window, "Năm:", tk.StringVar())
entry_award = create_label_entry(window, "Giải Thưởng:", tk.StringVar())
entry_nomination = create_label_entry(window, "Đề Cử:", tk.StringVar())

# Các nút
button_style = {"bg": "#007bff", "fg": "#ffffff", "font": ("Arial", 12), "width": 20}

btn_add = tk.Button(window, text="Thêm Phim", command=add_film, **button_style)
btn_add.pack(pady=10)

btn_delete = tk.Button(window, text="Xóa Phim", command=delete_film, **button_style)
btn_delete.pack(pady=10)

btn_load_csv = tk.Button(window, text="Tải Dữ Liệu Từ CSV", command=load_data_from_csv, **button_style)
btn_load_csv.pack(pady=10)

# Listbox hiển thị danh sách phim
listbox_film = tk.Listbox(window, width=60, height=15, font=("Arial", 10), bg="#f8f9fa")
listbox_film.pack(pady=10)

# Chạy chương trình
window.mainloop()
