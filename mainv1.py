
######### V1.1 #############
import subprocess,os,os.path
import time
import random
class colors:
	YELLOW = '\033[93m'
	BOLD = '\033[1m'
	RED = '\033[91m'
	END = '\033[0m'
############################################################################################
def asking_for_one_track():
	
	input_file =raw_input("Please insert the full path of your track: ")
        output_dir = raw_input("Please detrmine your destination directory: ")
        print ""
        bitrate = raw_input("Please Determine the Bitrate- just input number in kbps: ")+"K"

        if "." in input_file:
                input_file_notExtention = input_file.split(".")[0] #remove the extention file from the name of the input track
        else:
                input_file_notExtention = inpute_file

        if "/" in input_file:
                input_file_dir_list = input_file_notExtention.split("/")
                just_name_of_file = input_file_dir_list[len(input_file_dir_list)-1] #remove the parent dir address from the name of the input track
        else:
                just_name_of_file = input_file_notExtention

	return input_file, just_name_of_file, output_dir, bitrate

#############################################################################################
def asking_for_album(): #this function ask for inputing one album
	input_dir = raw_input("Please insert the full path of your album: ")+"/"
        output_album = raw_input("Plese determine your destination directory for this album: ")+"/"
        bitrate = raw_input("Please Determine the Bitrate- just input number in kbps: ")+"K"

        
	#p = subprocess.Popen(['ls', input_dir],stdout=subprocess.PIPE,stderr=subprocess.PIPE)#taking th content of a directory, (files in a directory)
        #out, err = p.communicate()
        list_of_tracks = os.listdir(input_dir)
	
	return input_dir, output_album, bitrate, list_of_tracks
	

#############################################################################################
def track_avconv_opus(): #this function convert just one track to .opus format by avconv program

	
	input_file, just_name_of_file, output_dir, bitrate = asking_for_one_track()
	  
	output_file = output_dir + just_name_of_file + ".opus" #creating the name of output track
	
	convert_to_opus_avconv = subprocess.call(['avconv' ,'-i' ,input_file ,'-codec:a' ,'opus' ,'-b:a' ,bitrate ,output_file ])

	if convert_to_opus_avconv == 0:
		print ""
		print colors.BOLD + colors.YELLOW + "The " + input_file + " converted to " + output_file + colors.END
		add_metadata(output_file)
#############################################################################################
def track_avconv_ogg(): #this function convert just one track to .ogg format by avconv program

        
        input_file, just_name_of_file, output_dir, bitrate = asking_for_one_track()
          
        output_file = output_dir + just_name_of_file + ".ogg" #creating the name of output track
        
        convert_to_ogg_avconv = subprocess.call(['avconv' ,'-i' ,input_file ,'-codec:a' ,'libvorbis' ,'-b:a' ,bitrate ,output_file ])

        if convert_to_ogg_avconv == 0:
                print ""
                print colors.BOLD + colors.YELLOW + "The " + input_file + " converted to " + output_file + colors.END


###############################################################################################

def album_avconv_opus(): #this function gets one album (folder including songs) and converts all tracks into .opus file
	

	input_dir, output_album, bitrate, list_of_tracks = asking_for_album()
	
	start_time = time.time()
	for track in list_of_tracks:
		track_notExtention = track.split(".")[0] #remove the extention file from the name of the input track	
		output_file = output_album + track_notExtention + ".opus" #creating the name of output track
		convert_to_opus_avconv = subprocess.call(['avconv' ,'-i' ,os.path.join(input_dir,track) ,'-codec:a' ,'opus' ,'-b:a' ,bitrate ,output_file ])
		
		if convert_to_opus_avconv == 0:
	                print ""
        	        print colors.BOLD + colors.YELLOW + "The " + track + " converted to " + output_file + colors.END
	end_time = time.time()		
	print "time for converting is: " , (end_time - start_time)
###############################################################################################

def album_avconv_ogg(): #this function gets one album (folder including songs) and converts all tracks into .ogg file
	

	input_dir, output_album, bitrate, list_of_tracks = asking_for_album()
	
	start_time = time.time()
	for track in list_of_tracks:
		track_notExtention = track.split(".")[0] #remove the extention file from the name of the input track	
		output_file = output_album + track_notExtention + ".ogg" #creating the name of output track
		convert_to_opus_avconv = subprocess.call(['avconv' ,'-i' ,os.path.join(input_dir,track) ,'-codec:a' ,'libvorbis' ,'-b:a' ,bitrate ,output_file ])
		
		if convert_to_opus_avconv == 0:
	                print ""
        	        print colors.BOLD + colors.YELLOW + "The " + track + " converted to " + output_file + colors.END
	end_time = time.time()
	print "time for converting is: " , (end_time - start_time)

#############################################################################################
def track_ffmpeg_opus(): #this function convert just one track to .opus format by ffmpeg program

	
	input_file, just_name_of_file, output_dir, bitrate = asking_for_one_track()
	  
	output_file = output_dir + just_name_of_file + ".opus" #creating the name of output track
	
	convert_to_opus_avconv = subprocess.call(['ffmpeg' ,'-i' ,input_file ,'-codec:a' ,'opus' ,'-b:a' ,bitrate ,output_file ])

	if convert_to_opus_avconv == 0:
		print ""
		print colors.BOLD + colors.YELLOW + "The " + input_file + " converted to " + output_file + colors.END
#############################################################################################
def track_ffmpeg_ogg(): #this function convert just one track to .ogg format by ffmpeg program

        
        input_file, just_name_of_file, output_dir, bitrate = asking_for_one_track()
          
        output_file = output_dir + just_name_of_file + ".ogg" #creating the name of output track
        
        convert_to_ogg_avconv = subprocess.call(['ffmpeg' ,'-i' ,input_file ,'-codec:a' ,'libvorbis' ,'-b:a' ,bitrate ,output_file ])

        if convert_to_ogg_avconv == 0:
                print ""
                print colors.BOLD + colors.YELLOW + "The " + input_file + " converted to " + output_file + colors.END


###############################################################################################

def album_ffmpeg_opus(): #this function gets one album (folder including songs) and converts all tracks into .opus file by ffmpeg program
	

	input_dir, output_album, bitrate, list_of_tracks = asking_for_album()
	start_time= time.time()
	for track in list_of_tracks:
		track_notExtention = track.split(".")[0] #remove the extention file from the name of the input track	
		output_file = output_album + track_notExtention + ".opus" #creating the name of output track
		convert_to_opus_avconv = subprocess.call(['ffmpeg' ,'-i' ,os.path.join(input_dir,track) ,'-codec:a' ,'opus' ,'-b:a' ,bitrate ,output_file ])
		
		if convert_to_opus_avconv == 0:
	                print ""
        	        print colors.BOLD + colors.YELLOW + "The " + track + " converted to " + output_file + colors.END
	end_time = time.time()
	print "time for converting is: " , (end_time - start_time)

###############################################################################################

def album_ffmpeg_ogg(): #this function gets one album (folder including songs) and converts all tracks into .ogg file by ffmpeg program
	

	input_dir, output_album, bitrate, list_of_tracks = asking_for_album()
	start_time = time.time()
	for track in list_of_tracks:
		track_notExtention = track.split(".")[0] #remove the extention file from the name of the input track	
		output_file = output_album + track_notExtention + ".ogg" #creating the name of output track
		convert_to_opus_avconv = subprocess.call(['ffmpeg' ,'-i' ,os.path.join(input_dir,track) ,'-codec:a' ,'libvorbis' ,'-b:a' ,bitrate ,output_file ])
		
		if convert_to_opus_avconv == 0:
	                print ""
        	        print colors.BOLD + colors.YELLOW + "The " + track + " converted to " + output_file + colors.END
	end_time = time.time()
	print "time for converting is: " , (end_time - start_time)
###############################################################################################
def add_metadata(output_file):
	print ""
	answer = raw_input("Do you have any input file to override the metadata? (y/n)")
	if answer.upper() == "Y":
		meta_file = raw_input("Please insert the address of metadata file: ")
		import_metadata = subprocess.call(['ffmpeg' ,'-i' , output_file , "-i", meta_file, "-map_metadata", "1" , '-codec' ,'copy' ,output_file ])	
			
		

############################################### MAIN ##########################################

print ""
command = ""
while command.upper() != "Q":
	subprocess.call(['clear'])
	print " a) select a track to convert to opus with ivconv"
	print " b) select a track to convert to ogg with ivconv"
	print " c) select an album to convert to opus with ivconv"
	print " d) select an album to convert to ogg with ivconv"	
	print " e) select a track to convert to opus with ffmpeg"
	print " f) select a track to convert to ogg with ffmpeg"
	print " g) select an album to convert to opus with ffmpeg"
	print " h) select an album to convert to ogg with ffmpeg"
	command = raw_input(colors.BOLD + colors.RED + " Please select one option: " + colors.END)
	
	if command.upper() == "A":
		track_avconv_opus()

	elif command.upper() == "B":
		track_avconv_ogg()
	

	elif command.upper() == "C":
		album_avconv_opus()

	elif command.upper() == "D":
		album_avconv_ogg()
	
	elif command.upper() == "E":
		track_ffmpeg_opus()

	elif command.upper() == "F":
		track_ffmpeg_ogg()
	

	elif command.upper() == "G":
		album_ffmpeg_opus()

	elif command.upper() == "H":
		album_ffmpeg_ogg()
