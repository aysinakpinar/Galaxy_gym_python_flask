import pytest
from models.user import *
from models import UserModel
from flask import *
from extension import db
from app import create_app
from tests.factories import create_user
# Khadija, Millie & Louis logout test code 
# create dummy user to log out

def test_logout(client):
    with client.session_transaction() as sess:
        sess['user_id'] = 1

    response = client.get('/auth/logout', follow_redirects=True)

    with client.session_transaction() as sess:
        assert 'user_id' not in sess
    
    assert response.status_code == 200
    


#Aysin's code to test signup
def test_create_user_username(app, database):
    with app.app_context():
        # Create a user with random fake attributes
        user = create_user()

        # Retrieve the user from the database
        saved_user = UserModel.query.filter_by(username=user.username).first()

        # Assertions
        assert saved_user is not None  # Ensure user exists
        assert saved_user.id is not None  # Ensure ID is assigned
        assert saved_user.username == user.username
        assert saved_user.email == user.email
        assert saved_user.location == user.location
#Aysin's code to test signup
def test_create_user_email(app, database):
    with app.app_context():
        # Create a user with random fake attributes
        user = create_user()

        # Retrieve the user from the database
        saved_user = UserModel.query.filter_by(email=user.email).first()

        # Assertions
        assert saved_user is not None  # Ensure user exists
        assert saved_user.id is not None  # Ensure ID is assigned
        assert saved_user.username == user.username
        assert saved_user.email == user.email
        assert saved_user.location == user.location
#Aysin's code to test signup    
def test_unique_user_details(app, database):
    with app.app_context():
        user = create_user()
        #verify Frank has been created
        assert UserModel.query.filter_by(username = user.username).first() is not None
        # Try creating a user with same email
        with pytest.raises(Exception, match="duplicate key value violates unique constraint"):
            user1 = create_user(None, user.email, None)
            db.session.add(user1)
        db.session.rollback()
        #Try creating a user with same username
        with pytest.raises(Exception, match="duplicate key value violates unique constraint"):
            user2 = create_user(user.username, None, None)
            db.session.add(user2)
            db.session.commit()
        db.session.rollback()
        assert UserModel.query.count() == 1, f"Expected 1 user, found {UserModel.query.count()}"