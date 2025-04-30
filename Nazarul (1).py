class Queue:
    def __init__(self):
        self.items = []

    def enqueue(self, item):
        self.items.append(item)

    def dequeue(self):
        if not self.is_empty():
            return self.items.pop(0)
        else:
            return "Queue is empty"

    def is_empty(self):
        return len(self.items) == 0

    def size(self):
        return len(self.items)


if __name__ == "__main__":
    printer_queue = Queue()
    while True:
        print("\n..........MENU PRINTER........:")
        print("1. Tambahkan dokumen ke antrian")
        print("2. Cetak dokumen berikutnya")
        print("3. Lihat jumlah dokumen dalam antrian")
        print("4. Keluar")
        pilihan = input("Masukkan pilihan Anda (1-4): ")

        if pilihan == "1":
            dokumen = input("Masukkan nama dokumen yang ingin ditambahkan: ")
            printer_queue.enqueue(dokumen)
            print(f"'{dokumen}' telah ditambahkan ke antrian.")
        elif pilihan == "2":
            if printer_queue.is_empty():
                print("Tidak ada dokumen dalam antrian untuk dicetak.")
            else:
                dokumen_dicetak = printer_queue.dequeue()
                print(f"Sedang mencetak dokumen: {dokumen_dicetak}")
        elif pilihan == "3":
            print(f"Jumlah dokumen dalam antrian: {printer_queue.size()}")
        elif pilihan == "4":
            print("Keluar dari program...")
            break
        else:
            print("Pilihan tidak valid. Silakan coba lagi.")
        


