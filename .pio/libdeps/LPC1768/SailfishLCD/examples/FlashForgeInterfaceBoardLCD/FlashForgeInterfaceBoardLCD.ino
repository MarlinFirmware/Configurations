#include "Arduino.h"
#include "SailfishLCD.h"
//The setup function is called once at startup of the sketch

const int PIN_LCD_STROBE         =  33;  // Out: LCD IC4094 shift-register strobe
const int PIN_LCD_DATA           =  34;  // Out: LCD IC4094 shift-register data
const int PIN_LCD_CLOCK          =  35;  // Out: LCD IC4094 shift-register clock
const int PIN_LCD_BACKLIGHT      =  15;  // Out: LCD backlight (PWM)
// srdata / srclock / strobe
LiquidCrystalSerial lcd(PIN_LCD_STROBE ,PIN_LCD_DATA, PIN_LCD_CLOCK);

// Creat a set of new characters
byte heart[8] = {
  0b00000, 0b01010, 0b11111, 0b11111, 0b11111, 0b01110, 0b00100, 0b00000
};

byte smiley[8] = {
  0b00000, 0b00000, 0b01010, 0b00000, 0b00000, 0b10001, 0b01110, 0b00000
};

byte frownie[8] = {
  0b00000, 0b00000, 0b01010, 0b00000, 0b00000, 0b00000, 0b01110, 0b10001
};

byte armsDown[8] = {
  0b00100, 0b01010, 0b00100, 0b00100, 0b01110, 0b10101, 0b00100, 0b01010
};

byte armsUp[8] = {
  0b00100, 0b01010, 0b00100, 0b10101, 0b01110, 0b00100, 0b00100, 0b01010
};

void setup(){
    pinMode(PIN_LCD_BACKLIGHT, OUTPUT);
    analogWrite(PIN_LCD_BACKLIGHT, 80);

    lcd.begin(20, 4);               // initialize the lcd
//    lcd.clear();

    // load characters to the LCD
    lcd.createChar(0, smiley);
    lcd.createChar(1, frownie);
    lcd.createChar(2, armsDown);
    lcd.createChar(3, armsUp);
    lcd.createChar(4, heart);

    lcd.home ();                   // go home
    lcd.setCursor (0, 0);
    lcd.print(F("LiquidCrystal_SRLCD3"));
    lcd.setCursor (0, 1);
    lcd.print(F("he.."));
    lcd.setCursor (0, 2);
    lcd.print(F("..lo"));
    lcd.setCursor (0, 3);
    lcd.print(F("World "));
    lcd.print(char(4));
    lcd.print(char(2));
    lcd.print(char(3));
    delay(2000);
}

void loop()
{
    for (int i = 5; i <= 15; i++){
      lcd.setCursor ( i, 1 );
      lcd.print(char(random(0,2)));
      delay(100);
      lcd.setCursor ( i, 1 );
      lcd.print(F(" "));
    }

    for (int i = 15; i >= 5; i--){
      lcd.setCursor ( i, 1 );
      lcd.print(char(random(0,2)));
      delay(100);
      lcd.setCursor ( i, 1 );
      lcd.print(F(" "));
    }

    // Turn the display on/off
    lcd.setCursor ( 5, 2 );
    lcd.print(F("Turn screen off"));
    delay(1000);
    lcd.noDisplay();
    delay(1000);
    lcd.display();

    lcd.setCursor ( 5, 2 );
    lcd.print(F("Toggle Cursor  "));
    delay(1000);
    lcd.setCursor ( 19, 2 );
    lcd.cursor();
    delay(2000);
    lcd.noCursor();

    lcd.setCursor ( 5, 2 );
    lcd.print(F("Toggle Blink   "));
    lcd.setCursor ( 19, 2 );
    lcd.blink();
    delay(2000);
    lcd.noBlink();

    lcd.setCursor ( 5, 2 );
    lcd.print(F("Scroll screen  "));
    delay(1000);
// This is an autoscroll demo, not super useful but here just in case.
//    lcd.setCursor(16,0);
//     lcd.autoscroll();
//     // print from 0 to 9:
//     for (uint8_t thisChar = 0; thisChar < 10; thisChar++) {
// 	lcd.print(char(2));
// 	delay(250);
// 	lcd.print(char(3));
// 	delay(250);
//     }
//     // turn off automatic scro
//     lcd.noAutoscroll();

    for (uint8_t positionCounter = 0; positionCounter < 10; positionCounter++) {
      // scroll one position left:
      lcd.scrollDisplayLeft();
      // wait a bit:
      delay(50);
    }

    // scroll 29 positions (string length + display length) to the right
    // to move it offscreen right:
    for (uint8_t positionCounter = 0; positionCounter < 20; positionCounter++) {
      // scroll one position right:
      lcd.scrollDisplayRight();
      // wait a bit:
      delay(50);
    }

      // scroll 16 positions (display length + string length) to the left
      // to move it back to center:
    for (uint8_t positionCounter = 0; positionCounter < 10; positionCounter++) {
      // scroll one position left:
      lcd.scrollDisplayLeft();
      // wait a bit:
      delay(50);
    }
    lcd.setCursor ( 5, 2 );
    lcd.print(F("               "));
}
