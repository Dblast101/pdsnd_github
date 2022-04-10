import time
import pandas as pd
import numpy as np

CITY_DATA = { 'Chicago': 'chicago.csv',
              'New York City': 'new_york_city.csv',
              'Washington': 'washington.csv' }

def get_filters():
    """
    Asks user to specify a city, month, and day to analyze.

    Returns:
        (str) city - name of the city to analyze
        (str) month - name of the month to filter by, or "all" to apply no month filter
        (str) day - name of the day of week to filter by, or "all" to apply no day filter

    """
    city_a = ['Chicago', 'New York City', 'Washington']
    month_a = ['January', 'February', 'March', 'April', 'May', 'June', 'All']
    day_a = ['Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday', 'Sunday', 'All']

    """
    ^ Stats all the available options that will not result in a non-valid entry.
    Below is it verifying each entry with the response given and then formating them to avoid the need to be case sensitive
    """

    print('Hello! Let\'s explore some US bikeshare data! Please choose from the options below.')

    while True:
        try:
                # TO DO: get user input for city (chicago, new york city, washington). HINT: Use a while loop to handle invalid inputs
            city = city_a.index(input('Which city would you like to see bikeshare data for out of: Chicago, New York City or Washington?\n').lower().title())
                #add While loops for invalid inputs

                # TO DO: get user input for month (all, january, february, ... , june)
            month = month_a.index(input('Which month do you wish to look at, there is: January, February, March, April, May and June? or you can type \'All\' instead.\n').lower().title())

                # TO DO: get user input for day of week (all, monday, tuesday, ... sunday)
            day = day_a.index(input('Which day to you wish to look at, there is Monday, Tuesday, Wednesday, Thursday, Friday, Saturday & Sunday? or you can type \'All\' instead.\n').lower().title())
            print('-'*40)
            return city_a[city], month_a[month], day_a[day]

        except ValueError:
            print('\nYour previous answer\s is not one of the listed options or has been type incorrectly, Check over your previous answer and please try again.\n')


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
    df = pd.read_csv(CITY_DATA[city])

    df['Start Time'] = pd.to_datetime(df['Start Time'])

    df['month'] = df['Start Time'].dt.month
    df['day_of_week'] = df['Start Time'].dt.weekday_name
    df['hour'] = df['Start Time'].dt.hour

    df['start'] = df['Start Station']
    df['end'] = df['End Station']

    df['travel'] = df['Trip Duration']

    df['users'] = df['User Type']

    df['gen'] = df['Gender']

    df['bir_yea'] = df['Birth Year']
    """
    ^ Above is a creation of many variables for later use, these connect to column in the .csv.
    Below is processing the month and day processes for the df.
    """

    if month != 'All':
        months = ['January', 'February', 'March', 'April', 'May', 'June']
        month = months.index(month) + 1

        df = df[df['month'] == month]

    if day != 'All':

        df = df[df['day_of_week'] == day.title()]

    return df



def time_stats(df):
    """Displays statistics on the most frequent times of travel."""

    print('\nCalculating The Most Frequent Times of Travel...\n')
    start_time = time.time()

    """
    Each answer is using pandas.datetime to process and find the correct answer, a legend for the month was added for readablity
    """

    # TO DO: display the most common month
    com_mon = df['month'].mode()[0]

    print('Most Common Month:', com_mon, '\n 1 = January, 6 = June')

    # TO DO: display the most common day of week
    com_day = df['day_of_week'].mode()[0]

    print('Most Common Day of the Week:', com_day)

    # TO DO: display the most common start hour
    com_hr = df['hour'].mode()[0]

    print('Most Common Start Hour:', com_hr)

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)



def station_stats(df):
    """Displays statistics on the most popular stations and trip."""

    print('\nCalculating The Most Popular Stations and Trip...\n')
    start_time = time.time()

    """
    Each answer is finding the most commonly used station, 3rd one is finded most commonly found matching start and end station
    """

    # TO DO: display most commonly used start station
    start_s = df['start'].mode().loc[0]

    print('Most Commonly Used Start Station:', start_s)

    # TO DO: display most commonly used end station
    end_s = df['end'].mode().loc[0]

    print('Most Commonly Used End Station:', end_s)


    # TO DO: display most frequent combination of start station and end station trip
    combo = df.groupby(['start', 'end']).size().idxmax()

    print('Most Frequent combination of Start Station and End Station are:', combo)

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def trip_duration_stats(df):
    """Displays statistics on the total and average trip duration."""

    print('\nCalculating Trip Duration...\n')
    start_time = time.time()

    """
    One is finding the total travel and the other is the average/mean
    """

    # TO DO: display total travel time
    tot_travel = df['travel'].sum()

    print('The total hours travelled time for this period is:', tot_travel)

    # TO DO: display mean travel time
    mean_travel = df['travel'].mean().round(2)

    print('The mean of all total hours travelled time for this period is:', mean_travel)

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def user_stats(df):
    """Displays statistics on bikeshare users."""

    print('\nCalculating User Stats...\n')
    start_time = time.time()

    """
    The useres have been broken down into individual fields for each question, 3rd one shows against peoples birth years.
    """

    # TO DO: Display counts of user types
    sub_count = df['users'].str.count('Subscriber').sum().astype(int)
    cus_count = df['users'].str.count('Customer').sum().astype(int)

    print('The total amount of each User types:\nSubscriber Counts:', sub_count, '\nCustomer Counts:', cus_count)
    # TO DO: Display counts of gender
    male_count = df['gen'].str.count('Male').sum().astype(int)
    female_count = df['gen'].str.count('Female').sum().astype(int)
    null_count = df['gen'].isnull().sum()

    print('\nThe total amount of each gender type:\nMale Count:', male_count, '\nFemale Counts:', female_count, '\nNone provided:', null_count)

    # TO DO: Display earliest, most recent, and most common year of birth
    early = df['bir_yea'].min().astype(int)
    most_rec = df['bir_yea'].max().astype(int)
    com_year = df['bir_yea'].iloc[0].max().astype(int)

    print('\nThe Earliest, Most Recent, and Most Common Year of Birth are: \nEarlist:', early, '\nMost Recent:', most_rec, '\nCommon Year of Birth:', com_year)

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)

    extra_raw = 5
    raw_data = input('\nDo you wish to see 5 lines of raw data? Enter y or n?\n')
    if raw_data.lower() == 'y':
        get_raw = df.head()
        print(get_raw)
        add_data = input('\nDo you wish to see another 5 lines of raw data? Enter y or n?\n')
        while True:
            if add_data.lower() == 'y':
                extra_raw = extra_raw + 5
                print(df.head(extra_raw))
                maybe = input('\nDo you wish to see another 5 lines of raw data? Enter y or n?\n')
                if maybe.lower() == 'y':
                    extra_raw + 5
                else:
                    break
        """
        ^ Above will show the first 5 raw data results, then added an extra 5 for each iteration, ultimately ended when the user chooses to stop.
        Pressing 'n' will break the loop while a 'y' will add 5 more.
        The break will prop the restart option for the user.
        """




def main():
    while True:
        city, month, day = get_filters()
        df = load_data(city, month, day)

        time_stats(df)
        station_stats(df)
        trip_duration_stats(df)
        user_stats(df)

        restart = input('\nWould you like to restart? Enter y or n.\n')
        if restart.lower() != 'y':
            break



if __name__ == "__main__":
	main()
