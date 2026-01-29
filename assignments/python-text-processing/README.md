# 📘 Assignment: Python Text Processing

## 🎯 Objective

Build Python programs that read, process, and transform text using strings and file I/O. You will practice reading and writing files, splitting and cleaning text, and performing simple analyses and transformations on real text data.

## 📝 Tasks

### 🛠️ Text File Reader & Cleaner

#### Description
Create a program that reads a text file from disk, cleans the text, and prints a nicely formatted result. This will help you practice basic file I/O and string operations.

#### Requirements
Completed program should:

- Ask the user for an input filename and safely open the text file
- Read the entire contents of the file and convert it to a consistent case (all lower or all upper)
- Remove leading/trailing whitespace from each line and ignore completely blank lines
- Print the cleaned lines to the screen with line numbers (for example: `1: this is a line`)


### 🛠️ Word Count & Text Analysis

#### Description
Extend your text-processing skills by analyzing the contents of a text file. Your program should count words and find useful information about how the text is used.

#### Requirements
Completed program should:

- Ask the user for an input filename and handle the case where the file does not exist with a clear error message
- Count the total number of lines, total number of words, and total number of characters (excluding newline characters) and display these counts
- Build a frequency count of each unique word (case-insensitive) and display the top 5 most common words with their counts
- Write the word frequency results to a new output file (for example: `word_counts.txt`) so they can be reviewed later
