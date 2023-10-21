def get_email_list(first_name, last_name, company):
    # Generate email addresses with different combinations
    email_variations = [
        # first_name.last_name@company.com
        f"{first_name.lower()}.{last_name.lower()}@{company.lower()}.com",

        # first_name.last_name@company.ca
        f"{first_name.lower()}.{last_name.lower()}@{company.lower()}.ca",

        # first_name last_name @company .com
        f"{first_name.lower()}{last_name.lower()}@{company.lower()}.com",

        # first_name last_name @company .com
        f"{first_name.lower()}.{last_name.lower()}@{company.lower()}.ca",

        # first_name[0] last_name@company.com
        f"{first_name[0].lower()}{last_name.lower()}@{company.lower()}.com",

        # first_name[0] last_name@company.ca
        f"{first_name[0].lower()}{last_name.lower()}@{company.lower()}.ca",

        # last_name . first_name @company.com
        f"{last_name.lower()}.{first_name.lower()}@{company.lower()}.com",

        # last_name . first_name @company.ca
        f"{last_name.lower()}.{first_name.lower()}@{company.lower()}.ca",

    ]

    return email_variations