void main() {
  //Numbers
  //For numbers - whole (int) and decimals (double)
  int num1 = 34;
  double num2 = 30.556789;
  int num3 = 40;
  double num4 = 50.5;

  //Summation
  num sum = num1 + num2 + num3 + num4;
  print(sum);

//Strings
//For text messages
//Declaring values
  String schoolName = 'Power Learn Project';
  String address = 'Africa';

//Printing values
  print("My School name is $schoolName and is located in $address");

//Booleans
//True or false statements
  bool areYouasleep = true;
  print("Sleep Status: $areYouasleep?");
  bool isThedooropen = false;
  print("Door status: $isThedooropen?");

  //Lists
  //An ordered collection of objects to store multiple
  //values without creating multiple variables.
  List<String> studentNames = ["Joseph", "Judah", "Benjamin", "Reuben"];
  print("The list of attendees was $studentNames");
  print("The first student to arrive was ${studentNames[0]}");
  print("The last student to arrive was ${studentNames[3]}");

  //Maps
  //A map is a dynamic collection that represents a set of values ​as
  //key-value pairs. Keys and values ​in the map can be of any type
//Creating a map with string keys and inteer values
  Map<String, int> ages = {'Joseph': 30, 'Benjamin': 25, 'Reuben': 45};
  print("Ages of students: $ages");
  print("Age of first student ${ages[0]}");

  //Runes
  //A rune can be defined as an integer used to represent any Unicode code
  //point. As a Dart string is a simple sequence of UTF-16 code units, 32-bit Unicode values in a string are represented using a special syntax
//Define a string with runes
  String runeString = "Runes in Dart: \u{1f600} \u{1f680} \u{1f648} ";
  print(runeString);

  //Arithmetic Operations using Numbers
  //Arithmetic operators are the most common types of operators. They perform
  //operations like addition, subtraction, multiplication, division
//declaring two numbers
  int num6 = 55;
  int num5 = 80;
  //performing arithmetic calculation
  sum = num6 + num5;
  int subtract = num5 - num6;
  int multiply = (num5 * num6);
  double divide = (num5 / num6);
  double div2 = num5 / num3;
  int mod = (num5 % num6);
  //printing info
  print("Addition is $sum");
  print("Subtraction is $subtract");
  print("Multiply is $multiply");
  print("First division is $divide");
  print("Second division is $div2");
  print("Modula is $mod");

  //Functions
  // writing function outside main function.
  void printName() {
    print("My name John James");
  }

// this is our main function.

  printName();

  //Function to find sum of two numbers
  void add(int num1, int num2) {
    int sum = num1 + num2;
    print("The sum is $sum");
  }

  {
    add(num1, num5);
  }
}
