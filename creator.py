import ast,os,random,string

matrix_file='matrices.txt'



#+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
#+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
#+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
#+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
class matrix_display:
    
    
    #=========================================================================
    #=========================================================================
    #=========================================================================
    def display_matrix(self, mtrx):
        print('#########################################')
        for i in mtrx:
            print('========================')
            for k in i:
                print(k)
            print('========================')
        print('#########################################')
    #=========================================================================
    #=========================================================================
    #=========================================================================
    
    #=========================================================================
    #=========================================================================
    #=========================================================================    
    def display_channels(self,channels):
        for i in range(len(channels)):
            item=channels[i]
            m_id=i
            
            info={'channel':item,'m_id':m_id}
            
            print('+++++++++++++++++++')
            for i in info:
                print(i,':',info[i])
            print('+++++++++++++++++++')
    #=========================================================================
    #=========================================================================
    #=========================================================================
    
    #=========================================================================
    #=========================================================================
    #=========================================================================
    '''used during creation of program'''
    def display_layer(self, layer):
        print('+++++++++++++++++++++++++++++++')
        for i in layer:
            print(i)
        print('+++++++++++++++++++++++++++++++') 
    #=========================================================================
    #=========================================================================
    #=========================================================================
        
        
#+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
#+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
#+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
#+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++


#+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
#+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
#+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
#+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
class matrix_manip: #matrix manipulator
    
    
    #=========================================================================
    #=========================================================================
    #=========================================================================
    '''this function turns the rows and columns of the matrix
    given int columns and rows respectively
    NOTE: for now this function is only known to work with
          matrix that consists of a length and width of the
          same size such as 3x3

    EX:
              Original
       ['000', '001', '002']
       ['010', '011', '012']
       ['020', '021', '022']

                New
       ['000', '010', '020']
       ['001', '011', '021']
       ['002', '012', '022']
    
    '''
    
    def flip(self,mtrx):
        height,width,length=self.get_matrix_dimensions(mtrx)
        wmatrix=mtrx
        fin_matrix=[]
        for i in range(height):
            m1=wmatrix[i]
            sub1=[]
            for k in range(width):
                sub1.append([])
            for k in range(width):
                m2=m1[k]

                for j in range(length):
                    item=m2[j]
                    sub1[j].append(item)
            fin_matrix.append(sub1)
        return fin_matrix
    #=========================================================================
    #=========================================================================
    #=========================================================================
    
    
    
    
    #=========================================================================
    #=========================================================================
    #=========================================================================
    '''this function reverses the order of the current rows
       from the given matrix.

       EX:         Original
            ['000', '001', '002']
            ['010', '011', '012']
            ['020', '021', '022']

                    New
            ['002', '001', '000']
            ['012', '011', '010']
            ['022', '021', '020']

      NOTE: this function is only known to work on a matrix
            with the same length and width'''

    def reverse(self,mtrx):
        height,width,length=self.get_matrix_dimensions(mtrx)
        fin_matrix=[]
        for i in range(height):
            trix1=mtrx[i]
            for k in range(width):
                trix2=trix1[k]
                nlis=[]
                for j in range(length):
                    item=trix2[j]
                    nlis.insert(0,item)
                trix1[k]=nlis
            fin_matrix.append(trix1)
        return fin_matrix
    #=========================================================================
    #=========================================================================
    #=========================================================================
    
    
    #=========================================================================
    #=========================================================================
    #=========================================================================
    
    '''this function take each row within each plane of a matrix
       and puts them together into a new matrix
        EX:       Original
            ========================
            ['000', '001', '002']
            ['010', '011', '012']
            ['020', '021', '022']
            ========================
            ========================
            ['100', '101', '102']
            ['110', '111', '112']
            ['120', '121', '122']
            ========================
            ========================
            ['200', '201', '202']
            ['210', '211', '212']
            ['220', '221', '222']
            ========================

                    New
            ========================
            ['000', '100', '200']
            ['001', '101', '201']
            ['002', '102', '202']
            ========================
            ========================
            ['010', '110', '210']
            ['011', '111', '211']
            ['012', '112', '212']
            ========================
            ========================
            ['020', '120', '220']
            ['021', '121', '221']
            ['022', '122', '222']
            ========================

       NOTE: this is only for now known to work with a 3 dimensional
             matrix whos height,width and length are of equal value'''
    def reslice(self,mtrx):
        height,width,length=self.get_matrix_dimensions(mtrx)
        fin_matrix=[]
        holder1=[]

        for k in range(height):
            holder1.append([])
        for i in range(height):
            trix1=mtrx[i]
            #print('--------------')
            for k in range(width):
                trix2=trix1[k]
                holder1[k].append(trix2)
            #print('--------------')
        fin_matrix=self.flip(holder1)
        return fin_matrix
        
    #=========================================================================
    #=========================================================================
    #=========================================================================
    
    
    #=========================================================================
    #=========================================================================
    #=========================================================================
    
    '''this function takes the layers of the given matrix and
       reverses the order of them.

       EX:         Original
            ========================
            ['000', '001', '002']
            ['010', '011', '012']
            ['020', '021', '022']
            ========================
            ========================
            ['100', '101', '102']
            ['110', '111', '112']
            ['120', '121', '122']
            ========================
            ========================
            ['200', '201', '202']
            ['210', '211', '212']
            ['220', '221', '222']
            ========================
                    New
            ========================
            ['200', '201', '202']
            ['210', '211', '212']
            ['220', '221', '222']
            ========================
            ========================
            ['100', '101', '102']
            ['110', '111', '112']
            ['120', '121', '122']
            ========================
            ========================
            ['000', '001', '002']
            ['010', '011', '012']
            ['020', '021', '022']
            ========================'''
    def reverse_planes(self,mtrx):
        working_matrix=mtrx
        fin_matrix=[]
        for i in working_matrix:
            fin_matrix.insert(0,i)
        return fin_matrix
        
    #=========================================================================
    #=========================================================================
    #=========================================================================
    
    #=========================================================================
    #=========================================================================
    #=========================================================================
    '''this function rotates the 3 dimensional matrix (not transpose)
       the matrix for now only supports a matrix with all sizes being equal
       such as in the case of a 3x3x3 matrix'''
    def rotate(self,direction,matr):
        
        og=matr

        #+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
        #+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
        
        #+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
        #+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++

        def rot_clock_wise(trix):
            fmat=self.flip(trix)
            rmat=self.reverse(fmat)
            return rmat

        def rot_clock_counter(trix):
            work_matrix=matr
            wm1=self.flip(self.reverse(work_matrix))
            return wm1
            #pass

        def rot_left(trix):
            wmatrix=matr
            s1=self.flip(wmatrix)
            s2=self.reslice(s1)
            s3=self.reverse_planes(s2)
            return s3


        def rot_right(trix):
            working_matrix=matr
            flipped=self.flip(working_matrix)
            planerev=self.reverse_planes(flipped)
            sliced=self.reslice(planerev)
            return sliced


        def rot_front(trix):
            sone=rot_right(trix)
            stwo=rot_clock_wise(trix)
            sthree=rot_left(trix)
            return sthree

        def rot_back(trix):
            sone=rot_left(trix)
            stwo=rot_clock_wise(trix)
            sthree=rot_right(trix)
            return sthree


        if direction=='left':
            rot_left(og)
        elif direction=='right':
            rot_right(og)
        elif direction=='front':
            rot_front(og)
        elif direction=='back':
            rot_back(og)
        elif direction=='clock_wise':
            rot_clock_wise(og)
        elif direction=='clock_counter':
            rot_clock_counter(og)
        else:
            print('that is not an option')


    #=========================================================================
    #=========================================================================
    #=========================================================================
    
    
    #=========================================================================
    #=========================================================================
    #=========================================================================
    def get_matrix_dimensions(self,mat):
        height=0
        width=0
        length=0
        
        for i in mat:
            height+=1
        for i in mat[0]:
            width+=1
            
        try:
            for i in mat[0][0]:
                length+=1
        except:
            length=width
            width=height
            height=0
            
        return height,width,length
    #=========================================================================
    #=========================================================================
    #=========================================================================
    
    #=========================================================================
    #=========================================================================
    #=========================================================================
    '''stores provided item (can be any type) within the coordinates
       provided within the matrix'''
    def store_item(self,item,x,y,z,matr):
        matr[x][y][z]=item
        return matr
        
    #=========================================================================
    #=========================================================================
    #=========================================================================
    
    
    #=========================================================================
    #=========================================================================
    #=========================================================================
    '''this function is meant ot store information into each spot in the matrix
       but is meant to be used with a string of bits where it will then seperate
       the string into individual parts and then distribute the bits and provide
       any overflow if all the information cannot fit within the matrix.'''

    def store_info(self,info,matr):
        height,width,length=self.get_matrix_dimensions(matr)
        items=[]
        over_flow=''
        count=0
    
        for i in info:
            items.append(i)
    
        for i in range(height):
            for k in range(width):
                for j in range(length):
                    matr=self.store_item(items[count],i,k,j,matr)
                    
                    count+=1 #might need intention
     
        
        if count != len(items):
            print(count,len(items))
            oflow=items[count:len(items)]
            fin_info=[matr ,''.join(oflow)]
            return fin_info
            
        else:
            return [matr,None]
          
    #=========================================================================
    #=========================================================================
    #=========================================================================

    #=========================================================================
    #=========================================================================
    #=========================================================================
    '''used to get the item held within the 3d coordinates within the matrix'''
    def get_item(self,x,y,z,matr):
        return matr[x][y][z]
    #=========================================================================
    #=========================================================================
    #=========================================================================
    
    #=========================================================================
    #=========================================================================
    #=========================================================================
    def get_channels(self,face,matr):
        
        height,width,length=self.get_matrix_dimensions(matr)
        matrix=matr
        fin_chans=[]
        
        def get_front():
            buf=[]
            for i in range(width):
                for k in range(length):
                    chan=[]
                    for j in range(height):
                        items=matrix[j][i][k]
                        chan.append(items)
                    buf.append(chan)
            return buf
            
        def get_back():
            buf=[]
            for i in range(width):
                for k in range(length):
                    chan=[]
                    k=(length-1)-k
                    for j in range(height):
                        j=(height-1)-j
                        item=matrix[j][i][k]
                        chan.append(item)
                    buf.append(chan)
            return buf
            
        def get_left():
            buf=[]
            chan_resorted=[]
            
            for i in range(height):
                i=(height-1)-i
                for k in range(width):
                    chan=[]
                    for j in range(length):
                        item=matrix[i][k][j] 
                        chan.append(item)
                    buf.append(chan)
            
            for i in range(height):
                section=buf[i:len(buf):height]
                for  k in section:
                    chan_resorted.append(k)
            return chan_resorted
            
        def get_right():
            buf=[]
            chan_resorted=[]
            
            for i in range(height):
                for k in range(width):
                    chan=[]
                    for j in range(length):
                        j=(length-1)-j
                        item=matrix[i][k][j]
                        chan.append(item)
                    buf.append(chan)
            
            for i in range(height):
                section=buf[i:len(buf):height]
                for k in section:
                    chan_resorted.append(k)
            
            return chan_resorted
            
            
        def get_top():
            buf=[]
            for i in range(height):
                i=(height-1)-i
                for k in range(length):
                    chan=[]
                    for j in range(width):
                        item=matrix[i][j][k]
                        chan.append(item)
                    buf.append(chan)
            return buf
            
            
        def get_bottom():
            buf=[]
            for i in range(height):
                for k in range(length):
                    chan=[]
                    for j in range(width):
                        j=(width-1)-j
                        item=matrix[i][j][k]
                        chan.append(item)
                    buf.append(chan)
            return buf
        
            
            
            
            
        
        if face=='front':
            return get_front()
        elif face=='back':
            return get_back()
        elif face=='left':
            return get_left()
        elif face=='right':
            return get_right()
        elif face=='top':
            return get_top()
        elif face=='bottom':
            return get_bottom()
        else:
            print('that is not an option')
                
        return fin_chans
                
        
    
    #=========================================================================
    #=========================================================================
    #=========================================================================
    
    #=========================================================================
    #=========================================================================
    #=========================================================================
    def get_all_channels(self,matr):
        m=matr
        faces=['front','back','left','right','top','bottom']
        fin_chans={}
        for i in faces:
            c=self.get_channels(i,m)
            fin_chans[i]=c
        return fin_chans
    #=========================================================================
    #=========================================================================
    #========================================================================= 

    #=========================================================================
    #=========================================================================
    #=========================================================================
    '''returns a 2 dimensional matrix of the information that is stored on the
       specified face within the 3 dimensional matrix '''
       
    def get_face(self,face,matr):
        work_matrix=matr 
        if face=='front':
            return work_matrix[0]

        elif face=='back':
            return work_matrix[len(work_matrix)-1]

        elif face=='left':
            flipped=self.flip(work_matrix)
            sliced=self.reslice(flipped)
            rev=self.reverse(sliced)
            return rev[0]

        elif face=='right':
            flipped=self.flip(work_matrix)
            sliced=self.reslice(flipped)
            return sliced[len(sliced)-1]

        elif face=='top':
            fin_matrix=self.flip(self.reslice(work_matrix))
            return fin_matrix[0]

        elif face=='bottom':
            fin_matrix=self.flip(self.reslice(work_matrix))
            return fin_matrix[len(fin_matrix)-1]




    #=========================================================================
    #=========================================================================
    #=========================================================================
    
    


#+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
#+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
#+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
#+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++


#+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
#+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
#+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
#+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
class matrix:
    def __init__(self,length,width,height):
        self.length=length
        self.width=width
        self.height=height

        self.matrix_final=[]
        self.matrix_layer=[]

        for i in range(height):
            self.matrix_final.append([])
            for j in range(width):
                self.matrix_final[i].append([])
                for k in range(length):
                    self.info=str(i)+str(j)+str(k)
                    self.matrix_final[i][j].append(self.info)




    '''def write_info(self):
        info=self.get_matrices_info()
        name=self.create_matrix_name()
        info['items'][name]=self.matrix_final
        info['names'].append(name)

        file=open(matrix_file,'w')
        file.write(str(info))
        file.close()'''
    
    #=========================================================================
    #=========================================================================
    #=========================================================================
    def get_matrix(self):
        return self.matrix_final
    #=========================================================================
    #=========================================================================
    #=========================================================================

    #=========================================================================
    #=========================================================================
    #=========================================================================
    def show_matrix(self):
        print('#########################################')
        for i in self.matrix_final:
            print('========================')
            for k in i:
                print(k)
            print('========================')
        print('#########################################')
    #=========================================================================
    #=========================================================================
    #=========================================================================
    

    #=========================================================================
    #=========================================================================
    #=========================================================================
    def replace_matrix(self,new_matrix):
        height=0
        width=0
        length=0
        
        print(len(new_matrix))
        for i in new_matrix:
            height+=1
            
            #for k in i:
            #    width+=1
            #    for j in k:
            #        length+=1
            
                    
        
        
    #=========================================================================
    #=========================================================================
    #=========================================================================



    


#+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
#+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
#+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
#+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++






#+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
#+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
#+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
#+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
#QUARENTINED REASON:cannot remember what it was going to be used
#                   for and how but could serve usefull in the future.
class MIH:  #Matrix Information Handle

    def __init__(self):
        self.base='base_files.txt'

        self.file=open(self.base,'r')
        info=ast.literal_eval(self.file.read())
        self.file.close()


        for i in info:
            path=info[i]

            if not os.path.isfile(path):
                file=open(path,'w')
                file.close()

    #=======================================================================
    #=======================================================================
    #=======================================================================
    '''evaluates the file that is given and returns the evalutated'''
    def eval_file(self,file):
        try:
            file=open(file,'r')
            info=ast.literal_eval(file.read())
            file.close()
            return info
        except:
            print('eval could not be done possibly due to bad formatting/nwith the file provided')
    #=======================================================================
    #=======================================================================
    #=======================================================================
    
    
    #=======================================================================
    #=======================================================================
    #=======================================================================
    def get_current_matrices(self):
        paths=self.get_paths()
        m_path=paths['matrices']
        info=self.eval_file(m_path)
        names=info['names']
        return names
    #=======================================================================
    #=======================================================================
    #=======================================================================
    
    #=======================================================================
    #=======================================================================
    #=======================================================================
    def get_paths(self):
        file=open(self.base,'r')
        info=ast.literal_eval(file.read())
        file.close()
        return info
    #=======================================================================
    #=======================================================================
    #=======================================================================


    #=======================================================================
    #=======================================================================
    #=======================================================================
    def format_auth(self):
        a_path=self.get_paths()['auth_file']
        forma="{'current_tags':[],'used_tags':[],'unused_tags':[]}"

        file=open(a_path,'w')
        file.write(forma)
        file.close()
    #=======================================================================
    #=======================================================================
    #=======================================================================
    
    #=======================================================================
    #=======================================================================
    #=======================================================================
    def get_matrix_dimensions(self,mat):
        height=0
        width=0
        length=0
        
        for i in mat:
            height+=1
        for i in mat[0]:
            width+=1
            
        try:
            for i in mat[0][0]:
                length+=1
        except:
            length=width
            width=height
            height=0
            
        return height,width,length
    #=======================================================================
    #=======================================================================
    #=======================================================================
    
    #=========================================================================
    #=========================================================================
    #=========================================================================
    '''used to get the item held within the 3d coordinates within the matrix'''
    def get_item(self,x,y,z,matr):
        return matr[x][y][z]
    #=========================================================================
    #=========================================================================
    #=========================================================================
    
    
    
    #=======================================================================
    #=======================================================================
    #=======================================================================
    def format_mstates(self):
        paths=self.get_paths()
        path=paths['m_states']
        form="{'primary_state':True}"
        file=open(path,'w')
        file.write(form)
        file.close()
    #=======================================================================
    #=======================================================================
    #=======================================================================
    
    #=======================================================================
    #=======================================================================
    #=======================================================================
    def get_primary_state(self):
        paths=self.get_paths()
        path=paths['m_states']
        info=self.eval_file(path)
        return info['primary_state']
    #=======================================================================
    #=======================================================================
    #=======================================================================
    
    #=======================================================================
    #=======================================================================
    #=======================================================================
    def format_b_files(self):
        self.format_mstates()
        self.format_auth()
    #=======================================================================
    #=======================================================================
    #=======================================================================    


    #^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
    #^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
    #^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
    
    
    #=======================================================================
    #=======================================================================
    #=======================================================================
    '''
    creates a basic matrix name by looking at "matrices.txt" and 
    checking the names that have been used and returning a name
    that currently does not exist
    '''
    def create_matrix_name(self):
        base_name='m_'
        m_file=self.eval_file(self.eval_file(self.base)['matrices'])
        names=m_file['names']
        count=0
        m_name=base_name+str(count)
        
        while m_name in names:
            count+=1
            m_name=base_name+str(count)
            
        return m_name
        
    #=======================================================================
    #=======================================================================
    #=======================================================================
    
    
    #=======================================================================
    #=======================================================================
    #=======================================================================
    
    '''
    creates an authentication key (a randomized key) and returns it: for now 
    the key is not being used but it might be later for authentication purposes
    while configuring the matrices or getting information about a matrix
    '''
    
    def create_auth_key(self):
        
        flag=True
        key_len=16
        final_key=''
        a_info=self.eval_file(self.eval_file(self.base)['auth_file'])
        ch=string.ascii_uppercase+string.punctuation
        
        
        def make_key():
            fin_key=''
            for i in range(key_len):
                fin_key+=ch[random.randrange(len(ch))]
            return fin_key
        
        
        while flag:
            count=0
            mkey=make_key()
            
            for i in a_info:
                if mkey not in a_info[i]:
                    count+=1
            
            
            if count == len(a_info):
                flag=False
                final_key=mkey
                
        return final_key
        
    #=======================================================================
    #=======================================================================
    #=======================================================================
    
    
    #=======================================================================
    #=======================================================================
    #=======================================================================
    def get_matrix_info(self,matrix_name):
        paths=self.get_paths()
        m_path=paths['matrices']
        info=self.eval_file(m_path)
        mat=info['items'][matrix_name]['matrix']
        flags=info['flag_status'][matrix_name]
        
        return [mat,flags]
    #=======================================================================
    #=======================================================================
    #=======================================================================
    
    #=======================================================================
    #=======================================================================
    #=======================================================================
    '''formats the matrices file "matrices.txt"'''
    def matrices_format(self):
        matrix_form="{'names':[],'items':{},'flag_status':{}}"
        file=open(matrix_file,'w')
        file.write(matrix_form)
        file.close()
        
    #=======================================================================
    #=======================================================================
    #=======================================================================
    
    #=======================================================================
    #=======================================================================
    #=======================================================================
    def get_matrix_face(self,face,matr):
        
        height,width,length=self.get_matrix_dimensions(matr)
        
        if face=='front':
            return matr[0]
        elif face=='back':
            return matr[height-1]
        elif face=='right':
            fm=[]
            
            for i in range(width):
                fm.append([])
            for i in range(height):
                
                for j in range(width):
                    item=matr[i][j][length-1]
                    fm[j].append(item)
            
            return fm
                
        elif face=='left':
            fm=[]
            
            for i in range(width):
                fm.append([])
            for i in range(height):
                
                for j in range(width):
                    item=matr[i][j][0]
                    fm[j].append(item)
            
            return fm
        elif face=='top':
            fm=[]
            
            for i in range(height):
                fm.append([])
            for i in range(height):
                i_2=(height-1)-i
                for j in range(length):
                    item=matr[i][0][j]
                    fm[i_2].append(item)
            return fm
            
        elif face=='bottom':
            fm=[]
            
            for i in range(height):
                fm.append([])
            for i in range(height):
                for j in range(length):
                    item=matr[i][width-1][j]
                    fm[i].append(item)
            
            return fm
                    

    #=======================================================================
    #=======================================================================
    #=======================================================================
    
    #=======================================================================
    #=======================================================================
    #=======================================================================
    def create_flag_layer(self,mt):
        matr=mt
        flag_layer={}
        faces=['front','back','right','left','top','bottom']
        
        
        for i in faces:
            
            fholder={}
            face=self.get_matrix_face(i,matr)
            h,w,l=self.get_matrix_dimensions(face)
            
            for k in range(w):
                for j in range(l):
                    fholder[face[k][j]]=[False,[None,None,None]] #[ is connected , [ matrix connected to , face , section ] ]
            flag_layer[i]=fholder
        
            
        return flag_layer
        
            
            
            
        #height,width,length=self.get_matrix_dimensions(matr)
        
    #=======================================================================
    #=======================================================================
    #=======================================================================

    #=======================================================================
    #=======================================================================
    #=======================================================================
    '''adds matrix information to the "matrices.txt" file'''
    def add_new_matrix(self,mat,channels):
        paths=self.eval_file(self.base)
        mat_path=paths['matrices']
        m_file=self.eval_file(mat_path)
        m_name=self.create_matrix_name()
        m_key=self.create_auth_key()
        flag_layer=self.create_flag_layer(mat)
        chans=channels
        
        
        fin_info={'auth_key':m_key,'matrix':mat,'channels':chans}
        m_file['names'].append(m_name)
        m_file['items'][m_name]=fin_info
        m_file['flag_status'][m_name]=flag_layer
        
        
        
        file=open(mat_path,'w')
        file.write(str(m_file))
        file.close()
        
    #=======================================================================
    #=======================================================================
    #=======================================================================
        
        
    
    #^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
    #^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
    #^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^


#+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
#+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
#+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
#+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++




#+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
#+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
#+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
#+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
class matrix_connector(MIH):
    def __init__(self):
        MIH.__init__(self)
        #print(self.get_current_matrices())
        names=self.get_current_matrices()
        info=self.get_matrix_info(names[0])
    
    def connect_matrices(self,m1_name,m2_name,m1_face,con_mode,m2_face=None,con_dir=None,dimen=None):
            #con_mode='connection_mode'
            #con_dir='connection_direction'
            #dimen='dimensions'
            
            
            
            
            
            
            matrix_one_info=self.get_matrix_info(m1_name) 
            matrix_two_info=self.get_matrix_info(m2_name)
            
            
            
            mt1_matr=matrix_one_info[0]
            mt1_flags=matrix_one_info[1]
            mt2_matr=matrix_two_info[0]
            mt2_flags=matrix_two_info[1]
            
            height1,width1,length1 = self.get_matrix_dimensions(mt1_matr)
            height2,width2,length2 = self.get_matrix_dimensions(mt2_matr)
            
            
            def convert_to_list_seg():
                
                for i in range(int(len(m1_con_names)/height1)):
                        name_buf.append(m1_con_names[start:end])
                        
                        start+=height1
                        if end+height1>len(m1_con_names):
                            end=len(m1_con_names)
                        else:
                            end+=height1
            
            
            if con_mode == 'full':
                if m1_face=='top':
                    if m2_face=='bottom' or m2_face == None:
                        
                        m1_top_flags=mt1_flags[m1_face]
                        m2_bot_flags=mt2_flags[m2_face]
                        
                        m1_con_names=[i for i in m1_top_flags]
                        m2_con_names=[i for i in m2_bot_flags]
                        
                        name_buf=[]
                        paired=[[] for i in range(len(m1_top_flags))]
                        
                        start=0
                        end=height1
                        
                        
                        
                                    
                        m1_con_names=name_buf
                        name_buf=[]
                        
                        
                        
                        
                        
                        
                        
                        
                        #print(m1_face)
                        #for i in m1_top_flags:
                        #    print(i,m1_top_flags[i])
                        #print('--')
                        #print(m2_face)
                        #for i in m2_bot_flags:
                        #    print(i,m2_bot_flags[i])
                    
                    else:
                        print(m2_face,'is not a valid option for')
                
            
            
            
            
            
            



#+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
#+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
#+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
#+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++

#+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
#+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++=======================TEST SECTION
#+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
#+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++

length=3
width=3
height=3
total=length*width*height
test_info=[]

for i in range(total):
    test_info.append(i)




handler=MIH()
mdisplay=matrix_display()
manip=matrix_manip()
connect=matrix_connector()

cube_one=matrix(length,width,height)
cube_two=matrix(length,width,height)


c1_mat=manip.store_info(test_info,cube_one.get_matrix())[0]
c2_mat=manip.store_info(test_info,cube_two.get_matrix())[0]


handler.matrices_format()
handler.add_new_matrix(c2_mat,manip.get_all_channels(c2_mat))
handler.add_new_matrix(c1_mat,manip.get_all_channels(c1_mat))


names=handler.get_current_matrices()

connect.connect_matrices(names[0],names[1],'top','full',m2_face='bottom')



    



#cube2=matrix(length,width,height)
#cube.write_info()
#print(cube.get_matrices_info())

#+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
#+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
#+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
#+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++








