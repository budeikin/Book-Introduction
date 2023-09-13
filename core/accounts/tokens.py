from django.contrib.auth.tokens import PasswordResetTokenGenerator
from six import text_type


# activation account token generator
class AccountActivationTokenGenerator(PasswordResetTokenGenerator):
    def _make_hash_value(self, user, timestamp):
        return (
                text_type(user.pk) + text_type(timestamp)
        )


# generate token
account_activation_token = AccountActivationTokenGenerator()
