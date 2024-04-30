from gtts import gTTS
from pydub import AudioSegment

# 歌曲歌词
lyrics = """
In the silence of the night, I hear the echoes of your voice,
Memories flood my mind, but now I have no choice.
The world feels cold and empty, since you went away,
Lost in a sea of sorrow, can't find the light of day.

Oh, how I miss you, my dear one,
Gone from this world, but your love still shines like the sun.
Everything has changed, since you've been gone,
A heartache so deep, it's hard to carry on.

The home once filled with laughter, now echoes with tears,
Your absence weighs heavy, like the burden of years.
The walls hold your memories, but they're fading away,
Leaving me stranded, in a world turned gray.

Oh, how I miss you, my dear one,
Gone from this world, but your love still shines like the sun.
Everything has changed, since you've been gone,
A heartache so deep, it's hard to carry on.

Work seems meaningless, and life feels so hollow,
Without your presence, I'm drowning in sorrow.
The world moves on, but I'm stuck in the past,
Longing for the moments, that went by too fast.

Oh, how I miss you, my dear one,
Gone from this world, but your love still shines like the sun.
Everything has changed, since you've been gone,
A heartache so deep, it's hard to carry on.

Though you're gone from sight, you'll always be near,
In my heart forever, your love will appear.
Through the pain and the tears, I'll find a way to cope,
For you're my guiding light, my eternal hope.
"""

# 使用 TTS 引擎生成歌词的音频
tts = gTTS(text=lyrics, lang='en', slow=False)
tts.save("lyrics.mp3")

# 背景音乐文件路径
background_music_path = "background_music.mp3"

# 读取背景音乐文件
background_music = AudioSegment.from_file(background_music_path)

# 将歌词音频与背景音乐合成
final_song = background_music.overlay(AudioSegment.from_mp3("lyrics.mp3"), position=0)

# 输出最终歌曲
final_song.export("final_song_with_lyrics.mp3", format="mp3")
