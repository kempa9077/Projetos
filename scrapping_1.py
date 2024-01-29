"""
Esse módulo faz chamadas básicas no site https://realpython.github.io/fake-jobs/.
"""

import requests
from bs4 import BeautifulSoup
from bs4.element import Tag

def get_page_content(
        url:str="https://realpython.github.io/fake-jobs/",
        id_:str= "ResultsContainer"
        )->Tag:
    """
    Essa função faz a requisição de uma página e filtra por um id específico. 
    Tanto a url como o id estão default, ou seja, em caso de não serem passados
    assumirão os valores acima, porém eles podem ser passados.

    Parameters
    ----------
    url: str 
        Url dá pagina.
    id: str 
        id de busca da página.

    Returns
    -------
    results: bs4.element.Tag

    Examples
    --------
    >>> get_page_content(url,id)
    Output:
        <div class="columns is-multiline" id="ResultsContainer">
        <div class="column is-half">
        <div class="card">
        <div class="card-content">
        ...

    """
    page = requests.get(url, timeout=10)
    soup = BeautifulSoup(page.content, "html.parser")
    results = soup.find(id=id_)
    return results

def main():
    """
    Função principal do script.

    Esta função executa as tarefas principais do script. No exemplo atual não fará nada
    pois ela somente tira print dos cargos, mas poderíamos mudar isso para ela fazer algo
    de fato.

    Parameters
    ----------
    Não possui parâmetros.

    Returns
    -------
    None

    Examples
    --------
    Para executar a função diretamente do terminal, certifique-se de que este script
    não está sendo importado como um módulo e então execute:

    >>> python scrapping.py
    """
    resultado = get_page_content()
    job_elements = resultado.find_all("div", class_="card-content")

    for job_element in job_elements:
        title_element = job_element.find("h2", class_="title is-5")
        company_element = job_element.find("h3", class_="subtitle is-6 company")
        location_element = job_element.find("p", class_="location")
        print(title_element.text.strip())
        print(company_element.text.strip())
        print(location_element.text.strip())
        print()

if __name__=="main":
    main()
