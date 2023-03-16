Requires the following chage to "...\Marlin\src\module\temperature.cpp"

Comment the sanity check for temperature error as following 

/** #define CHECK_MAXTEMP_(N,M,S) static_assert( \
    S >= 998 || M <= _MAX(TT_NAME(S)[0].celsius, TT_NAME(S)[COUNT(TT_NAME(S)) - 1].celsius) - HOTEND_OVERSHOOT, \
    "HEATER_" STRINGIFY(N) "_MAXTEMP (" STRINGIFY(M) ") is too high for thermistor_" STRINGIFY(S) ".h with HOTEND_OVERSHOOT=" STRINGIFY(HOTEND_OVERSHOOT) ".");
  #define CHECK_MAXTEMP(N) TERN(TEMP_SENSOR_##N##_IS_THERMISTOR, CHECK_MAXTEMP_, CODE_0)(N, HEATER_##N##_MAXTEMP, TEMP_SENSOR_##N)
  REPEAT(HOTENDS, CHECK_MAXTEMP)
*/

Add the 	

/** 
	*/