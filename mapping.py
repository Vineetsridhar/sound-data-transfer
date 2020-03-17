class MyMapping:
    def itoa(self, num, base) : 
        ret = ""
        if (num == 0): 
            return "0"
        while (num != 0): 
            ret = str(num % base) + ret
            num = int(num / base)  
        return ret
    
    def decoder(self, n) : 
        letters = " abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789"
        dic = {}
        for i in range(n + 1) :  
            dic["{}".format(self.itoa(i, 2)).zfill(6)] = letters[i]
        return dic

    def __init__(self):
        self.mapping = self.decoder(62)
