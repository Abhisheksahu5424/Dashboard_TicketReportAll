# from selenium import webdriver
#
# # Create a WebDriver instance (assuming you have ChromeDriver installed)
# driver = webdriver.Chrome()
#
# # JavaScript code to be executed
# javascript_code = """
#     function callback() {
#         gremlins.createHorde({
#             species: [gremlins.species.clicker(), gremlins.species.toucher(), gremlins.species.formFiller(), gremlins.species.scroller(), gremlins.species.typer()],
#             mogwais: [gremlins.mogwais.alert(), gremlins.mogwais.fps(), gremlins.mogwais.gizmo()],
#             strategies: [gremlins.strategies.distribution(), gremlins.strategies.allTogether(), gremlins.strategies.bySpecies()]
#         }).unleash();
#     }
#     var s = document.createElement("script");
#     s.src = "https://unpkg.com/gremlins.js";
#     if (s.addEventListener) {
#         s.addEventListener("load", callback, false);
#     } else if (s.readyState) {
#         s.onreadystatechange = callback;
#     }
#     document.body.appendChild(s);
# """
#
# # Navigate to a webpage
# driver.get("https://reports.parkzap.com")
#
# # Execute the JavaScript code
# driver.execute_script(javascript_code)
#
# # Optional: You can add a delay to observe the effects on the webpage
# import time
# time.sleep(10)
#
# # Close the browser
# driver.quit()
import time
import unittest
from selenium import webdriver
from HtmlTestRunner import HTMLTestRunner


class TestGremlinsExecution(unittest.TestCase):

    def test_gremlins_execution(self):
        # Create a WebDriver instance (assuming you have ChromeDriver installed)
        driver = webdriver.Chrome()

        # JavaScript code to be executed
        javascript_code = """
            function callback() {
                gremlins.createHorde({
                    species: [gremlins.species.clicker(), gremlins.species.toucher(), gremlins.species.formFiller(), gremlins.species.scroller(), gremlins.species.typer()],
                    mogwais: [gremlins.mogwais.alert(), gremlins.mogwais.fps(), gremlins.mogwais.gizmo()],
                    strategies: [gremlins.strategies.distribution(), gremlins.strategies.allTogether(), gremlins.strategies.bySpecies()]
                }).unleash();
            }
            var s = document.createElement("script");
            s.src = "https://unpkg.com/gremlins.js";
            if (s.addEventListener) {
                s.addEventListener("load", callback, false);
            } else if (s.readyState) {
                s.onreadystatechange = callback;
            }
            document.body.appendChild(s);
        """

        try:
            # Navigate to a webpage
            driver.get("https://reports.parkzap.com")

            # Execute the JavaScript code
            driver.execute_script(javascript_code)

            # Optional: You can add a delay to observe the effects on the webpage
            time.sleep(10)

        finally:
            # Close the browser
            driver.quit()

if __name__ == "__main__":
    # Define the HTML report file
    report_file = "monkey_report.html"

    # Create a test suite
    test_suite = unittest.TestLoader().loadTestsFromTestCase(TestGremlinsExecution)

    # Open the report file in write mode
    with open(report_file, "w") as report:
        # Create an HTMLTestRunner instance
        runner = HTMLTestRunner(stream=report, title="monkey Test Report", description="Execution of Gremlins on a Webpage")

        # Run the test suite using the HTMLTestRunner
        runner.run(test_suite)
