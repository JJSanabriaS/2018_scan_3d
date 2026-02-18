import barcode

hr = barcode.get_barcode_class('ean13')
Hr = hr('1234567891012')
print(type(Hr))
qr = Hr.save('123')