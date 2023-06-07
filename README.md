# Zoom Chat Transcript to CSV Converter

This script converts exported Zoom chat transcripts into a CSV format, extracting timestamps and associated messages. Converting the transcripts into a CSV format allows for easy data analysis and readability. In order to maintain privacy and confidentiality, user names are omitted from the output. The original file will be replaced by the new CSV file, which will have the same filename prefix but with a `.csv` extension.

🚨 Note: this will overwrite your original chat download.

## Getting Started

These instructions will guide you through the process of using this script.

### Prerequisites

- Python 3.6 or higher
- An exported Zoom chat transcript file

### Exporting Chat Transcripts from Zoom

To export a chat transcript from Zoom, follow these steps:

1. Start or join a meeting.
2. Click on the `Chat` option in the meeting controls.
3. Click on the `...` option in the chat box.
4. Click on `Save Chat`.
5. This will save a text file (.txt) of the chat to your computer.

### Converting Chat Transcripts to CSV Format

To convert your Zoom chat transcript to CSV format:

1. Ensure your Python environment is set up and ready.
2. Save the script `scrubtocsv.py` on your computer.
3. Run the script with the text file name as an argument in the terminal/command line as follows: `python scrubtocsv.py yourfile.txt`
4. The script will process the original text file and create a CSV version. The original text file will be replaced by the new CSV file, which will have the same name as the original file, but with a .csv extension.

Please note that the script only processes lines in the transcript that contain a timestamp and a message. All other lines will be ignored.

### Excel issues with output file and Emojis

When opening in Excel, encoding issues can sometimes happen, particularly with emojis. Excel is notorious for handling UTF-8 encoding poorly.

Here's a workaround: Import the data into Excel; don't just open the file. 

Here's how:

1. Open Excel and create a new spreadsheet.
2. Go to the Data tab and click From Text.
3. Navigate to your CSV file and click Import.
4. In the Text Import Wizard, choose the Delimited option, then click Next.
5. Check the Comma box, then click Next.
6. Select the column with emojis and change the Column data format to Text, then click Finish.

Or use Apple Numbers 😉
