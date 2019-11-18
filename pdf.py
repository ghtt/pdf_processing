import PyPDF2
import argparse


WATERMARK_PDF_FILE = "wtr.pdf"
OUTPUT_FILE = "test.pdf"


def add_watermark(file, watermark):
	"""Add watermark pdf"""
	pdf = PyPDF2.PdfFileReader(file)

	# for each page add watermark
	for page in pdf.pages:
		page.mergePage(watermark)
	
	# add all pages from reader to writer
	writer = PyPDF2.PdfFileWriter()	
	writer.appendPagesFromReader(pdf)

	# save result to new pdf file
	with open(OUTPUT_FILE, 'ab') as out:
		writer.write(out)


def get_watermark(file):
	"""Get watermark from wtr.pdf file"""
	return PyPDF2.PdfFileReader(file).getPage(0)


if __name__ == "__main__":

	arg_parser = argparse.ArgumentParser()
	arg_parser.add_argument(
		"input",
		nargs=1,
		type=str)
	arguments = arg_parser.parse_args()

	wtrmrk = get_watermark(WATERMARK_PDF_FILE)
	add_watermark(*arguments.input, wtrmrk)
