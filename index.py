import calendar
import datetime

def getDates():

    currentDateTime = datetime.datetime.now()
    currentDay = currentDateTime.day 
    currentMonth = currentDateTime.month
    currentYear = currentDateTime.year
    
    return ({'currentDay':currentDay, 'currentMonth':currentMonth ,'currentYear':currentYear })

def getNumberOfDaysElapsed(day, month, year):

    totalOfDays = 0
    cursor = 1

    while (cursor < month):
        totalOfDays += calendar.monthrange(year, cursor)[1]
        cursor += 1
    
    totalOfDays += day

    return totalOfDays 

def getPercentOfYearElapsed(daysElapsed):

    daysOfYear = 365 
    percent = round(100 * daysElapsed / daysOfYear, 1)
    return (percent)

def showProgress(percent):
    cursor = 1
    fill = "."
    fillPercent = "."
    limitVar = "."
    yearVar = ""
    while (cursor < 100):

        limitVar+= "."

        if (cursor < percent):
            fill += "*"
        else:
            if (cursor == 99):
                fill +="."
            else:
                fill += " "

        if(49 == cursor ):
            fillPercent += str(percent)+'%'
        
        else:

            if( not (48 <= cursor and cursor <= 52)):

                if (cursor < percent):
                    fillPercent += "*"
                else:
                    if (cursor == 99):
                        fillPercent +="."
                    else:
                        fillPercent +=" "
            
        cursor+=1
    
    
    yearVar+= limitVar + "\n"+fill +"\n"+fillPercent +"\n"+fillPercent +"\n"+fill +"\n"+limitVar + "\n"

    
    return (yearVar)


def main():

    dates = getDates()
    numberOfDaysElapsed = getNumberOfDaysElapsed(dates['currentDay'], dates['currentMonth'],dates['currentYear'])
    percent = getPercentOfYearElapsed(numberOfDaysElapsed)
    progressVar = showProgress(percent)

    print ("Date: " + str( dates['currentDay'] ) + '/' + str( dates['currentMonth'] ) + '/' + str( dates['currentYear'] ) + "\nThe percentage of the progress of the year is:" )
    print(progressVar)
main()