#!/usr/bin/env python

from gtts import gTTS
import subprocess

THROWS = [
    'De-ashi-barai',
    'Hiza-guruma',
    'Sasae-tsurikomi-ashi',
    'Uki-goshi',
    'Osoto-gari',
    'O-goshi',
    'Ouchi-gari',
    'Seoi-nage',
    'Kosoto-gari',
    'Kouchi-gari',
    'Koshi-guruma',
    'Tsurikomi-goshi',
    'Okuri-ashi-barai',
    'Tai-otoshi',
    'Harai-goshi',
    'Uchi-mata',
    'Kosoto-gake',
    'Tsuri-goshi',
    'Yoko-otoshi',
    'Ashi-guruma',
    'Hane-goshi',
    'Harai-tsurikomi-ashi',
    'Tomoe-nage',
    'Kata-guruma',
    'Sumi-gaeshi',
    'Tani-otoshi',
    'Hane-makikomi',
    'Sukui-nage',
    'Utsuri-goshi',
    'O-guruma',
    'Soto-makikomi',
    'Uki-otoshi',
    'Osoto-guruma',
    'Uki-waza',
    'Yoko-wakare',
    'Yoko-guruma',
    'Ushiro-goshi',
    'Ura-nage',
    'Sumi-otoshi',
    'Yoko-gake'
]

def play(msg):
    tts = gTTS(msg.replace('-',' '), lang='ja')
    tts.save(f'sound/{msg}.mp3')
    subprocess.call(["ffplay", "-nodisp", "-autoexit", f"sound/{msg}.mp3"])

for throw in THROWS:
    play(throw)
