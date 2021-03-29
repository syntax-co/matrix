import math

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
    
    def get_slices(self,mat,sdirect):
        
        height,width,length=self.get_matrix_dimensions(mat)
        fin_matrix=[]
        
        
        # /*\/*\/*\/*\/*\/*\/*\/*\/*\/*\/*\/*\/*\/*\
        if sdirect=='front':
            return mat
        # /*\/*\/*\/*\/*\/*\/*\/*\/*\/*\/*\/*\/*\/*\
        
        # /*\/*\/*\/*\/*\/*\/*\/*\/*\/*\/*\/*\/*\/*\
        elif sdirect=='back':
            
            d1=height
            d2=width
            d3=length
            
            for i in range(d1):
                
                i=(d1-1)-i
                
                buf=[[] for k in range(d2)]
                for k in range(d2):
                    for j in range(d3):
                        
                        j=(d3-1)-j
                        
                        item=mat[i][k][j]
                        buf[k].append(item)
                fin_matrix.append(buf)
        # /*\/*\/*\/*\/*\/*\/*\/*\/*\/*\/*\/*\/*\/*\
        
        # /*\/*\/*\/*\/*\/*\/*\/*\/*\/*\/*\/*\/*\/*\        
        elif sdirect=='left':
            
            d1=length
            d2=width
            d3=height
            
            for i in range(d1):
                
                buf=[[] for k in range(d2)]
                for k in range(d2):
                    for j in range(d3):
                        
                        j=(d3-1)-j
                        
                        item=mat[j][k][i]
                        buf[k].append(item)
                fin_matrix.append(buf)
        # /*\/*\/*\/*\/*\/*\/*\/*\/*\/*\/*\/*\/*\/*\
                
        # /*\/*\/*\/*\/*\/*\/*\/*\/*\/*\/*\/*\/*\/*\
        elif sdirect=='right':
            
            d1=length
            d2=width
            d3=height
            
            for i in range(d1):
                i=(d1-1)-i
                buf=[[] for k in range(d2)]
                for k in range(d2):
                    for j in range(d3):
                        
                        item=mat[j][k][i]
                        buf[k].append(item)
                fin_matrix.append(buf)
        # /*\/*\/*\/*\/*\/*\/*\/*\/*\/*\/*\/*\/*\/*\
        
        # /*\/*\/*\/*\/*\/*\/*\/*\/*\/*\/*\/*\/*\/*\
        elif sdirect=='top':
            
            d1=width
            d2=height
            d3=length
            
            
            for i in range(d1):
                buf=[[] for k in range(d2)]
                for k in range(d2):
                    # k=(d2-1)-k
                    for j in range(d3):
                        item=mat[k][i][j]
                        buf[(d2-1)-k].append(item)
                fin_matrix.append(buf)
        # /*\/*\/*\/*\/*\/*\/*\/*\/*\/*\/*\/*\/*\/*\
        
        # /*\/*\/*\/*\/*\/*\/*\/*\/*\/*\/*\/*\/*\/*\    
        elif sdirect=='bottom':
            
            d1=width
            d2=height
            d3=length
            
            for i in range(d1):
                i=(d1-1)-i
                buf=[[] for i in range(d2)]
                for k in range(d2):
                    for j in range(d3):
                        item=mat[k][i][j]
                        buf[k].append(item)
                fin_matrix.append(buf)
        # /*\/*\/*\/*\/*\/*\/*\/*\/*\/*\/*\/*\/*\/*\
            
            
        if len(fin_matrix)>0:
            return fin_matrix
        else:
            print('No Matrix to Return')
        
        
        
            
            
    def rotate(self,matrix,dire):
        # self.get_matrix_dimensions(matr)
        show=matrix_display()
        w_matrix=matrix
        
        def get_next_position(dex,size,direction):
            
            if direction=='clock_wise':
                start=size-1
                step=dex*start
                floor=int(dex//size)
                drop=((size**2)-(size-2))+start
                final=start + (step-(drop*floor))
                return final
                
                
            elif direction=='clock_counter':
                start=(size**2)-size
                step=dex*(size+1)
                floor=int(dex//size)
                drop=(size**2)+1
                final=(start-step)+(drop*floor)
                return final
                
        def rotate_layer(lay,direction,msize):
            layer_list=self.get_list(lay)
            
            post_list=[None for i in range(len(layer_list))]
            
            for i in range(len(layer_list)):
                item=layer_list[i]
                change=get_next_position(i,msize,direction)
                ndex=i+change
                post_list[ndex]=item
                
            post_lay=self.turn_list(post_list)
            return post_lay
                
            
        dire="Front"
        
        if dire=='clock-wise':
            for i in range(len(w_matrix)):
                
                l_dim=len(w_matrix)
                prelayer=w_matrix[i]
                postlayer=rotate_layer(prelayer,'clock_wise',l_dim)
                w_matrix[i]=postlayer
        
        if dire=='clock-counter':
            for i in range(len(w_matrix)):
                l_dim=len(w_matrix)
                prelayer=w_matrix[i]
                postlayer=rotate_layer(prelayer,'clock_counter',l_dim)
                w_matrix[i]=postlayer
                
        if dire=='Left':
            sliced=self.get_slices(w_matrix,'top')
            
            for i in range(len(sliced)):
                l_dim=len(sliced)
                prelayer=sliced[i]
                postlayer=rotate_layer(prelayer,'clock_wise',l_dim)
                sliced[i]=postlayer
            resliced=self.get_slices(sliced,'bottom')
            w_matrix=resliced
        
        if dire=='Right':
            sliced=self.get_slices(w_matrix,'top')
            
            for i in range(len(sliced)):
                l_dim=len(sliced)
                prelayer=sliced[i]
                postlayer=rotate_layer(prelayer,'clock_counter',l_dim)
                sliced[i]=postlayer
            resliced=self.get_slices(sliced,'bottom')
            w_matrix=resliced
            
        if dire=='Front':
            sliced=self.get_slices(w_matrix,'left')
            
            for i in range(len(sliced)):
                l_dim=len(sliced)
                prelayer=sliced[i]
                postlayer=rotate_layer(prelayer,'clock_wise',l_dim)
                sliced[i]=postlayer
            resliced=self.get_slices(sliced,'right')
            w_matrix=resliced
            
            
        if dire=='Back':
            sliced=self.get_slices(w_matrix,'left')
        
            for i in range(len(sliced)):
                l_dim=len(sliced)
                prelayer=sliced[i]
                postlayer=rotate_layer(prelayer,'clock_counter',l_dim)
                sliced[i]=postlayer
            resliced=self.get_slices(sliced,'right')
            w_matrix=resliced
            
        return w_matrix
            
            
        
        
        
        
    
    #=========================================================================
    #=========================================================================
    #=========================================================================
    '''this function rotates the 3 dimensional matrix (not transpose)
       the matrix for now only supports a matrix with all sizes being equal
       such as in the case of a 3x3x3 matrix'''
    def old_rotate(self,direction,matr): #v1
        
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
            return rot_left(og)
        elif direction=='right':
            return rot_right(og)
        elif direction=='front':
            return rot_front(og)
        elif direction=='back':
            return rot_back(og)
        elif direction=='clock_wise':
            return rot_clock_wise(og)
        elif direction=='clock_counter':
            return rot_clock_counter(og)
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
    def get_difference(self,matrix_list1,matrix_list2):
        m1=matrix_list1
        m2=matrix_list2
        
        dif_list=[]
        
        for i in range(len(m1)):
            item1=m1[i]
            for m in range(len(m2)):
                item2=m2[m]
                
                
                if item1==item2:
                    dif_list.append(m-i)
                    
        return dif_list
    
    #=========================================================================
    #=========================================================================
    #=========================================================================
    
    
    
    #=========================================================================
    #=========================================================================
    #=========================================================================
    def get_list(self,layer):
        final_list=[]
        
        for i in layer:
            for k in i:
                final_list.append(k)
        
        return final_list
        
    #=========================================================================
    #=========================================================================
    #========================================================================= 
    
    
    #=========================================================================
    #=========================================================================
    #========================================================================= 
    def turn_list(self,lis):
        dim=int(math.sqrt(len(lis)))
        net=[]
        start=0
        end=dim
        
        for i in range(dim):
            section=lis[start:end]
            net.append(section)
            start+=dim
            end+=dim
        
        return net
        
        
        
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


