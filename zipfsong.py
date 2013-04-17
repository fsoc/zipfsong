import sys

class Playlist:
    def __init__(self): 
        arguments = sys.stdin.readline().split()
        self.max_songs = int(arguments[1])
        self.songs = []

        i = 1
        for line in sys.stdin:
            line_data = line.rsplit()
            self.songs.append({'score' : long(line_data[0])*i,
                'name' : line_data[1]})
            i = i + 1

    def print_top_songs(self):
        self.songs.sort(key=lambda s:s['score'], reverse=True)
        for i in range(0, self.max_songs):
            print self.songs[i]['name'] 

class Main:
    if __name__ == '__main__':
        Playlist().print_top_songs()
