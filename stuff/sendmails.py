import requests
from bs4 import BeautifulSoup
import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart

# def scrape_justgiving_page(url):
#     response = requests.get(url)
#     soup = BeautifulSoup(response.content, 'html.parser')
    
#     title = soup.find('h1', class_='jg-h1').text.strip()
#     description = soup.find('p', class_='jg-s-story').text.strip()
#     target = soup.find('span', class_='jg-text--brand-large').text.strip()
#     raised = soup.find('span', class_='jg-color--primary').text.strip()
#     owner = soup.find('h2', class_='sPcQN').text.strip()
    
#     return {
#         'title': title,
#         'description': description,
#         'target': target,
#         'raised': raised,
#         'owner': owner
#     }

# def create_email_html(page_info):
#     html = f"""
#     <html>
#         <head>
#             <style>
#                 body {{ font-family: Arial, sans-serif; }}
#                 .container {{ max-width: 600px; margin: 0 auto; padding: 20px; }}
#                 .header {{ background-color: #88288F; color: white; padding: 20px; text-align: center; }}
#                 .content {{ padding: 20px; }}
#                 .button {{ background-color: #25CA76; color: white; padding: 10px 20px; text-decoration: none; display: inline-block; }}
#             </style>
#         </head>
#         <body>
#             <div class="container">
#                 <div class="header">
#                     <h1>{page_info['title']}</h1>
#                     <p>by {page_info['owner']}</p>
#                 </div>
#                 <div class="content">
#                     <p>{page_info['description']}</p>
#                     <p>Target: {page_info['target']}</p>
#                     <p>Raised so far: {page_info['raised']}</p>
#                     <a href="" class="button">Donate Now</a>
#                 </div>
#             </div>
#         </body>
#     </html>
#     """
#     return html

def scrape_justgiving_page(url):
    response = requests.get(url)
    soup = BeautifulSoup(response.content, 'html.parser')
    
    title = soup.find('h1', class_='jg-h1').text.strip()
    description = soup.find('p', class_='jg-s-story').text.strip()
    target = soup.find('span', class_='jg-text--brand-large').text.strip()
    raised = soup.find('span', class_='jg-color--primary').text.strip()
    owner = soup.find('h2', class_='sPcQN').text.strip()
    
    # Get the full story
    story_container = soup.find('div', class_='jFlpr')
    full_story = ' '.join([p.text.strip() for p in story_container.find_all('p')])
    
    # Get the main image URL
    image_div = soup.find('div', class_='eY2IS')
    image_url = image_div['style'].split('url(')[1].split(')')[0] if image_div else ''
    
    return {
        'title': title,
        'description': description,
        'target': target,
        'raised': raised,
        'owner': owner,
        'full_story': full_story,
        'image_url': image_url
    }

def create_email_html(page_info):
    html = f"""
    <html>
        <head>
            <style>
                body {{ font-family: Arial, sans-serif; }}
                .container {{ max-width: 600px; margin: 0 auto; padding: 20px; }}
                .header {{ background-color: #88288F; color: white; padding: 20px; text-align: center; }}
                .content {{ padding: 20px; }}
                .button {{ background-color: #25CA76; color: white; padding: 10px 20px; text-decoration: none; display: inline-block; }}
                .image {{ width: 100%; max-width: 600px; height: auto; }}
            </style>
        </head>
        <body>
            <div class="container">
                <div class="header">
                    <h1>{page_info['title']}</h1>
                    <p>by {page_info['owner']}</p>
                </div>
                <div class="content">
                    <img src="{page_info['image_url']}" alt="Campaign Image" class="image">
                    <h2>Our Story</h2>
                    <p>{page_info['full_story']}</p>
                    <p>Target: {page_info['target']}</p>
                    <p>Raised so far: {page_info['raised']}</p>
                    <a href="justgivepage" class="button">Donate Now</a>
                </div>
            </div>
        </body>
    </html>
    """
    return html



thingy = "hffv zvky qxzg ahze"
def send_email_to_self(your_email, your_password, subject, html_content):
    message = MIMEMultipart('alternative')
    message['Subject'] = subject
    message['From'] = your_email
    message['To'] = your_email

    html_part = MIMEText(html_content, 'html')
    message.attach(html_part)

    with smtplib.SMTP_SSL('smtp.gmail.com', 465) as server:
        server.login(your_email, your_password)
        server.sendmail(your_email, your_email, message.as_string())

# Usage
justgiving_url = 'somepage'
page_info = scrape_justgiving_page(justgiving_url)
email_html = create_email_html(page_info)

send_email_to_self("", thingy, "PIZAA for compsci",email_html)


