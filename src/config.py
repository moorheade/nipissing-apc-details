### Fill in the values below to localize

#The sheet of publisher information that has been shared to CSV
PUB_URL = "https://docs.google.com/spreadsheets/d/e/2PACX-1vTxghcrpoO4YJAJQzTyCiYqtO-lUch1-tdkOhlCmyl7iU1KDtwqOXcuHPp8_Q-bB1hJe6XJSY0grP83/pub?gid=360928744&single=true&output=csv"

#The sheet of journal information that has been shared to CSV
JOURNAL_URL = "https://docs.google.com/spreadsheets/d/e/2PACX-1vTxghcrpoO4YJAJQzTyCiYqtO-lUch1-tdkOhlCmyl7iU1KDtwqOXcuHPp8_Q-bB1hJe6XJSY0grP83/pub?gid=0&single=true&output=csv"
#The form that is collecting the 'logged' ISSN and Publisher look-ups. Please check docs for more info
L_URL = "https://docs.google.com/forms/d/e/1FAIpQLSfUjfd8Uti6m_C3b1dZkTJEW9UPMjxBcohNCc7qgiey2bSFyQ/formResponse"
ISSN_ENTRY = "entry.477500605"
PUBLISHER_ENTRY = "entry.811465550"


### You can use Markdown in the following to localize to your place
PREAMBLE = """
# Article Processing Charge Agreements
Below are details about what Article Processing Charge (APC) discounts and waivers are available to members of the Nipissing community. 

 :spiral_calendar: **Information Last Updated - September 17, 2026.**


"""


STATUS_DESCRIPTION = """

|Status|APC Discount/Waiver?|
|--|--|
|⛔| None available|
|❓| Please check|
|✅| Confirmed|


"""

PUBLISHER_LEADIN = """

#### Agreements by Publisher


"""


APC_LINK  = """

Interested in learning more about APCs❓

Cantrell MH, Caldwell R, Mezick JA, Estill M, Collister LB (2026) “The system is obviously bonkers”: The APC Trap and the bind of scholarly publishing across four research intensive institutions in the U.S.. _PLOS ONE_ 21(7): e0351430. [https://doi.org/10.1371/journal.pone.0351430](https://doi.org/10.1371/journal.pone.0351430)


"""

MISSING_TITLE_HELP = """

Good question! 

It probably means we do not have a discount for that title. We are keeping track of titles we have agreements for, if we don't specifically know the status of a title, discount or not, we won't list it here. 

Please contact Erin [:mailbox:](https://www.nipissingu.ca/users/erin-moorhead) to discuss this more.

"""


HELP_MESSAGE = """


_Need more help:question: Contact Erin [:mailbox:]
"""

### Other Configs
LOGGING = True #Switch to true to log lookups of publisher and issn to Google Sheet defined in L_URL
IMAGE_PATH = "images/logo.png" #Put your logo in the images folder, renamed to logo.png, defaults to 200 px wide
