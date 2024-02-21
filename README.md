# The idea

Extract possible chapters from the subtitles of a video.

# How to use it

1.   Install the dependencies of requirements.txt
2.   Setup OPENAI_API_KEY environment variable with your key

    export OPENAI_API_KEY=your_key
    
3.   Run the code:

    python getChapters.py https://www.youtube.com/watch?v=i_LwzRVP7bg en

You must pass the language of the subtitles as the second argument.

# Expected output
```JSON
{"start":"00:00:00","end":"00:04:50","topic":"Introduction to Machine Learning and Using the UCI Machine Learning Repository"}
{"start":"00:04:23","end":"00:09:39","topic":"Introduction to Machine Learning"}
{"start":"00:09:14","end":"00:14:06","topic":"Introduction to Machine Learning and its Types"}
{"start":"00:13:43","end":"00:18:35","topic":"Types of Data and Predictions in Supervised Learning"}
{"start":"00:18:14","end":"00:23:10","topic":"Supervised Learning and Model Training"}
{"start":"00:22:47","end":"00:27:41","topic":"Training, Validation, and Testing Data Sets and Loss in Machine Learning"}
{"start":"00:27:19","end":"00:32:27","topic":"Loss Functions and Performance Measures"}
{"start":"00:32:09","end":"00:37:28","topic":"Data visualization and data set splitting"}
```

# Author

Ronaldo Richieri

https://github.com/richieri
