#/bin/bash
UTUBELINK=https://www.youtube.com/user/PewDiePie/videos
rm .videos .unparsedLink.txt .link.txt &>/dev/null
touch .videos .unparsedLink.txt
wget $UTUBELINK &>/dev/null
mv videos .videos
cat .videos | grep -m1 Duration >> .unparsedLink.txt
python3 scrapeLink.py
echo "Playing latest video"
mpv $(cat .link.txt) &>/dev/null
rm .videos .unparsedLink.txt .link.txt &>/dev/null
