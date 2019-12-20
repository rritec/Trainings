# Sending mail to Multiple Users
import smtplib
# list of emails to send the mail
li = ["navyakrishnatest@gmail.com","Srikarreddy0007@gmail.com"]

for i in range(len(li)):
	s = smtplib.SMTP('smtp.gmail.com',587)
	s.starttls()
	s.login("navyakrishnatest@gmail.com", "navya@2321")
	message = "HI!!! How are you? Where are you from?"
	s.sendmail("Srikarreddy0007@gmail.com", li[i], message)
	s.quit()
	