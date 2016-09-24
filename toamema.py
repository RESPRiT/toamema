'''
Toa Mema 0.2
'''
import time
import praw
import OAuth2Util
from datetime import date
BETRAYAL_DATE = date(2016, 7, 29)
DISCLAIMER = '^I ^am ^a ^bot ^that ^is ^currently ^in ^development! ^Contact ^the ^mods ^if ^something ^goes ^wrong!'

def parse_submissions():
  data = {}
  data['oc'] = 0
  data['classic'] = 0
  count = 0
  
  for submission in sub.get_new(limit=None):
    count += 1
    
    if submission.link_flair_text == 'OC':
      data['oc'] += 1
    
    if submission.link_flair_text == 'Classic':
      data['classic'] += 1
    
    if count <= 25: #only check the most recent 25 posts  
      do_comment = False
      
      if submission.id not in already_done:
        flat_comments = praw.helpers.flatten_tree(submission.comments)
      
      if submission.link_flair_text == None:
        do_comment = True
        for comment in flat_comments:
          if comment.author.name == 'ToaMema' and 'post flair' in comment.body:
            do_comment = False
            
      if do_comment:
        print('    I am going to comment on post', submission.id)
        submission.add_comment('Don\'t forget to give your post flair! This comment will be automatically removed once your post is flaired :)\n\n' + DISCLAIMER)

      if submission.link_flair_text is not None and submission.id not in already_done:
        for comment in flat_comments:
          if comment.author.name == 'ToaMema' and 'post flair' in comment.body:
            print('    I am going to delete a flair comment on', submission.id)
            comment.delete()
        already_done.add(submission.id)
    
  print('  OC Conut: ', data['oc'])
  print('  Classic Count: ', data['classic'])
  print('  Meme Count: ', data['oc'] + data['classic'])
  return data
    
def get_days_since_betrayal():
  return (date.today() - BETRAYAL_DATE).days
    
def get_sidebar():
  settings = r.get_settings(sub)
  return settings['description']

def generate_sidebar(data):
  f = open('txt\\sidebar.txt', 'r')
  sidebar = f.read()
  f.close()
  
  sidebar = sidebar.replace('CANCEL_DAYS', str(get_days_since_betrayal()))
  sidebar = sidebar.replace('MEME_COUNT', str(data['oc'] + data['classic']))
  lastedit = '*^Last edited on: ' + time.strftime("%d %b %Y %X") + '*'
  sidebar = sidebar.replace('LAST_EDIT', lastedit.replace(' ', ' ^'))
  
  return sidebar
  
def set_sidebar(str):
  r.update_settings(r.get_subreddit('bioniclememes'), description=str, allow_images='true')
  
def save_sidebar():
  f = open('txt\\lastsidebar.txt', 'w+')
  f.write(get_sidebar())
  f.close()
  
#Main Bot Loop
while True:
  try:
    print('Logging in...')
    r = praw.Reddit('Toa Mema v 0.2')
    o = OAuth2Util.OAuth2Util(r)
    o.refresh(force=True)
    
    waittime = 5 * 60;
    already_done = set()
    sub = r.get_subreddit('bioniclememes')
    
    print('Starting bot loop...')
    while True:
      o.refresh()
      
      print('The current time is:', time.strftime("%d %b %Y %X"))
      
      print('  Parsing submissions...')
      data = parse_submissions()
      
      print('  Saving previous sidebar...')
      save_sidebar()
      
      print('  Generating sidebar...')
      sidebar_content = generate_sidebar(data)
      
      print('  Updating sidebar...')
      set_sidebar(sidebar_content)
      
      print('Waiting ', waittime, ' seconds to continue...')
      time.sleep(waittime)
  except KeyboardInterrupt:
    print('Bye!') 
    break
  except:
    print('*** Something went wrong, probably a connection error! ***')
    print('         Restarting the script in 15 seconds...')
    time.sleep(15)
    pass
  else:
    print('!!! Uh oh - not sure what is wrong but I am going to bail now !!!')
    break
