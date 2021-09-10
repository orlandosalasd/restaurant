
class ProfileRoles(object):
    """ Profile Rols choice to users """
    ADMINISTRATOR = 'administrator'
    CUSTOMER = 'customer'

    CHOICES = (
        (ADMINISTRATOR, ADMINISTRATOR.upper()),
        (CUSTOMER, CUSTOMER.upper())
    )
