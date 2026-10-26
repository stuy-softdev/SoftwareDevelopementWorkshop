**The Tallyers: Saxon, Rona, and Marcos**

**Software Development**

**K31 -- Give and Take**

**10/21/2026**

**Time spent: 3.2**


# Flowchart

**Check Session:** Is the user in session?
  - **Yes:**
    - Load the response page
    - Has the user logged out?
      - **Yes:** pop the username from the session
      - **No:** Nothing
  - **No**
    - Load login page
    - Did the user attempt to sign in?
      - **Yes** Check credentials to the csv and if valid load the website
      - **No** Tell the user it's invalid
    - If the user attempts to create an account add credentials to the csv and load response page
    
## DISCOVERIES ##
## QUESTIONS/COMMENTS/CONCERNS ##
