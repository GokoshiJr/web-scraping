import emoji

def processing_text(text: str, smile_emoji_array: list) -> dict:
  """ 
    Process of text

    Args:
      param1 (str): string with emojis
      param2 (list[][]): list of emojis list

    Returns: 
      dict {
        emoji_all (str), \n
        count_emoji_all (int), \n
        text_without_emoji (str)
      }
  """

  emoji_all = []
  count_emoji_all = 0
  text_without_emoji = ''
  emj_emotion = 0
  
  for letter in text:
    if (emoji.is_emoji(letter)):
      for row in smile_emoji_array:
        if (letter == row[2]):
          emj_emotion += 1
      count_emoji_all += 1
      emoji_all.append(letter)
    else:
      text_without_emoji += letter

  return {
    "emoji_all": emoji_all,
    "count_emoji_all": count_emoji_all,
    "text_without_emoji": " ".join(text_without_emoji.split()),
    "emj_emotion": emj_emotion
  }
