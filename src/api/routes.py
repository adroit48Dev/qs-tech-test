from src import db, jsonify, status
from . import currency_bp
from flask import current_app
from src.models import CurrencyRates, logger
import src.status
from datetime import *

import os
import csv
import logging

DATA_DIR = os.getcwd()


def load_db():
    # initialize database
    dir_path = os.getcwd()

    data_dir = dir_path + '/data/'

    # get the list of files in the directory
    existing_files = os.listdir(data_dir)

    for file_name in existing_files:
        # check if the file is a regular file and has .csv extension
        if file_name.endswith('.csv'):  # check if the file is a CSV file
            file_path = os.path.join(data_dir, file_name)

            with open(file_path) as f:
                reader = csv.reader(f)
                print("Initializing..")
                next(reader)  # skip header row
                for row in reader:
                    try:
                        logging.info(
                            "Flask app is initializing with database and table")
                        business_date = datetime.strptime(
                            row[0], '%d/%m/%Y').date()
                        country_name = row[1]
                        currency_code = row[2]
                        exchange_rate = float(row[3])
                    except (ValueError, IndexError) as e:
                        logging.error(
                            f'Invalid data in line {reader.line_num}: {e}')
                        continue

                    currency_rate = CurrencyRates(business_date=business_date, country_name=country_name,
                                                  currency_code=currency_code, exchange_rate=exchange_rate)
                    db.session.add(currency_rate)
                    db.session.commit()


# Home Route
@currency_bp.route('/')
def home():
    res = "Hey! QuantSpark!!"
    return jsonify({"message": res}, status.HTTP_200_OK)


# Get All Currency data by date
@currency_bp.route('/api/currencies/<date>', methods=['GET'])
def get_all_currency(date):
    try:
        currency_rates = CurrencyRates.query.filter_by(
            business_date=date).all()
        current_app.logger.info(f"Request to create DB")
        results = [
            {
                "id": rate.id,
                "business_date": rate.business_date.strftime("%Y-%m-%d"),
                "currency_code": rate.currency_code,
                "exchange_rate": rate.exchange_rate
            }
            for rate in currency_rates
        ]
        return jsonify({"rates": results}), status.HTTP_200_OK
    except ValueError as e:
        current_app.logger.warning(f"Error while creating DB: {e}")


# Getting Movements from currency rates
@currency_bp.route('/api/movements/<date>', methods=['GET'])
def movements(date):
    date_str = date
    if not date_str:
        return jsonify({"error": 'Please provide a date parameter in the format yyyy-mm-dd'}), 400
    try:
        date = datetime.strptime(date, '%Y-%m-%d').date()
    except ValueError:
        return 'Invalid date format. Please use the format yyyy-mm-dd', 400

    prev_day_rates = CurrencyRates.query.filter(
        CurrencyRates.business_date == date).all()
    prev_day_rates_dict = {
        (rate.currency_code, rate.country_name): rate for rate in prev_day_rates}

    if not prev_day_rates_dict:
        return jsonify({"message": 'No data found for the requested date'}), status.HTTP_404_NOT_FOUND

    prev_business_date = prev_day_rates[0].business_date - timedelta(days=1)
    prev_day_rates = CurrencyRates.query.filter(
        CurrencyRates.business_date == prev_business_date).all()

    movements = []

    try:
        for rate in prev_day_rates:
            prev_rate = prev_day_rates_dict.get(
                (rate.currency_code, rate.country_name))

            if prev_rate:
                movement = (1 - rate.exchange_rate /
                            prev_rate.exchange_rate) * 100
                movements.append({'country_name': rate.country_name, 'currency_code': rate.currency_code,
                                  'movement': round(movement, 2)})

        if len(movements) == 0:  # if no data found for movements
            print("no content")
            return jsonify({"message": "Movements are not captured due to lack of data."}, status.HTTP_204_NO_CONTENT)

        current_app.logger.info('Successfully calculate movements.')
        return jsonify({'movements': movements}, status.HTTP_200_OK)

    except ValueError as e:
        current_app.logger.warning(
            f'Something went wrong while getting movements: {e}')
        return jsonify({'Error': e}, 400)

