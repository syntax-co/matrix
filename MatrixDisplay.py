#+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
#+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
#+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
#+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
class matrix_display:
    
    
    #=========================================================================
    #=========================================================================
    #=========================================================================
    def display_matrix(self, mtrx,reverse=False):
        print('#########################################')
        for i in range(len(mtrx)):
            if reverse:
                i=(len(mtrx)-1)-i
            layer=mtrx[i]
            print('========================')
            for k in layer:
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