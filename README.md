# Welcome Wonderbotz Team to This Repository

I have created a small Python Selenium script to automate the application process for the "Automation Anywhere Developer" position on your website. This task took me approximately **1 hour** to complete with the assistance of ChatGPT.
![ - visual selection](https://github.com/user-attachments/assets/321a0885-2892-488b-9730-c073a9d57211)

## I Worked On
![ - visual selection-13](https://github.com/user-attachments/assets/29be1de2-f9c8-4889-8c6b-467034b41059)


## Purpose
This script is designed to:
1. Automatically fill out the application form.
2. Upload a resume file.
3. Handle dropdowns, calendar fields, and regular input fields.
4. Click through the CAPTCHA (requires manual intervention for solving).
5. Submit the application form.

## How to Use
![ - visual selection-11](https://github.com/user-attachments/assets/e5e26015-d1b0-4b7a-8bc1-07a1f897a818)

### Setup Instructions
1. Clone this repository to your local machine.
2. Install the required Python dependencies using:
   ```bash
   pip install selenium webdriver-manager
   ```
3. Update the `test_data` dictionary in the script with your personal details.
4. Update the `resume_file_path` variable with the absolute path to your resume file.
5. Run the script using:
   ```bash
   python automation_script.py
   ```
![ - visual selection-12](https://github.com/user-attachments/assets/7ab7158e-cb70-452a-b4c1-7d8cddbc27b8)

### File Structure
![ - visual selection-6](https://github.com/user-attachments/assets/fea50783-8a67-4311-9b62-eb8d402ef0a4)

## Features
- **Multi-browser Support:** The script is designed to run on Chrome, Firefox, and Edge.
- **Dynamic Field Handling:** Automatically detects and handles input fields, dropdowns, and calendar fields.
- **Resume Upload:** Automates the resume upload process.
- **Error Handling:** Provides error messages for any field that could not be filled.
![ - visual selection-7](https://github.com/user-attachments/assets/ef7663d5-73b1-46da-9bab-06e8a206d79a)

## Video Demo
The attached `fill form.mp4` file provides a demonstration of the script in action, showcasing its ability to automate the form submission process.

## Notes
- CAPTCHA resolution requires manual intervention as it cannot be automated.
- Ensure the file path for the resume is accurate to avoid errors during upload.

For any questions or further improvements, feel free to reach out!

