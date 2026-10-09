import curses,time,random
from ui import put,run
class Game:
 def __init__(self,seed=None):self.rng=random.Random(seed);self.level=1;self.score=0;self.lives=3;self.paddle=.5;self.new_level()
 def new_level(self):self.bricks={(r,c) for r in range(min(5,2+self.level)) for c in range(10)};self.reset()
 def reset(self):self.x=.5;self.y=.78;self.vx=self.rng.choice((-.18,.18));self.vy=-.35;self.waiting=True
 def launch(self):self.waiting=False
 def step(self,dt,move=0):
  dt=max(0,min(.05,dt));self.paddle=max(.1,min(.9,self.paddle+move*.8*dt))
  if self.waiting or self.lives<=0:return
  self.x+=self.vx*dt;self.y+=self.vy*dt
  if self.x<.02:self.x=.02;self.vx=abs(self.vx)
  if self.x>.98:self.x=.98;self.vx=-abs(self.vx)
  if self.y<.04:self.y=.04;self.vy=abs(self.vy)
  if self.vy>0 and .87<=self.y<=.93 and abs(self.x-self.paddle)<=.11:
   self.y=.87;self.vy=-abs(self.vy);self.vx=(self.x-self.paddle)*2.4
   if abs(self.vx)<.08:self.vx=self.rng.choice((-.08,.08))
  if self.y>1:self.lives-=1;self.reset();return
  row=int((self.y-.12)/.045);col=int(self.x*10)
  if self.y>=.12 and (row,col) in self.bricks:
   self.bricks.remove((row,col));self.vy=-self.vy;self.score+=10*self.level
   if not self.bricks:self.level+=1;self.new_level()
def loop(s):
 s.timeout(50);g=Game();last=time.monotonic();paused=False
 while True:
  frame_start=time.monotonic()
  now=time.monotonic();dt=now-last;last=now;h,w=s.getmaxyx();k=s.getch();s.erase()
  if k in (ord('q'),ord('Q')):return
  if k in (ord('r'),ord('R')):g=Game()
  if k in (ord('p'),ord('P')):paused=not paused
  if k==32:g.launch()
  playable=h>=24 and w>=60
  move=-1 if k in (curses.KEY_LEFT,ord('a')) else 1 if k in (curses.KEY_RIGHT,ord('d')) else 0
  if playable and not paused:
   # Keyboard events need useful movement independent of render tick timing.
   if move:g.paddle=max(.1,min(.9,g.paddle+move*.055))
   g.step(dt,0)
  put(s,1,2,'S H A R D O V Y R R I X',curses.A_BOLD);put(s,2,2,'Level '+str(g.level)+' | Score '+str(g.score)+' | Lives '+str(g.lives))
  if not playable:put(s,4,2,'Resize to60x24. Paused.')
  else:
   top=4;height=h-8;width=w-4
   for r,c in g.bricks:put(s,top+int((.12+r*.045)*height),2+int(c/10*width),'█'*max(1,width//10-1),curses.color_pair(1+r%4))
   put(s,top+int(.9*height),max(2,int(2+(g.paddle-.1)*width)),'▀'*max(4,int(width*.2)),curses.color_pair(2))
   put(s,top+min(height-1,int(g.y*height)),2+int(g.x*width),'●',curses.color_pair(4))
   put(s,h-3,2,'Game over. R restart.' if g.lives<=0 else 'Paused. P resumes.' if paused else 'Space launches ball.' if g.waiting else 'Break every brick to advance.')
  put(s,h-2,2,'A/D or arrows paddle | Space launch | P pause | R reset | Q quit');s.refresh()
  # Key-repeat must not bypass the network-friendly frame cap.
  time.sleep(max(0,.05-(time.monotonic()-frame_start)))
if __name__=='__main__':raise SystemExit(run(loop))
