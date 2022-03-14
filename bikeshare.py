import time
import pandas as pd
import numpy as np


 
CITY_DATA = { 'chicago': 'chicago.csv',
              'new york city': 'new_york_city.csv',
              'washington': 'washington.csv' }
#Firstly 
# we will put our months, days and cities into lists to be used later
months=['january','february', 'march', 'april', 'may', 'june' , 'all']
states=['chicago', 'new york city', 'washington']
week=['saturday', 'sunday', 'monday', 'tuesday', 'wednesday', 'thursday', 'friday', 'all']

# alist created to be used in gender calculation

genlist = ['chicago', 'new york city']

#a list will be created containig a response to be used in the preview
#of the raw data
    
data = ['no']

#Secondly filers function will be defined as below

def get_filters():
    
    
    """
    Asks user to specify a city, month, and day to analyze.

    Returns:
        (str) city - name of the city to analyze
        (str) month - name of the month to filter by, or "all" to apply no month filter
        (str) day - name of the day of week to filter by, or "all" to apply no day filter
    """
    print('Hello! Let\'s explore some US bikeshare data!')
    print("Data of cities allowed are for chicago, new york city, and washington")
    print('-' * 70)
    print('------------------------Attention please !!!-------------------------')
    print("Your month filter must be applied within the following period")
    print(months)
    print("Your day filter must be applied within the following choices")
    print(week)
#we will ask the user to chose a city from this list
    print('-' * 70)
# TO DO: get user input for city (chicago, new york city, washington). HINT: Use a while loop to handle invalid inputs
    while True:
      city = str(input("\nchose a city from the previously mentioned:\n")).lower()
     
      if city not in states:
        print("Unrecognised city choice re-enter the city")
      else:
        break
                
# TO DO: get user input for month (all, january, february, ... , june)
    
    
    while True:
      month=str(input("\nplease specify a month from above mentioned list & for the whole period chose 'all':\n ")).lower()
      if month not in months:
        print("Unrecognised month choice re-enter the month:\n ")
      else:
        break
        
     
      
 #Ask the user to specify the day of the required data from an automatic appeared list
    
    while True:
        day=str(input("please specify a day from above mentioned list & for the whole period chose 'all':\n ")).lower()
        if day not in week:
            print("Unrecognized day choice kindly chose from the above list: ")
        else:
            break     
    print('-' * 70)           
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
#loading the data of the 3 cities into a data frame
    
    df = pd.read_csv(CITY_DATA[city])

#return the start time column into date time

    df['Start Time'] = pd.to_datetime(df['Start Time'])
    
# form a new columns for month and day from the start time column

    df['month'] =df['Start Time'].dt.month  
    df['day_of_week'] = df['Start Time'].dt.weekday_name
 #Filtration process will begin from here from month through day

    if month != 'all':
       month = months.index(month) + 1 
       df = df[df['month']== month]
       
#apply filters for day  if it is necessary
    if day != 'all':
       df = df[df['day_of_week']== day.title()]

    return df


def time_stats(df):
    """Displays statistics on the most frequent times of travel."""
    print('\nCalculation of frequent times for the travel\n')
    start_time = time.time()
   
    # TO DO: display the most common month and its count
    #cm is an abbreviation for "common month"
   
    cm = df['month'].mode()[0]
    print(f'Most Common Month: {cm}')

    # TO DO: display the most common day of week
    #cd is an abbreviation for "common day"
    cd= df['day_of_week'].mode()[0]
    print(f"According to your choices , the most common day is: {cd}")

    # TO DO: display the most common start hour
    df['hour'] = df['Start Time'].dt.hour
    common_start_hour = df['hour'].mode()[0]
    print(f"According to your choices , the most common hour is {common_start_hour}")
    
    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*70)

#statistical analysus for stations data

def station_stats(df):
    """Displays statistics on the most popular stations and trip."""
    print('\nCalculating The Most Popular Stations and Trip...\n')
    start_time = time.time()

    # TO DO: display most commonly used start station
    css = df["Start Station"].mode()[0]           #css---> abbreviation for common start station
    print(f"The most common start staion is:\n{css}")

    # TO DO: display most commonly used end station
    ces = df["End Station"].mode()[0]             #ces----> abbreviation for commonly end station
    print(f"The most common end staion is:\n{ces}")

    # TO DO: display most frequent combination of start station and end station trip
    
    '''the arrow direction lead to the end station
    '''
    
    station_combination = df['Start Station']+ "  "+"--->"+"  " +df['End Station'].mode()[0]
    print(f"\nThe most comonly used combinations of pick up stations and release stations are :\n {station_combination}")
    
    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*70)


def trip_duration_stats(df):
    """Displays statistics on the total and average trip duration."""

    print('\nThe Total Duration of A Ride Details...\n')
    start_time = time.time()

    # TO DO: display total travel time
    total_travel_time=  df["Trip Duration"].sum()
    #CONVERTING SECONDS TO HOUR
    hr= int(total_travel_time/(24*3600))
    print(f'Here is the total travel time in hour(s) according to your selection:\n{hr} hours')
    # TO DO: display mean travel time
    mtt = int(df['Trip Duration'].mean()/60)
    print(f"Mean travel time:\n{mtt} Minutes ")

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*70)


def user_stats(df, city):
    """Displays statistics on bikeshare users."""

    print('\nDetails Of Users Statistical Analyses\n')
    start_time = time.time()

    # TO DO: Display counts of user types
    counter_of_user = df['User Type'].value_counts()
    print(f"\nUsers can be sorted into 2 categories\n {counter_of_user}")
    
    # TO DO: Display counts of gender
   
    if city in genlist:
        # Display counts of gender
        gencounter = df['Gender'].value_counts()
        print(gencounter)
    else:
        print('NO gender data for washington')

             
    # TO DO: Display earliest, most recent, and most common year of birth
    # for the earliest year we will search for the minimum value in the years column
    if city in genlist:
        early= int(df['Birth Year'].min())
        print (f"the oldest person in your data was born in the year of {early}")
    #while for the recent year we will search for the largest number in the birth date column
        recent= int(df['Birth Year'].max())
        print (f"the youngest person in your data was born in the year of {recent}")
    #while for the most common we will search for the frequent one
        common= int(df['Birth Year'].value_counts().idxmax())
        print (f"most of the persons in your data was born in the year of {common}")
    else:
        print('no birth data for washington')

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*70)

    # we will ask the user if he or she wants to preview raw data for thier choices 
def raw_data(df):
    print(''' Kindly we need to ask you if you want to preview 
    raw data for your choices kindly choose yes or  no
          ''')
    preview = df.iloc[0 : 5, :10]
    answer = str(input("Enter your answer: ")).lower()
    if answer not in data:
        print (preview)
    else:
        print('End Of The Programe')
        

def main():
    while True:
        city, month, day = get_filters()
        df = load_data(city, month, day)

        time_stats(df)
        station_stats(df)
        trip_duration_stats(df)
        user_stats(df , city)
        raw_data(df)
        restart = input('\nWould you like to restart? Enter yes or no.\n')
        if restart.lower() != 'yes':
            break


if __name__ == "__main__":
	main()
