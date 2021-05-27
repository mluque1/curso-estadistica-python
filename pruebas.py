class Student:
    def __init__(self, name):
        self.name = name

def pi_converter(st):
    if(st.isnumeric()):
        return int(st)
    return len(st)

def text_to_pi():
    initial_string = 'Con 1 flor y 5 mariposas se pueden hacer mil cosas'.split(' ')
    list_pi = list(map(pi_converter, initial_string))
    st = ''
    for digit in list_pi:
        st += str(digit)
    st = st[0:1] + '.' + st[1:]
    print(st)

if __name__ == '__main__':
    text_to_pi()
    


