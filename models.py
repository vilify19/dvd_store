from sqlalchemy import Column, Integer, String, DateTime, ForeignKey, Float, Boolean
from sqlalchemy.ext.declarative import declarative_base
from session import engine


Base = declarative_base(bind=engine)


class Category(Base):
    __tablename__ = "category"

    id = Column(Integer, primary_key=True, autoincrement=True)
    name = Column(String(50), nullable=False)
    last_update = Column(DateTime, onupdate=True)

    def __str__(self):
        return self.name


class FilmCategory(Base):
    __tablename__ = "film_category"

    id = Column(Integer, primary_key=True, autoincrement=True)
    film_id = Column(Integer, ForeignKey('film.id'))
    category_id = Column(Integer, ForeignKey('category.id'))
    last_update = Column(DateTime, onupdate=True)

    def __str__(self):
        return f'Film: {self.film_id}, Category:{self.category_id}'


class Film(Base):
    __tablename__ = "film"

    id = Column(Integer, primary_key=True, autoincrement=True)
    title = Column(String(50), nullable=False)
    description = Column(String(200), nullable=False)
    release_year = Column(DateTime, nullable=False)
    language_id = Column(Integer, ForeignKey('language.language_id'))
    rental_duration = Column(Integer, nullable=False, default=0)
    rental_rate = Column(Integer, nullable=False, default=0)
    length = Column(Integer, nullable=False)
    replacement_cost = Column(Float, nullable=False, default=0)
    rating = Column(Integer, nullable=False)
    last_update = Column(DateTime, onupdate=True)
    special_features = Column(String(50), nullable=False)
    fulltext = Column(String(200), nullable=False)

    def __str__(self):
        return f'Title: {self.title}'


class Language(Base):
    __tablename__ = "language"

    language_id = Column(Integer, primary_key=True, autoincrement=True)
    name = Column(String(50), nullable=False)
    last_update = Column(DateTime, onupdate=True)

    def __str__(self):
        return f'Language: {self.name}'


class FilmActor(Base):
    __tablename__ = "film_actor"

    id = Column(Integer, primary_key=True, autoincrement=True)
    actor_id = Column(Integer, ForeignKey('actor.actor_id'))
    film_id = Column(Integer, ForeignKey('film.id'))
    last_update = Column(DateTime, onupdate=True)

    def __str__(self):
        return f'Film_id: {self.film_id}'


class Actor(Base):
    __tablename__ = "actor"

    actor_id = Column(Integer, primary_key=True, autoincrement=True)
    first_name = Column(String(50), nullable=False)
    last_name = Column(String(50), nullable=False)
    last_update = Column(DateTime, onupdate=True)

    def __str__(self):
        return f'{self.first_name} {self.last_name}'


class Inventory(Base):
    __tablename__ = "inventory"

    inventory_id = Column(Integer, primary_key=True, autoincrement=True)
    film_id = Column(Integer, ForeignKey('film.id'))
    store_id = Column(Integer, ForeignKey('store.store_id'))
    last_update = Column(DateTime, onupdate=True)

    def __str__(self):
        return f'Film: {self.film_id}, Store: {self.store_id}'


class Rental(Base):
    __tablename__ = "rental"

    rental_id = Column(Integer, primary_key=True, autoincrement=True)
    rental_date = Column(DateTime, nullable=False)
    inventory_id = Column(Integer, ForeignKey('inventory.inventory_id'))
    customer_id = Column(Integer, ForeignKey('customer.customer_id'))
    return_date = Column(DateTime, nullable=False)
    stuff_id = Column(Integer, ForeignKey('staff.staff_id'))
    last_update = Column(DateTime, onupdate=True)

    def __str__(self):
        return f'Rental: {self.rental_id}, Rental Date: {self.rental_date}'


class Customer(Base):
    __tablename__ = 'customer'

    customer_id = Column(Integer, primary_key=True, autoincrement=True)
    store_id = Column(Integer, ForeignKey('store.store_id'))
    first_name = Column(String(50), nullable=False)
    last_name = Column(String(50), nullable=False)
    email = Column(String(50), nullable=False)
    address_id = Column(Integer, ForeignKey('address.address_id'))
    is_active = Column(Boolean, nullable=False, default=True)
    create_date = Column(DateTime, nullable=False)
    lastupdate = Column(DateTime, onupdate=True)
    rental_id = Column(Integer, ForeignKey('rental.rental_id'))

    def __str__(self):
        return f'Customer: {self.first_name} {self.last_name}'


class Payment(Base):
    __tablename__ = 'payment'

    payment_id = Column(Integer, primary_key=True, autoincrement=True)
    customer_id = Column(Integer, ForeignKey('customer.customer_id'))
    stuff_id = Column(Integer, ForeignKey('staff.staff_id'))
    rental_id = Column(Integer, ForeignKey('rental.rental_id'))
    amount = Column(Float, nullable=False)
    payment_date = Column(DateTime, nullable=False)

    def __str__(self):
        return f'Payment: {self.amount} {self.payment_date}'


class Staff(Base):
    __tablename__ = 'staff'

    staff_id = Column(Integer, primary_key=True, autoincrement=True)
    first_name = Column(String(50), nullable=False)
    last_name = Column(String(50), nullable=False)
    address_id = Column(Integer, ForeignKey('address.address_id'))
    store_id = Column(Integer, ForeignKey('store.store_id'))
    active = Column(Boolean, default=True)
    username = Column(String(50), nullable=False)
    password = Column(String(50), nullable=False)
    last_update = Column(DateTime, onupdate=True)
    picture = Column(String(50), nullable=False)

    def __str__(self):
        return f'Staff: {self.first_name} {self.last_name}'


class Address(Base):
    __tablename__ = 'address'

    address_id = Column(Integer, primary_key=True, autoincrement=True)
    address = Column(String(100), nullable=False)
    address2 = Column(String(100), nullable=False)
    district = Column(String(50), nullable=False)
    city_id = Column(Integer, ForeignKey('city.city_id'))
    postal_code = Column(String(50), nullable=False)
    phone = Column(String(50), nullable=False)
    last_update = Column(DateTime, onupdate=True)

    def __str__(self):
        return f'Address: {self.address} {self.postal_code}'


class Store(Base):
    __tablename__ = 'store'

    store_id = Column(Integer, primary_key=True, autoincrement=True)
    manager_staff_id = Column(Integer, ForeignKey('staff.staff_id'))
    address_id = Column(Integer, ForeignKey('address.address_id'))
    last_update = Column(DateTime, onupdate=True)

    def __str__(self):
        return f'Store: {self.store_id} {self.manager_staff_id}'


class City(Base):
    __tablename__ = 'city'

    city_id = Column(Integer, primary_key=True, autoincrement=True)
    city = Column(String(50), nullable=False)
    country_id = Column(Integer, ForeignKey('country.country_id'))
    last_update = Column(DateTime, onupdate=True)

    def __str__(self):
        return f'City: {self.city}'


class Country(Base):
    __tablename__ = 'country'

    country_id = Column(Integer, primary_key=True, autoincrement=True)
    country = Column(String(50), nullable=False)
    last_update = Column(DateTime, onupdate=True)

    def __str__(self):
        return f'City: {self.country}'
