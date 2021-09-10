from django.test import TestCase
from person.choices import ProfileRoles
from person.forms import SingUpForm


class SingFormTest(TestCase):

    def test_rol_choice_field_get_corrects_choices(self):
        """ Case to test the rol choice field to validate its have the corrects choices """
        form = SingUpForm()
        self.assertEquals(list(ProfileRoles.CHOICES), form.fields['rol'].choices)
