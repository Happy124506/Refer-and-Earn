import smtplib

def send_email(to_email, subject, message):
    server = smtplib.SMTP('smtp.gmail.com', 587)
    server.starttls()
    server.login("your_email@example.com", "password")
    email_message = f"Subject: {subject}\n\n{message}"
    server.sendmail("your_email@example.com", to_email, email_message)
    server.quit()

# Example Usage
if __name__ == "__main__":
    send_email("user@example.com", "Congratulations!", "You earned ₹500 for referring 5 friends!")
  
