import shutil

# Folder you want to zip
project_folder = "C:/Users/EMBAKOM ASHENAFI/OneDrive/Desktop/SMART_MAIL"
output_zip = "C:/Users/EMBAKOM ASHENAFI/OneDrive/Desktop/SMART_MAIL_Project"

# Create the zip
shutil.make_archive(output_zip, 'zip', project_folder)

print("✅ Project zipped successfully:", output_zip + ".zip")
