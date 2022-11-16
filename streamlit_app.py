import streamlit
import snowflake.connector
import pandas

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


color_list = df[0].values.tolist()

option = streamlit.selectbox("Pick a sweatsuit color or style:", list(color_list))

product_caption = "Our warm, confortable, ' + option + ' sweatsuit!'

my_cur.execute("select direct_url, price, size_list, upsell_product_desc from catalog_for_website where color_or_style ='" + option + "';")

df2 = my_cur.fatchone()

streamlit.image(
  df2[0],
  width = 400,
  caption=product_caption
)

streamlit.write('Price:', df2[1])
streamlit.write('Sizes Available:', df2[2])
streamlit.write('Up sell product desc: ', df2[3])
