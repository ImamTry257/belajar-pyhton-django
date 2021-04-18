from django.http import HttpResponse

def index(req):
	return HttpResponse(req, 'Hallooo')


def angka(req, **input):
	print(input)
	heading = "<h1>Hallo</h1>"
	strTanggal = "tanggal: "+input['tanggal']+"<br>"
	strBulan = "bulan: "+input['bulan']+"<br>"
	strTahun = "tahun: "+input['tahun']+"<br>"
	str = heading + strTanggal + strBulan + strTahun
	return HttpResponse(str)