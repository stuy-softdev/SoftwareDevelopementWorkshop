The Tallyers: Saxon, Rona, and Marcos
Software Development
K28 -- Take and Give
10/15/2026

DISCO:
- the root route needed GET, and the /auth route needed POST
- the request variable stores the things you submit in the form
- you can get a specific result from the form with request.args['argname']
- separate the arguments in render_template() with commas!
- return render_template( 'login.html', goo=goo )
- import a custom module and use its function is easy. just do like how you normally would
- goo = testmod0.goo()

WHAT TO KNOW about GET/POST + request.args/request.headers:
- @app.route("/"): allows GET (default)
- @app.route("/", methods=['GET']): allows GET explicitly
- @app.route("/", methods=['POST']): allows POST but GET fails
- @app.route("/", methods=['GET', 'POST']): allows POST and GET
- request.args returns a Immutable Dictionary using the parts after the ? part of url (each {x}={y} after ? is added as a value key pair)
- request.headers gives us a bunch of data abt the local server and what is being used to access the site.
- The GET and POST don't break each other, its just the pages sometimes broke if we didn't provide them with the method they needed
- e.g. root route broke w/o GET
- e.g. /auth broke w/o POST
- Form route -> information gets sent to form (Use POST); Destination route -> when you send a request to form destination route; location of information (use GET)
- When you go to the other url with the information from the form (auth route), the function is run with the information within the request at the route of the final destination for the form, not the route of the form itself

HOW TO SEE testmod0 output:
- With the import uncommented "M-O-O-N. That spells 'Nebraska'!" is printed in the terminal
- Call print(testmod0.goo())
- print(testmod0.goo()) in app.py prints the goo() string in the terminal
- You have to run the testmod0.py by itself in a terminal to see the final line because it only prints if name = main
- The nebraska: it prints if you import testmod0 or run testmod0.
- lunch: only prints if you run testmod0.
- goo() return statement: after importing testmod0, do this:
- print( testmod0.goo() )

Q/C/C:
- Can we use GET and POST to our advantage, instead of it just being something we need to add so it doesn't break?
- What is the difference between GET and POST and why would you want to allow one but not the other?
- Are there other methods other than GET and POST?
- Are all code at the first level of the indent run when you import a file?
- The request variable has a LOT of info in it.
- Weishenme Tian Shang Taiyang na me hao ting de ge?

OTHER?
- nada
- zilch
- mei you
