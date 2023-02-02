def convert_temp(unit_in, unit_out, temp):
    """Convert fahrenheit <-> celsius and return results.

    - unit_in: either "f" or "c" 
    - unit_out: either "f" or "c"
    - temp: temperature (in f or c, depending on unit_in)

    Return results of conversion, if any.

    If unit_in or unit_out are invalid, return "Invalid unit [UNIT_IN]".

    For example:

      convert_temp("c", "f", 0)  =>  32.0
      convert_temp("f", "c", 212) => 100.0
    """
    # Convert f to c = subtract 32 and multiply by .5556
    # Convert c to f = multiply by 1.8 (or 9/5) and add 32
    if unit_in == "f" and unit_out == "c":
      to_fahrenheit = round((temp - 32) * .5556, 1)
      return to_fahrenheit
    if unit_in == "c" and unit_out == "f":
      to_celsius = round(temp * 1.8 + 32, 1)
      return to_celsius
    if unit_in == unit_out:
      return temp
    if unit_in != "f" or unit_in != "c":
      return f"Invalid unit {unit_in}"
    if unit_out != "f" or unit_out != "c":
      return f"Invalid unit {unit_out}"
      
      
      


print("c", "f", 0, convert_temp("c", "f", 0), "should be 32.0")
print("f", "c", 212, convert_temp("f", "c", 212), "should be 100.0")
print("z", "f", 32, convert_temp("z", "f", 32), "should be Invalid unit z")
print("c", "z", 32, convert_temp("c", "z", 32), "should be Invalid unit z")
print("f", "f", 75.5, convert_temp("f", "f", 75.5), "should be 75.5")
