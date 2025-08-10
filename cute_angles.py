DEGREE = "\u00B0"

def dms(angle):
    degrees = int(angle)
    deg_fraction = round(angle - int(angle), 6)
    min_and_sec = 60 * deg_fraction
    minutes = int(min_and_sec)
    seconds = round((min_and_sec - minutes) * 60)
    padded_minutes = f"{str(minutes).zfill(2)}'"
    padded_seconds = f"{str(seconds).zfill(2)}\""
    return (f"{degrees}{DEGREE}{padded_minutes}{padded_seconds}")
  
print(dms(30) == "30°00'00\"")
print(dms(76.73) == "76°43'48\"")
print(dms(254.6) == "254°35'59\"" or dms(254.6) == "254°36'00\"")
print(dms(93.034773) == "93°02'05\"")
print(dms(0) == "0°00'00\"")
print(dms(360) == "360°00'00\"" or dms(360) == "0°00'00\"")


# approach
# integer portion converts directly to degrees
# fractional part is the tricky part
# So take the full float e.g. 0.73 and mult by 60 = 43.8
# so the integer part becomes the minutes
# the fractional part is then also multiplied by 60 = 48
# So final solution is the combination
# So question: how do you get just the decimal
# one approach: x - int(x) = .73
# then directly multiply by 60
