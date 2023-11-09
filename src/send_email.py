import os


class SendEmail:

    def __init__(self, page, credentials):
        self.page = page
        self.name_io = None
        self.name_from_contacts = credentials["name_from_contacts"]
        self.email_address_from_contacts = credentials["email_address_from_contacts"]

    def iframe_name_io(self):
        try:
            # Extract id and the 'name' attribute
            # Condition: expected state iframe "Kontakty" is already open
            iframe_element = self.page.locator('iframe[id^="I0_"]').first
            self.name_io = iframe_element.get_attribute('name')
        except Exception as e:
            print(f'It looks like iframe named "Kontakty" is closed. '
                  f'Iframe "Kontakty" will be opened and the testing will continue {e}')

        finally:
            if self.name_io is None:
                self.page.get_by_label("Kontakty").locator("div").nth(2).click()
                iframe_element = self.page.locator('iframe[id^="I0_"]').first
                self.name_io = iframe_element.get_attribute('name')

    def prepare_email(self):
        self.iframe_name_io()
        print(f'from def prepare_email {self.name_io}')
        self.page.frame_locator(f"iframe[name=\"{self.name_io}\"]"
                                ).get_by_label(f"Meno: {self.name_from_contacts},"
                                               f" opis: {self.email_address_from_contacts}.").click()
        self.page.frame_locator(f"iframe[name=\"{self.name_io}\"]").get_by_label("Poslať e-mail").click()
        self.page.get_by_placeholder("Predmet").fill("test")
        self.page.get_by_role("textbox", name="Telo správy").fill("test\n")

    def add_attachment(self):
        working_directory = os.getcwd()
        path_to_file = os.path.join(working_directory, 'files/attachment/funny_picture.png')

        with self.page.expect_file_chooser() as paper_clip:
            file_input = self.page.get_by_label("Priložiť súbory")
            file_input.click()
            file_chooser = paper_clip.value
            file_chooser.set_files(path_to_file)

        self.page.wait_for_timeout(5000)

    def send_email(self):
        self.page.get_by_label("Odoslať ‪(Ctrl-Enter)‬").click()
