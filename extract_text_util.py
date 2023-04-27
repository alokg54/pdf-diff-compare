"""
**Module Name** : extract__text_util

Module to extract text from PDF using PyPDF2 library and pdftohtml,
It has two method implementation :func: extract_text_pdf_py2pdf
"""
import os
import PyPDF2
from PyPDF2.utils import PdfReadError
from bs4 import BeautifulSoup as Soup
import log_util
log = log_util.configure_logger()


class pdftoText:
    """
    Class to generate plain text from pdf files
    Used two methods to do it -
    (1). PyPDF2 library
    (2). pdftohtml from Calibre tool

    """

    def __init__(self):
        pass

    @staticmethod
    def extract_text_pdf_py2pdf(pdf_filepath):
        """
        Method to extract text from the input pdf file

        :return: ``text data, number of pages in file``
        :rtype: ``string``
        """
        try:
            # Open pdf file in read mode using PyPDF2 module
            _pdf_file_obj = open(pdf_filepath, 'rb')
            pdf_reader = PyPDF2.PdfFileReader(_pdf_file_obj)
            # calc number of pages
            num_pages = pdf_reader.numPages
            count = 0
            pdf_text = ""
            while count < num_pages:
                pageObj = pdf_reader.getPage(count)
                count += 1
                pdf_text += pageObj.extractText()
            # if pdf_text == "":
            #     # extract text using teserract engine
            #     pdf_text = textract.process(pdf_filepath, method='tesseract',
            #                                 language='eng')
            pdf_name = os.path.basename(pdf_filepath)
            print(pdf_name)
            if pdf_text and pdf_text.isspace() or pdf_text == '':
                log.error(f'Error : Unable to parse PDF'
                          f' {os.path.basename(pdf_filepath)}')
                pdf_text = f'Error : Unable to parse PDF' \
                    f' {os.path.basename(pdf_filepath)}'
                raise PdfReadError(pdf_text)
            return pdf_text, num_pages, pdf_name
        except PdfReadError:
            log.warning(f'PDF error occurred while processing'
                        f' {os.path.basename(pdf_filepath)}, Hence returning '
                        f'error text')
            return f'Error : Unable to parse PDF' \
                   f' {os.path.basename(pdf_filepath)}', None, \
                   os.path.basename(pdf_filepath)
        except Exception as exp:
            log.error(f'Exception occurred: {exp}')
            raise exp

    @staticmethod
    def _get_xml_from_pdf_pdftohtml(file_path):
        """
        Method to generate xml file from pdf file using pdftohtml

        :param file_path: ``generated xml file path``
        :return: ``xml file path``
        """
        try:
            assert os.path.exists(file_path), f'File ' \
                                    f':{os.path.basename(file_path)}not found'
            if not os.path.exists(file_path):
                raise FileNotFoundError(f'File : '
                                        f'{os.path.basename(file_path)} not '
                                        f'found')
            else:
                _dir_name = os.path.dirname(os.path.abspath(file_path))
                file_name = os.path.basename(file_path).split(".")[0]
                xml_parent_folder = os.path.join(_dir_name, 'XML')
                if not os.path.exists(xml_parent_folder):
                    log.info(f'XML Folder Path : {xml_parent_folder}')
                    os.mkdir(xml_parent_folder)
                xml_folder = os.path.join(xml_parent_folder, file_name)
                xml_file_path = os.path.join(xml_folder, f'{file_name}.xml')
                log.info(f'XML file path : [{xml_file_path}]')
                if not os.path.exists(xml_folder):
                    os.mkdir(xml_folder)
                #Command to convert pdf to xml using pdftohtml tool
                cmd = f'pdftohtml -xml "{file_path}" "{xml_file_path}"'
                log.debug(f'Pdftohtml Command : {cmd} ')
                # TODO call command using subprocess module with silent
                os.system(cmd)
                # checks if file exists else raise error
                assert os.path.exists(xml_file_path), f'Unable to generate XML' 'file {file_name}.xml'
                return xml_file_path
        except Exception as exp:
            log.error(exp)
            raise exp

    @staticmethod
    def _parse_xml(file):
        """
        Method to parse xml file and return plain text format

        :param file: ``xml file path``
        :return: ``plain text, page count``
        """
        try:
            handler = open(file, encoding='utf-8').read()
            soup = Soup(handler)
            plain_text = ""
            # get page count using len of page tag
            page_count = soup.findAll('page').__len__()
            for message in soup.findAll('text'):
                text_value = str(message.contents[0])
                # TODO use regex to removed the HTML tags
                text_value = text_value.replace('<b>', '')
                text_value = text_value.replace('</b>', '')
                text_value = text_value.replace('<a href="', '')
                text_value = text_value.replace('">', '')
                text_value = text_value.replace('</a>', '')
                plain_text = plain_text + ' ' + text_value
                # pdf_text_dict.update({page.attrs['number']: plain_text})
            if not plain_text:
                plain_text = f'Error : Unable to parse PDF' \
                            f'{os.path.basename(file).split(".")[0]}.pdf'
            return plain_text, page_count
        except Exception as exp:
            log.error(exp)
            raise exp

    def extract_text_pdf_pdftohtml(self, pdf_filepath):
        """
        Method to consolidate _get_xml_from_pdf_pdftohtml and _parse_xml methods

        :param pdf_filepath: ``pdf file path``
        :return: ``plain text of pdf, page count and pdf file name``
        """
        try:
            xml_path = self._get_xml_from_pdf_pdftohtml(pdf_filepath)
            pdf_text, page_count = self._parse_xml(xml_path)
            pdf_filename = os.path.basename(pdf_filepath)
            assert pdf_text is not None, f'Empty text for PDF : {pdf_filepath}'
            return pdf_text, page_count, pdf_filename
        except Exception as exp:
            log.error(exp)
            raise exp


if __name__ == '__main__':
    pdf_path = 'G:\\PDF_Diff\\TEST\\sample\\ss\\CBRLD1 SERIES.pdf'
    a = pdftoText()
    a.extract_text_pdf_pdftohtml(pdf_path)

