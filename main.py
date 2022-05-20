import pdfplumber
from gtts import gTTS
from pathlib import Path
from art import tprint

def from_pdf_to_mp3(file_path='test_file.pdf', lang='en'):
	"""
	This func transforms pdf file into a string and then creates an mp3 file
	using gTTS package
	"""

	if Path(file_path).is_file() and Path(file_path).suffix == '.pdf':

		print(f'[+] Fiile to convert: {Path(file_path).name}')
		print(f'[+] Processing...')

		with pdfplumber.PDF(open(file=file_path, mode='rb')) as pdf:
			pages = [page.extract_text() for page in pdf.pages]

		text = ''.join(pages)
		text = text.replace('/n', '')

		audio = gTTS(text=text, lang=lang)
		file_name = Path(file_path).stem
		audio.save(f'{file_name}.mp3')

		return f'[+]{file_name}.mp3 was created successfully!'

	else:
		return 'There is no such file! Check directory!'

def main():
	tprint(f'PDF-->TO-->MP3')
	file_path = input(f'\nEnter path to the file: ')
	lang = input(f'Enter language of pdf file(ex: ru or en): ')
	print(from_pdf_to_mp3(file_path='C:/Users/Sung_JinWoo/Desktop/my_projects/pdf_files/cat.pdf', lang='en'))	

if __name__ == '__main__':
	main()