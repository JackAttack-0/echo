
# Echo Docs:

## 1: Comments
  ### 1.1 Single Line Comments
    - Use // to comment out one line
  ### 1.2 Multi-Line Comments
    - Use /* to begin a multi-line comment and */ to end it
  ### 1.3 Comments usage
    - Interpreter will ignore any text between comments
## 2: Variables
  ### 2.1 Declare Variable
    - Use the tag "var" to declare a varible
  ### 2.2 Variable types
    - Next, name the variable. The first character of the variable determines what type it is.
      ? = Boolean = True/False
      _ = String = text, should be in "quotes"
      # = Interger = Non-decimal numbers
      ^ = Float/Double = All numbers
  ### 2.3 Constants
    - Use the tag "cons" or "constant" after keyword "var"
    - Variable name should be in all caps to signify it's constant status
    Ex.
      var cons ?CHICKEN = True;
    - Error ConstantError will be produced if an attempted reasgnment statement is run,
    Ex.
      var cons ?CHICKEN = True;
      ?CHICKEN = True;
      end
      
      -> ERROR: Line 2:
      ConstantError: Variable ?CHICKEN cannot be reassigned as it is a constant

  
  ### 2.4 Variable names
     - As specified in 2.2, variables should begin with the symbol used for their type. 
     Ex. 1:
       var ?chicken = True;
       // Defines a variable "chicken" with type Boolean and value True
     Ex. 2:
       var #chonken = 99;
       // Defines a variable "chonken" with type Interger and value 99
     Ex. 3:
        
