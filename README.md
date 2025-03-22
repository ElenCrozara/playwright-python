# Projeto de Teste de Carrinho de Compras com Playwright e Pytest

Este projeto contém testes automatizados para um carrinho de compras usando Playwright com Python e Pytest.

## Padrão Page Objects

Ele foi desenvolvido utilizando o padrão Page Objects para melhor organização, manutenção e legibilidade dos testes automatizados. O padrão Page Objects visa criar classes que representam as páginas da aplicação, encapsulando os seletores e as ações específicas de cada página. Isso facilita a reutilização de código e reduz a duplicação, tornando os testes mais robustos e fáceis de manter.

## Pré-requisitos

* Python 3.8+
* Playwright
* Pytest

## Instalação


1.  Crie um ambiente virtual (recomendado):

    ```bash
    python3 -m venv venv
    source venv/bin/activate # No Linux/macOS
    source venv\Scripts\activate # No Windows
    ```

2.  Instale as dependências:

    ```bash
    pip install playwright pytest
    playwright install
    ```

## Configurações do Playwright

As configurações do Playwright estão definidas no arquivo `playwright.config.py`.

```python
from playwright.sync_api import Playwright, sync_playwright, expect
from playwright.config import PlaywrightTestConfig

config = PlaywrightTestConfig(
    use={
        "viewport": {"width": 1920, "height": 1080}, # Define o tamanho da janela como 1920x1080 (Full HD)
        "video": "on-first-retry", # Configura gravação de vídeo para testes com falha na primeira tentativa.
        "screenshot": "only-on-failure", # Configura gravação de screenshots apenas para testes com falha.
    }
)
```

## Como executar os testes

`pytest --headed test test_cart_page.py`.

## Arquivos do projeto

* `tests/test_cart_page.py`:Contém os testes automatizados.
* `pages/cart_page.py`: Contém a classe CartPage com os métodos para interagir com a página do carrinho de compras.
* `playwright.config.py`: Contém as configurações do Playwright.
* `README.md`: Este arquivo com as instruções do projeto.

## Estrutura do projeto

``` playwright-python/
├── tests/
│   └── test_cart_page.py
├── pages/
│   └── cart_page.py
├── playwright.config.py
└── README.md
```

## Dependências

* Playwright: Para automação de testes em navegadores.
* Pytest: Para execução de testes em Python.

## Licença

Este projeto está sob a licença MIT.
