To do for v0.5.0
 - Creation and selection of configs
 - Tracking non printed parts
 - Tracking sales
 - Purchasing tools
 - Better data analysis
 - Better input system

To do later
 - Divide interface copy file into multiple different files
   - Equipment
   - Materials
   - Purchasing
   - Usage
   - Projects
 - Get rid of original main and interface

Bugs to fix
 - Exiting after going through collection and project

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