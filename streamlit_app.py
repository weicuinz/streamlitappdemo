import streamlit
import snowflake.connector

streamlit.title('My Parents New Healthy Diner')

my_cnx = snowflake.connector.connect(**streamlit.secrets["snowflake"])
my_cur = my_cnx.cursor()
my_cur.execute("SELECT CURRENT_USER(), CURRENT_REGION(), CURRENT_ACCOUNT()")

my_data_row = my_cur.fetchone()
streamlit.text("Hello from Snowflake:")
streamlit.text(my_data_row)

# run a snowflake query
my_cur.execute("select color_or_style from zenas_athleisure_db.products.catalog_for_website;")
my_catalog = my_cur.fetchall()

# put data into a dataframe
df = pandas.DataFrame(my_catalog)

# write data frame output to the web app.
streamlit.write(df)
