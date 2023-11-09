import os


class SendEmail:

    def __init__(self, page):
        self.page = page
        self.name_io = None

    def iframe_name_io(self):
        try:
            # Activate the iframe
            self.page.get_by_label("Kontakty").locator("div").nth(2).click()
            # Extract id and the 'name' attribute
            iframe_element = self.page.locator('iframe[id^="I0_"]').first
            self.name_io = iframe_element.get_attribute('name')
            print(f'from def iframe_name_io {self.name_io}')

        except Exception as e:
            print(f'Can not open dynamic frame named as "Kontakty" {e}')

    def prepare_email(self, credentials):
        if self.name_io is None:
            self.iframe_name_io()
        print(f'from def prepare_email {self.name_io}')
        name_from_contacts = credentials["name_from_contacts"]
        email_address_from_contacts = credentials["email_address_from_contacts"]
        self.page.frame_locator(f"iframe[name=\"{self.name_io}\"]"
                                ).get_by_label(f"Meno: {name_from_contacts}, opis: {email_address_from_contacts}."
                                               ).click()
        self.page.frame_locator(f"iframe[name=\"{self.name_io}\"]").get_by_label("Poslať e-mail").click()
        self.page.get_by_placeholder("Predmet").fill("test")
        self.page.get_by_role("textbox", name="Telo správy").fill("test\n")

    def add_attachment(self):
        print(f'from def add_attachment {self.name_io}')
        working_directory = os.getcwd()
        path_to_file = os.path.join(working_directory, 'files/attachment/funny_picture.png')
        self.page.get_by_label("Priložiť súbory").click()
        self.page.get_by_role("textbox", name="Telo správy").set_input_files(path_to_file)

    def send_email(self):
        if self.name_io is None:
            self.iframe_name_io()
        print(f'from def send_email {self.name_io}')
        self.page.get_by_label("Odoslať ‪(Ctrl-Enter)‬").click()
        self.page.frame_locator(f"iframe[name=\"{self.name_io}\"]").get_by_label("Close side panel").click()
