BDD TESTS
---------

The Playwright setup for the test is done by fixtures in the `conftes.py` file.
Additional set up e.g. **headless mode** or **slow_mo** for the web browser can be done in the fixtures/browser.py

.. code:: python

    @pytest.fixture(scope="session")
    def browser() -> Generator[Browser, None, None]:
        """
        Fixture to launch the browser and close it at the end of the session.

        :return: Playwright Browser object.
        """
        with sync_playwright() as p:
            start_browser = p.firefox.launch(headless=False, slow_mo=800)
            yield start_browser
            start_browser.close()
