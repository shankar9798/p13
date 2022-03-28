var bow , arrow,  background, arrowGroup, redB, pinkB, greenB, blueB;

var bowImage, arrowImage, green_balloonImage, red_balloonImage, pink_balloonImage ,blue_balloonImage, backgroundImage;

function preload(){
  
  backgroundImage = loadImage("background0.png");
  arrowImage = loadImage("arrow0.png");
  bowImage = loadImage("bow0.png");
  red_balloonImage = loadImage("red_balloon0.png");
  green_balloonImage = loadImage("green_balloon0.png");
  pink_balloonImage = loadImage("pink_balloon0.png");
  blue_balloonImage = loadimage("blue_balloon0.png");
  
}



function setup() {
  createCanvas(600, 600);
  
  //creating background
  background = createSprite(0,0,600,600);
  background.addImage(backgroundImage);
  background.scale = 2.5
  
  // creating bow to shoot arrow
  bow = createSprite(480,220,20,50);
  bow.addImage(bowImage); 
  bow.scale = 1;

  score = 0 
  redB = new Group();
  greenB = new Group();
  blueB = new Group();
  pinkB = new Group();
  arrowGroup = new Group();

}

function draw() {
 background(0);
  // moving ground
    background.velocityX = -3 

    if (background.x < 0){
      background.x = background.width/2;
    }
  
  //moving bow
  bow.y = World.mouseY
  
   // release arrow when space key is pressed
  if (keyDown("space")) {
    createArrow();
    
  }
  
  //creating continous balloons
  var select_balloon = Math.round(random(1,4));
  
  if (World.frameCount % 100 == 0) {
    if (red_balloon == 1) {
      redBalloon();
    } else if (green_balloon == 2) {
      greenBalloon();
    } else if (pink_balloon == 3) {
      pinkBalloon();
    } else if (blue_balloon == 4) {
      blueBalloon();
    }
  }
  if (arrowGroup.isTouching(redB)) {
    redB.destroyEach();
    arrowGroup.destroyEach();
    score=score+1;
  }
  if (arrowGroup.isTouching(greenB)) {
    greenB.destroyEach();
    arrowGroup.destroyEach();
    score=score+3;

  }
  if (arrowGroup.isTouching(blueB)) {
    blueB.destroyEach();
    arrowGroup.destroyEach();
    score=score+2;
  }
  if (arrowGroup.isTouching(pinkB)) {
    pinkB.destroyEach();
    arrowGroup.destroyEach();
    score=score+1;
  }






  drawSprites();
  text("score:" + score,500,50);
}


// Creating  arrows for bow
 function createArrow() {
  var arrow= createSprite(100, 100, 60, 10);
  arrow.addImage(arrowImage);
  arrow.x = 360;
  arrow.y=bow.y;
  arrow.velocityX = -4;
  arrow.lifetime = 100;
  arrow.scale = 0.3;
  arrowGroup.add(arrow);
}


function redBalloon() {
  var red = createSprite(0,Math.round(random(20, 370)), 10, 10);
  red.addImage(red_balloonImage);
  red.velocityX = 3;
  red.lifetime = 150;
  red.scale = 0.1;
  redB.add(red);

}

function blueBalloon() {
  var blue=
  createSprite(0,Math.random(random(20,370)),10,10);
  blue.addImage(blue_balloonImage);
  blue.velocityX = 4;
  blue.lifetime = 150;
  blue.scale = 0.1;
  blueB.add(blue);
  //write code for spwaning blue balloons
}

function greenBalloon() {

  var green=
  createSprite(0,Math.random(random(20,370)),10,10);
  green.addImage(blue_balloonImage);
  green.velocityX = 4;
  green.lifetime = 150;
  green.scale = 0.1;
  blueB.add(blue);
  //write code for spwaning green balloons
}

function pinkBalloon() {
  
  var pink=
  createSprite(0,Math.random(random(20,370)),10,10);
  pink.addImage(blue_balloonImage);
  pink.velocityX = 4;
  pink.lifetime = 150;
  pink.scale = 0.1;
  pinkB.add(pink);
  //write code for spwaning pink balloons
}















