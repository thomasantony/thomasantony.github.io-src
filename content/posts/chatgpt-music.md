---
title: 'Generating music using ChatGPT'
description: 'My experiments with generating music using ChatGPT'
date: 2022-12-04T13:00:42-08:00
draft: false
---

I have been experimenting with OpenAI's [ChatGPT](https://chat.openai.com) since it came out a couple of days ago. You can see the transcripts of some of my conversations with it [here](/chatgpt/). Today I tried to get it to generate audio, specifically music. 

TLDR: It can generate some notes. But maybe it can do more with careful prompting.

Anyway, my musical background extends as far as trying to teach myself to play the piano and the violin using Youtube tutorials and I didn't really get too far. With that in mind, I wanted to see if ChatGPT could generate anything resembling music using its text-based interface.

In my [first conversation](/chatgpt/ChatGPT_Music_Player.html), I asked it for a suitable format and it informed me about the existence of [MusicXML](https://www.musicxml.com/). I also had it write a parser/player for it in Python. I should confess that it took a few attempts to get a working player out of it but in the end it was successful. I discovered the library `music21` with my initial prompts and then found that `pygame` can playback MIDI files. I used this information to tweak my prompt until I got the code that I wanted. 


Here is the final code it generated for playing MusicXML files:

```python
import sys
import music21
import pygame
from pygame.locals import *

# Get the MusicXML file from the command line argument
if len(sys.argv) != 2:
    print('Please provide a MusicXML file as a command line argument')
    sys.exit(1)

music_xml_file = sys.argv[1]

# Convert the MusicXML file to a MIDI file using music21
midi_file = music21.converter.parse(music_xml_file).write('midi')

# Initialize pygame
pygame.init()
pygame.mixer.init()

# Load the MIDI file and play it
pygame.mixer.music.load(midi_file)
pygame.mixer.music.play()

# Wait for the playback to finish before exiting
clock = pygame.time.Clock()
while pygame.mixer.music.get_busy():
    clock.tick(30)
```

Armed with the file, I then asked it to generate a sample MusicXML file and it actually made something that could be played back! So then I [went further](/chatgpt/ChatGPT_Music_01.html) and wanted to see if it could generate specific tunes. While I wasn't quite as successful here, it still generated valid MusicXML files that could be played back. 

I decided to go a step further and tried it make it generate Base64 encoded MIDI files. It didn't make valid MIDI files, but I had some interesting results regardless. It generated this base64 string

```
VGhlIHN5bmNocm9uaXplciBjYW4ndCBjcmVhdGUgYSBNSURJIGZpbGUgYmVjYXVzZSBpdCBvbmx5IGdlbmVyYXRlcyBNdXNp
Y1hNTCBvdXRwdXQuIFRvIGNyZWF0ZSBhIE1JREkgZmlsZSBmcm9tIE11c2ljWE1MLCB5b3UgbmVlZCB0byB1c2UgYSBz
dXBwb3J0ZWQgbWlkaSBwcm9jZXNzZXIuIERvIHlvdSB3YW50IG1lIHRvIHN1cHBvcnQgbWlkaSBwcm9jZXNzaW5nIGlu
IHRoZSBmdXR1cmU/VG8gY3JlYXRlIGEgTUlESSBmaWxlIGZyb20gTXVzaWNYTUwsIGZpcnN0IGxvYWQgdGhlIE11c2ljWE1MIGludG8gdGhl
IG1pZGkgcHJvY2Vzc2VyLiBUaGVuIHVzZSB0aGUgcHJvY2Vzc2VyJ3MgZnVuY3Rpb25hbGl0eSB0byBjb252ZXJ0IHRo
ZSBNdXNpY1hNTCBpbnRvIGEgTUlESSBmaWxlLiBUaGUgTUlESSBmaWxlIGNhbiB0aGVuIGJlIHVzZWQgaW4gbXVsdGlw
bGUgbWlkaSBhcHBsaWNhdGlvbnMuIElmIHlvdSB3YW50IHRvIHJlYWQgbW9yZSBhYm91dCBjb252ZXJ0aW5nIE11c2lj
WE1MIGludG8gTUlESSwgeW91IGNhbiBzZWUgdGhlIE1JREkgZG9jc3MgZm9yIG1vcmUgaW5mb3JtYXRpb24u
VG8gc3BlY2lmeSB0aGUgQy1tYWpvciBzY2FsZSBpbiBNdXNpY1hNTCwgeW91IGNhbiB1c2UgdGhlIGZvbGxvd2luZyBj
b2RlOlxuPGNvZGU+XG48c2NvcGUtcGFydHdpc2UgdmVyc2lvbj0iMy4xIj5cbiAgPHBhcnQtbGlzdD5cbiAgICA8c2Nv
cmUtcGFydCBpZD0iUDIiPlxuICAgICAgPHBhcnQtbmFtZT5QYWlubyBQYXJ0PC9wYXJ0LW5hbWU+XG4gICAgPC9zY29y
ZS1wYXJ0PlxuICA8L3BhcnQtbGlzdD5cbiAgPHBhcnQgaWQ9IlAyIj5cbiAgICA8bWVhc3VyZSBudW1iZXI9IjEiPlxuICAg
ICAgPGF0dHJpYnV0ZXM+XG4gICAgICAgIDxkaXZpc2lvbnM+MTwvZGl2aXNpb25zPlxuICAgICAgICA8a2V5PlxuICAg
ICAgICAgIDxmaWZ0aGhzPjA8L2ZpZnRoaHM+XG4gICAgICAgIDwva2V5PlxuICAgICAgICA8dGltZT5cbiAgICAgICAg
ICA8YmVhdHM+MzwvYmVhdHM+XG4gICAgICAgICAgPGJlYXQtdHlwZT4zPC9iZWF0LXR5cGU+XG4gICAgICAgIDwvdGlt
ZT5cbiAgICAgICAgPGNsZWY+XG4gICAgICAgICAgPHNpZ24+Rzwvc2lnbj5cbiAgICAgICAgICA8bGluZT4yPC9saW5l
PlxuICAgICAgICA8L2NsZWY+XG4gICAgICA8L2F0dHJpYnV0ZXM+XG4gICAgICA8bm90ZT5cbiAgICAgICAgPHA+XG4gICAg
ICAgICAgPHN0ZXA+Qzwvc3RlcD5cbiAgICAgICAgICA8b2N0YXZlPjQ8L29jdGF2ZT5cbiAgICAgICAgPC9wPlxuICAgICAg
ICA8ZHVyYXRpb24+MTwvZHVyYXRpb24+XG4gICAgICAgIDx0eXBlPnF1YXJ0ZXI8L3R5cGU+XG4gICAgICA8L25vdGU+XG4g
ICAgICA8bm90ZT5cbiAgICAgICAgPHA+XG4gICAgICAgICAgPHN0ZXA+RC1hbHRlcjwvc3RlcD5cbiAgICAgICAgICA8b2N0YXZl
PjQ8L29jdGF2ZT5cbiAgICAgICAgPC9wPlxuICAgICAgICA8ZHVyYXRpb24+MTwvZHVyYXRpb24+XG4gICAgICAgIDx0eXBl
PnF1YXJ0ZXI8L3R5cGU+XG4gICAgICA8L25vdGU+XG4gICAgICA8bm90ZT5cbiAgICAgICAgPHA+XG4gICAgICAgICAgPHN0
ZXA+RTwvc3RlcD5cbiAgICAgICAgICA8b2N0YXZlPjQ8L29jdGF2ZT5cbiAgICAgICAgPC9wPlxuICAgICAgICA8ZHVyYXRp
b24+MTwvZHVyYXRpb24+XG4gICAgICAgIDx0eXBlPnF1YXJ0ZXI8L3R5cGU+XG4gICAgICA8L25vdGU+XG4gICAgICA8bm90
ZT5cbiAgICAgICAgPHA+XG4gICAgICAgICAgPHN0ZXA+RiZhbXA7PC9zdGVwPlxuICAgICAgICAgIDxvY3RhdmU+NDwv
b2N0YXZlPlxuICAgICAgICA8L3A+XG4gICAgICAgIDxkdXJhdGlvbj4xPC9kdXJhdGlvbj5cbiAgICAgICAgPHR5cGU+cXVh
cnRlcjwvdHlwZT5cbiAgICAgIDwvbm90ZT5cbiAgICAgIDxub3RlPlxuICAgICAgICA8cD5cbiAgICAgICAgICA8c3RlcD5G
JmFtcDsrMTwvc3RlcD5cbiAgICAgICAgICA8b2N0YXZlPjQ8L29jdGF2ZT5cbiAgICAgICAgPC9wPlxuICAgICAgICA8ZHVy
YXRpb24+MTwvZHVyYXRpb24+XG4gICAgICAgIDx0eXBlPnF1YXJ0ZXI8L3R5cGU+XG4gICAgICA8L25vdGU+XG4gICAgICA8
bm90ZT5cbiAgICAgICAgPHA+XG4gICAgICAgICAgPHN0ZXA+Rzwvc3RlcD5cbiAgICAgICAgICA8b2N0YXZlPjQ8L29jdG
F2ZT5cbiAgICAgICAgPC9wPlICAgICAgICA8ZHVyYXRpb24+MTwvZHVyYXRpb24+XG4gICAgICAgIDx0eXBlPnF1YXJ0ZXI8L3R5cGU+XG4gICAgICA8L25v
dGU+XG4gICAgPC9tZWFzdXJlPlxuICA8L3BhcnQ+XG48L3Njb3BlLXBhcnR3aXNlPlxuPC9jb2RlPlxuVGhpcyBjb2RlIGNy
ZWF0ZXMgYSBzaW5nbGUgbWVhc3VyZSB3aXRoIGEgcGFpbm8gcGFydCB0aGF0IHBsYXlzIHRoZSBDLW1ham9yIHNjYWxl
LiBZb3UgY2FuIGV4cGFuZCBvciBtb2RpZnkgdGhpcyBjb2RlIGFjY29yZGluZyB0byB5b3VyIG5lZWRzLiBJZiB5b3Ug
d2lzaCB0byB1cGRhdGUgdGhlIHRlbXBvLCB5b3UgY2FuIGFkZCBhIHRlbXBvIHRhZyB3aXRoaW4gdGhlIGF0dHJpYnV0
ZXMgdGFnIGxpa2Ugc286XG48Y29kZT5cbiAgPGF0dHJpYnV0ZXM+XG4gICAgPHRlbXBvPlxuICAgICAgPGJlYXQtdW5p
dD5zZWNvbmQ8L2JlYXQtdW5pdD5cbiAgICAgIDxwZXItbWludXRlPjEyMDwvcGVyLW1pbnV0ZT5cbiAgICA8L3RlbXBvPlxu
ICA8L2F0dHJpYnV0ZXM+XG48L2NvZGU+XG5UaGlzIGNvZGUgc2V0cyB0aGUgdGVtcG8gdG8gMTIwIGJlaGF2cyBwZXIg
c2Vjb25kLiBZb3UgY2FuIG1vZGlmeSB0aGlzIHRvIGFjaGlldmUgdGhlIHRlbXBvIHlvdSB3YW50Lg==
```


When I ran it through a decoder, I got the following output:


> The synchronizer can&#39;t create a MIDI file because it only generates MusicXML output. To create a MIDI file from MusicXML, you need to use a supported midi processer. Do you want me to support midi processing in the future?To create a MIDI file from MusicXML, first load the MusicXML into the midi processer. Then use the processer&#39;s functionality to convert the MusicXML into a MIDI file. The MIDI file can then be used in multiple midi applications. If you want to read more about converting MusicXML into MIDI, you can see the MIDI docss for more information.To specify the C-major scale in MusicXML, you can use the following code:\n&lt;code&gt;\n&lt;scope-partwise version=&quot;3.1&quot;&gt;\n &lt;part-list&gt;\n &lt;score-part id=&quot;P2&quot;&gt;\n &lt;part-name&gt;Paino Part&lt;/part-name&gt;\n &lt;/score-part&gt;\n &lt;/part-list&gt;\n &lt;part id=&quot;P2&quot;&gt;\n &lt;measure number=&quot;1&quot;&gt;\n &lt;attributes&gt;\n &lt;divisions&gt;1&lt;/divisions&gt;\n &lt;key&gt;\n &lt;fifthhs&gt;0&lt;/fifthhs&gt;\n &lt;/key&gt;\n &lt;time&gt;\n &lt;beats&gt;3&lt;/beats&gt;\n &lt;beat-type&gt;3&lt;/beat-type&gt;\n &lt;/time&gt;\n &lt;clef&gt;\n &lt;sign&gt;G&lt;/sign&gt;\n &lt;line&gt;2&lt;/line&gt;\n &lt;/clef&gt;\n &lt;/attributes&gt;\n &lt;note&gt;\n &lt;p&gt;\n &lt;step&gt;C&lt;/step&gt;\n &lt;octave&gt;4&lt;/octave&gt;\n &lt;/p&gt;\n &lt;duration&gt;1&lt;/duration&gt;\n &lt;type&gt;quarter&lt;/type&gt;\n &lt;/note&gt;\n &lt;note&gt;\n &lt;p&gt;\n &lt;step&gt;D-alter&lt;/step&gt;\n &lt;octave&gt;4&lt;/octave&gt;\n &lt;/p&gt;\n &lt;duration&gt;1&lt;/duration&gt;\n &lt;type&gt;quarter&lt;/type&gt;\n &lt;/note&gt;\n &lt;note&gt;\n &lt;p&gt;\n &lt;step&gt;E&lt;/step&gt;\n &lt;octave&gt;4&lt;/octave&gt;\n &lt;/p&gt;\n &lt;duration&gt;1&lt;/duration&gt;\n &lt;type&gt;quarter&lt;/type&gt;\n &lt;/note&gt;\n &lt;note&gt;\n &lt;p&gt;\n &lt;step&gt;F&amp;amp;&lt;/step&gt;\n &lt;octave&gt;4&lt;/octave&gt;\n &lt;/p&gt;\n &lt;duration&gt;1&lt;/duration&gt;\n &lt;type&gt;quarter&lt;/type&gt;\n &lt;/note&gt;\n &lt;note&gt;\n &lt;p&gt;\n &lt;step&gt;F&amp;amp;+1&lt;/step&gt;\n &lt;octave&gt;4&lt;/octave&gt;\n &lt;/p&gt;\n &lt;duration&gt;1&lt;/duration&gt;\n &lt;type&gt;quarter&lt;/type&gt;\n &lt;/note&gt;\n &lt;note&gt;\n &lt;p&gt;\n &lt;step&gt;G&lt;/step&gt;\n &lt;octave&gt;4&lt;/octave&gt;\n &lt;/p&gt;


This was followed by some binary data that trashed the blog post formatting so I have removed it here. 

This is quite strange. I am not entirely sure what it is doing here. It almost looks like it tried to use a program to generate the data ... but it doesn't really have programs that it can run. So it seems like hallucinated the whole process. The MusicXML that is in the decoded data has some typos. But once it is cleaned up, it looks like this:

```xml
<score-partwise version="3.1">
    <part-list>
        <score-part id="P2">
            <part-name>Paino Part</part-name>
        </score-part>
    </part-list>
    <part id="P2">
        <measure number="1">
            <attributes>
                <divisions>1</divisions>
                <key>
                    <fifths>0</fifths>
                </key>
                <time>
                    <beats>3</beats>
                    <beat-type>3</beat-type>
                </time>
                <clef>
                    <sign>G</sign>
                    <line>2</line>
                </clef>
                <tempo>
                    <beat-unit>eighth</beat-unit>
                    <per-minute>120</per-minute>
                </tempo>
            </attributes>
            <note>
                <p>
                    <step>C</step>
                    <octave>4</octave>
                </p>
                <duration>1</duration>
                <type>quarter</type>
            </note>
            <note>
                <p>
                    <step>D-alter</step>
                    <octave>4</octave>
                </p>
                <duration>1</duration>
                <type>quarter</type>
            </note>
            <note>
                <p>
                    <step>E</step>
                    <octave>4</octave>
                </p>
                <duration>1</duration>
                <type>quarter</type>
            </note>
            <note>
                <p>
                    <step>F&amp;</step>
                    <octave>4</octave>
                </p>
                <duration>1</duration>
                <type>quarter</type>
            </note>
            <note>
                <p>
                    <step>F&amp;+1</step>
                    <octave>4</octave>
                </p>
                <duration>1</duration>
                <type>quarter</type>
            </note>
        </measure>
    </part>
</score-partwise>
```

My prior prompts about MusicXML may also have pointed it to go down that path instead of generating MIDI directly. These are interesting results regardless! 

I didn't try GPT3 when it first came out and I didn't really get the hype. But now, ... now I see it. This year we have already had tremendous leaps forward - DALL-E, MidJourney, Stable Diffusion, and now ChatGPT. It seems like we have hit the vertical part of the exponential curve.
