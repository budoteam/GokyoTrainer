#!/usr/bin/env python

from gtts import gTTS
import subprocess
import time

THROWS = [
    [
        'De-ashi-barai',
        'Hiza-guruma',
        'Sasae-tsurikomi-ashi',
        'Uki-goshi',
        'Osoto-gari',
        'O-goshi',
        'Ouchi-gari',
        'Seoi-nage'
    ],
    [
        'Kosoto-gari',
        'Kouchi-gari',
        'Koshi-guruma',
        'Tsurikomi-goshi',
        'Okuri-ashi-barai',
        'Tai-otoshi',
        'Harai-goshi',
        'Uchi-mata'
    ],
    [
        'Kosoto-gake',
        'Tsuri-goshi',
        'Yoko-otoshi',
        'Ashi-guruma',
        'Hane-goshi',
        'Harai-tsurikomi-ashi',
        'Tomoe-nage',
        'Kata-guruma'
    ],
    [
        'Sumi-gaeshi',
        'Tani-otoshi',
        'Hane-maki-komi',
        'Sukui-nage',
        'Utsuri-goshi',
        'O-guruma',
        'Soto-maki-komi',
        'Uki-otoshi'
    ],
    [
        'Osoto-guruma',
        'Uki-waza',
        'Yoko-wakare',
        'Yoko-guruma',
        'Ushiro-goshi',
        'Ura-nage',
        'Sumi-otoshi',
        'Yoko-gake'
    ]
]

def play(msg, lg, speed):
    tts = gTTS(msg.replace('-',' '), lang=lg, slow=speed)
    tts.save(f'sound/{msg}.mp3')
    subprocess.call(["ffplay", "-nodisp", "-autoexit", f"sound/{msg}.mp3"])

play('Start in 10 seconds', 'en', False)
time.sleep(10)
play('here we go', 'en', False)

for group in THROWS:
    for throw in group:
        play(throw, 'ja', True)
        time.sleep(12)

    play("30 seconds pause", 'en', False)
    time.sleep(25)
    play("On it goes!", 'en', False)


