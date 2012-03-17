from django.dispatch import Signal
"""
Sample how to use in your models.py:

from moneybookers.signals import moneybookers_signal
from django.db import transaction
from django.core.mail import mail_admins

@transaction.commit_manually
def MoneybookersSignal(sender, **kwargs):
	if sender.error:
		mail_admins("Moneybookers: bad transaction %s" % sender.transaction_id, sender.error_text)
		return
	sid = transaction.savepoint()
	try:
		user = User.objects.get(id=sender.user_id)
		profile = user.get_profile()
		profile.money = profile.money + sender.amount
		profile.save()
		mail_admins( "Moneybookers: good transaction %s" % sender.transaction_id, "%s added to user %s" % (sender.amount, sender.user_id) )
		transaction.savepoint_commit(sid)
	except Exception, e:
		transaction.savepoint_rollback(sid)
		mail_admins("Moneybookers: database rollback: transaction %s" % sender.transaction_id, e)
	transaction.commit()

moneybookers_signal.connect(MoneybookersSignal, dispatch_uid="yourapp.models.MoneybookersSignal")
"""
moneybookers_signal = Signal()
