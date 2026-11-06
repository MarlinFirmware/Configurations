/**
 * Marlin 3D Printer Firmware
 * Copyright (c) 2024 MarlinFirmware [https://github.com/MarlinFirmware/Marlin]
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
 * along with this program.  If not, see <https://www.gnu.org/licenses/>.
 *
 */

/**
 * Made with Marlin Bitmap Converter
 * https://marlinfw.org/tools/u8glib/converter.html
 */

#pragma once

#define STATUS_LOGO_X         0
#define STATUS_LOGO_Y         8
#define STATUS_LOGO_WIDTH     38

const unsigned char status_logo_bmp[] PROGMEM = {
  B00000000,B00000000,B00000000,B00000000,B00000000,
  B00000000,B00000000,B00000000,B00000000,B00000000,
  B11110000,B00000010,B00000000,B00000000,B00110000,
  B10000000,B00000010,B00000000,B00000000,B01001000,
  B10000101,B10001110,B00110011,B01100000,B00001000,
  B11100110,B01010010,B01001001,B10001111,B00010000,
  B10000100,B01010010,B01111001,B00000000,B00100000,
  B10000100,B01010010,B01000001,B00000000,B01000000,
  B11110100,B01001111,B00111011,B10000000,B01111000,
  B00000000,B00000000,B00000000,B00000000,B00000000,
  B00000000,B00000000,B00000000,B00000000,B00000000,
  B00000000,B00011110,B00000000,B00000000,B00000000,
  B00000000,B00010001,B00000000,B00000000,B00000000,
  B00000000,B00010001,B00000000,B00000000,B00000000,
  B00000000,B00011110,B00110110,B00110000,B00000000,
  B00000000,B00010000,B00011000,B01001000,B00000000,
  B00000000,B00010000,B00010000,B01001000,B00000000,
  B00000000,B00010000,B00010000,B01001000,B00000000,
  B00000000,B00010000,B00111000,B00110000,B00000000
};
