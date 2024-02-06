# The idea

Extract possible chapters from the subtitles of a video.

# How to use it

1.   Install the dependencies of requirements.txt
2.   Place the "captions.vtt" file in the same folder as the script.
3.   Setup OPENAI_API_KEY environment variable with your key
4.   Run the code :)

# How to get a captions.vtt file

If you don't have the captions file yet, you can generate them at https://savesubs.com/ . Go to their sites, paste the YouTube video URL in the main box, and ask for download.

After generating it, Savesubs will give a few different formats of subtitles, pick VTT.

The file format must be something like this:

```
WEBVTT

00:00:00.000 --> 00:00:06.000
Kylie Ying has worked at many interesting places such as MIT, CERN, and Free Code Camp.

00:00:06.000 --> 00:00:10.880
She's a physicist, engineer, and basically a genius. And now she's going to teach you

00:00:10.880 --> 00:00:14.720
about machine learning in a way that is accessible to absolute beginners.

00:00:15.280 --> 00:00:21.600
What's up you guys? So welcome to Machine Learning for Everyone. If you are someone who

```

# Author

Ronaldo Richieri

https://github.com/richieri
