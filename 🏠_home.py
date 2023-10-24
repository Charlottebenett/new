import streamlit as st
import pandas as pd
import numpy as np

if __name__ == '__main__':
    st.title('Uber Chicken pickups in NYC')
    st.markdown('''
    This is a new world app'app' that shows the Uber_Poule pickups
    geographic distribution in New York City. Use the slider
    to pick a specific hour and look at how the charts change.
    [See source code](
                https://github.com/streamlit/demo-uber-nyc)
    ''')
    # Load data from CSV file:
    DATE_COLUMN = 'date/time'
    DATA_URL = ('https://s3-us-west-2.amazonaws.com/'
                'streamlit-demo-data/uber-raw-data-sep14.csv.gz')
    @st.cache_data
    def load_data(nrows):
        data_load_state = st.text('Loading data...')
        data = pd.read_csv(DATA_URL, nrows=nrows)
        lowercase = lambda x: str(x).lower()
        data.rename(lowercase, axis='columns', inplace=True)
        data[DATE_COLUMN] = pd.to_datetime(data[DATE_COLUMN])
        data_load_state.text('Loading data...done!')
        return data
    # Create a text element and let the reader know the data is loading.
    data_load_state = st.empty()
    data_load_state.text("Done! (using st.cache_data)")
    data = load_data(10000)
    # Display the dataset:
    if st.checkbox('Show raw data my Chiks'):
        st.subheader('Raw data my Chiks')
        st.write(data)
    # Draw a histogram:
    st.subheader('Number of pickups Chiks by hour')
    hist_values = np.histogram(
        data[DATE_COLUMN].dt.hour, bins=24, range=(0,24))[0]
    st.bar_chart(hist_values)
    # Plot data on a map:
    st.subheader('Map of all Chiks pickups')
    st.map(data)
    # Plot data on a map (with slider):
    hour_to_filter = st.slider('hour', 0, 23, 17)
    filtered_data = data[data[DATE_COLUMN].dt.hour == hour_to_filter]
    st.subheader(f'Map of all Chiks pickups at {hour_to_filter}:00 lheure de fu**in pointe')
    st.map(filtered_data)

# now i want to add a background to my app 