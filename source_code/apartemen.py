from hunian import Hunian

class Apartemen(Hunian):
    def __init__(self, nama_pemilik, jml_penghuni, jml_kamar, harga_sewa, image):
        super().__init__("Apartemen", jml_penghuni, jml_kamar, image = image)
        self.nama_pemilik = nama_pemilik
        self.harga_sewa = harga_sewa

    def get_dokumen(self):
        return "Sertifikat Hak Milik Atas Satuan Rumah Susun (SHMSRS) a/n " + self.nama_pemilik + "."

    def get_nama_pemilik(self):
        return self.nama_pemilik
    
    def get_harga_sewa(self):
        return self.harga_sewa
    
    def get_detail(self):
        return "Pemilik : " + self.nama_pemilik + "\nJumlah Kamar : " + str(self.jml_kamar) + "\nHarga Sewa :" + str(self.get_harga_sewa()) + "\n"