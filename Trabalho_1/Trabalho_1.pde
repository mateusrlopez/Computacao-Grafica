boolean drag = false;

float ballx = 50.0;
float bally = 150.0;

float ballRadius = 40.0;

float ballxSpeed = 1;
float ballySpeed = 2;

float p2x = 70;
float p2y = 10;

void setup() {
    size(900,900);
    frameRate(60);

    // (1,1)
    fill(128, 128, 128);
    rect(0, 0, 300, 300);
    
    // (1,2)
    fill(255, 224, 32);
    rect(300, 0, 300, 300);
    
    // (1,3)
    fill(255, 160, 16);
    rect(600, 0, 300, 300);
  
    // (2,1)
    fill(160, 32, 255);
    rect(0, 300, 300, 300);
    
    // (2,2)
    fill(255, 96, 208);
    rect(300, 300, 300, 300);
    
    // (2,3)
    fill(255, 0, 0);
    rect(600, 300, 300, 300);

    // (3,1)
    fill(0, 255, 0);
    rect(0, 600, 300, 300);
    
    // (3,2)
    fill(160, 128, 96);
    rect(300, 600, 300, 300);
    
    // (3,3)
    fill(0, 0, 255);
    rect(600, 600, 300, 300);
}

void draw() {
    // Questão A
    fill(128, 128, 128);
    rect(0, 0, 300, 300);

    translate(150, 150);

    float radius = 300 * 0.4;
    float sides = 3 + frameCount / 120 % 10;
    float theta = TWO_PI / sides;

    beginShape();

    for (int i = 0; i < sides; i++) {
        float x = radius * cos(theta * i);
        float y = radius * sin(theta * i);

        vertex(x, y);
    }

    endShape(CLOSE);

    translate(-150, -150);

    // Questão B
    fill(255, 224, 32);
    rect(300, 0, 300, 300);

    translate(300, 0);

    float ax = 0.0;
    float ay = 150.0;

    float bx = 300.0;
    float by = 150.0;

    koch(ax, ay, bx, by, 5);

    translate(-300, 0);

    // Questão C
    fill(255, 160, 16);
    rect(600, 0, 300, 300);

    translate(600, 150);

    float sunRadius = 60.0;
    float earthRadius = 40.0;
    float moonRadius = 20.0;

    float earthAngle = TWO_PI * frameCount / 1200;
    float moonAngle = TWO_PI * frameCount / 300 - earthAngle;

    pushMatrix();

    translate(150, 0);

    fill(250, 253, 15);
    circle(0, 0, sunRadius);

    pushMatrix();
    
    rotate(earthAngle);

    translate(90, 0);

    fill(0, 32, 255);
    circle(0, 0, earthRadius);

    pushMatrix();
    
    rotate(moonAngle);

    translate(40, 0);

    fill(194, 197, 204);
    circle(0, 0, moonRadius);

    popMatrix();

    popMatrix();

    popMatrix();

    translate(-600, -150);
    
    // Questão D
    if (frameCount % 1200 == 0) {
        fill(160, 32, 255);
        rect(0, 300, 300, 300); 
    }
    
    translate(0, 450);
    
    pushMatrix();

    translate(150, 0);

    pushMatrix();
    
    rotate(earthAngle);

    translate(90, 0);

    pushMatrix();
    
    rotate(moonAngle);

    translate(40, 0);

    fill(0, 0, 0);
    circle(0, 0, moonRadius);

    popMatrix();

    popMatrix();

    popMatrix();
    
    translate(0, -450);
    
    // Questão E
    if (frameCount % 600 == 0) {
        fill(255, 96, 208);
        rect(300, 300, 300, 300); 
    }
    
    translate(300, 450);
    
    moonRadius = 40.0;
    
    earthAngle = TWO_PI * frameCount / 600;
    moonAngle = TWO_PI * frameCount / 100 - earthAngle;
    
    pushMatrix();

    translate(150, 0);

    pushMatrix();
    
    rotate(earthAngle);

    translate(90, 0);

    pushMatrix();
    
    rotate(moonAngle);

    translate(40, 0);

    fill(0, 0, 0);
    circle(0, 0, moonRadius);

    popMatrix();

    popMatrix();

    popMatrix();
    
    translate(-300, -450);
    
    // Questão F
    translate(750, 450);
    
    float u = frameCount / 100.0;
    
    float ux = 35 * cos(u) * (exp(cos(u)) - 2 * cos(4 * u) - sin(pow(u / 12, 5)));
    float uy = 35 * sin(u) * (exp(cos(u)) - 2 * cos(4 * u) - sin(pow(u / 12, 5)));
    
    circle(ux, uy, 5);
    
    translate(-750, -450);
    
    // Questão G
    translate(150, 750);
    
    translate(-150, -750);
    
    // Questão H
    fill(160, 128, 96);
    rect(300, 600, 300, 300);
    
    translate(300, 600);
    
    float p1x = 10;
    float p1y = 150;

    if (drag) {
       p2x = min(max(mouseX - 300, 0), 300);
       p2y = min(max(mouseY - 600, 0), 300);
    }

    float p3x = 290;
    float p3y = 150;

    bezier(p1x, p1y, p2x, p2y, p3x, p3y);
    
    translate(-300, -600);
    
    fill(0, 0, 255);
    rect(600, 600, 300, 300);
    
    translate(600, 600);
    
    ballx += ballxSpeed;
    bally += ballySpeed;
    
    if (ballx <= 20 || ballx >= 280) {
       ballxSpeed *= -1; 
    }
    
    if (bally <= 20 || bally >= 280) {
       ballySpeed *= -1; 
    }
    
    circle(ballx,bally,ballRadius);
    
    translate(-600, -600);
}

void koch(float ax, float ay, float bx, float by, int rounds) {
    if (rounds == 0) {
        line(ax, ay, bx, by);
        return;
    }

    float theta = PI / 3;

    float cx = (bx - ax) / 3 + ax;
    float cy = (by - ay) / 3 + ay;
    
    float ex = (bx - ax) * 2 / 3 + ax;
    float ey = (by - ay) * 2 / 3 + ay;

    float dx = ((ex - cx) * cos(theta) + (ey - cy) * sin(theta)) + cx;
    float dy = ((ey - cy) * cos(theta) - (ex - cx) * sin(theta)) + cy;

    koch(ax, ay, cx, cy, rounds - 1);
    koch(cx, cy, dx, dy, rounds - 1);
    koch(dx, dy, ex, ey, rounds - 1);
    koch(ex, ey, bx, by, rounds - 1);
}

void bezier(float p1x, float p1y, float p2x, float p2y, float p3x, float p3y) {
    noFill();
    beginShape();
    vertex(p1x, p1y);
    
    for(float t = 0; t <= 1; t += 0.05)
    {
      float ax = p1x + t * (p2x - p1x);
      float bx = p2x + t * (p3x - p2x);
      float cx = ax + t * (bx - ax);
      float ay = p1y + t * (p2y - p1y);
      float by = p2y + t * (p3y - p2y);
      float cy = ay + t * (by - ay);

      vertex(cx,cy);  
    }

    vertex(p3x, p3y);
    
    endShape(CLOSE);
}

void mousePressed() {
    drag = true;
}

void mouseReleased() {
   drag = false; 
}
