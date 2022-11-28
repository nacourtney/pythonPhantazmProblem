import graphics as g

win = g.GraphWin("Welcome Home", 500, 500)

houseBrown = (g.color_rgb(150, 103, 85))
roofBrown = (g.color_rgb(79, 56, 47))

daySky = g.Rectangle(g.Point(0, 0), g.Point(500, 160))
daySky.setFill('skyBlue')
daySky.setWidth(0)
daySky.draw(win)

grass = g.Rectangle(g.Point(0, 160), g.Point(500, 500))
grass.setFill('darkgreen')
grass.setWidth(0)
grass.draw(win)

street = g.Rectangle(g.Point(0, 375), g.Point(500, 500))
street.setFill('gray')
street.setWidth(0)
street.draw(win)

streetLine = g.Line(g.Point(15, 435), g.Point(55, 435))
streetLine.setWidth(6)
streetLine.setFill("white")
streetLine.draw(win)

currentStreetLine = streetLine
for i in range(6):
    currentStreetLine = currentStreetLine.clone()
    currentStreetLine.move(80, 0)
    currentStreetLine.draw(win)

frontWall = g.Rectangle(g.Point(100, 200), g.Point(300, 325))
frontWall.setFill(houseBrown)
frontWall.draw(win)

address = g.Text(g.Point(200, 260), "2317")
address.draw(win)

centerRoofPoint = g.Point(200, 130)

roof = g.Polygon(g.Point(100, 200), centerRoofPoint, g.Point(300, 200))
roof.setFill(houseBrown)
roof.draw(win)

roofSide = g.Polygon(centerRoofPoint, g.Point(300, 200),
                     g.Point(430, 160), g.Point(330, 90),)
roofSide.setFill(roofBrown)
roofSide.draw(win)

sideWall = g.Polygon(g.Point(300, 200), g.Point(430, 160),
                     g.Point(430, 270), g.Point(300, 325))
sideWall.setFill(houseBrown)
sideWall.draw(win)

sideWindow = g.Polygon(g.Point(330, 218), g.Point(
    350, 210), g.Point(350, 275), g.Point(330, 285))
sideWindow.setFill('white')
sideWindow.setWidth(3)
sideWindow.draw(win)

sideWindowVertical = g.Line(g.Point(340, 215), g.Point(340, 282))
sideWindowVertical.setWidth(2)
sideWindowVertical.draw(win)

sideWindowHorizontal = g.Line(g.Point(330, 255), g.Point(350, 245))
sideWindowHorizontal.setWidth(2)
sideWindowHorizontal.draw(win)

rightSideWindow = sideWindow.clone()
rightSideWindow.move(53, -20)
rightSideWindow.draw(win)

rightSideWindowVertical = sideWindowVertical.clone()
rightSideWindowVertical.move(53, -20)
rightSideWindowVertical.draw(win)

rightSideWindowHorizontal = sideWindowHorizontal.clone()
rightSideWindowHorizontal.move(53, -20)
rightSideWindowHorizontal.draw(win)

door = g.Rectangle(g.Point(180, 270), g.Point(220, 325))
door.setFill('black')
door.draw(win)

doorKnob = g.Circle(g.Point(212, 300), 4)
doorKnob.setFill('yellow')
doorKnob.draw(win)

leftWindow = g.Rectangle(g.Point(125, 230), g.Point(150, 260))
leftWindow.setFill('white')
leftWindow.setWidth(3)
leftWindow.draw(win)

hWindowLine = g.Line(g.Point(125, 245), g.Point(150, 245))
hWindowLine.setWidth(2)
hWindowLine.draw(win)

vWindowLine = g.Line(g.Point(137.5, 230), g.Point(137.5, 260))
vWindowLine.setWidth(2)
vWindowLine.draw(win)

rightWindow = leftWindow.clone()
rightWindow.move(125, 0)
rightWindow.draw(win)

rightHorizWindowLine = hWindowLine.clone()
rightHorizWindowLine.move(125, 0)
rightHorizWindowLine.draw(win)

rightVertWindowLine = vWindowLine.clone()
rightVertWindowLine.move(125, 0)
rightVertWindowLine.draw(win)

circleWindow = g.Circle(g.Point(200, 170), 15)
circleWindow.setFill('white')
circleWindow.setWidth(3)
circleWindow.draw(win)

circleLine = g.Line(g.Point(185, 170), g.Point(215, 170))
circleLine.setWidth(2)
circleLine.draw(win)

circleLineTwo = g.Line(g.Point(200, 155), g.Point(200, 185))
circleLineTwo.setWidth(2)
circleLineTwo.draw(win)


path = g.Rectangle(g.Point(180, 326), g.Point(220, 375))
path.setFill('tan3')
path.setWidth(0)
path.draw(win)

frontChimney = g.Polygon(g.Point(315, 90), g.Point(
    345, 80), g.Point(345, 140), g.Point(315, 150))
frontChimney.setFill(houseBrown)
frontChimney.draw(win)

sideChimney = g.Polygon(g.Point(295, 75), g.Point(
    315, 90), g.Point(315, 150), g.Point(295, 135))
sideChimney.setFill(houseBrown)
sideChimney.draw(win)

topChimney = g.Polygon(g.Point(295, 75), g.Point(
    323, 65), g.Point(345, 80), g.Point(315, 90))
topChimney.setFill('black')
topChimney.draw(win)

fencePost = g.Polygon(g.Point(3, 340), g.Point(8, 335), g.Point(
    13, 340), g.Point(13, 370), g.Point(3, 370))
fencePost.setFill('white')
fencePost.setOutline('white')
fencePost.draw(win)

current_fence_post = fencePost
for i in range(9):
    current_fence_post = current_fence_post.clone()
    current_fence_post.move(17, 0)
    current_fence_post.draw(win)

leftBeginningPost = fencePost.clone()
leftBeginningPost.move(230, 0)
leftBeginningPost.draw(win)

newLeftPost = leftBeginningPost
for i in range(17):
    newLeftPost = newLeftPost.clone()
    newLeftPost.move(17, 0)
    newLeftPost.draw(win)


upperRightFenceLine = g.Line(g.Point(0, 350), g.Point(170, 350))
upperRightFenceLine.setWidth(3)
upperRightFenceLine.setFill('white')
upperRightFenceLine.draw(win)

lowRightFenceLine = g.Line(g.Point(0, 365), g.Point(170, 365))
lowRightFenceLine.setWidth(3)
lowRightFenceLine.setFill('white')
lowRightFenceLine.draw(win)

upperLeftFenceLine = g.Line(g.Point(228, 350), g.Point(500, 350))
upperLeftFenceLine.setWidth(3)
upperLeftFenceLine.setFill('white')
upperLeftFenceLine.draw(win)

lowLeftFenceLine = g.Line(g.Point(228, 365), g.Point(500, 365))
lowLeftFenceLine.setWidth(3)
lowLeftFenceLine.setFill('white')
lowLeftFenceLine.draw(win)


cloudPuff = g.Circle(g.Point(50, 70), 8)
cloudPuff.setFill('white')
cloudPuff.setWidth(0)
cloudPuff.draw(win)

cloudPuffTwo = g.Circle(g.Point(60, 68), 10)
cloudPuffTwo.setFill('white')
cloudPuffTwo.setWidth(0)
cloudPuffTwo.draw(win)

cloudPuffThree = g.Circle(g.Point(75, 65), 13)
cloudPuffThree.setFill('white')
cloudPuffThree.setWidth(0)
cloudPuffThree.draw(win)

cloudPuffFour = cloudPuffTwo.clone()
cloudPuffFour.move(30, 0)
cloudPuffFour.draw(win)

sun = g.Circle(g.Point(500, 0), 65)
sun.setFill('yellow')
sun.setOutline('orange')
sun.draw(win)

midCloud = g.Circle(g.Point(238, 50), 10)
midCloud.setFill('white')
midCloud.setWidth(0)
midCloud.draw(win)

midCloudTwo = g.Circle(g.Point(250, 48), 12)
midCloudTwo.setFill('white')
midCloudTwo.setWidth(0)
midCloudTwo.draw(win)

midCloudThree = g.Circle(g.Point(265, 46), 16)
midCloudThree.setFill('white')
midCloudThree.setWidth(0)
midCloudThree.draw(win)

midCloudFour = midCloudTwo.clone()
midCloudFour.move(30, 0)
midCloudFour.draw(win)

midCloudFive = g.Circle(g.Point(290, 50), 8)
midCloudFive.setFill('white')
midCloudFive.setWidth(0)
midCloudFive.draw(win)


lastCloud = g.Circle(g.Point(430, 50), 10)
lastCloud.setFill('white')
lastCloud.setWidth(0)
lastCloud.draw(win)

lastCloudTwo = g.Circle(g.Point(420, 49), 7)
lastCloudTwo.setFill('white')
lastCloudTwo.setWidth(0)
lastCloudTwo.draw(win)

lastCloudThree = g.Circle(g.Point(443, 48), 14)
lastCloudThree.setFill('white')
lastCloudThree.setWidth(0)
lastCloudThree.draw(win)

lastCloudFour = lastCloud.clone()
lastCloudFour.move(30, 0)
lastCloudFour.draw(win)

win.getMouse()

nightSky = g.Polygon(g.Point(0, 0), g.Point(500, 0), g.Point(500, 160), g.Point(
    430, 160), g.Point(330, 90), centerRoofPoint, g.Point(156, 160), g.Point(0, 160))
nightSky.setFill('black')
nightSky.draw(win)

frontChimney = g.Polygon(g.Point(315, 90), g.Point(
    345, 80), g.Point(345, 140), g.Point(315, 150))
frontChimney.setFill(houseBrown)
frontChimney.draw(win)

sideChimney = g.Polygon(g.Point(295, 75), g.Point(
    315, 90), g.Point(315, 150), g.Point(295, 135))
sideChimney.setFill(houseBrown)
sideChimney.draw(win)

topChimney = g.Polygon(g.Point(295, 75), g.Point(
    323, 65), g.Point(345, 80), g.Point(315, 90))
topChimney.setFill('black')
topChimney.setOutline('darkgray')
topChimney.draw(win)

lightMoon = g.Circle(g.Point(450, 50), 40)
lightMoon.setFill('yellow')
lightMoon.draw(win)

darkMoon = g.Circle(g.Point(420, 50), 40)
darkMoon.setFill('black')
darkMoon.draw(win)

star = g. Polygon(g.Point(10, 30), g.Point(12, 25), g.Point(14, 30), g.Point(19, 30), g.Point(
    15, 35), g.Point(18, 40), g.Point(13, 37), g.Point(7, 40), g.Point(9, 35), g.Point(4, 30))
star.setFill('yellow')
star.draw(win)

starTwo = star.clone()
starTwo.move(100, -15)
starTwo.draw(win)

starThree = star.clone()
starThree.move(55, 15)
starThree.draw(win)

starFour = star.clone()
starFour.move(20, 60)
starFour.draw(win)

starFive = star.clone()
starFive.move(60, 95)
starFive.draw(win)

starSix = starFour.clone()
starSix.move(80, 0)
starSix.draw(win)

starSeven = starTwo.clone()
starSeven.move(150, 0)
starSeven.draw(win)

starEight = starThree.clone()
starEight.move(126, 28)
starEight.draw(win)

starNine = starThree.clone()
starNine.move(80, 0)
starNine.draw(win)

starTen = starFive.clone()
starTen.move(80, 0)
starTen.draw(win)

starEleven = starFour.clone()
starEleven.move(420, 48)
starEleven.draw(win)

starTwelve = starTwo.clone()
starTwelve.move(280, 12)
starTwelve.draw(win)

starThirteen = starEight.clone()
starThirteen.move(45, 15)
starThirteen.draw(win)

starFourteen = starThirteen.clone()
starFourteen.move(-20, -50)
starFourteen.draw(win)

starFifteen = starFourteen.clone()
starFifteen.move(69, 16)
starFifteen.draw(win)

smokePuff = g.Oval(g.Point(315, 50), g.Point(330, 20))
smokePuff.setFill('gray')
smokePuff.setWidth(0)
smokePuff.draw(win)

secondSmokePuff = smokePuff.clone()
secondSmokePuff.move(-5, 20)

thirdSmokePuff = secondSmokePuff.clone()
thirdSmokePuff.move(5, 8)
thirdSmokePuff.draw(win)

fourthSmokePuff = secondSmokePuff.clone()
fourthSmokePuff.move(10, -3)
fourthSmokePuff.draw(win)
secondSmokePuff.draw(win)

paleYellow = (g.color_rgb(244, 242, 127))
sideWindow.setFill(paleYellow)
rightSideWindow.setFill(paleYellow)
circleWindow.setFill(paleYellow)
leftWindow.setFill(paleYellow)
rightWindow.setFill(paleYellow)
