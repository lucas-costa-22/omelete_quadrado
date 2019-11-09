raio = 10
px, py = 200, 200

def setup(): #comeco do setup e posicao
    global px, py, vx, vy
    size(450, 450)
    vx = random(-4, 4)
    vy = random(-4, 4)
       
def draw(): #desenho
    global px, py, vx, vy
    background(255, 0, 0)
    omelete(px, py, 100, color(random(255),
                            random(255),
                            random(255)))
    px = px + vx
    py = py + vy
    if px > width - raio or px < raio:
        vx = -vx
    if py > height - raio or py < raio:
        vy = -vy
         
def omelete(x, y, largura, cor): #definicoes do omelete
    noStroke()
    fill(255)
    rectMode(CENTER)
    rect(x, y, largura, largura)
    fill(cor)
    circle(x, y, largura / 2)
    fill(0)
    circle(x, y, largura / 6)
