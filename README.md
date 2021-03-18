# Canvas Study Guide Generator
### By Tyler Brittain
A python script that will generate a study guide. This works by parsing Canvas quizzes and collecting all of the questions into a single text file. 
This script is intended to take questions from various quizzes and have them all in one place to make reviewing materials a much more streamlined process.
<br><br>
**Note**  
 The way this program works is by iterating through all of the subfolders of a directory because it assumes that you are structuring your quizzes by section. See quiz_structure_example for reference.
<br><br>
**Potential Error**
If the readFrom folder consists of anything, but subfiles the program will crash. To remedy this simply store all of your txt files into a subfolder such as "readFrom -> subfolder -> *.txt files" to remedy this issue.