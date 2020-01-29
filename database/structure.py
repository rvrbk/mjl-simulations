import db

def create_car_table():
    d = db.DB()
    
    d.query("""
        CREATE TABLE IF NOT EXISTS cars (
            id integer PRIMARY KEY,
            name varchar(255) NOT NULL,
            weight integer NOT NULL
        );
    """)

def create_piezo_table():
    d = db.DB()
    
    d.query("""
        CREATE TABLE IF NOT EXISTS piezos (
            id integer PRIMARY KEY,
            name varchar(255) NOT NULL,
            weight integer NOT NULL,
            length integer NOT NULL,
            width integer NOT NULL,
            height integer NOT NULL,
            min_output integer NOT NULL,
            max_output integer NOT NULL
        );
    """)

def create_tire_table():
    d = db.DB()
    
    d.query("""
        CREATE TABLE IF NOT EXISTS tires (
            id integer PRIMARY KEY,
            name varchar(255) NOT NULL,
            section_width integer NOT NULL,
            aspect_ratio integer NOT NULL,
            wheel_diameter integer,
            weight integer NOT NULL
        );
    """)

def create_setup_table():
    d = db.DB()
    
    d.query("""
        CREATE TABLE IF NOT EXISTS setups (
            id integer PRIMARY KEY,
            name varchar(255) NOT NULL,
            description text NOT NULL,
            piezo_id integer NOT NULL,
            tire_id integer NOT NULL,
            amount_sidewall integer NOT NULL,
            amount_base integer NOT NULL
        );
    """)

def create_scenario_table():
    d = db.DB()
    
    d.query("""
        CREATE TABLE IF NOT EXISTS scenarios (
            id integer PRIMARY KEY,
            car_id integer NOT NULL,
            setup_id integer NOT NULL,
            speed integer NOT NULL,
            distance integer NOT NULL
        );
    """)

def create_result_table():
    d = db.DB()
    
    d.query("""
        CREATE TABLE IF NOT EXISTS results (
            id integer PRIMARY KEY,
            setup_id integer NOT NULL,
            scenario_id integer NOT NULL,
            min_output float NOT NULL,
            max_output float NOT NULL,
            created datetime NOT NULL
        );
    """)

create_car_table()
create_piezo_table()
create_tire_table()
create_setup_table()
create_scenario_table()
create_result_table()