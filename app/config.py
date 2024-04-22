import os


class Config:
	SECRET_KEY = 'secret'#os.environ.get('SECRET_KEY')

	# SQLALCHEMY_DATABASE_URI = os.environ.get('DATABASE_URL', '').replace('postgres://','postgresql://')
	# SQLALCHEMY_DATABASE_URI = os.environ.get('DATABASE_URL', '')
	SQLALCHEMY_DATABASE_URI = 'sqlite:///site.db'

	MAIL_SERVER = 'smtp.googlemail.com'
	MAIL_PORT = 587
	MAIL_USE_TLS = True
	MAIL_USERNAME = "g.nft.1.256@gmail.com"#os.environ.get('EMAIL_USER')
	MAIL_PASSWORD = "gnft1256"#os.environ.get('EMAIL_PASS')
	EMAIL_USER = "g.nft.1.256@gmail.com"
	EMAIL_PASS = "gnft1256"
