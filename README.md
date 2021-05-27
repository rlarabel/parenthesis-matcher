# parenthesis-matcher
Using a stack to see if parenthesis match in a given string. This file uses other stack examples,
but the section for the parenthesis-matcher is commented on. 

## Input 
#### Entering an equation
- Enter a string equation of any sort 
#### To get a matched parenthesis
- All '(' must be closed with a ')' before reach the end of line or another '('
- Must contain one set of parenthesis


## Process
#### Match parentheses
- Uses a stack data structure to track parenthesis
- Only a '('  is pushed onto the stack
- after encountering a ')' the stack is popped 
#### Reasons for a Negative Results
- If stack is popped, but it was already empty
- After parsing the equation completely and the stack is not yet empty of '(' 

## Output
- Display the other example of using stacks in python
#### Match parentheses
- Displays a verifying message if all parentheses match 
    
 
## Known Errors/Problems
- N/A