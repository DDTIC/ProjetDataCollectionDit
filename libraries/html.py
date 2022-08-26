from bs4 import BeautifulSoup

BASE_URL = 'DATABASES/data-zIybdmYZoV4QSwgZkFtaB.html'


class HtmlFactory(object):
    @classmethod
    def openFile(cls):
        with open(BASE_URL) as file:
            data = file.read()
            data = BeautifulSoup(
                data,
                'html.parser')
            file.close()
        return data

    @classmethod
    def main(cls):
        data = cls.openFile()
        tr = data.find_all('tr')
        donneeBrut = [
                      item.find_all('td')
                      for item in tr
                  ][1:]
        listeEmployer = [
            {
                'name': name.string.strip(),
                'phone': phone.string.strip(),
                'email': email.string.strip(),
                'address': '',
                'latlng': latlng.string.strip(),
                'salary': float(salary.string.strip()),
                'age': int(age.string.strip())
            }
            for (name, phone, email, latlng, salary, age) in donneeBrut
        ]
        return listeEmployer


