"""
DB Models for creating fx rate data and movements
"""
from src import db
from datetime import date, datetime
import os
import csv
import logging

# getting logger
logger = logging.getLogger()
logging.basicConfig(
    filename='currency.log',
    level=logging.DEBUG,
    format=f'%(asctime)s %(levelname)s %(name)s %(threadName)s : %(message)s'
)

# Currency Model


class CurrencyRates(db.Model):
    """ Currency Rate table to hold day wise currency rates"""
    __tablename__ = 'currency_rates'
    id = db.Column(db.Integer, primary_key=True)
    business_date = db.Column(db.Date)
    country_name = db.Column(db.String(50))
    currency_code = db.Column(db.String(5))
    exchange_rate = db.Column(db.Float)

    def __repr__(self):
        """ Represents Data from Currency rate table"""
        return f'<CurrencyRates {self.business_date} {self.currency_code} {self.exchange_rate}>'

    @staticmethod
    def get_movement(current_rate, previous_rate):
        return (1 - (current_rate.exchange_rate / previous_rate.exchange_rate)) * 100

    ##################################################
    # CLASS METHODS
    ##################################################

    @classmethod
    def all(cls) -> list:
        """Returns all data in the database"""
        logger.info("Processing all data")
        logger.warning('Warning level log')
        return cls.query.all()

    @classmethod
    def find_all_by_date(cls, business_date: date):
        """Finds Data by it's date
        :param date: the date of the business_date to find
        :type date: date
        :return: all movements by date, or None if not found
        :rtype: Movements
        """
        logger.info("Processing lookup for date %s ...", date)
        return cls.query.get(date)
