import time
import pandas as pd
import numpy as np

CITY_DATA = { 'chicago': 'chicago.csv',
              'new york city': 'new_york_city.csv',
              'washington': 'washington.csv' }

def get_filters():
    """
    Asks user to specify a city, month, and day to analyze.

    Returns:
        (str) city - name of the city to analyze
        (str) month - name of the month to filter by, or "all" to apply no month filter
        (str) day - name of the day of week to filter by, or "all" to apply no day filter
    """
    print('Hello! Let\'s explore some US bikeshare data!')
    # get user input for city (chicago, new york city, washington). HINT: Use a while loop to handle invalid inputs
    city = input(" Please,Enter Valid City Name!( chicago , new york city , washington) :").lower()
    while city not in (CITY_DATA.keys()):
        print("you provide a wrong city !")
        city = input(" Please,Enter Valid City Name!( chicago , new york city , washington) :").lower()


    # get user input for month (all, january, february, ... , june)
    months = ["january", "february", "march", "april", "may", "june","all"]
    all = months
    month = input("Which month :( January, February, March, April, May, June , all ) : ").lower()
    while month not in months:
        print("You provided invalid month!")
        month = input("Which month :( January, February, March, April, May, June , all ) : ").lower()
    

    # get user input for day of week (all, monday, tuesday, ... sunday)
    days = ["saturday","sunday","monday","tuesday","wednesday","thursday","friday","all"]
    all = days
    day = input("Which day :( Saturday, Sunday, Monday, Tuesday, Wednesday, Thursday, Friday, all ) : ").lower()
    while day not in days:
        print("You provided invalid day!")
        day = input("Which day :( Saturday, Sunday, Monday, Tuesday, Wednesday, Thursday, Friday, all ) : ").lower()

    print('-'*40)
    return city, month, day


def load_data(city, month, day):
    """
    Loads data for the specified city and filters by month and day if applicable.

    Args:
        (str) city - name of the city to analyze
        (str) month - name of the month to filter by, or "all" to apply no month filter
        (str) day - name of the day of week to filter by, or "all" to apply no day filter
    Returns:
        df - Pandas DataFrame containing city data filtered by month and day
    """
    # load a data file into a dataframe
    df = pd.read_csv(CITY_DATA[city])

    # convert the Start Time column in dataframe to datetime :
    df["Start Time"] = pd.to_datetime(df["Start Time"])

    # extract month and day of week from Start Time to create new columns :
    df["month"] = df["Start Time"].dt.month
    df["day_of_week"] = df["Start Time"].dt.day_name()

    # filter by month if need Or all :
    if month != "all":
        # use the index of the months list to get the corresponding integr
        months = ["january", "february", "march", "april", "may", "june"]
        month = months.index(month) + 1

        # filter by month to create new dataframe
        df = df[df['month'] == month]

    # filter by day of week if need Or all :
    if day != "all":
        # filter by day of week to create the new dataframe
        df = df[df["day_of_week"] == day.title()]


    return df


def time_stats(df):
    """Displays statistics on the most frequent times of travel."""

    print('\nCalculating The Most Frequent Times of Travel...\n')
    start_time = time.time()

    # display the most common month

    stat1 = df["month"].mode()[0]
    print("\n the most common month is : {}".format(stat1))

    # display the most common day of week
    
    stat2 = df["day_of_week"].mode()[0]
    print("\n the most common day of week is : {}".format(stat2))

    # display the most common start hour
    df["hour"] = df["Start Time"].dt.hour
    stat3 = df["hour"].mode()[0]
    print("\n the most common start hour is : {}".format(stat3))


    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def station_stats(df):
    """Displays statistics on the most popular stations and trip."""

    print('\nCalculating The Most Popular Stations and Trip...\n')
    start_time = time.time()

    # display most commonly used start station
    stat4 = df["Start Station"].mode()[0]
    print("\n the most commonly used start station is : {}".format(stat4))
    
    # display most commonly used end station
    stat5 = df["End Station"].mode()[0]
    print("\n the most commonly used end station is : {}".format(stat5))
    
    # display most frequent combination of start station and end station trip
    df["Trip"] = " From " + df["Start Station"] + " To " + df["End Station"]
    stat6 = df["Trip"].mode()[0]
    print("\n the most frequent combination of start station and end station trip is : {}".format(stat6))


    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def trip_duration_stats(df):
    """Displays statistics on the total and average trip duration."""

    print('\nCalculating Trip Duration...\n')
    start_time = time.time()

    # display total travel time
    stat7 = df["Trip Duration"].sum()
    print("\n the total travel time is : {}".format(stat7))

    # display mean travel time
    stat8 = df["Trip Duration"].mean()
    print("\n the mean travel time is : {}".format(stat8))

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def user_stats(df):
    """Displays statistics on bikeshare users."""

    print('\nCalculating User Stats...\n')
    start_time = time.time()

    # Display counts of user types
    stat9 = df["User Type"].value_counts()
    print("\n counts of users is : {}".format(stat9))

    # Display counts of gender
    try:
        stat10 = df["Gender"].value_counts()
        print("\n coints of gender is : {}".format(stat10))
    except:
        print(" Gender is not found !")

    # Display earliest, most recent, and most common year of birth
    try:
        stat11 = df["Birth Year"].min()
        stat12 = df["Birth Year"].max()
        stat13 = df["Birth Year"].mode()[0]
        print("\n the erliest year of birth is : {}".format(stat11))
        print("\n the most recent year of birth is : {}".format(stat12))
        print("\n the most common year of birth is : {}".format(stat13))
    except:
        print (" Birth Year is not found !")
    

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)
    
def display_Raw_Data(df):
    """" displays followed data according to user input
    Args:
        df - pd.DataFrame of city data filtered by month and day which return from load_data() function
    
    """
    demand = input("would you like to display Raw Data ? (yes Or no )").lower()

    while demand == "yes":
        print(df.sample(5))

        demand = input("would you like to display Raw Data ? (yes Or no )").lower()

def main():
    while True:
        city, month, day = get_filters()
        df = load_data(city, month, day)

        time_stats(df)
        station_stats(df)
        trip_duration_stats(df)
        user_stats(df)
        display_Raw_Data(df)

        restart = input('\nWould you like to restart? Enter yes or no.\n')
        if restart.lower() != 'yes':
            break

if __name__ == "__main__":
	main()
