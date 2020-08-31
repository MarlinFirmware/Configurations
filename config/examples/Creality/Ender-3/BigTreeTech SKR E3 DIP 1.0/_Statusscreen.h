/**
 * Marlin 3D Printer Firmware
 * Copyright (c) 2020 MarlinFirmware [https://github.com/MarlinFirmware/Marlin]
 *
 * Based on Sprinter and grbl.
 * Copyright (c) 2011 Camiel Gubbels / Erik van der Zalm
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
 * along with this program.  If not, see <http://www.gnu.org/licenses/>.
 *
 */
#pragma once

/**
 * Custom Status Screen bitmap
 *
 * Place this file in the root with your configuration files
 * and enable CUSTOM_STATUS_SCREEN_IMAGE in Configuration.h.
 *
 * Use the Marlin Bitmap Converter to make your own:
 * http://marlinfw.org/tools/u8glib/converter.html
 */

//
// Status Screen Logo bitmap
//
#define STATUS_LOGO_Y            0
#define STATUS_LOGO_WIDTH       39

const unsigned char status_logo_bmp[] PROGMEM = {
  B00111110,B00000000,B00100000,B00000000,B01110000, // ..#####...........#..............###...
  B00100000,B00000000,B00100000,B00000000,B10001000, // ..#...............#.............#...#..
  B00100000,B11110001,B11100111,B00101110,B00001000, // ..#.....####...####..###..#.###.....#..
  B00111100,B10001010,B00101000,B10110000,B00110000, // ..####..#...#.#...#.#...#.##......##...
  B00100000,B10001010,B00101111,B10100011,B00001000, // ..#.....#...#.#...#.#####.#...##....#..
  B00100000,B10001010,B00101000,B00100000,B00001000, // ..#.....#...#.#...#.#.....#.........#..
  B00100000,B10001010,B00101000,B00100000,B10001000, // ..#.....#...#.#...#.#.....#.....#...#..
  B00111110,B10001001,B11100111,B10100000,B01110000, // ..#####.#...#..####..####.#......###...
  B00000000,B00000000,B00000000,B00000000,B00000000, // .......................................
  B00000000,B00000000,B00000000,B00000000,B00000000, // .......................................
  B00000000,B00000000,B00000000,B00000000,B00000000, // .......................................
  B01110010,B00101111,B00000011,B10000111,B00111100, // .###..#...#.####......###....###..####.
  B10001010,B01001000,B10000010,B01000010,B00100010, // #...#.#..#..#...#.....#..#....#...#...#
  B10000010,B10001000,B10000010,B00100010,B00100010, // #.....#.#...#...#.....#...#...#...#...#
  B01110011,B00001000,B10000010,B00100010,B00100010, // .###..##....#...#.....#...#...#...#...#
  B00001011,B00001111,B00000010,B00100010,B00111100, // ....#.##....####......#...#...#...####.
  B00001010,B10001010,B00000010,B00100010,B00100000, // ....#.#.#...#.#.......#...#...#...#....
  B10001010,B01001001,B00000010,B01000010,B00100000, // #...#.#..#..#..#......#..#....#...#....
  B01110010,B00101000,B10000011,B10000111,B00100000, // .###..#...#.#...#.....###....###..#....
};

//
// Use default bitmaps
//
#define STATUS_HOTEND_ANIM
#define STATUS_BED_ANIM
#define STATUS_HEATERS_XSPACE   20
#if HOTENDS < 2
  #define STATUS_HEATERS_X      48
  #define STATUS_BED_X          72
#else
  #define STATUS_HEATERS_X      40
  #define STATUS_BED_X          80
#endif
