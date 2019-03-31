import time

import numpy as np
import pandas as pd

CITY_DATA = { 'chicago': 'chicago.csv',
              'new york city': 'new_york_city.csv',
              'washington': 'washington.csv' }
cities = ['chicago', 'new york city', 'washington']
months = ['january', 'february', 'march', 'april', 'may', 'june', 'all']
days = ['monday','tuesday', 'wednesday', 'thursday', 'friday', 'saturday', 'sunday', 'all']

def get_filters():
    """
    Asks user to specify a city, month, and day to analyze.

    Returns:
        (str) city - name of the city to analyze
        (str) month - name of the month to filter by, or "all" to apply no month filter
        (str) day - name of the day of week to filter by, or "all" to apply no day filter
    """
    print('Hello! Let\'s explore some US bikeshare data!')
    # TO DO: get user input for city (chicago, new york city, washington). HINT: Use a while loop to handle invalid inputs

    while True:
        city = input("Which city do you like to evaluate. Chicago, New York City or Washington? ").lower()
        if city in cities:
            break

    # TO DO: get user input for month (all, january, february, ... , june)
    while True:
        month = input("Which month are you interested in? Choose from january until june or all for no filter. " ).lower()
        if month in months:
            break

    # TO DO: get user input for day of week (all, monday, tuesday, ... sunday)
    while True:
        day = input("For which day of the week you would like to do yout anlysis? Choose a day from monday to sunday or all for no filter. " \
                    ).lower()
        if day in days:
            break

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
    # load data file into a dataframe
    df = pd.read_csv(CITY_DATA[city])

    # convert the Start Time column to datetime
    df['Start Time'] = pd.to_datetime(df['Start Time'])

    # extract month and day of week from Start Time to create new columns
    df['month'] = df['Start Time'].dt.month
    df['day_of_week'] = df['Start Time'].dt.weekday_name
    df['hour'] = df['Start Time'].dt.hour

    # filter by month if applicable
    if month != 'all':
        # use the index of the months list to get the corresponding int
        months = ['january', 'february', 'march', 'april', 'may', 'june']
        month = months.index(month) + 1

        # filter by month to create the new dataframe
        df = df[df['month'] == month]

    # filter by day of week if applicable
    if day != 'all':
        # filter by day of week to create the new dataframe
        df = df[df['day_of_week'] == day.title()]

    return df

def time_stats(df):
    """Displays statistics on the most frequent times of travel."""

    print('\nCalculating The Most Frequent Times of Travel...\n')
    start_time = time.time()

    # TO DO: display the most common month
    popular_month = df['month'].mode()[0]
    print("The most common month is",popular_month,".")

    # TO DO: display the most common day of week
    popular_day = df['day_of_week'].mode()[0]
    print("The most common day of the week is",popular_day,".")

    # TO DO: display the most common start hour
    popular_hour = df['hour'].mode()[0]
    print("The most common start hour is",popular_hour, "o'clock.")

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def station_stats(df):
    """Displays statistics on the most popular stations and trip."""

    print('\nCalculating The Most Popular Stations and Trip...\n')
    start_time = time.time()

    # TO DO: display most commonly used start station
    popular_start_station = df['Start Station'].mode()[0]
    print("The most commonly used start station :", popular_start_station)

    # TO DO: display most commonly used end station
    popular_end_station = df['End Station'].mode()[0]
    print("The most commonly used end station :", popular_end_station)

    # TO DO: display most frequent combination of start station and end station trip
    popular_start_end_station = df[['Start Station', 'End Station']].mode().loc[0]
    print("The most commonly used start station and end station : {}, {}"\
            .format(popular_start_end_station[0], popular_start_end_station[1]))

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def trip_duration_stats(df):
    """Displays statistics on the total and average trip duration."""

    print('\nCalculating Trip Duration...\n')
    start_time = time.time()

    # TO DO: display total travel time
    travel_time = df['Trip Duration'].sum()
    print("Total travel time :", travel_time)

    # TO DO: display mean travel time
    travel_mean = df['Trip Duration'].mean()
    print("Mean travel time :", travel_mean)

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def user_stats(df):
    """Displays statistics on bikeshare users."""

    print('\nCalculating User Stats...\n')
    start_time = time.time()

    # TO DO: Display counts of user types
    user_counts = df['User Type'].value_counts()
    print("Counts of user types:\n", user_counts)



    # TO DO: Display counts of gender
    if set(['Gender']).issubset(df.columns):
        gender_counts = df['Gender'].value_counts()
        print("\nCounts of gender:\n", gender_counts)
    else:
        print("\nNo gender data.")


    # TO DO: Display earliest, most recent, and most common year of birth
    if set(['Birth Year']).issubset(df.columns):
        birth_year = df['Birth Year']

        earliest_year = int(birth_year.min())
        print("\nThe most earliest birth year is {}.".format(earliest_year))

        most_common_year = int(birth_year.mode()[0])
        print("The most common birth year is {}.".format(most_common_year))

        most_recent = int(birth_year.max())
        print("The most recent birth year is {}.".format(most_recent))
    else:
        print("\nNo birth data.")

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def main():
    while True:
        city, month, day = get_filters()
        df = load_data(city, month, day)

        time_stats(df)
        station_stats(df)
        trip_duration_stats(df)
        user_stats(df)

        i = 5
        while True:
            display = input("\nWould you like to see the raw data? Enter yes or no.\n")
            if display.lower() == 'yes':
                print(df.iloc[(i-5):i])
                i = i + 5
            else:
                break

        restart = input('\nWould you like to restart? Enter yes or no.\n')
        if restart.lower() != 'yes':
           break


if __name__ == "__main__":
	main()
