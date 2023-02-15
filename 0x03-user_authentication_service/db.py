#!/usr/bin/env python3
"""DB module
"""
from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
from sqlalchemy.orm.session import Session
from user import Base, User
from sqlalchemy.orm.exc import NoResultFound
from sqlalchemy.exc import InvalidRequestError


class DB:
    """DB class
    """

    def __init__(self) -> None:
        """Initialize a new DB instance
        """
        self._engine = create_engine("sqlite:///a.db", echo=False)
        Base.metadata.drop_all(self._engine)
        Base.metadata.create_all(self._engine)
        self.__session = None

    @property
    def _session(self) -> Session:
        """Memoized session object
        """
        if self.__session is None:
            DBSession = sessionmaker(bind=self._engine)
            self.__session = DBSession()
        return self.__session

    def add_user(self, email: str, hashed_password: str) -> User:
        """ add user to session ?"""
        u = User(email=email, hashed_password=hashed_password)
        self._session.add(u)
        self._session.commit()
        return u

    def find_user_by(self, **kwargs: dict) -> User:
        """ get user filter_by kwargs criteria """
        attrs = ["id", "email", "hashed_password", "session_id", "reset_token"]
        for key in kwargs:
            if key not in attrs:
                raise InvalidRequestError
        usr = self._session.query(User).filter_by(**kwargs).first()
        if not usr:
            raise NoResultFound
        return usr

    def update_user(self, user_id: int, **kwargs: dict) -> None:
        """ update user """
        try:
            usr = self.find_user_by(id=user_id)
        except Exception:
            raise ValueError
        attrs = ["id", "email", "hashed_password", "session_id", "reset_token"]
        if not kwargs:
            raise ValueError
        for key, val in kwargs.items():
            if key not in attrs:
                raise ValueError
            else:
                setattr(usr, key, val)
        self._session.commit()
