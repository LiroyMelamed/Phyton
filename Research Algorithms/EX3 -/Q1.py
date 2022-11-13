import re

MailForm = r'([A-Za-z0-9]+[-_.])*[A-Za-z0-9]+@[A-Za-z0-9-]+\.[A-Z|a-z]{2,}'


def CheckEmail(email):
    # Checking if the email address fit in the form
    if re.match(MailForm, email):
        return True
    return False


def SortFile(example):
    # Making two lists of mail valid and invalid
    ValidMail = []
    InvalidMail = []
    # Opening the file that we get
    with open(example, "r") as file:
        # Reading the file and splitting the address into list
        RowInFile = list(file.read().split("\n"))

        # For each email in the list
        for row in RowInFile:
            # Splitting the words/email address in the row
            EmailList = list(row.split(" "))
            for email in EmailList:
                # Distinct the emails address
                if "@" in email:
                    # If the email is valid put it in its list
                    if CheckEmail(email):
                        ValidMail.append(email)
                    # The email is invalid so put it in its list
                    else:
                        InvalidMail.append(email)

    print(f"The valid mail address are:\n{ValidMail}")
    print(f"The invalid mail address are:\n{InvalidMail}")


SortFile('EmailAddress')
