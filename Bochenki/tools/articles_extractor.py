import csv
import os
import re


class ArticlesExtractor:
    """
    ArticlesExtractor is a utility class designed to extract articles from a CSV file and save them as text files.
    Each article's title is sanitized to remove characters not allowed in filenames and spaces are replaced with
    underscores. The articles are then saved to the specified output directory, with the filenames derived from
    their titles.
    """
    def _title_to_filename(self, title: str) -> str:
        """
        Converts an article title into a safe filename by removing characters that are not allowed in filenames
        and replacing spaces with underscores. This method is used internally to sanitize article titles before
        saving them as text files.

        Args:
            title (str): The article's title that needs to be converted into a filename.

        Returns:
            str: A sanitized version of the title that can safely be used as a filename.
        """

        filename = re.sub(r'[<>:"/\\|?*]', '', title.replace(' ', '_'))
        return filename

    def extract_articles_from_csv(self, csv_file_path: str, output_directory: str) -> None:
        """
        Extracts articles from a CSV file and saves them as text files in the specified output directory. The CSV
        file should have at least two columns named "Text" and "Title". Each article is saved as a separate text file,
        with the file name derived from its title. The output directory is created if it does not already exist.

        Args:
            csv_file_path (str): The path to the CSV file containing the articles to be extracted. The CSV file
                                 should be encoded in UTF-8 and contain columns for "Text" and "Title".
            output_directory (str): The path to the directory where the extracted articles will be saved as text
                                    files. This directory will be created if it does not exist.

        Returns:
            None
        """
        os.makedirs(output_directory, exist_ok=True)  # Create the directory if it doesn't exist
        with open(csv_file_path, mode='r', encoding='utf-8') as csv_file:
            csv_reader = csv.DictReader(csv_file)
            for row in csv_reader:
                title = self._title_to_filename(row['Title'])  # Sanitize article's title
                text = row['Text']
                output_file_path = os.path.join(output_directory, f"{title}.txt")
                with open(output_file_path, mode='w', encoding='utf-8') as text_file:
                    text_file.write(text)
