def checkYear (rowSeries):
    if int(rowSeries.Year)==int(rowSeries.year_newDate):
        return True
    return False


def transforma_fatal (n):
    if n== 'Y' or n=='N':
        return n
    else:
        return 'NaN'


def hemisphere(x):
    if x in ['USA','BAHAMAS', 'MEXICO', 'ITALY']:
        return 'NORTE'
    else:
        return 'SUR'


def season(month,hemisphere):
    if month in ['04','05','06','07','08','09'] and hemisphere == 'NORTE':
        return 'WARM'
    elif month in ['01','02','03','10','11','12'] and hemisphere == 'SUR':
        return 'WARM'
    else:
        return 'COLD'    