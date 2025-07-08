import csv

from db import db_session
from models import Deals

def read_csv(file_name):
    with open(file_name, 'r') as f:
        fields = [
                'agent', 'contractor', 'ds_create_date', 'ds_name',
                'deal_create_date', 'name_deal', 'deal_subject',
                'ds_deal_subject', 'price'
        ]
        reader = csv.DictReader(f, fields, delimiter=';')
        for row in reader:
            if row['ds_create_date']:
                row['ds_create_date'] = row['ds_create_date']
            else:
                row['ds_create_date'] = None
            save_deals_data(row)

def save_deals_data(row):
        deal = Deals(
        agent=row['agent'],
        contractor=row['contractor'],
        ds_create_date=row['ds_create_date'],
        ds_name=row['ds_name'],
        deal_create_date=row['deal_create_date'],
        name_deal=row['name_deal'],
        deal_subject=row['deal_subject'],
        ds_deal_subject=row['ds_deal_subject'],
        price=row['price']
        )
        db_session.add(deal)
        db_session.commit()

if __name__ == '__main__':
    read_csv('deals_all.csv')