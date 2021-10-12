from Detik.bmkg import ekstraksi_data, tampilkan_data
from Detik.detik import tampilkan_data_detik, ekstraksi_data_detik

if __name__ == '__main__':
    result = ekstraksi_data()
    tampilkan_data(result)
    print('\n')
    result = ekstraksi_data_detik()
    tampilkan_data_detik(result)