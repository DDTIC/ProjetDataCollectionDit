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
        listEmployer = []
        for item in donneeBrut:
            donneeEmployer = []
            for subitem in item:
                element = subitem.contents
                el = element[0]
                donneeEmployer.append(el)
            employer = {
                'name': donneeEmployer[0],
                'phone': donneeEmployer[1],
                'email': donneeEmployer[2],
                'adress': "",
                'latlng': donneeEmployer[3]
            }
            listEmployer.append(employer)

        return listEmployer
