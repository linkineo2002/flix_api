from django.db import models

NATIONALITY_CHOICES = (
    ('US', 'Estados Unidos'),
    ('BR', 'Brasil'),
    ('FR', 'França'),
    ('JP', 'Japão'),
    ('IN', 'Índia'),
    ('GB', 'Reino Unido'),
    ('DE', 'Alemanha'),
    ('IT', 'Itália'),
    ('ES', 'Espanha'),
    ('CN', 'China'),
    ('KR', 'Coreia do Sul'),
    ('RU', 'Rússia'),
    ('MX', 'México'),
    ('CA', 'Canadá'),
    ('AU', 'Austrália'),
    ('AR', 'Argentina'),
    ('ZA', 'África do Sul'),
)

class Actor(models.Model):
    name = models.CharField(max_length=200)
    birthday = models.DateField(null=True, blank=True)
    nationality = models.CharField(max_length=100, choices=NATIONALITY_CHOICES, blank=True, null=True)

    def __str__(self):
        return self.name