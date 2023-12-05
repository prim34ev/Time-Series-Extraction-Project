import pandas as pd

cgmdata = pd.read_csv('./source/CGMData.csv')
insulindata = pd.read_csv('./source/InsulinData.csv')
reverse_insulindata = insulindata.loc[::-1,:]

auto_mode_reverse_insulindata = reverse_insulindata[reverse_insulindata['Alarm'].isin(['AUTO MODE ACTIVE PLGM OFF'])]
auto_mode_reverse_insulindata

auto_mode_start_index = auto_mode_reverse_insulindata['Index'].iloc[0]
manual_mode_start_index = reverse_insulindata["Index"].iloc[0]
manual_mode_end_index = auto_mode_start_index

manual_mode_start_date = insulindata[insulindata['Index'] == manual_mode_start_index]['Date'].iloc[0]
manual_mode_start_time = insulindata[insulindata['Index'] == manual_mode_start_index]['Time'].iloc[0]
manual_mode_end_date = insulindata[insulindata['Index'] == manual_mode_end_index]['Date'].iloc[0]
manual_mode_end_time = insulindata[insulindata['Index'] == manual_mode_end_index]['Time'].iloc[0]
auto_mode_start_date = insulindata[insulindata['Index'] == auto_mode_start_index]['Date'].iloc[0]
auto_mode_start_time = insulindata[insulindata['Index'] == auto_mode_start_index]['Time'].iloc[0]

print('manual_mode_start_date', manual_mode_start_date)
print('manual_mode_start_time', manual_mode_start_time)
print('auto_mode_start_date: ', auto_mode_start_date)
print('auto_mode_start_time: ', auto_mode_start_time)

cgmdata['Date Time'] = pd.to_datetime(cgmdata['Date'] + ' ' + cgmdata['Time'])

wholeday_manual_cgmdata = cgmdata.loc[(cgmdata['Date Time'] >= manual_mode_start_date + ' ' + manual_mode_start_time) & (cgmdata['Date Time'] <= manual_mode_end_date + ' ' + manual_mode_end_time)][['Index', 'Date', 'Time', 'Sensor Glucose (mg/dL)', 'Date Time']]
display('wholeday_manual_cgmdata')
display(wholeday_manual_cgmdata)

wholeday_auto_cgmdata = cgmdata.loc[(cgmdata['Date Time'] >= auto_mode_start_date + ' ' + auto_mode_start_time)][['Index', 'Date', 'Time', 'Sensor Glucose (mg/dL)', 'Date Time']]
display('wholeday_auto_cgmdata')
display(wholeday_auto_cgmdata)

wholeday_manual_cgmdata = wholeday_manual_cgmdata.dropna()
wholeday_auto_cgmdata = wholeday_auto_cgmdata.dropna()

display('wholeday_auto_cgmdata', wholeday_auto_cgmdata.count(0))
display('wholeday_manual_cgmdata', wholeday_manual_cgmdata.count(0))

wholeday_auto_cgmdata = wholeday_auto_cgmdata.groupby('Date').filter(lambda x : len(x)> 57.6)
wholeday_manual_cgmdata = wholeday_manual_cgmdata.groupby('Date').filter(lambda x : len(x)> 57.6)

display(wholeday_auto_cgmdata.count(0))
display(wholeday_manual_cgmdata.count(0))

greater_than_180_wholeday_manual_cgmdata = wholeday_manual_cgmdata.loc[wholeday_manual_cgmdata['Sensor Glucose (mg/dL)'] > 180]
greater_than_250_wholeday_manual_cgmdata = wholeday_manual_cgmdata.loc[wholeday_manual_cgmdata['Sensor Glucose (mg/dL)'] > 250]
greater_equal_70_and_less_equal_180_wholeday_manual_cgmdata = wholeday_manual_cgmdata.loc[(wholeday_manual_cgmdata['Sensor Glucose (mg/dL)'] >= 70) & (wholeday_manual_cgmdata['Sensor Glucose (mg/dL)'] <= 180)]
greater_equal_70_and_less_equal_150_wholeday_manual_cgmdata = wholeday_manual_cgmdata.loc[(wholeday_manual_cgmdata['Sensor Glucose (mg/dL)'] >= 70) & (wholeday_manual_cgmdata['Sensor Glucose (mg/dL)'] <= 150)]
less_than_70_wholeday_manual_cgmdata = wholeday_manual_cgmdata.loc[wholeday_manual_cgmdata['Sensor Glucose (mg/dL)'] < 70]
less_than_54_wholeday_manual_cgmdata = wholeday_manual_cgmdata.loc[wholeday_manual_cgmdata['Sensor Glucose (mg/dL)'] < 54]

tt = wholeday_manual_cgmdata.groupby(['Date']).count()
display(tt)
num = len(wholeday_manual_cgmdata.groupby(['Date']).count())
print(num)

greater_than_180_wholeday_auto_cgmdata = wholeday_auto_cgmdata.loc[wholeday_auto_cgmdata['Sensor Glucose (mg/dL)'] > 180]
greater_than_250_wholeday_auto_cgmdata = wholeday_auto_cgmdata.loc[wholeday_auto_cgmdata['Sensor Glucose (mg/dL)'] > 250]
greater_equal_70_and_less_equal_180_wholeday_auto_cgmdata = wholeday_auto_cgmdata.loc[(wholeday_auto_cgmdata['Sensor Glucose (mg/dL)'] >= 70) & (wholeday_auto_cgmdata['Sensor Glucose (mg/dL)'] <= 180)]
greater_equal_70_and_less_equal_150_wholeday_auto_cgmdata = wholeday_auto_cgmdata.loc[(wholeday_auto_cgmdata['Sensor Glucose (mg/dL)'] >= 70) & (wholeday_auto_cgmdata['Sensor Glucose (mg/dL)'] <= 150)]
less_than_70_wholeday_auto_cgmdata = wholeday_auto_cgmdata.loc[wholeday_auto_cgmdata['Sensor Glucose (mg/dL)'] < 70]
less_than_54_wholeday_auto_cgmdata = wholeday_auto_cgmdata.loc[wholeday_auto_cgmdata['Sensor Glucose (mg/dL)'] < 54]

count_greater_than_180_wholeday_manual_cgmdata = greater_than_180_wholeday_manual_cgmdata.groupby(['Date'], as_index=False).count()
count_greater_than_250_wholeday_manual_cgmdata = greater_than_250_wholeday_manual_cgmdata.groupby(['Date'], as_index=False).count()
count_greater_equal_70_and_less_equal_180_wholeday_manual_cgmdata = greater_equal_70_and_less_equal_180_wholeday_manual_cgmdata.groupby(['Date'], as_index=False).count()
count_greater_equal_70_and_less_equal_150_wholeday_manual_cgmdata = greater_equal_70_and_less_equal_150_wholeday_manual_cgmdata.groupby(['Date'], as_index=False).count()
count_less_than_70_wholeday_manual_cgmdata = less_than_70_wholeday_manual_cgmdata.groupby(['Date'], as_index=False).count()
count_less_than_54_wholeday_manual_cgmdata = less_than_54_wholeday_manual_cgmdata.groupby(['Date'], as_index=False).count()

count_greater_than_180_wholeday_auto_cgmdata = greater_than_180_wholeday_auto_cgmdata.groupby(['Date'], as_index=False).count()
count_greater_than_250_wholeday_auto_cgmdata = greater_than_250_wholeday_auto_cgmdata.groupby(['Date'], as_index=False).count()
count_greater_equal_70_and_less_equal_180_wholeday_auto_cgmdata = greater_equal_70_and_less_equal_180_wholeday_auto_cgmdata.groupby(['Date'], as_index=False).count()
count_greater_equal_70_and_less_equal_150_wholeday_auto_cgmdata = greater_equal_70_and_less_equal_150_wholeday_auto_cgmdata.groupby(['Date'], as_index=False).count()
count_less_than_70_wholeday_auto_cgmdata = less_than_70_wholeday_auto_cgmdata.groupby(['Date'], as_index=False).count()
count_less_than_54_wholeday_auto_cgmdata = less_than_54_wholeday_auto_cgmdata.groupby(['Date'], as_index=False).count()

wholeday_total_data = 288
count_greater_than_180_wholeday_manual_cgmdata['Whole Day Percentage'] = 100 * (count_greater_than_180_wholeday_manual_cgmdata['Date Time'] / wholeday_total_data)
count_greater_than_250_wholeday_manual_cgmdata['Whole Day Percentage'] = 100 * (count_greater_than_250_wholeday_manual_cgmdata['Date Time'] / wholeday_total_data)
count_greater_equal_70_and_less_equal_180_wholeday_manual_cgmdata['Whole Day Percentage'] = 100 * (count_greater_equal_70_and_less_equal_180_wholeday_manual_cgmdata['Date Time'] / wholeday_total_data)
count_greater_equal_70_and_less_equal_150_wholeday_manual_cgmdata['Whole Day Percentage'] = 100 * (count_greater_equal_70_and_less_equal_150_wholeday_manual_cgmdata['Date Time'] / wholeday_total_data)
count_less_than_70_wholeday_manual_cgmdata['Whole Day Percentage'] = 100 * (count_less_than_70_wholeday_manual_cgmdata['Date Time'] / wholeday_total_data)
count_less_than_54_wholeday_manual_cgmdata['Whole Day Percentage'] = 100* (count_less_than_54_wholeday_manual_cgmdata['Date Time'] / wholeday_total_data)

count_greater_than_180_wholeday_auto_cgmdata['Whole Day Percentage'] = 100 * count_greater_than_180_wholeday_auto_cgmdata['Date Time'] / wholeday_total_data
count_greater_than_250_wholeday_auto_cgmdata['Whole Day Percentage'] = 100 * count_greater_than_250_wholeday_auto_cgmdata['Date Time'] / wholeday_total_data
count_greater_equal_70_and_less_equal_180_wholeday_auto_cgmdata['Whole Day Percentage'] = 100 * count_greater_equal_70_and_less_equal_180_wholeday_auto_cgmdata['Date Time'] / wholeday_total_data
count_greater_equal_70_and_less_equal_150_wholeday_auto_cgmdata['Whole Day Percentage'] = 100 * count_greater_equal_70_and_less_equal_150_wholeday_auto_cgmdata['Date Time'] / wholeday_total_data
count_less_than_70_wholeday_auto_cgmdata['Whole Day Percentage'] = 100 * count_less_than_70_wholeday_auto_cgmdata['Date Time'] / wholeday_total_data
count_less_than_54_wholeday_auto_cgmdata['Whole Day Percentage'] = 100 * count_less_than_54_wholeday_auto_cgmdata['Date Time'] / wholeday_total_data

manual_total_days = len(wholeday_manual_cgmdata.groupby(['Date']).count())
auto_total_days = len(wholeday_auto_cgmdata.groupby(['Date']).count())

count_greater_than_180_wholeday_manual_cgmdata_percentage = count_greater_than_180_wholeday_manual_cgmdata['Whole Day Percentage'].sum()/manual_total_days if not count_greater_than_180_wholeday_manual_cgmdata.empty else 0
count_greater_than_250_wholeday_manual_cgmdata_percentage = count_greater_than_250_wholeday_manual_cgmdata['Whole Day Percentage'].sum()/manual_total_days if not count_greater_than_250_wholeday_manual_cgmdata.empty else 0
count_greater_equal_70_and_less_equal_180_wholeday_manual_cgmdata_percentage = count_greater_equal_70_and_less_equal_180_wholeday_manual_cgmdata['Whole Day Percentage'].sum()/manual_total_days if not count_greater_equal_70_and_less_equal_180_wholeday_manual_cgmdata.empty else 0
count_greater_equal_70_and_less_equal_150_wholeday_manual_cgmdata_percentage = count_greater_equal_70_and_less_equal_150_wholeday_manual_cgmdata['Whole Day Percentage'].sum()/manual_total_days if not count_greater_equal_70_and_less_equal_150_wholeday_manual_cgmdata.empty else 0
count_less_than_70_wholeday_manual_cgmdata_percentage = count_less_than_70_wholeday_manual_cgmdata['Whole Day Percentage'].sum()/manual_total_days if not count_less_than_70_wholeday_manual_cgmdata.empty else 0
count_less_than_54_wholeday_manual_cgmdata_percentage = count_less_than_54_wholeday_manual_cgmdata['Whole Day Percentage'].sum()/manual_total_days if not count_less_than_54_wholeday_manual_cgmdata.empty else 0

count_greater_than_180_wholeday_auto_cgmdata_percentage = count_greater_than_180_wholeday_auto_cgmdata['Whole Day Percentage'].sum()/auto_total_days if not count_greater_than_180_wholeday_auto_cgmdata.empty else 0
count_greater_than_250_wholeday_auto_cgmdata_percentage = count_greater_than_250_wholeday_auto_cgmdata['Whole Day Percentage'].sum()/auto_total_days if not count_greater_than_250_wholeday_auto_cgmdata.empty else 0
count_greater_equal_70_and_less_equal_180_wholeday_auto_cgmdata_percentage = count_greater_equal_70_and_less_equal_180_wholeday_auto_cgmdata['Whole Day Percentage'].sum()/auto_total_days if not count_greater_equal_70_and_less_equal_180_wholeday_auto_cgmdata.empty else 0
count_greater_equal_70_and_less_equal_150_wholeday_auto_cgmdata_percentage = count_greater_equal_70_and_less_equal_150_wholeday_auto_cgmdata['Whole Day Percentage'].sum()/auto_total_days if not count_greater_equal_70_and_less_equal_150_wholeday_auto_cgmdata.empty else 0
count_less_than_70_wholeday_auto_cgmdata_percentage = count_less_than_70_wholeday_auto_cgmdata['Whole Day Percentage'].sum()/auto_total_days if not count_less_than_70_wholeday_auto_cgmdata.empty else 0
count_less_than_54_wholeday_auto_cgmdata_percentage = count_less_than_54_wholeday_auto_cgmdata['Whole Day Percentage'].sum()/auto_total_days if not count_less_than_54_wholeday_auto_cgmdata.empty else 0

print('manual_total_days', manual_total_days)
print('auto_total_days', auto_total_days)

print('count_greater_than_180_wholeday_manual_cgmdata_percentage: ', count_greater_than_180_wholeday_manual_cgmdata_percentage)
print('count_greater_than_250_wholeday_manual_cgmdata_percentage: ', count_greater_than_250_wholeday_manual_cgmdata_percentage)
print('count_greater_equal_70_and_less_equal_180_wholeday_manual_cgmdata_percentage: ', count_greater_equal_70_and_less_equal_180_wholeday_manual_cgmdata_percentage)
print('count_greater_equal_70_and_less_equal_150_wholeday_manual_cgmdata_percentage: ', count_greater_equal_70_and_less_equal_150_wholeday_manual_cgmdata_percentage)
print('count_less_than_70_wholeday_manual_cgmdata_percentage: ', count_less_than_70_wholeday_manual_cgmdata_percentage)
print('count_less_than_54_wholeday_manual_cgmdata_percentage: ', count_less_than_54_wholeday_manual_cgmdata_percentage)


print('count_greater_than_180_wholeday_auto_cgmdata_percentage:', count_greater_than_180_wholeday_auto_cgmdata_percentage)
print('count_greater_than_250_wholeday_auto_cgmdata_percentage:', count_greater_than_250_wholeday_auto_cgmdata_percentage)
print('count_greater_equal_70_and_less_equal_180_wholeday_auto_cgmdata_percentage:', count_greater_equal_70_and_less_equal_180_wholeday_auto_cgmdata_percentage)
print('count_greater_equal_70_and_less_equal_150_wholeday_auto_cgmdata_percentage:', count_greater_equal_70_and_less_equal_150_wholeday_auto_cgmdata_percentage)
print('count_less_than_70_wholeday_auto_cgmdata_percentage:', count_less_than_70_wholeday_auto_cgmdata_percentage)
print('count_less_than_54_wholeday_auto_cgmdata_percentage:', count_less_than_54_wholeday_auto_cgmdata_percentage)

daytime_start = '06:00:00'
daytime_end = '23:59:59'
greater_than_180_daytime_manual_cgmdata = greater_than_180_wholeday_manual_cgmdata.set_index('Date Time').between_time(daytime_start, daytime_end).reset_index()
greater_than_250_daytime_manual_cgmdata = greater_than_250_wholeday_manual_cgmdata.set_index('Date Time').between_time(daytime_start, daytime_end).reset_index()
greater_equal_70_and_less_equal_180_daytime_manual_cgmdata = greater_equal_70_and_less_equal_180_wholeday_manual_cgmdata.set_index('Date Time').between_time(daytime_start, daytime_end).reset_index()
greater_equal_70_and_less_equal_150_daytime_manual_cgmdata = greater_equal_70_and_less_equal_150_wholeday_manual_cgmdata.set_index('Date Time').between_time(daytime_start, daytime_end).reset_index()
less_than_70_daytime_manual_cgmdata = less_than_70_wholeday_manual_cgmdata.set_index('Date Time').between_time(daytime_start, daytime_end).reset_index()
less_than_54_daytime_manual_cgmdata = less_than_54_wholeday_manual_cgmdata.set_index('Date Time').between_time(daytime_start, daytime_end).reset_index()
greater_than_180_daytime_auto_cgmdata = greater_than_180_wholeday_auto_cgmdata.set_index('Date Time').between_time(daytime_start, daytime_end).reset_index()
greater_than_250_daytime_auto_cgmdata = greater_than_250_wholeday_auto_cgmdata.set_index('Date Time').between_time(daytime_start, daytime_end).reset_index()
greater_equal_70_and_less_equal_180_daytime_auto_cgmdata = greater_equal_70_and_less_equal_180_wholeday_auto_cgmdata.set_index('Date Time').between_time(daytime_start, daytime_end).reset_index()
greater_equal_70_and_less_equal_150_daytime_auto_cgmdata = greater_equal_70_and_less_equal_150_wholeday_auto_cgmdata.set_index('Date Time').between_time(daytime_start, daytime_end).reset_index()
less_than_70_daytime_auto_cgmdata = less_than_70_wholeday_auto_cgmdata.set_index('Date Time').between_time(daytime_start, daytime_end).reset_index()
less_than_54_daytime_auto_cgmdata = less_than_54_wholeday_auto_cgmdata.set_index('Date Time').between_time(daytime_start, daytime_end).reset_index()

overnight_start = '12:00:00AM'
overnight_end = '05:59:59'
greater_than_180_overnight_manual_cgmdata = greater_than_180_wholeday_manual_cgmdata.set_index('Date Time').between_time(overnight_start, overnight_end).reset_index()
greater_than_250_overnight_manual_cgmdata = greater_than_250_wholeday_manual_cgmdata.set_index('Date Time').between_time(overnight_start, overnight_end).reset_index()
greater_equal_70_and_less_equal_180_overnight_manual_cgmdata = greater_equal_70_and_less_equal_180_wholeday_manual_cgmdata.set_index('Date Time').between_time(overnight_start, overnight_end).reset_index()
greater_equal_70_and_less_equal_150_overnight_manual_cgmdata = greater_equal_70_and_less_equal_150_wholeday_manual_cgmdata.set_index('Date Time').between_time(overnight_start, overnight_end).reset_index()
less_than_70_overnight_manual_cgmdata = less_than_70_wholeday_manual_cgmdata.set_index('Date Time').between_time(overnight_start, overnight_end).reset_index()
less_than_54_overnight_manual_cgmdata = less_than_54_wholeday_manual_cgmdata.set_index('Date Time').between_time(overnight_start, overnight_end).reset_index()
greater_than_180_overnight_auto_cgmdata = greater_than_180_wholeday_auto_cgmdata.set_index('Date Time').between_time(overnight_start, overnight_end).reset_index()
greater_than_250_overnight_auto_cgmdata = greater_than_250_wholeday_auto_cgmdata.set_index('Date Time').between_time(overnight_start, overnight_end).reset_index()
greater_equal_70_and_less_equal_180_overnight_auto_cgmdata = greater_equal_70_and_less_equal_180_wholeday_auto_cgmdata.set_index('Date Time').between_time(overnight_start, overnight_end).reset_index()
greater_equal_70_and_less_equal_150_overnight_auto_cgmdata = greater_equal_70_and_less_equal_150_wholeday_auto_cgmdata.set_index('Date Time').between_time(overnight_start, overnight_end).reset_index()
less_than_70_overnight_auto_cgmdata = less_than_70_wholeday_auto_cgmdata.set_index('Date Time').between_time(overnight_start, overnight_end).reset_index()
less_than_54_overnight_auto_cgmdata = less_than_54_wholeday_auto_cgmdata.set_index('Date Time').between_time(overnight_start, overnight_end).reset_index()

count_greater_than_180_daytime_manual_cgmdata = greater_than_180_daytime_manual_cgmdata.groupby(['Date'], as_index=False).count()
count_greater_than_250_daytime_manual_cgmdata = greater_than_250_daytime_manual_cgmdata.groupby(['Date'], as_index=False).count()
count_greater_equal_70_and_less_equal_180_daytime_manual_cgmdata = greater_equal_70_and_less_equal_180_daytime_manual_cgmdata.groupby(['Date'], as_index=False).count()
count_greater_equal_70_and_less_equal_150_daytime_manual_cgmdata = greater_equal_70_and_less_equal_150_daytime_manual_cgmdata.groupby(['Date'], as_index=False).count()
count_less_than_70_daytime_manual_cgmdata = less_than_70_daytime_manual_cgmdata.groupby(['Date'], as_index=False).count()
count_less_than_54_daytime_manual_cgmdata = less_than_54_daytime_manual_cgmdata.groupby(['Date'], as_index=False).count()
count_greater_than_180_daytime_auto_cgmdata = greater_than_180_daytime_auto_cgmdata.groupby(['Date'], as_index=False).count()
count_greater_than_250_daytime_auto_cgmdata = greater_than_250_daytime_auto_cgmdata.groupby(['Date'], as_index=False).count()
count_greater_equal_70_and_less_equal_180_daytime_auto_cgmdata = greater_equal_70_and_less_equal_180_daytime_auto_cgmdata.groupby(['Date'], as_index=False).count()
count_greater_equal_70_and_less_equal_150_daytime_auto_cgmdata = greater_equal_70_and_less_equal_150_daytime_auto_cgmdata.groupby(['Date'], as_index=False).count()
count_less_than_70_daytime_auto_cgmdata = less_than_70_daytime_auto_cgmdata.groupby(['Date'], as_index=False).count()
count_less_than_54_daytime_auto_cgmdata = less_than_54_daytime_auto_cgmdata.groupby(['Date'], as_index=False).count()

count_greater_than_180_overnight_manual_cgmdata = greater_than_180_overnight_manual_cgmdata.groupby(['Date'], as_index=False).count()
count_greater_than_250_overnight_manual_cgmdata = greater_than_250_overnight_manual_cgmdata.groupby(['Date'], as_index=False).count()
count_greater_equal_70_and_less_equal_180_overnight_manual_cgmdata = greater_equal_70_and_less_equal_180_overnight_manual_cgmdata.groupby(['Date'], as_index=False).count()
count_greater_equal_70_and_less_equal_150_overnight_manual_cgmdata = greater_equal_70_and_less_equal_150_overnight_manual_cgmdata.groupby(['Date'], as_index=False).count()
count_less_than_70_overnight_manual_cgmdata = less_than_70_overnight_manual_cgmdata.groupby(['Date'], as_index=False).count()
count_less_than_54_overnight_manual_cgmdata = less_than_54_overnight_manual_cgmdata.groupby(['Date'], as_index=False).count()
count_greater_than_180_overnight_auto_cgmdata = greater_than_180_overnight_auto_cgmdata.groupby(['Date'], as_index=False).count()
count_greater_than_250_overnight_auto_cgmdata = greater_than_250_overnight_auto_cgmdata.groupby(['Date'], as_index=False).count()
count_greater_equal_70_and_less_equal_180_overnight_auto_cgmdata = greater_equal_70_and_less_equal_180_overnight_auto_cgmdata.groupby(['Date'], as_index=False).count()
count_greater_equal_70_and_less_equal_150_overnight_auto_cgmdata = greater_equal_70_and_less_equal_150_overnight_auto_cgmdata.groupby(['Date'], as_index=False).count()
count_less_than_70_overnight_auto_cgmdata = less_than_70_overnight_auto_cgmdata.groupby(['Date'], as_index=False).count()
count_less_than_54_overnight_auto_cgmdata = less_than_54_overnight_auto_cgmdata.groupby(['Date'], as_index=False).count()

count_greater_than_180_daytime_manual_cgmdata['Daytime Percentage'] = 100* count_greater_than_180_daytime_manual_cgmdata['Date Time'] / wholeday_total_data
count_greater_than_250_daytime_manual_cgmdata['Daytime Percentage'] = 100* count_greater_than_250_daytime_manual_cgmdata['Date Time'] / wholeday_total_data
count_greater_equal_70_and_less_equal_180_daytime_manual_cgmdata['Daytime Percentage'] = 100* count_greater_equal_70_and_less_equal_180_daytime_manual_cgmdata['Date Time'] / wholeday_total_data
count_greater_equal_70_and_less_equal_150_daytime_manual_cgmdata['Daytime Percentage'] = 100* count_greater_equal_70_and_less_equal_150_daytime_manual_cgmdata['Date Time'] / wholeday_total_data
count_less_than_70_daytime_manual_cgmdata['Daytime Percentage'] = 100* count_less_than_70_daytime_manual_cgmdata['Date Time'] / wholeday_total_data
count_less_than_54_daytime_manual_cgmdata['Daytime Percentage'] = 100* count_less_than_54_daytime_manual_cgmdata['Date Time'] / wholeday_total_data
count_greater_than_180_daytime_auto_cgmdata['Daytime Percentage'] = 100* count_greater_than_180_daytime_auto_cgmdata['Date Time'] / wholeday_total_data
count_greater_than_250_daytime_auto_cgmdata['Daytime Percentage'] = 100* count_greater_than_250_daytime_auto_cgmdata['Date Time'] / wholeday_total_data
count_greater_equal_70_and_less_equal_180_daytime_auto_cgmdata['Daytime Percentage'] = 100* count_greater_equal_70_and_less_equal_180_daytime_auto_cgmdata['Date Time'] / wholeday_total_data
count_greater_equal_70_and_less_equal_150_daytime_auto_cgmdata['Daytime Percentage'] = 100* count_greater_equal_70_and_less_equal_150_daytime_auto_cgmdata['Date Time'] / wholeday_total_data
count_less_than_70_daytime_auto_cgmdata['Daytime Percentage'] = 100* count_less_than_70_daytime_auto_cgmdata['Date Time'] / wholeday_total_data
count_less_than_54_daytime_auto_cgmdata['Daytime Percentage'] = 100* count_less_than_54_daytime_auto_cgmdata['Date Time'] / wholeday_total_data

count_greater_than_180_overnight_manual_cgmdata['Overnight Percentage'] = 100* count_greater_than_180_overnight_manual_cgmdata['Date Time'] / wholeday_total_data
count_greater_than_250_overnight_manual_cgmdata['Overnight Percentage'] = 100* count_greater_than_250_overnight_manual_cgmdata['Date Time'] / wholeday_total_data
count_greater_equal_70_and_less_equal_180_overnight_manual_cgmdata['Overnight Percentage'] = 100* count_greater_equal_70_and_less_equal_180_overnight_manual_cgmdata['Date Time'] / wholeday_total_data
count_greater_equal_70_and_less_equal_150_overnight_manual_cgmdata['Overnight Percentage'] = 100* count_greater_equal_70_and_less_equal_150_overnight_manual_cgmdata['Date Time'] / wholeday_total_data
count_less_than_70_overnight_manual_cgmdata['Overnight Percentage'] = 100* count_less_than_70_overnight_manual_cgmdata['Date Time'] / wholeday_total_data
count_less_than_54_overnight_manual_cgmdata['Overnight Percentage'] = 100* count_less_than_54_overnight_manual_cgmdata['Date Time'] / wholeday_total_data
count_greater_than_180_overnight_auto_cgmdata['Overnight Percentage'] = 100* count_greater_than_180_overnight_auto_cgmdata['Date Time'] / wholeday_total_data
count_greater_than_250_overnight_auto_cgmdata['Overnight Percentage'] = 100* count_greater_than_250_overnight_auto_cgmdata['Date Time'] / wholeday_total_data
count_greater_equal_70_and_less_equal_180_overnight_auto_cgmdata['Overnight Percentage'] = 100* count_greater_equal_70_and_less_equal_180_overnight_auto_cgmdata['Date Time'] / wholeday_total_data
count_greater_equal_70_and_less_equal_150_overnight_auto_cgmdata['Overnight Percentage'] = 100* count_greater_equal_70_and_less_equal_150_overnight_auto_cgmdata['Date Time'] / wholeday_total_data
count_less_than_70_overnight_auto_cgmdata['Overnight Percentage'] = 100* count_less_than_70_overnight_auto_cgmdata['Date Time'] / wholeday_total_data
count_less_than_54_overnight_auto_cgmdata['Overnight Percentage'] = 100* count_less_than_54_overnight_auto_cgmdata['Date Time'] / wholeday_total_data

count_greater_than_180_daytime_manual_cgmdata_percentage = count_greater_than_180_daytime_manual_cgmdata['Daytime Percentage'].sum()/manual_total_days if not count_greater_than_180_daytime_manual_cgmdata.empty else 0
count_greater_than_250_daytime_manual_cgmdata_percentage = count_greater_than_250_daytime_manual_cgmdata['Daytime Percentage'].sum()/manual_total_days if not count_greater_than_250_daytime_manual_cgmdata.empty else 0
count_greater_equal_70_and_less_equal_180_daytime_manual_cgmdata_percentage = count_greater_equal_70_and_less_equal_180_daytime_manual_cgmdata['Daytime Percentage'].sum()/manual_total_days if not count_greater_equal_70_and_less_equal_180_daytime_manual_cgmdata.empty else 0
count_greater_equal_70_and_less_equal_150_daytime_manual_cgmdata_percentage = count_greater_equal_70_and_less_equal_150_daytime_manual_cgmdata['Daytime Percentage'].sum()/manual_total_days if not count_greater_equal_70_and_less_equal_150_daytime_manual_cgmdata.empty else 0
count_less_than_70_daytime_manual_cgmdata_percentage = count_less_than_70_daytime_manual_cgmdata['Daytime Percentage'].sum()/manual_total_days if not count_less_than_70_daytime_manual_cgmdata.empty else 0
count_less_than_54_daytime_manual_cgmdata_percentage = count_less_than_54_daytime_manual_cgmdata['Daytime Percentage'].sum()/manual_total_days if not count_less_than_54_daytime_manual_cgmdata.empty else 0

count_greater_than_180_daytime_auto_cgmdata_percentage = count_greater_than_180_daytime_auto_cgmdata['Daytime Percentage'].sum()/auto_total_days if not count_greater_than_180_daytime_auto_cgmdata.empty else 0
count_greater_than_250_daytime_auto_cgmdata_percentage = count_greater_than_250_daytime_auto_cgmdata['Daytime Percentage'].sum()/auto_total_days if not count_greater_than_250_daytime_auto_cgmdata.empty else 0
count_greater_equal_70_and_less_equal_180_daytime_auto_cgmdata_percentage = count_greater_equal_70_and_less_equal_180_daytime_auto_cgmdata['Daytime Percentage'].sum()/auto_total_days if not count_greater_equal_70_and_less_equal_180_daytime_auto_cgmdata.empty else 0
count_greater_equal_70_and_less_equal_150_daytime_auto_cgmdata_percentage = count_greater_equal_70_and_less_equal_150_daytime_auto_cgmdata['Daytime Percentage'].sum()/auto_total_days if not count_greater_equal_70_and_less_equal_150_daytime_auto_cgmdata.empty else 0
count_less_than_70_daytime_auto_cgmdata_percentage = count_less_than_70_daytime_auto_cgmdata['Daytime Percentage'].sum()/auto_total_days if not count_less_than_70_daytime_auto_cgmdata.empty else 0
count_less_than_54_daytime_auto_cgmdata_percentage = count_less_than_54_daytime_auto_cgmdata['Daytime Percentage'].sum()/auto_total_days if not count_less_than_54_daytime_auto_cgmdata.empty else 0

print('count_greater_than_180_daytime_manual_cgmdata_percentage: ', count_greater_than_180_daytime_manual_cgmdata_percentage)
print('count_greater_than_250_daytime_manual_cgmdata_percentage: ', count_greater_than_250_daytime_manual_cgmdata_percentage)
print('count_greater_equal_70_and_less_equal_180_daytime_manual_cgmdata_percentage: ', count_greater_equal_70_and_less_equal_180_daytime_manual_cgmdata_percentage)
print('count_greater_equal_70_and_less_equal_150_daytime_manual_cgmdata_percentage: ', count_greater_equal_70_and_less_equal_150_daytime_manual_cgmdata_percentage)
print('count_less_than_70_daytime_manual_cgmdata_percentage: ', count_less_than_70_daytime_manual_cgmdata_percentage)
print('count_less_than_54_daytime_manual_cgmdata_percentage: ', count_less_than_54_daytime_manual_cgmdata_percentage)

print('count_greater_than_180_daytime_auto_cgmdata_percentage:', count_greater_than_180_daytime_auto_cgmdata_percentage)
print('count_greater_than_250_daytime_auto_cgmdata_percentage:', count_greater_than_250_daytime_auto_cgmdata_percentage)
print('count_greater_equal_70_and_less_equal_180_daytime_auto_cgmdata_percentage:', count_greater_equal_70_and_less_equal_180_daytime_auto_cgmdata_percentage)
print('count_greater_equal_70_and_less_equal_150_daytime_auto_cgmdata_percentage:', count_greater_equal_70_and_less_equal_150_daytime_auto_cgmdata_percentage)
print('count_less_than_70_daytime_auto_cgmdata_percentage:', count_less_than_70_daytime_auto_cgmdata_percentage)
print('count_less_than_54_daytime_auto_cgmdata_percentage:', count_less_than_54_daytime_auto_cgmdata_percentage)

count_greater_than_180_overnight_manual_cgmdata_percentage = count_greater_than_180_overnight_manual_cgmdata['Overnight Percentage'].sum()/manual_total_days if not count_greater_than_180_overnight_manual_cgmdata.empty else 0
count_greater_than_250_overnight_manual_cgmdata_percentage = count_greater_than_250_overnight_manual_cgmdata['Overnight Percentage'].sum()/manual_total_days if not count_greater_than_250_overnight_manual_cgmdata.empty else 0
count_greater_equal_70_and_less_equal_180_overnight_manual_cgmdata_percentage = count_greater_equal_70_and_less_equal_180_overnight_manual_cgmdata['Overnight Percentage'].sum()/manual_total_days if not count_greater_equal_70_and_less_equal_180_overnight_manual_cgmdata.empty else 0
count_greater_equal_70_and_less_equal_150_overnight_manual_cgmdata_percentage = count_greater_equal_70_and_less_equal_150_overnight_manual_cgmdata['Overnight Percentage'].sum()/manual_total_days if not count_greater_equal_70_and_less_equal_150_overnight_manual_cgmdata.empty else 0
count_less_than_70_overnight_manual_cgmdata_percentage = count_less_than_70_overnight_manual_cgmdata['Overnight Percentage'].sum()/manual_total_days if not count_less_than_70_overnight_manual_cgmdata.empty else 0
count_less_than_54_overnight_manual_cgmdata_percentage = count_less_than_54_overnight_manual_cgmdata['Overnight Percentage'].sum()/manual_total_days if not count_less_than_54_overnight_manual_cgmdata.empty else 0

count_greater_than_180_overnight_auto_cgmdata_percentage = count_greater_than_180_overnight_auto_cgmdata['Overnight Percentage'].sum()/auto_total_days if not count_greater_than_180_overnight_auto_cgmdata.empty else 0
count_greater_than_250_overnight_auto_cgmdata_percentage = count_greater_than_250_overnight_auto_cgmdata['Overnight Percentage'].sum()/auto_total_days if not count_greater_than_250_overnight_auto_cgmdata.empty else 0
count_greater_equal_70_and_less_equal_180_overnight_auto_cgmdata_percentage = count_greater_equal_70_and_less_equal_180_overnight_auto_cgmdata['Overnight Percentage'].sum()/auto_total_days if not count_greater_equal_70_and_less_equal_180_overnight_auto_cgmdata.empty else 0
count_greater_equal_70_and_less_equal_150_overnight_auto_cgmdata_percentage = count_greater_equal_70_and_less_equal_150_overnight_auto_cgmdata['Overnight Percentage'].sum()/auto_total_days if not count_greater_equal_70_and_less_equal_150_overnight_auto_cgmdata.empty else 0
count_less_than_70_overnight_auto_cgmdata_percentage = count_less_than_70_overnight_auto_cgmdata['Overnight Percentage'].sum()/auto_total_days if not count_less_than_70_overnight_auto_cgmdata.empty else 0
count_less_than_54_overnight_auto_cgmdata_percentage = count_less_than_54_overnight_auto_cgmdata['Overnight Percentage'].sum()/auto_total_days if not count_less_than_54_overnight_auto_cgmdata.empty else 0

print('count_greater_than_180_overnight_manual_cgmdata_percentage: ', count_greater_than_180_overnight_manual_cgmdata_percentage)
print('count_greater_than_250_overnight_manual_cgmdata_percentage: ', count_greater_than_250_overnight_manual_cgmdata_percentage)
print('count_greater_equal_70_and_less_equal_180_overnight_manual_cgmdata_percentage: ', count_greater_equal_70_and_less_equal_180_overnight_manual_cgmdata_percentage)
print('count_greater_equal_70_and_less_equal_150_overnight_manual_cgmdata_percentage: ', count_greater_equal_70_and_less_equal_150_overnight_manual_cgmdata_percentage)
print('count_less_than_70_overnight_manual_cgmdata_percentage: ', count_less_than_70_overnight_manual_cgmdata_percentage)
print('count_less_than_54_overnight_manual_cgmdata_percentage: ', count_less_than_54_overnight_manual_cgmdata_percentage)

print('count_greater_than_180_overnight_auto_cgmdata_percentage:', count_greater_than_180_overnight_auto_cgmdata_percentage)
print('count_greater_than_250_overnight_auto_cgmdata_percentage:', count_greater_than_250_overnight_auto_cgmdata_percentage)
print('count_greater_equal_70_and_less_equal_180_overnight_auto_cgmdata_percentage:', count_greater_equal_70_and_less_equal_180_overnight_auto_cgmdata_percentage)
print('count_greater_equal_70_and_less_equal_150_overnight_auto_cgmdata_percentage:', count_greater_equal_70_and_less_equal_150_overnight_auto_cgmdata_percentage)
print('count_less_than_70_overnight_auto_cgmdata_percentage:', count_less_than_70_overnight_auto_cgmdata_percentage)
print('count_less_than_54_overnight_auto_cgmdata_percentage:', count_less_than_54_overnight_auto_cgmdata_percentage)

list1_manual = [count_greater_than_180_overnight_manual_cgmdata_percentage, count_greater_than_250_overnight_manual_cgmdata_percentage, count_greater_equal_70_and_less_equal_180_overnight_manual_cgmdata_percentage, count_greater_equal_70_and_less_equal_150_overnight_manual_cgmdata_percentage, count_less_than_70_overnight_manual_cgmdata_percentage, count_less_than_54_overnight_manual_cgmdata_percentage, count_greater_than_180_daytime_manual_cgmdata_percentage, count_greater_than_250_daytime_manual_cgmdata_percentage, count_greater_equal_70_and_less_equal_180_daytime_manual_cgmdata_percentage, count_greater_equal_70_and_less_equal_150_daytime_manual_cgmdata_percentage, count_less_than_70_daytime_manual_cgmdata_percentage, count_less_than_54_daytime_manual_cgmdata_percentage, count_greater_than_180_wholeday_manual_cgmdata_percentage, count_greater_than_250_wholeday_manual_cgmdata_percentage, count_greater_equal_70_and_less_equal_180_wholeday_manual_cgmdata_percentage, count_greater_equal_70_and_less_equal_150_wholeday_manual_cgmdata_percentage, count_less_than_70_wholeday_manual_cgmdata_percentage, count_less_than_54_wholeday_manual_cgmdata_percentage]
list2_auto = [count_greater_than_180_overnight_auto_cgmdata_percentage, count_greater_than_250_overnight_auto_cgmdata_percentage, count_greater_equal_70_and_less_equal_180_overnight_auto_cgmdata_percentage, count_greater_equal_70_and_less_equal_150_overnight_auto_cgmdata_percentage, count_less_than_70_overnight_auto_cgmdata_percentage, count_less_than_54_overnight_auto_cgmdata_percentage, count_greater_than_180_daytime_auto_cgmdata_percentage, count_greater_than_250_daytime_auto_cgmdata_percentage, count_greater_equal_70_and_less_equal_180_daytime_auto_cgmdata_percentage, count_greater_equal_70_and_less_equal_150_daytime_auto_cgmdata_percentage, count_less_than_70_daytime_auto_cgmdata_percentage, count_less_than_54_daytime_auto_cgmdata_percentage, count_greater_than_180_wholeday_auto_cgmdata_percentage, count_greater_than_250_wholeday_auto_cgmdata_percentage, count_greater_equal_70_and_less_equal_180_wholeday_auto_cgmdata_percentage, count_greater_equal_70_and_less_equal_150_wholeday_auto_cgmdata_percentage, count_less_than_70_wholeday_auto_cgmdata_percentage, count_less_than_54_wholeday_auto_cgmdata_percentage]
print_df = pd.DataFrame(list1_manual).T
print_df = print_df.append(pd.Series(list2_auto), ignore_index=True)
print_df

print_df.to_csv('Results.csv', header=False, index=False)