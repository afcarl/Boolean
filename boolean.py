#-----------------------------------------------------------MODULE-------------------------------------------------------#
import sys

#------------------------------------------------------------FILES-------------------------------------------------------#
Original_File=open('GRID.dat','r')                                            # File to be modified
Modified_File=open('DFEM_Node1-Root-joint_v2.1_STEP2_DFEM_modified.dat','w')  # File New File after modification
Node_To_Be_Removed=open('Node_To_Be_removed.dat','r')                         # File with Node to be deleted

#------------------------------------------------------Initialize variable-----------------------------------------------#
List_Node_To_Be_Removed=[] # Nodes list of the Modified File
Compteur_Node_Deleted=0    # Node deleted

#-------------------------------------------------Number of Lines in Original File---------------------------------------#

Total_Lines_in_Files=0     # Initialize Total Lines in Original file
for l in Original_File:
    Total_Lines_in_Files += 1

print 'Number of lines : {0}'. format(Total_Lines_in_Files)
Original_File.close()

#---------------------------------------------------------ProgressBar----------------------------------------------------#
Line_Read=0

def ProgressBar():
    fin=""
    percent=(float(Line_Read)/Total_Lines_in_Files)*100
    nbetoiles = int(percent / 5)
    nbespaces = 20 - nbetoiles
    e='['+'#'*nbetoiles+' '*nbespaces+'] %d%% %s' % (percent, fin)
    #e='%d%% %s' % (percent, fin)
    sys.stdout.write('\r%s' % e)
    sys.stdout.flush()

    if int(percent)==100:
        fin="Finished !"
        print (fin)

#----------------------------------------------Creation of Node List to be Removed--------------------------------------#

for ID in Node_To_Be_Removed:
    ID=ID.rstrip()
    List_Node_To_Be_Removed.append(ID)
    
Nbr_Node_To_Deleted = len(List_Node_To_Be_Removed)

print 'There are {0} nodes to be Deleted'.format(Nbr_Node_To_Deleted)

#-------------------------------------------------------Main Program----------------------------------------------------#

Original_File=open('GRID.dat','r')
Card_to_be_changed = 'GRID'

for lines in Original_File:
    i=0
    A_Node_To_Be_Deleted=0
    Line_Read+=1

    ProgressBar()

    if lines[:4]==Card_to_be_changed:
        
        ID_Node_To_Be_Removed=lines[8:16].strip()

        for id in List_Node_To_Be_Removed:
            Node_1=List_Node_To_Be_Removed[i]
            i=i+1


            if int(Node_1)==int(ID_Node_To_Be_Removed):
                A_Node_To_Be_Deleted = A_Node_To_Be_Deleted+1
                Compteur_Node_Deleted=Compteur_Node_Deleted+1

            else:
                if i==(Nbr_Node_To_Deleted) and A_Node_To_Be_Deleted==0:
                    Modified_File.write(lines)
    else :
        Modified_File.write(lines)

print 'They have {0} Node(s) were removed'.format(Compteur_Node_Deleted)

#-------------------------------------------------------Close Files-----------------------------------------------------#
Original_File.close()
Modified_File.close()
Node_To_Be_Removed.close()

#------------------------------------------------------End of Program---------------------------------------------------#
