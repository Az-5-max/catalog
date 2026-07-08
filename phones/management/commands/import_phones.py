import csv
from django.core.management.base import BaseCommand
from phones.models import Phone


class Command(BaseCommand):
    help = 'Import phones from CSV'

    def handle(self, *args, **options):
        with open('phones.csv', 'r', encoding='utf-8') as file:
            reader = csv.reader(file, delimiter=';')
            next(reader)

            for row in reader:
                phone = Phone(
                    id=int(row[0]),
                    name=row[1],
                    image=row[2],
                    price=float(row[3]),
                    release_date=row[4],
                    lte_exists=row[5].lower() == 'true',
                )
                phone.save()
                self.stdout.write(f'Добавлен: {phone.name}')