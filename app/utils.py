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


def email_body(first_name, company):
    body = f"Dear {first_name[0].upper()}{first_name[1:]},<br/><br/>"
    body += "I hope this email finds you well. My name is Shubh, and I'm graduating from Western University. I have done my Bachelor's in Computer Science from SRMIST(Chennai, India).<br/><br/>"
    body += "During my academic life, I have built numerous projects in various tech stacks such as JS, React, Next, Node, Django, Python etc.<br/>"
    body += "Please feel free to check out <a href='https://shubh-jhawar-portfolio.vercel.app/'>My Portfolio</a>.<br/>"
    body += "These are some of the projects I have worked on - <a href='https://pictopiaaa.netlify.app/'>Pictopia (social-media)</a>, <a href='https://beatbox-ekrtmg8cy-shubhjhawar.vercel.app/'>Beatbox (e-commerce)</a><br/>"
    body += "This one is my personal favourite <a href='https://illusiogen.vercel.app/'>Illusiogen</a>, you can type a prompt and the AI will generate an Image from it.<br/><br/>"
    body += "I just applied for the Associate Software Engineer position. I would urge you to have a quick talk with me this week and assess if I have got what it takes.<br/><br/>"
    body += "I would be grateful for your help.<br/><br/>"
    body += "Looking forward to hear from you soon.<br/><br/>"
    body += "Best regards,<br/>Shubh"
    return body

def send_emails_to_veeva(first_name, last_name, company):
    pass