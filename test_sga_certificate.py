import unittest

from selenium import webdriver

BASE_URL = "https://aluno.tce.mt.gov.br/valida/certificado"
CPF = "57087040120"
VALID_CERTIFICATE_NUMBER = "2015906DB4A3"
INVALID_CERTIFICATE_NUMBER = "2015906DB4A2"


class SGACertificate(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.Firefox()

    def test_is_certificate_valid(self):
        """
        Informar um número de certificado existente e assegura que há a mensagem
        'Certificado Válido' quando submeter o formulário
        """
        self.driver.get(BASE_URL)
        cpf_element = self.driver.find_element_by_name("cpf")
        cpf_element.send_keys(CPF)
        certificate_id = self.driver.find_element_by_name("codigo_certificado")
        certificate_id.send_keys(VALID_CERTIFICATE_NUMBER)
        submit_button = self.driver.find_element_by_css_selector("button[type='submit']")
        submit_button.click()
        self.assertIn("Certificado Válido", self.driver.page_source)

    def test_is_certificate_invalid(self):
        """
        Informar um número de certificado que não existe e assegura que não há a mensagem
        'Certificado Válido' quando submeter o formulário
        """
        self.driver.get(BASE_URL)
        cpf_element = self.driver.find_element_by_name("cpf")
        cpf_element.send_keys(CPF)
        certificate_id = self.driver.find_element_by_name("codigo_certificado")
        certificate_id.send_keys(INVALID_CERTIFICATE_NUMBER)
        submit_button = self.driver.find_element_by_css_selector("button[type='submit']")
        submit_button.click()
        self.assertNotIn("Certificado Válido", self.driver.page_source)

    def tearDown(self):
        self.driver.close()


if __name__ == "__main__":
    unittest.main()
