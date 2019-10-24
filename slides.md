% Bytebeats
% Noah Weninger
% October 25, 2019

# Digital sound

- $f:\mathbb{Z}\to\mathbb{Z}$ where $|f(t)|\le b$
- ![picture of spaghetti](sound.png)


# Digital music

- Digital sound, but more periodic
- Powers of 2 are everywhere!
- ![the sound of music](music.png)

# Digital music
- ![the sound of bits](function.png)
- Same thing, right?
- ```f(t)=(t^t/4^t/32)&31```

# Bytebeats
https://greggman.com/downloads/examples/html5bytebeat/html5bytebeat.html#t=0&e=0&s=32000&bb=5d000001001b0000000000000000141d01f00425d021087b406c8fc1583215ef67aaf4dbfb98cf515fff390c0000
https://greggman.com/downloads/examples/html5bytebeat/html5bytebeat.html#t=0&e=0&s=44100&bb=5d000001001e00000000000000001461cc5e31197925169763d83a2fc92836b2f4fbee7b3baf844f91a0b3fffff93e0000

# Conclusion

<audio controls><source src="out43.flac" type="audio/flac"></audio>

- And the answer is...
- $f(x)=\sum_{n=0}^\infty\frac{f^{(n)}(a)}{n!}(x-a)^n$

