#Calculate how many sectors a given 16GB HDD has.
#The HDD is dvided into sectors of 512byte each. Divide the total bytes on the drive  by the number of bytes in a sector to calculate the number of sectors.
# multiply 16 by 1024 three times to convert it to 16GB
disk_size=16*1024*1024*1024
sector_size=512
sector_amount=disk_size/sector_size
print(sector_amount)#33554432.0
