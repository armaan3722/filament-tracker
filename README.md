Objectives
 - Keep track of filament usage
   - List of all rolls, current and future
   - List of remaining capacity in rolls
   - List of remaining capacity over time in rolls per day
   - List of all projects with day printed and time print taken
 - Keep track of other parts usage
   - List all sizes of heat set inserts and screws
   - List amount of solder left
   - List all electronics left
   - Day and time that everything was used
 - Keep track of purchases and revenue
   - Amount spent when, on what
   - Amount made for sales
 - Keep track of hours of printer usage
   - Hours each project
   - Hours each day
 - Analyze data and sort into tables and graphs
   - Most used filament colours, types, and companies
   - Hours of printing each day or each month
   - Line graph of each unique roll's usage over time
   - Line graph of each type of filament's usage over time
   - Line graph of each non printed part's usage over time

Strategy
 - Data stored in csv files
 - Analysis done in pandas and matlibplot
 - Input done with python terminal

Files
 - main.py (runs main program)
 - analyzer.py (runs data analysis and graph generation functions)
 - utils.py (runs formatting and other useful functions)
 - data.py (reads all csv files)
 - data/
   - prints.csv (stores print name, date, and print id)
   - filamentUsed.csv (stores filament id and use for each print id)
   - allRolls.csv (stores current information about all rolls)

Important information
 - Printer purchased on Jan 4 - $500
 - Calipers purchased on Feb 1
 - Others purchased on Feb 9
 - Everything else pre owned
 - Solder measured by weight
 - 2 inserts used on Feb 17