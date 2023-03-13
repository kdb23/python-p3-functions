""" function myFunction(param) {
    console.log("Running myFunction");
    return param + 1;
} """

def my_function(param):
     print("Running my_function")
    return param + 1

""" function sayHi(name) {
    console.log("Hi there, ${name} !");
} """

def say_hi(name):
    print(f"Hi there, {name} !")

say_hi("Kim")

""" function sayHi(name = "friend") {
    console.log("Hi there, ${name}!");
}

sayHi();
sayHi("Sunny"); """

def say_hi(name="Engineer"):
    print(f"Hi there, {name}!")

say_hi()

say_hi("Sunny")

""" function addAndLog(num1, num2) {
  console.log(num1 + num2);
}

function addAndReturn(num1, num2) {
  return num1 + num2;
}

const sum1 = addAndLog(2, 2);
const sum2 = addAndReturn(2, 2); """

def stylish_painter():
    best_hairstyle = "Bob Ross"
    return "Jean-Michel Basquiat"
    return best_hairstyle
    print(best_hairstyle)

stylish_painter()

""" will return Jean-Michel Basquiat beacuse return keyword will disrupt the execution of your function and prevent python from running anylines of code after the return keyword """

def my_future_function():
    pass

""" Use when youre writing code and know that you will need a function later, but dont know what to put in there yet. Pass preferred over return None becaue it is a statement rather than an expression - it does not terminate the funciton like a return statement would do. If you put code after pass it will be executed. *** Reminds you there is work to be done without interfering with your development*** """

def greet_programmer():
    print("Hello, programmer!")

greet_programmer()