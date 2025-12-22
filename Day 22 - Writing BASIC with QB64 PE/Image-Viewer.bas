Screen _NewImage(605, 605, 32)
_Title "Maker Advent 2025 Day 22"
Cls , _RGB32(220, 220, 220)

music& = _SndOpen("Christmas.mp3")
_SndLoop music&

img& = _LoadImage("logo.png", 32)
_PutImage (0, 0), img&

Do
    _Limit 60
Loop Until InKey$ <> ""

_SndStop music&
_SndClose music&
_FreeImage img&
End


