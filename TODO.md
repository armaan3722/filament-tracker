To do for version 0.2.0
 - Add ability to input purpose of each print (personal, for research, for selling)
   - Everything can be organized into categories (personal, comercial, etc)
   - Can be further put into projects (throttle, phone stand, etc)
   - Can be even further put into stages (research, production, etc)
   - Can be even further put into collections of prints for multi plate prints
 - Add ability to create new categories, projects, stages, and collections
 - Add ability to view all of this information

Plan
 - filamentUsage has filament id and print id
 - prints has print id and revision id
 - revisions has revision id and collection iteration id
 - collectionIteration has collection iteration id and collection id
 - collections has collection id and stage id
 - stages has stage id and project id
 - projects has project id and category id
 - categories has category id

Category (personal, comercial)
Project (throttle, phone stand)
State (research, production)
Collection (v1, v2)
Revision (revision 1, revision 2)
Iteration (copy 1, copy 2)
Print (plate 1, plate 2)
Filament (filament 1, filament 2)

Category is purpose for print
Project is what the print is for
State is the phase the project is about
Collection is large changes to project
Revision is small changes to project
Iteration is copy of project
Print is plate printed
Filament is filament used