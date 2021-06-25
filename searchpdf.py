import streamlit as st
import requests
import bs4

st.set_page_config(page_title='PDF Documents Search | By Akshay Toshniwal', initial_sidebar_state='auto', layout='wide')


hide_streamlit_style = """
            <style>
            #MainMenu {visibility: hidden;}
            footer {visibility: hidden;}
            </style>
            """
st.markdown(hide_streamlit_style, unsafe_allow_html=True)

st.markdown("<h1 style='text-align: center; color: white;'>Search PDF Documents by entering keywords</h1>", unsafe_allow_html=True)

col1, col2, col3 = st.beta_columns(3)

col1.header('Enter keyword to search')
col1.info('PDF links will be fetched for keyword entered. You can click and the source will open in new tab')
search_data = col1.text_input('Enter your keyword')

col2.header('Number of results')
col2.info('For blank, it is default 10, for any other input it is specific. Total number of results may vary')
num = col2.number_input('Enter number, max=100', min_value=1, max_value=100, value=10)

col3.header('Which page to load')
col3.info('For input 0, it is page 1, input 1, it is page 2 and likewise')
page_start = col3.number_input('Enter page number, max=99', min_value=0, max_value=99, value=0)
if page_start == 0:
    page_start = (page_start * 10) + 10
else:
    page_start = page_start * 10

st.text('Results will pop up and shown below once you hit Enter or Tab on the Keyword or Click after entering the keyword')


def search_pdf(num, page_start):
    if search_data and num and page_start:
        url="https://google.com/search?q=" + 'filetype:pdf ' + search_data + '&num=' + str(num) + '&start=' + str(page_start)
        # webbrowser.get().open(url)
        link_results = requests.get(url)
        soup = bs4.BeautifulSoup(link_results.text, 'html')
        main_text_data = soup.find_all('h3')
        main_links_data = soup.find_all('a')
        title_data = []
        link_data = []
        for title in main_text_data:
            title_data.append(title.getText())

        updated_data = []
        for i in range(0, len(title_data)):
            if 'PDF' in title_data[i]:
                updated_data.append(title_data[i])

        for link in main_links_data:
            link_href = link.get('href')
            if "url?q=" in link_href and not "webcache" in link_href:
                link_data.append((link.get('href').split("?q=")[1].split("&sa=U")[0]))

        updated_links = []

        # st.write(link_data)

        for i in range(0, len(link_data)):
            if 'pdf' in link_data[i] or 'PDF' in link_data[i] or 'downloads' in link_data[i] or 'content' in link_data[i]:
                if 'google.com' in link_data[i]:
                    print()
                else:
                    updated_links.append(link_data[i])

        st.header("Free PDF Sources")

        for i in range (0,len(updated_links)):
            st.write(updated_links[i])


    else:
        st.error('Input the keyword to search')


page_num = num

if search_pdf(page_num, page_start):
    st.balloons()

st.markdown("<pre style='text-align: center; color: white;'>By Akshay R Toshniwal</pre>", unsafe_allow_html=True)
