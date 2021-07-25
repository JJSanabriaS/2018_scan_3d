import barcode
#from barcode.writer import ImageWriter
from barcode import generate
def testEan():
    EAN = barcode.get_barcode_class('ean13')
    ean = EAN(u'5901234123457', writer=ImageWriter())
    fullname = ean.save('ean13_barcode')
    u'ean13_barcode.png'
    name = generate('EAN13', u'5901234123457', output='barcode_svg')
    print(name)
if __name__ == '__main__':
    testEan()
