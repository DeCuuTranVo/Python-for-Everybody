text = "X-DSPAM-Confidence:    0.8475"
colon_position = text.find(":")
text_after_colon = text[colon_position+1:]
text_trim = text_after_colon.strip()
text_value = float(text_trim)
print(text_value)