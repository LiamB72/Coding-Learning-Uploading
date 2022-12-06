number=[0,1,2,3,4,5,6,7,8,9]

def ConvertToStringlatitude(latitude):
    for j in range(len(number)):
        for i in range(len(latitude)):
            if latitude[i] == number[j]:
                latitude[i] = number[j]
    return latitude

#lycée Touchard
latitude="47° 59.698'N"
longitude="0° 12.276'E"


#VLT au Chili
#latitude="24° 37.649'S"
#longitude=" 70° 24.250'W"
    #à compléter