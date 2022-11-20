import time
import pandas as pd
import numpy as np
import json



CITY_DATA = { 'chicago': 'chicago.csv',
              'new york city': 'new_york_city.csv',
              'washington': 'washington.csv' }
CITIES = ['chicago', 'new york', 'washington']

MONTHS = ['january', 'february', 'march', 'april', 'may', 'june']

DAYS = ['sunday', 'monday', 'tuesday', 'wednesday', \
        'thursday', 'friday', 'saturday' ]

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
        city=input("which city you choose Chicago,New York or Washington? \n>").lower()
        if city in CITIES:
            break

    # TO DO: get user input for month (all, january, february, ... , june)
    month = get_user_input('All right! now it\'s time to provide us a month name '\
                    'or just say \'all\' to apply no month filter. \n(e.g. all, january, february, march, april, may, june) \n> ', MONTHS)

    # TO DO: get user input for day of week (all, monday, tuesday, ... sunday)
    day = get_user_input('One last thing. Could you type one of the week day you want to analyze?'\
                   ' You can type \'all\' again to apply no day filter. \n(e.g. all, monday, sunday) \n> ', DAYS)
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

    # extract month and day of week and hour from Start Time to create new columns
    df['month'] = df['Start Time'].dt.month
    df['day_of_week'] = df['Start Time'].dt.weekday_name
    df['hour'] = df['Start Time'].dt.hour

    # filter by month if applicable
    if month != 'all':
        month =  MONTHS.index(month) + 1
        df = df[ df['month'] == month ]

    # filter by day of week if applicable
    if day != 'all':
        # filter by day of week to create the new dataframe
        df = df[ df['day_of_week'] == day.title()]
        return df


def time_stats(df):
    """Displays statistics on the most frequent times of travel."""

print('\nCalculating The Most Frequent Times of Travel...\n')
start_time = time.time()

    # TO DO: display the most common month
most_common_month=df['month'].value_counts().idmax()
print("most common month of the year is : " ,most_commom_month)

    # TO DO: display the most common day of week
most_common_day_of_week=df['day_of_week'].value_counts().idmax()
print("most common day of the week is : " ,most_common_day_of_week)


    # TO DO: display the most common start hour
most_common_start_hour=df['hour'].value_counts().idmax()
print("most common start hour is : " ,most_common_start_hour)

print("\nThis took %s seconds." % (time.time() - start_time))
print('-'*40)


def station_stats(df):
    """Displays statistics on the most popular stations and trip."""

    print('\nCalculating The Most Popular Stations and Trip...\n')
    start_time = time.time()

    # TO DO: display most commonly used start station
most_common_start_station=df['Start Station'].value_counts().idmax()
print("most common used start station is : ", most_common_start_station)


    # TO DO: display most commonly used end station
most_common_end_station=df['End Station'].value_counts().idmax()
print("most common used end station is : ", most_common_end_station)


    # TO DO: display most frequent combination of start station and end station trip
most_common__start_end_station=df[['Start Station','End Station']].mode().loc[0]
print("most common used start station and end station :{},{}",format(most_common__start_end_station[0],most_common__start_end_station[1]))

print("\nThis took %s seconds." % (time.time() - start_time))
print('-'*40)


def trip_duration_stats(df):
    """Displays statistics on the total and average trip duration."""

    print('\nCalculating Trip Duration...\n')
    start_time = time.time()

    # TO DO: display total travel time
total_travel_time=df['Trip Duration'].sun()
 
print('total travel time is ',total_travel_time)    

    # TO DO: display mean travel time
mean_travel_time=df['Trip Duration'].mean()
print('mean travel time is ',mean_travel_time)

print("\nThis took %s seconds." % (time.time() - start_time))
print('-'*40)


def user_stats(df):
    """Displays statistics on bikeshare users."""

    print('\nCalculating User Stats...\n')
    start_time = time.time()

    # TO DO: Display counts of user types
counts_user_type=df['User Type'].count_values()
print(counts_user_type)

    # TO DO: Display counts of gender
counts_gender=df['Gender'].count_values()
print(counts_gender)

    # TO DO: Display earliest, most recent, and most common year of birth
earliest_year=df['Birth Year'].min()
print("the most earliest birth year is ",earliest_year)
recent_year=df['Birth Year'].max()
print("the most recent birth year is ",recent_year)
most_common_year=df['Birth Year'].value_counts().idmax()
print("the most common birth year is ",most_common_year)

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

        restart = input('\nWould you like to restart? Enter yes or no.\n')
        if restart.lower() != 'yes':
            break


if __name__ == "__main__":
	main()
