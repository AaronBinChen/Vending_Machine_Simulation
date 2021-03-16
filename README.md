# Vending Machine Simulation 
Resideo Coding Exercise March 2021 by Aaron Chen

Video Demo: https://www.youtube.com/watch?v=51xrGU4eQfw

## Thought and Design Process
<p>
    This project was done for the coding exercise given by Eric Oh. The exercise was to allow a GUI screen to show a customer 4 different product selections. Each product has a different cost and the customer can purchase any amount. I originally planned on using Django to create the front-end and the back-end. However, I decide that it will be much simpler to just stick with Tkinter because of the simplicity of their grid system and widgets. 
</p>

![alt text](Design_Layout.png)

<p>
    Shown above is the design layout that I came out for this vending machine simulation. I thought of the entire rectangle as one large frame, where it will then be split into three columns. The left column will hold the images and labels for each product. There will be a mini frame for each product. The top frame of the middle column will allow us to preview the product when we hover over its label. The bottom frame of the middle column will display an image of the product that was just purchased. The right column will display messages on the availability of the products in the vending machine, display records of transaction (money inserted, number of products purchased, change), display price board, and allow customers to insert money and choose the number of product they want to purchase. Last but not least, the restock button is at the very bottom of this right hand column. 
</p>

<p>
    Note to keep in mind: When we display the image of the product that was just purchased, it shows up in the top frame of the middle column. This is due to the way the grid system and widgets work in Tkinter. When we are no longer hovering over the product label, there will no longer be a preview. As a result, the size of the top frame will collapse to basically one line. Thus, when the image of the product purchased is displayed, it'll basically be displayed on the first line + size of bottom half frame.
</p>

## Running the Code
This python file uses several Python libraries such as Pillow and pygame. First, download these requirements:
```
pip install Pillow
pip install pygame
```

Once you're done downloading these libraries, just run the sim.py file on Visual Studio Code. Enjoy!

## Final Product
![alt text](Final_Product.PNG)
<p>
    This is the display right when the python file is run. Note that the middle column is empty because there's nothing to display yet. Also note that the status box and transaction system on the right hand column is also empty due to the same reason.
</p>

## Using the Vending Machine Simulation
<p>
    To get a preview of the product, please hover over the words of each product label. You can hover and unhover to see more than one preview of a product. 
</p>

<p>
    You may have noticed that the buttons where the product images are located seem to be grayed-out. For this to be active, you first have to insert your payment and then click the green 'Pay Now' Button. Then, you have to type in a certain amount of the products that you want to buy. Once you type it in, press the red 'Submit Item Amount' button. You will notice that the buttons, where the product images are located, are now normal. Feel free to press any one product and see what happens!  
</p>

<p>
    If you did not insert enough money the first time, that's perfectly ok. Please just type in the amount that will be required to make up the difference. For example, let's say you put in 25 cents for a Yakult. This isn't enough as an Yakult cost 50 cents. At this point, you can just type 25 cents into the entry field again instead of 50 cents. By typing 25 cents, the system will add this newly entered 25 cents to the previously entered 25 cents to make up a total of 50 cents. 
</p>

<p>
    The restock button can just be pressed once and the vending machine will be fully restocked to 30 items per product. 
</p>

![alt text](Snapshot_from_Demo.png)

<p>
    Shown above is a snapshot of the video demo I gave. I was hovering over the Fanta product label while waiting for the dispension of the Yakult. 
</p>