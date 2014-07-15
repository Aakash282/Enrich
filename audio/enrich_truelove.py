from mutagen.id3 import ID3, TXXX
audio = ID3("04 True Love.mp3")
audio.add(TXXX(encoding=3, desc=u"(v, 4:04, $//www.youtube.com/embed/sx1jg1BCQ_4?autoplay=1$)(ix, 4:03, $ $)(i, 0:02, $https://goo.gl/ukyTG9$)(h, 0:02, $http://www.coldplay.com$)(p, 0:08, $For a second I was in control$)(s, 0:12, $I had it once I lost it though$)(s, 0:15, $And all along the fire below would rise$)(s, 0:24, $And I wish you could have let me know$)(s, 0:28, $What's really going on below$)(s, 0:32, $I've lost you now, you let me go$)(s, 0:35, $But one last time$)(p, 0:42, $Tell me you love me$)(s, 0:46, $If you don't then lie$)(s, 0:51, $Oh lie to me$)(p, 1:13, $Remember once upon a time$)(s, 1:16, $When I was yours and you were blind$)(s, 1:20, $A fire would sparkle in your eyes$)(s, 1:24, $And mine$)(p, 1:30, $So tell me you love me$)(s, 1:34, $If you don't then lie$)(s, 1:40, $Oh lie to me$)(s, 1:46, $Just tell me you love me$)(s, 1:50, $If you don't then lie$)(s, 1:55, $Oh lie to me$)(s, 2:02, $If you don't then lie$)(s, 2:08, $Oh lie to me$)(p, 2:16, $Call it true, call it true love$)(s, 2:24, $Call it true, call it true love$)", text=u"(p, 0:08, $For a second I was in control$)(s, 0:12, $I had it once I lost it though$)(s, 0:15, $And all along the fire below would rise$)(s, 0:24, $And I wish you could have let me know$)(s, 0:28, $What's really going on below$)(s, 0:32, $I've lost you now, you let me go$)(s, 0:35, $But one last time$)(p, 0:42, $Tell me you love me$)(s, 0:46, $If you don't then lie$)(s, 0:51, $Oh lie to me$)(p, 1:13, $Remember once upon a time$)(s, 1:16, $When I was yours and you were blind$)(s, 1:20, $A fire would sparkle in your eyes$)(s, 1:24, $And mine$)(p, 1:30, $So tell me you love me$)(s, 1:34, $If you don't then lie$)(s, 1:40, $Oh lie to me$)(s, 1:46, $Just tell me you love me$)(s, 1:50, $If you don't then lie$)(s, 1:55, $Oh lie to me$)(s, 2:02, $If you don't then lie$)(s, 2:08, $Oh lie to me$)(p, 2:16, $Call it true, call it true love$)(s, 2:24, $Call it true, call it true love$)"))
print audio.pprint()
audio.save()