from reportlab.platypus import Flowable

class tick(Flowable):

    def __init__(self, w1, h1, s, t, w, color='black'):
        Flowable.__init__(self)
        self.w1 = w1
        self.h1 = h1
        self.s = s
        self.t = t
        self.w = w
        self.color = color
        
    def draw(self):
        s = float(self.s)
        self.canv.rect(self.w1, self.h1, self.w1 + s, self.h1 - s)
        if self.t == 1:
            self.canv.setStrokeColor(self.color)
            self.canv.setLineWidth(self.w)
            self.canv.line(self.w1+(s*0.15), self.h1-(s*0.35), self.w1+(s*0.35), self.h1-(s*0.15))
            self.canv.line(self.w1+(s*0.35), self.h1-(s*0.15), self.w1+(s*0.85), self.h1-(s*0.85))
            
            
class tick_2(Flowable):

    def __init__(self, x1, y1, x2, y2, t, w, color='black'):
        Flowable.__init__(self)
        self.x1 = x1
        self.y1 = y1
        self.x2 = x2
        self.y2 = y2
        self.t = t
        self.w = w
        self.d1 = float(abs(x1 - x2))
        self.d2 = float(abs(y1 - y2))
        self.color = color
        
    def draw(self):
        self.canv.rect(self.x1, self.y1, self.x2, self.y2)
        if self.t == 1:
            self.canv.setStrokeColor(self.color)
            self.canv.setLineWidth(self.w)
            self.canv.line(self.x1 + (self.d1 * 0.15), self.y1 + (self.d2 * 0.55),
                           self.x1 + (self.d1 * 0.35), self.y1 + (self.d2 * 0.25))
            self.canv.line(self.x1 + (self.d1 * 0.35), self.y1 + (self.d2 * 0.25),
                           self.x1 + (self.d1 * 0.85), self.y1 + (self.d2 * 1.05))
            

class line(Flowable):

    def __init__(self, w1, h1, w2, h2, color):
        Flowable.__init__(self)
        self.w1 = w1
        self.h1 = h1
        self.w2 = w2
        self.h2 = h2
        self.color = color
 
    def draw(self):
        self.canv.setStrokeColor(self.color)
        self.canv.line(self.w1, self.h1, self.w2, self.h2)

class square(Flowable):

    def __init__(self, w1, h1, w2, h2, s, color):
        Flowable.__init__(self)
        self.w1 = w1
        self.h1 = h1
        self.w2 = w2
        self.h2 = h2
        self.s = s
        self.color = color
 
    def draw(self):
        self.canv.setStrokeColor(self.color)
        self.canv.setLineWidth(self.s)
        self.canv.rect(self.w1, self.h1, self.w2, self.h2)
        
class semi_square(Flowable):

    def __init__(self, wo, ho, wup, hup, wl, hl, s, color):
        Flowable.__init__(self)
        self.wo = wo
        self.ho = ho
        self.wup = wup
        self.hup = hup
        self.wl = wl
        self.hl = hl
        self.s = s
        self.color = color
 
    def draw(self):
        self.canv.setStrokeColor(self.color)
        self.canv.setLineWidth(self.s)
        self.canv.line(self.wo, self.ho, self.wup, self.hup)
        self.canv.line(self.wo, self.ho, self.wl, self.hl)
