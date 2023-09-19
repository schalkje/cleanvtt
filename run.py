import sys
import logging
from cleanVTT import clean_vtt_file

def main():
    # Configure logging
    logging.basicConfig(format='%(asctime)s - %(levelname)s - %(message)s', level=logging.INFO)
    
    # Verify command-line arguments
    if len(sys.argv) != 2:
        logging.error("Usage: python run.py <filename>")
        return
    
    # Get the filename from command line argument
    filename = sys.argv[1]
    
    # Check if the filename has a file extension
    if '.' not in filename:
        filename += ".vtt"
    
    input_file_path = 'examples/' + filename
    output_file_path = 'examples/' + filename + '.cleaned'
    
    logging.info("Input file: %s", input_file_path)
    logging.info("Output file: %s", output_file_path)
    
    # Call the clean_file function
    clean_vtt_file(input_file_path, output_file_path)

if __name__ == "__main__":
    main()