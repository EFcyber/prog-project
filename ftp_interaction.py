from ftplib import FTP

def get_file_name(ftp,date):
    
    dir_contents = ftp.nlst()
    for med_file in dir_contents:
        if (date.replace("/","")) in med_file:
            file_name = med_file
    return file_name


def ftp_file_download(ip_addr, user, passwd, date):
    
    try:
        # Initiate connection to ftp server
        with FTP(ip_addr) as ftp:
            try:
                # Login to server with provided credentials
                ftp.login(user=user, passwd=passwd)
            except:
                print(f"ERROR: Authentication failure for user {user}.")
                return 1
        
            try:
                # Select file with the user specified date
                server_file = get_file_name(ftp, date)
            except:
                print("ERROR: Cannot retrieve file names")
                return 2

            try:
                # Create local file in current working directory
                with open(server_file, 'w') as temp_file:
                    try:
                        # Download contents of ftp file to the local file
                        ftp.retrlines("RETR " + server_file, temp_file.write)
                        ftp.quit()
                    except:
                        print("ERROR: Unable to retrieve file.")
                        return 3
            except:
                print("ERROR: File cannot be downloaded to this location.")
                return 4
    except:
        print("ERROR: Cannot connect to FTP server.")
        return 5
    return temp_file
