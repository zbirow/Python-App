import os

def convert_srt_to_ass(folder_path):
    """
    Convert all .srt files in the specified folder to .ass format manually.
    """
    if not os.path.isdir(folder_path):
        print(f"The folder {folder_path} does not exist.")
        return

    srt_files = [f for f in os.listdir(folder_path) if f.endswith('.srt')]

    if not srt_files:
        print("No .srt files found in the specified folder.")
        return

    for srt_file in srt_files:
        srt_path = os.path.join(folder_path, srt_file)
        ass_path = os.path.join(folder_path, srt_file.replace('.srt', '.ass'))

        print(f"Converting {srt_path} to {ass_path}...")

        try:
            with open(srt_path, 'r', encoding='utf-8') as srt_file:
                srt_content = srt_file.readlines()

            ass_content = [
                "[Script Info]",
                "Title: Converted from SRT",
                "ScriptType: v4.00+",
                "Collisions: Normal",
                "PlayDepth: 0",
                "",
                "[V4+ Styles]",
                "Format: Name, Fontname, Fontsize, PrimaryColour, SecondaryColour, OutlineColour, BackColour, "
                "Bold, Italic, Underline, StrikeOut, ScaleX, ScaleY, Spacing, Angle, BorderStyle, Outline, "
                "Shadow, Alignment, MarginL, MarginR, MarginV, Encoding",
                "Style: Default,Arial,20,&H00FFFFFF,&H000000FF,&H00000000,&H64000000,-1,0,0,0,100,100,0,0,1,1,0,2,10,10,10,1",
                "",
                "[Events]",
                "Format: Layer, Start, End, Style, Name, MarginL, MarginR, MarginV, Effect, Text"
            ]

            start_time, end_time = None, None
            dialogue_lines = []

            for line in srt_content:
                line = line.strip()
                if line.isdigit():
                    continue  # Skip subtitle indices
                elif "  " in line:  # Timecodes with double spaces
                    times = line.split("  ")
                    if len(times) == 2:
                        start_time = convert_time_to_ass_format(times[0].strip())
                        end_time = convert_time_to_ass_format(times[1].strip())
                elif line:  # Subtitle text
                    if start_time and end_time:
                        dialogue_lines.append(
                            f"Dialogue: 0,{start_time},{end_time},Default,,0,0,0,,{line}"
                        )
                        start_time, end_time = None, None  # Reset for the next block

            # Add dialogue lines to ASS content
            ass_content.extend(dialogue_lines)

            with open(ass_path, 'w', encoding='utf-8') as ass_file:
                ass_file.write("\n".join(ass_content))

            print(f"Successfully converted: {ass_path}")

        except Exception as e:
            print(f"Error converting {srt_path}: {e}")

def convert_time_to_ass_format(srt_time):
    """
    Convert SRT time format (hh:mm:ss,ms) to ASS time format (h:mm:ss.cs).
    """
    try:
        parts = srt_time.replace(",", ":").split(":")
        if len(parts) == 4:  # hh:mm:ss,ms format
            hours, minutes, seconds, milliseconds = parts
            return f"{int(hours)}:{minutes}:{seconds}.{milliseconds[:2]}"
        else:
            raise ValueError(f"Invalid time format: {srt_time}")
    except Exception as e:
        print(f"Error converting time: {srt_time} - {e}")
        return "0:00:00.00"

# Example usage
folder = "D:/Claymore (2007)/wyp"
convert_srt_to_ass(folder)
