try:
    import requests
except ImportError:
    print('Requests is not installed! terminating program')
    exit(-1)
try:
    from bs4 import BeautifulSoup
except ImportError:
    print('BeautifulSoup4 is not installed! terminating program')
    exit(-1)

def test_linkedin(username, password):

    session = requests.session()
    homepage_url = 'https://www.linkedin.com?allowUnsupportedBrowser=true'
    login_url = 'https://www.linkedin.com/uas/login-submit?allowUnsupportedBrowser=true'
    request = session.get(homepage_url).content
    soup = BeautifulSoup(request, 'html.parser')
    csrf = soup.find(id="loginCsrfParam-login")['value'] #get randomly genreated csfr token for session
    login_query = {'session_key': username,
                   'session_password': password,
                   'loginCsrfParam': csrf} #create login query using csfr token
    post = session.post(login_url, data=login_query) #send post request to login url
    soup = BeautifulSoup(post.content, 'html.parser')
    soup_list = str(soup).strip().splitlines()
    failed = False
    for line in soup_list: #iterate through html parsed soup and check if password or username failed
        if ('wrong_password' or 'invalid_username' or 'empty_password' or
                'invalid_email_phone_format' or 'invalid_email_format' or 'generic_login_error_message') in line:
                failed = True
                break
    return failed

def test_twitter(username, password):
    url = "https://twitter.com/sessions"
    session = requests.session()
    html = session.get(url).content
    soup = BeautifulSoup(html, 'html.parser')
    authenticity_token = soup.input['value'] #get authenticity token from soup dictionary
    ui_metrics = '' #ui metrics needs to be empty
    post = session.post(url, data={
        'session[username_or_email]': username,
        'session[password]': password,
        'authenticity_token': authenticity_token,
        'ui_metrics': ui_metrics,
        'scribe_log': '',
        'redirect_after_login': '',
        'remember_me': '1'})
    soup = BeautifulSoup(post.content, 'html.parser')
    span_list = soup.find_all('span') #find span tag within soup
    failed = False
    for span in span_list:
        if 'The username and password you entered did not match our records.' in str(span):
            failed = True
            break
    return failed

def call_tests(username, password,file_flag):
    dict = {}
    failed_twitter = test_twitter(username, password)
    failed_linkedin = test_linkedin(username, password)
    if file_flag:
        credential = username + ' ' + password #create credential string
        if failed_twitter:
            dict.update({credential + ' for Twitter': 'Failed'})
        else:
            dict.update({credential + ' for Twitter': 'Successful'})
        if failed_linkedin:
            dict.update({credential + ' for Linkedin': 'Failure'})
        else:
            dict.update({credential + ' for Linkedin': 'Successful'})
    else:
        if failed_twitter:
            dict.update({'Twitter': 'Failed'})
        else:
            dict.update({'Twitter': 'Successful'})
        if failed_linkedin:
            dict.update({'Linkedin': 'Failed'})
        else:
            dict.update({'Linkedin': 'Successful'})
    return dict
