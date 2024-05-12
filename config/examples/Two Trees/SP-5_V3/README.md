## Two Trees SP-5 V3 Configurations

This folder contains default configurations for the SP-5 V3.

Changes from default Two Trees SP-5 V3 supplied configuration:

- Using `TFT_COLOR_UI`

  The [original Marlin code from Two Trees](https://wetransfer.com/downloads/80c678c69652aae3dc35635262ebd0a320240418061003/27392ff160a713aeea143b9c7ffad79d20240418061018/6ffdaa?trk=TRN_TDL_01&utm_campaign=TRN_TDL_01&utm_medium=email&utm_source=sendgrid) uses a modified version of `TFT_LVGL_UI` with its own graphics and some additional screens.

  To fully support Marlin this configuration uses `TFT_COLOR_UI` instead.

In future mainline Marlin may have more complete support for the Two Trees UI.
