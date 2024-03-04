from tkinter import Tk, Label, Entry, Button, filedialog
from tkinter import messagebox  # messageboxをインポート

from mutagen.easyid3 import EasyID3


class MetadataEditor:
    """
    MP3 Metadata Editor is a Python-based GUI application that allows users to edit the metadata of MP3 files. Using the `mutagen.easyid3` library, it supports editing common metadata fields such as title, artist, album, track number, genre, and date. The application provides a user-friendly interface to load an MP3 file, view and edit its metadata, and save the changes.
    """
    def __init__(self, root):
        self.root = root
        self.root.geometry("600x600")  # ウィンドウサイズを調整
        self.root.title("MP3 Metadata Editor")

        # ファイル選択ボタン
        self.load_button = Button(root, text="Load MP3", command=self.load_file)
        self.load_button.pack(pady=10)

        # 各種メタデータのラベルとエントリーフィールド
        self.metadata_fields = ['title', 'artist', 'album', 'tracknumber', 'genre', 'date']
        self.entries = {}
        for field in self.metadata_fields:
            label = Label(root, text=field.capitalize() + ":")
            label.pack(pady=(5, 0))
            entry = Entry(root)
            entry.pack(pady=(0, 5))
            self.entries[field] = entry

        # 保存ボタン
        self.save_button = Button(root, text="Save Metadata", command=self.save_metadata)
        self.save_button.pack(pady=10)

        self.file_path = None

    def load_file(self):
        self.file_path = filedialog.askopenfilename(filetypes=[("MP3 files", "*.mp3")])
        if self.file_path:
            audio = EasyID3(self.file_path)
            for field in self.metadata_fields:
                self.entries[field].delete(0, 'end')
                self.entries[field].insert(0, audio.get(field, [''])[0])

    def save_metadata(self):
        if self.file_path:
            try:
                audio = EasyID3(self.file_path)
                for field, entry in self.entries.items():
                    audio[field] = entry.get()
                # ここで各メタデータフィールドの値を設定
                audio.save()
                messagebox.showinfo("Success", "Metadata saved successfully.")  # 成功ダイアログを表示
            except Exception as e:
                messagebox.showerror("Error", f"Failed to save metadata: {e}")  # エラーダイアログを表示
        else:
            messagebox.showwarning("Warning", "No file loaded.")  # 警告ダイアログを表示


if __name__ == "__main__":
    root = Tk()
    app = MetadataEditor(root)
    root.geometry("600x400")  # ウィンドウのサイズを600x400に設定
    root.mainloop()
