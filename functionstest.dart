void main() {
  int num1 = 28;
  int num2 = 33;
  double num3 = 23.5;

  //AddTwo - takes two numbers as arguments and returns the sum of those two numbers.
  int add = num2 + num1;
  print("AddTwo is $add");

//subtractTwo - takes two numbers as arguments and returns the difference of those two numbers.
  int subtract = num1 - num2;
  print("SubractTwo = $subtract");

//multiplyTwo - takes two numbers as arguments and returns the product of those two numbers.
  int multiply = num2 * num1;
  print("MultiplyTwo is $multiply");
//divideTwo - takes two numbers as arguments and returns the quotient of those two numbers.
  double div = num1 / num3;
  print("DivideTwo is $div");
//stringLength -takes an argument of type String and returns the length of that string.
  List<String> names = ["Joseph", "Judah", "Benjamin", "Reuben"];
  print("Stringlenth is $names");
//getFirstElement - takes a list as an argument and returns the first element of that list.
  print("The first element is ${names[0]}");
}
