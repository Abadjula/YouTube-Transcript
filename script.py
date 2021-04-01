while True:
    try:
        from youtube_transcript_api import YouTubeTranscriptApi as yta
        import urllib.request
        import re
        Context = input("Enter a youtube search: ")
        Search = ""
        for space in Context:
            if space in " ":
                Search += "+"
            else:
                Search += space
        html = urllib.request.urlopen("https://www.youtube.com/results?search_query=" + Search)
        video_id = re.findall(r"watch\?v=(\S{11})", html.read().decode())
        data = yta.get_transcript(video_id[0])
        transcript = ""
        for value in data:
            for key, val in value.items():
                if key == "text":
                    transcript += val
        l = transcript.splitlines()
        final_tra = " ".join(l)
        print(final_tra)
        transcript_file = open("Transcript.txt", "w")
        transcript_file.write(final_tra)
        transcript_file.close()
    except OSError:
        print("Please check your internet connection")
    except:
        print(f"I couldn't find the transcript for {Context}")
