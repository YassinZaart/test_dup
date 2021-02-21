import models
from variables import db
import states


def login(email, password):
    user = models.UserModel.query.filter_by(email=email).first()
    if user is None:
        return states.LoginState.USER_NOT_FOUND
    if user.password == password:
        return states.LoginState.LOGIN_SUCCESSFUL
    else:
        return states.LoginState.INCORRECT_PASSWORD


def signup(email, name, password, city, street, phone_number):
    user = models.UserModel.query.filter_by(email=email).first()
    if user is not None:
        return states.SignupState.EMAIL_ALREADY_EXIST

    user = models.UserModel.query.filter_by(name=name).first()
    if user is not None:
        return states.SignupState.NAME_ALREADY_EXIST

    user = models.UserModel(email=email, name=name, phone_number=phone_number,
                            city=city, street=street, password=password, is_admin=False)
    db.session.add(user)
    db.session.commit()
    return states.SignupState.SIGNUP_SUCCESSFUL


def get_user(name):
    user = models.UserModel.query.filter_by(name=name).all()
    return user


def get_donee(id):
    user = models.DoneeModel.query.filter_by(id=id).first()
    return user


def insert_donee(id, fname, lname, city, street, phone_number):
    donee = models.UserModel.query.filter_by(id=id).first()
    if donee is None:
        return states.DoneeInsertionState.DONEE_EXISTS
    donee = models.DoneeModel(id=id, first_name=fname, last_name=lname, city=city,
                              street=street, phone_number=phone_number)
    db.session.add(donee)
    db.session.commit()
    return states.DoneeInsertionState.INSERTION_SUCCESSFUL


def get_donations_by_donee(id):
    donations = models.DonationModel.query.filter_by(id=id).all()
    return donations


def get_donations_by_user(name):
    donations = models.DonationModel.query.filter_by(name=name).all()
    return donations


def insert_donation(id, name, date_time, type, value):
    donation = models.UserModel.query.filter_by(id=id).first()
    if donation is None:
        return states.DonationInsertionState.DONEE_DOESNT_EXIST
    donation = models.UserModel.query.filter_by(name=name).first()
    if donation is None:
        return states.DonationInsertionState.USER_DOESNT_EXIST
    donation = models.DoneeModel(id=id, name=name, date=date_time,
                                 type=type, value=value)
    db.session.add(donation)
    db.session.commit()
    return states.DonationInsertionState.INSERTION_SUCCESSFUL