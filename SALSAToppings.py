import os

distance = 20   #MINIMUM DISTANCE BETWEEN PEAKS
threshold = 50  #THRESHOLD FOR PEAK

variableFile = open('variables.txt')
variables = variableFile.readlines()
distance = int(variables[1][11:-1])
threshold = int(variables[3][12:])
variableFile.close()

print(distance, threshold)

outputFileDetailed = open('data/output/outputDataDetailed.txt','a')
outputFileDetailed = open('data/output/outputDataDetailed.txt', 'r+')
outputFileDetailed.truncate(0)
outputFileDetailed.writelines(('DISTANCE: ' + str(distance) + ' | THRESHOLD: ' + str(threshold) + '\n'))

outputFileTSV = open('data/output/outputDataTSV.txt','a')
outputFileTSV = open('data/output/outputDataTSV.txt', 'r+')
outputFileTSV.truncate(0)
outputFileTSV.writelines(str('GLong' + '\t' + 'x1' + '\t' + 'x2' + '\t' + 'x3' + '\n'))

print(sorted(os.listdir('data\input')))

for filename in sorted(os.listdir('data\input')):
  f = os.path.join('data\input', filename)
  if os.path.isfile(f):
    f = open(f, "r")
    content = f.readlines()

    x = []
    y = []
    lineIndex = 8
    while lineIndex < len(content):
      splitCoords = content[lineIndex].split(' ')
      x.append(float(splitCoords[0]))
      y.append(float(splitCoords[1]))
      lineIndex = lineIndex + 1
    #print(x, y)

    linesToWriteTSV = []
    linesToWriteDetailed = [
      '\n',
      'FILENAME: ', f.name,
      '\nTIME MAY BE INCORRECT - ',
      content[2], #DATE
      content[3], #GLON and GLAT given in degrees
      content[4], #GLON=64.8010272859894
      content[5], #GLAT=0.11676624005829851
      'PEAKS:\n'
    ]

    if True:  ### Calculations
      #####
      i = distance
      if max(y) > threshold:
        y1 = max(y)
        x1 = x[y.index(y1)]
        x1Index = y.index(y1)

        while i > (-distance-1):
          if ((x1Index-1) + i) >= 0 and ((x1Index-1) + i) < len(x):
            x.pop((x1Index-1) + i)
            y.pop((x1Index-1) + i)
          i = i-1

      if max(y) > threshold:
        y2 = max(y)
        x2 = x[y.index(y2)]
        x2Index = y.index(y2)

        i = distance
        while i > (-distance-1):
          if ((x2Index-1) + i) >= 0 and ((x2Index-1) + i) < len(x):
            x.pop((x2Index-1) + i)
            y.pop((x2Index-1) + i)
          i = i-1

      if max(y) > threshold:
        y3 = max(y)
        x3 = x[y.index(y3)]
        x3Index = y.index(y3)

        i = distance
        while i > (-distance-1):
          if ((x3Index-1) + i) >= 0 and ((x3Index-1) + i) < len(x):
            x.pop((x3Index-1) + i)
            y.pop((x3Index-1) + i)
          i = i-1

      #print('--- Left ---')
      #print(x)
      #print(y)
      #print('--- Values ---')
      if 'x1' in locals():
        #print('x1:', x1, 'y1:', y1)
        linesToWriteDetailed.append('x1:' + str(x1*1000) + ', y1:' + str(y1) + '\n')
        line = str(str(content[4][7:20]) + '\t' + str(x1*1000) + '\n')
      else:
        #print('No peaks found!')
        linesToWriteDetailed.append
      if 'x2' in locals():
        #print('x2:', x2, 'y2:', y2)
        linesToWriteDetailed.append('x2:' + str(x2*1000) + ', y2:' + str(y2) + '\n')
        line = str(str(content[4][7:20]) + '\t' + str(x1*1000) + '\t' + str(x2*1000) + '\n')
      if 'x3' in locals():
        #print('x3:', x3, 'y3:', y3) 
        linesToWriteDetailed.append('x3:' + str(x3*1000) + ', y3:' + str(y3) + '\n')
        line = str(str(content[4][7:20]) + '\t' + str(x1*1000) + '\t' + str(x2*1000) + '\t' + str(x3*1000) + '\n')
      linesToWriteTSV.append(line)
      #####
    
    if 'x1' in locals():
      del x1
    if 'x2' in locals():
      del x2
    if 'x3' in locals():
      del x3        

    linesToWriteDetailed = [period.replace('.', ',') for period in linesToWriteDetailed]
    linesToWriteTSV = [period.replace('.', ',') for period in linesToWriteTSV]

    outputFileDetailed.writelines(linesToWriteDetailed)
    outputFileTSV.writelines(linesToWriteTSV)
    f.close()
outputFileDetailed.close()
outputFileTSV.close()