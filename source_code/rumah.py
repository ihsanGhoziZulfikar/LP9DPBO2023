from hunian import Hunian

class Rumah(Hunian):
    def __init__(self, nama_pemilik, jml_penghuni, jml_kamar, harga_beli, image):
        super().__init__("Rumah", jml_penghuni, jml_kamar, image = image)
        self.nama_pemilik = nama_pemilik
        self.harga_beli = harga_beli

    def get_dokumen(self):
        return "Izin Mendirikan Bangunan (IMB) a/n " + self.nama_pemilik

    def get_nama_pemilik(self):
        return self.nama_pemilik

    def get_harga_beli(self):
        return self.harga_beli
   
    def get_detail(self):
        return "Pemilik : " + self.nama_pemilik + "\nJumlah Kamar : " + str(self.jml_kamar) + "\nHarga Beli : " + str(self.get_harga_beli()) + "\n"