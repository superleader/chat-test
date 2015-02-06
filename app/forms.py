from flask.ext.wtf import Form
from wtforms import TextField, BooleanField
from wtforms.validators import Required


class LoginForm(Form):
    openid = TextField('openid', validators = [Required()])
    remember_me = BooleanField('remember_me', default = False)


class PostForm(Form):
    body = TextField('body', validators = [Required()])
                            		
    
class ChannelForm(Form):
    name = TextField('name', validators = [Required()])


	