#https://github.com/Riokarbu
from bing_image_downloader import downloader

def main():
    print("EASY IMAGE SCRAPER\n")
    print("https://github.com/Riokarbu")

    #meminta pencarian yang ingin di cari pengguna
    pencarian = input("Type the image you want to search:")
    
    # Meminta jumlah gambar yang ingin diunduh dari pengguna
    jumlah = int(input("Enter the number of images you want to download: "))

    #class download
    download_query = pencarian
    output_dir = 'download-image'
    adult_filter_off = True

    #kode download image
    hasil = downloader.download(download_query, limit=jumlah, output_dir=output_dir, adult_filter_off=adult_filter_off, timeout=60)

    if hasil == 1:
            print("Images downloaded successfully!")
    else:
            print("Failed to download images.")

#kembali ke main
if __name__ == "__main__":
    main()