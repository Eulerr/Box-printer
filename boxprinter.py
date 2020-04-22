num_of_boxes = int(input('How many boxes: '))
print(' '*num_of_boxes +'_'*num_of_boxes)
if num_of_boxes-1 == 0:
    print('/_/|')
    print('|_|/')
else:
    for i in range(num_of_boxes-1):
        print(' '*(num_of_boxes-i-1) + '/' + ' '*num_of_boxes + '/' + ' '*i + '|')
    print('/'+'_'*num_of_boxes+'/'+ ' '*(num_of_boxes-1) + '|')
    for i in range(num_of_boxes-1):
        print('|' + ' '*num_of_boxes + '|' + ' '*(num_of_boxes-1-i) + '/')
    print('|' + '_'*num_of_boxes + '|/')
