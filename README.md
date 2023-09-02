# General
This repo contains homeworks for Ryan.

In general, your homework should be written cleanly and follow best practices. The following best practices should be followed:
* Variables, classes, and functions should have meaningful names. For example, if you have a shape class, and initiate that to a shape instance, shape1 is a good name, square1 is even 
better.
* Comments are good to explain code. But commenting obvious code is worse. Remember code should explain itself (which is why we use good variable/class/function names). But if the code is still a bit hard to understand, comments can be good to summarize.
* Use type annotation for function parameters and return types.
* DRY - Don't Repeat Yourself. If you find yourself doing something pretty similiar in multiple parts of code, extract that out to a file or class or function, as appropriate. Then resuse that wherever needed.
* KISS - "Keep It Simple, Stupid". Ignore the stupid part. This just means that simple code is better than complex code. Keep lines of code easy to under. If its complex, figure out how to simplify it.
* SOLID
	* S - Single-responsibility Principle: Instead of having one class that does a lot of things like pulling a website from the internet, parsing it, making it pretty, and outputing, its better to make several classes, each one doing one thing. If a function or class is doing too many things, break it up.
	* O - Open-closed Principle: Objects or entities should be open for extension but closed for modification. If we create a Shape function, if another developer needs the Shape function to do something very specific, they shouldn't modify Shape. Instead, they should extend it and add the functionality they want.
	* L - Listov Substitution Principle: A base class should be able to be used in place of its parent. IE any function that can take a Shape class should also be able to work with a Square class, assuming Square extends Shape.
	* I - Interface Segregation Principle: Don't add required functions in an interface/base class that aren't always needed. For example, Shape should not have a volume function, since squares don't have volumes, they only have areas.
	* D - Dependency Inversion Principle: Your code should depend on abstractions (base classes or interfaces), instead of concrete classes, when appropriate. This will allow users to modify behavior by creating new extensions of the base class. They can modify the behavior of an application by modifying the new class, without having to change your code.

# Testing
To run tests and code, you need to install the dependencies using pipenv.

This will install the pacakges both for production and for development.
pipenv install --dev

To activate the environment, you would run:
pipenv shell

To deactivate the environment, you can type:
exit
