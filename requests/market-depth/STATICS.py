PREFIX = "!"
INVALIDMARKET = "No such market found.\nCorrect format: !market"
INVALIDHELP = "Try using '!help' instead."
INVALIDCLEAR = "Try using '!clear' instead."
MAXORDERS = 2
INMAX= "Maximum amount of orders per user: " + str(MAXORDERS)
CURRENCY = "bis"
CURRENCY2 = "sats"
HELPER = "Correct format: !wtb {} {}\nEx. !wtb 1000 7000".format(CURRENCY, CURRENCY2)
HELP = "**Welcome to Bismuth OTC Bot!**\n\nCommands:\n!wtb {} {}\n!wts {} {}\n!market\n!clear\n\nFor buy and sell orders, fill in the {} price **per** {}.".format(CURRENCY, CURRENCY2, CURRENCY, CURRENCY2, CURRENCY2, CURRENCY)