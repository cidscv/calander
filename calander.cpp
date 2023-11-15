/*Owen Reid Calander program he wrote at 4am*/

#include <iostream>
#include <string>
#include <cstdlib>

void printMonth(int month, int year);
void printYear(int year);

using namespace std;

int main()
{

  int year_choice;
  int month_choice;
  string choice;
  cout << "Year or Month?: "; /*Asks the user if they want a calander of a specific month
                                in any given year or a calander for all months in any
                                given year*/
  cin >> choice;

  if (choice == "Year")
  { // calls function printYear for inputed year

    cout << "Which year?: ";
    cin >> year_choice;

    printYear(year_choice);
  }

  else if (choice == "Month")
  { // calls function printMonth for inputed month and year

    cout << "Which year?: ";
    cin >> year_choice;

    cout << "Which month? (1=Jan ... 12=Dec): ";
    cin >> month_choice;

    printMonth(month_choice, year_choice);
  }

  return 0;
}

/*Function to print any given months calander of any given year using the gregorian
calander. Wrote all this code at 4am after having an epiphany on how to do this assignment*/

void printMonth(int month, int year)
{

  int d = 1;   // d repersents what day we're looking for in the algorithm (first day)
  int i, j, k; // Intializes all my variables for my "for statements" later on

  /*Algorithm to detirmine the first day of any given month (0=Sunday, 6=Saturday)
  First published by Michael Keith and Tom Craver in 1990*/

  int first_day = (d += month < 3 ? year-- : year - 2, 23 * month / 9 + d + 4 + year / 4 - year / 100 + year / 400) % 7;

  // Intializes array for months of length 12 (0-11)

  string month_names[] = {"January", "Febuary", "March", "April", "May", "June", "July",
                          "August", "September", "October", "November", "December"};

  int yearpr = year; /*This is used cause Jan and Feb have to be taken back a year
                     for the algorithm to work*/
  if (month < 3)
  { // So if the month is Jan or Feb then the year adds 1
    yearpr = year + 1;
  }

  cout << endl
       << month_names[month - 1] << " " << yearpr << endl
       << endl;
  ;
  cout << " S  M Tu  W Th  F  S" << endl;
  for (i = 0; i < first_day; i++)
  { // This prints spaces before the first day comes
    // if the first day is sunday it moves 0 spaces if its saturday it moves 6 spaces
    cout << "   ";
  }
  cout << " 1"
       << "  "; // prints the first day of the month once the spaces are set

  int first_week = 7 - first_day; // detirmines how many more days it has to print out
                                  // in the first week

  for (j = 2; j <= first_week; j++)
  { // prints out the rest of the first week
    cout << j << "  ";
  }
  cout << endl;
  cout << " ";

  /*This block of code (below) detirmines days in month for every month. Jan, March, May,
  July-Aug, October, Dec all have 31 days. April, June, Sept, and Nov all have 30
  days and Feb has either 28 days or 29 days depending on if its a leap year or not
  (Leap year is detirmined by if statements below)*/

  int dim;
  if (month == 1 || month == 3 || month == 5 || month == 7 || month == 8 || month == 10 || month == 12)
  {
    dim = 31;
  }

  if (month == 2)
  {

    if (yearpr % 4 == 0 && yearpr % 100 != 0)
    {
      dim = 29;
    }
    else if (yearpr % 4 == 0 && yearpr % 4 == 0 && yearpr % 400 == 0)
    {
      dim = 29;
    }
    else
    {
      dim = 28;
    }
  }

  if (month == 4 || month == 6 || month == 9 || month == 11)
  {
    dim = 30;
  }

  int p = 0; // sets counter p to 0
  for (k = j; k <= dim; k++)
  { // for loop to print the rest of the days of the month
    p++;
    if (k < 9)
    { // formatting changes if its single digit or double digit
      cout << k << "  ";
    }
    if (k >= 9)
    {
      cout << k << " ";
    }
    if (p == 7)
    { // once counter reaches end of week (7 days) start a new line (new week)
      cout << endl;
      if (k < 9)
      { // This is put here in case the third week still has single digit numbers
        // for formatting properly (lineing up to the days of the week)
        cout << " ";
      }
      p = 0; // resets counter p to 0
    }
  }

  cout << endl
       << endl;
}

void printYear(int year)
{

  for (int i = 1; i <= 12; i++)
  { // for a given year print calander for all 12 months

    printMonth(i, year); // i changes with each iteration till it reaches 12
  }
}
