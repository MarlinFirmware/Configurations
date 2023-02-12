# Making a Custom Boot Screen

To make a custom boot screen there are 5 requirements:

1. The file format must be JPEG.
2. Progressive must be tuned off in the export settings (under "Advanced" in GIMP).
3. The Sub-sampling format must be chroma quartered (4:2:0) (also under "Advanced" in GIMP).
4. The resolution must be 480x272.
   Note: The left side of the image will be the top. You can compose the image oriented upright as 272x480, but it must be
   rotated prior to export. (Rotating *during* export only applies a "rotation" attribute that won't be parsed by DWIN / DACAI.)
5. For DACAI the file must be named "`0`" and placed in `private/image`. For DWIN the file must be named "`0_start`" and placed in `DWIN_SET`.

After replacing the Boot Screen follow the usual screen flashing instructions.
