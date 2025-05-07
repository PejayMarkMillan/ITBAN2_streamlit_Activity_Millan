Activity 1

This activity 1 creates a simple web application using Streamlit by first importing the library and displaying a title, header, and short description. It then presents three input fields to the user: one for their name, one for their age (with a minimum value of 1), and one for their email address. If all fields are filled out, the app displays a personalized message showing the user's name, age, and email using the st.write function.

![image alt](https://github.com/PejayMarkMillan/ITBAN2_streamlit_Activity_Millan/blob/8ca44d14296f5ab3ad7f667c688a4a950a73e296/Screenshot%20(252).png)
![image alt](https://github.com/PejayMarkMillan/ITBAN2_streamlit_Activity_Millan/blob/2cfb55889c7427a83d0ea5c9175a62755237b2c6/act1.png)

Activity 2

In Activity 2, the Streamlit script allows users to upload a CSV file, which is then read into a DataFrame using pandas and displayed on the screen. After uploading, the app provides an interface to filter the data: the user selects a column from the CSV and chooses one or more values from that column using a dropdown and multiselect box. If values are selected, the app filters the DataFrame to show only rows where the selected column matches the chosen values and displays the filtered result; otherwise, it indicates that no filter has been applied.

![image aLT](https://github.com/PejayMarkMillan/ITBAN2_streamlit_Activity_Millan/blob/b05b9fdcd06341cb60cb0d168502ae7b7820385f/Screenshot%20(253).png)

Activity 3

In activity 3, it creates an interactive educational app focused on data warehousing and enterprise data management. It starts with a sidebar that allows users to select a topic from a dropdown, and a collapsible expander introduces the concept of data warehousing and EDM. Based on the selected topic, the main area displays relevant content using structured headers, columns, and bullet points—covering concepts like ETL, data integration, governance, and performance optimization—while additional learning materials are organized into three tabs discussing real-time analytics, cloud warehousing, and data archiving.



Activity 4

This Streamlit app creates an interactive COVID-19 data dashboard that lets users select a country (e.g., USA, Philippines) and fetches the last 30 days of historical data using the Disease.sh API. If the API request is successful and timeline data is available, the app processes the data into a Pandas DataFrame, converts dates for visualization, and displays various charts: a line chart for daily cases, a bar chart for daily deaths, an area chart for daily recoveries, and a pie chart summarizing the totals using Matplotlib. It concludes with a summary section showing total cases, deaths, and recoveries using st.metric; otherwise, it displays an error if the data is missing or the request fails.



Activity 5

Activity 5 connects to a MySQL database and provides a hospital management dashboard with login authentication and the ability to view and insert records for doctors and patients. After a successful login, the user can select a table (either "doctors" or "patients") and view its contents, with an optional filter for SQL queries. The app also allows inserting new records into the selected table by filling out a form, and upon submission, it executes the corresponding SQL INSERT statement to add the record into the database, displaying a success message.



Activity 6

This Streamlit app allows users to apply various webcam filters, such as grayscale, Canny edge detection, and face detection, to images taken with the webcam. Users can select a filter and adjust the Canny edge detection thresholds using a sidebar, and once a snapshot is captured, the app processes the image using OpenCV functions based on the chosen filter: converting to grayscale, applying edge detection, or detecting faces using a pre-trained Haar Cascade model. The processed image is then displayed on the app, allowing users to see the effect of the selected filter on the captured photo.
