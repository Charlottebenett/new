### Fetch some data :

1) Let's start by writing a function to load the data. Add this code to your script:

````
DATE_COLUMN = 'date/time'
DATA_URL = ('https://s3-us-west-2.amazonaws.com/'
         'streamlit-demo-data/uber-raw-data-sep14.csv.gz')

def load_data(nrows):
    data = pd.read_csv(DATA_URL, nrows=nrows)
    lowercase = lambda x: str(x).lower()
    data.rename(lowercase, axis='columns', inplace=True)
    data[DATE_COLUMN] = pd.to_datetime(data[DATE_COLUMN])
    return data

````

You'll notice that load_data is a plain old function that downloads some data, puts it in a Pandas dataframe, and converts the date column from text to datetime. The function accepts a single parameter (nrows), which specifies the number of rows that you want to load into the dataframe.

### Effortless caching
Streamlit has an automatic caching mechanism that you can use with `st.cache`. Here is how we will apply it to our function:

/////////////////////////////////////////////////////////////////

### Inspect the raw data

In the Main concepts guide you learned that st.write will render almost anything you pass to it. In this case, you're passing in a dataframe and it's rendering as an interactive table.

st.write tries to do the right thing based on the data type of the input. If it isn't doing what you expect you can use a specialized command like st.dataframe instead. For a full list, see API reference.


````
st.subheader('Raw data')
st.write(data)
````
