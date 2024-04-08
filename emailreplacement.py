#domain email replacement from old domain name to new domaina name
def replace_domain(email,old_domain,new_domain):
	if "@" + old_domain in email: #checks by concatenating the @ and old domain
		index= email.index("@"+ old_domain)
		new_email =email[:index] + "@" + new_domain
		print (new_email)
	else: 
		print(email)

replace_domain("olajide.usman@jaid.com","jaid.com","sumbo.com")
replace_domain("ola.sumbo@sunbees.com","yunbees.com","sumbo.com")


