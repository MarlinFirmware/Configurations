/*
 * SailfishLCD.h
 *
 *  Created on: Jan 5, 2019
 *      Author: mikes
 */
#pragma once

#ifndef SAILFISHLCD_H_
#define SAILFISHLCD_H_

#include <Arduino.h>

/* StandardLiquidCrystalSerial
 *
 * This is an implementation of communciation routines for the
 * Makerbot OEM display hardware.
 *
 * This program is free software: you can redistribute it and/or modify
 * it under the terms of the GNU General Public License as published by
 * the Free Software Foundation, either version 3 of the License, or
 * (at your option) any later version.
 *
 * This program is distributed in the hope that it will be useful,
 * but WITHOUT ANY WARRANTY; without even the implied warranty of
 * MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
 * GNU General Public License for more details.
 *
 * You should have received a copy of the GNU General Public License
 * along with this program.  If not, see <http://www.gnu.org/licenses/>
 */

// commands
#define LCD_CLEARDISPLAY 0x01
#define LCD_RETURNHOME 0x02
#define LCD_ENTRYMODESET 0x04
#define LCD_DISPLAYCONTROL 0x08
#define LCD_CURSORSHIFT 0x10
#define LCD_FUNCTIONSET 0x20
#define LCD_SETCGRAMADDR 0x40
#define LCD_SETDDRAMADDR 0x80

// flags for display entry mode
#define LCD_ENTRYRIGHT 0x00
#define LCD_ENTRYLEFT 0x02
#define LCD_ENTRYSHIFTINCREMENT 0x01
#define LCD_ENTRYSHIFTDECREMENT 0x00

// flags for display on/off control
#define LCD_DISPLAYON 0x04
#define LCD_DISPLAYOFF 0x00
#define LCD_CURSORON 0x02
#define LCD_CURSOROFF 0x00
#define LCD_BLINKON 0x01
#define LCD_BLINKOFF 0x00
#define LCD_BACKLIGHT 0x08

// flags for display/cursor shift
#define LCD_DISPLAYMOVE 0x08
#define LCD_CURSORMOVE 0x00
#define LCD_MOVERIGHT 0x04
#define LCD_MOVELEFT 0x00

// flags for function set
#define LCD_8BITMODE 0x10
#define LCD_4BITMODE 0x00
#define LCD_2LINE 0x08
#define LCD_1LINE 0x00
#define LCD_5x10DOTS 0x04
#define LCD_5x8DOTS 0x00

// Custom chars
// Unlike the Gen 4 LCD, this module -- ACM2004 series -- this
// LCD display module only provides 8 custom characters and
// n % 8 == n

#define LCD_CUSTOM_CHAR_DOWN 0
#define LCD_CUSTOM_CHAR_EXTRUDER_NORMAL 2
#define LCD_CUSTOM_CHAR_EXTRUDER_HEATING 3
#define LCD_CUSTOM_CHAR_PLATFORM_NORMAL 4
#define LCD_CUSTOM_CHAR_PLATFORM_HEATING 5
#define LCD_CUSTOM_CHAR_FOLDER 6 // Must not be 0
#define LCD_CUSTOM_CHAR_RETURN 7 // Must not be 0

#define LCD_CUSTOM_CHAR_DEGREE 0xdf // MAY ALSO BE 0xdf
#define LCD_CUSTOM_CHAR_UP 0x5e     // ^
#define LCD_CUSTOM_CHAR_RIGHT 0x7e // right pointing arrow (0x7f is left pointing)

class LiquidCrystalSerial : public Print{

public:
	LiquidCrystalSerial(int strobe, int data, int CLK);
	void init(int strobe, int data, int CLK);
	void begin(uint8_t cols, uint8_t rows, uint8_t charsize = LCD_5x8DOTS);
	void clear();
	void home();

	void homeCursor();      // faster version of home()
	void clearHomeCursor(); // clear() and homeCursor() combined
	void noDisplay();
	void display();
	void noBlink();
	void blink();
	void noCursor();
	void cursor();
	void scrollDisplayLeft();
	void scrollDisplayRight();
	void leftToRight();
	void rightToLeft();
	void autoscroll();
	void noAutoscroll();

	void createChar(uint8_t, uint8_t[]);
	void setCursor(uint8_t, uint8_t);
	void setRow(uint8_t);
	void setCursorExt(int8_t col, int8_t row);

	virtual size_t write(uint8_t);
	using Print::write;
	/** Added by MakerBot Industries to support storing strings in flash **/
	void writeInt(uint16_t value, uint8_t digits);
	void moveWriteInt(uint8_t col, uint8_t row, uint16_t value, uint8_t digits);
	void writeInt32(uint32_t value, uint8_t digits);
	void writeFloat(float value, uint8_t decimalPlaces,
			uint8_t rightJustifyToCol);

	void writeString(char message[]);

	/** Display the given line until a newline or null is encountered.
	 * Returns a pointer to the first character not displayed.
	 */
	char *writeLine(char *message);

	void writeFromPgmspace(const unsigned char message[]);
	void moveWriteFromPgmspace(uint8_t col, uint8_t row,
			const unsigned char message[]);

	void command(uint8_t);

private:
	void send(uint8_t, bool);
	void writeSerial(uint8_t);
	void write4bits(uint8_t value, bool dataMode);
	void pulseEnable(uint8_t value);

	uint8_t _strobe_pin; // LOW: command.  HIGH: character.
	uint8_t _data_pin;   // LOW: write to LCD.  HIGH: read from LCD.
	uint8_t _clk_pin;    // activated by a HIGH pulse.

	uint8_t _displayfunction;
	uint8_t _displaycontrol;
	uint8_t _displaymode;


	uint8_t _initialized;

	uint8_t _xcursor;
	uint8_t _ycursor;

	uint8_t _numlines, _numCols;
};

#endif /* SAILFISHLCD_H_ */
