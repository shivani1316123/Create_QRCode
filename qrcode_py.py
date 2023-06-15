import qrcode as qr
img=qr.make("https://www.youtube.com/watch?v=DInMru2Eq6E")
img.save("ws_youtube.png")
