def celsius_converter(f_temp):
    """
    Converts a temperature from Fahrenheit to Celsius.
    """
    celsius = (float(f_temp) - 32) * 5 / 9
    return round(celsius, 2)



def parse_and_clean(line):
    """
    Parses and cleans a single weather station log line.

    """
    if not line.strip():
        return None

    parts = line.split("|")
    parts = [part.strip() for part in parts]

    if len(parts) != 5:
        return None

    if any(part == "" for part in parts):
        return None

    if parts[2] in ("ERROR", "N/A"):
        return None

    if parts[4] != "ACTIVE":
        return None

    return parts

corrupted_count = 0

with open("environmental_raw.txt", "r") as input_file:
    with open("cleaned_weather.csv", "w") as output_file:
        output_file.write(
            "Timestamp,StationID,Temp(C),Humidity(%),Sensor_Status\n"
            )
        for line in input_file:
            cleaned_data = parse_and_clean(line)

            if cleaned_data is None:
                corrupted_count += 1
                continue
            temperature_c = celsius_converter(cleaned_data[2])
            cleaned_data[2] = temperature_c
            output_file.write(
                ",".join(map(str, cleaned_data)) + "\n"
                )
print(
    f"Number of corrupted lines skipped: {corrupted_count}"
    )