{
 "cells": [
  {
   "cell_type": "code",
   "execution_count": 1,
   "id": "940be9d1-25f9-4082-a590-f4220aa2d5fa",
   "metadata": {},
   "outputs": [
    {
     "name": "stderr",
     "output_type": "stream",
     "text": [
      "usage: loom-dl [-h] [-o OUT] url\n",
      "loom-dl: error: unrecognized arguments: -f\n"
     ]
    },
    {
     "ename": "SystemExit",
     "evalue": "2",
     "output_type": "error",
     "traceback": [
      "An exception has occurred, use %tb to see the full traceback.\n",
      "\u001b[0;31mSystemExit\u001b[0m\u001b[0;31m:\u001b[0m 2\n"
     ]
    },
    {
     "name": "stderr",
     "output_type": "stream",
     "text": [
      "/opt/homebrew/opt/ipython/libexec/lib/python3.12/site-packages/IPython/core/interactiveshell.py:3556: UserWarning: To exit: use 'exit', 'quit', or Ctrl-D.\n",
      "  warn(\"To exit: use 'exit', 'quit', or Ctrl-D.\", stacklevel=1)\n"
     ]
    }
   ],
   "source": [
    "#!/usr/bin/python3\n",
    "\n",
    "import argparse\n",
    "import json\n",
    "import urllib.request\n",
    "\n",
    "\n",
    "def fetch_loom_download_url(id):\n",
    "    request = urllib.request.Request(\n",
    "        url=f\"https://www.loom.com/api/campaigns/sessions/{id}/transcoded-url\",\n",
    "        headers={},\n",
    "        method=\"POST\",\n",
    "    )\n",
    "    response = urllib.request.urlopen(request)\n",
    "    body = response.read()\n",
    "    content = json.loads(body.decode(\"utf-8\"))\n",
    "    url = content[\"url\"]\n",
    "    return url\n",
    "\n",
    "\n",
    "def download_loom_video(url, filename):\n",
    "    urllib.request.urlretrieve(url, filename)\n",
    "\n",
    "\n",
    "def parse_arguments():\n",
    "    parser = argparse.ArgumentParser(\n",
    "        prog=\"loom-dl\", description=\"script to download loom.com videos\"\n",
    "    )\n",
    "    parser.add_argument(\n",
    "        \"url\", help=\"Url of the video in the format https://www.loom.com/share/[ID]\"\n",
    "    )\n",
    "    parser.add_argument(\"-o\", \"--out\", help=\"Path to output the file to\")\n",
    "    arguments = parser.parse_args()\n",
    "    return arguments\n",
    "\n",
    "\n",
    "def extract_id(url):\n",
    "    return url.split(\"/\")[-1]\n",
    "\n",
    "\n",
    "def main():\n",
    "    arguments = parse_arguments()\n",
    "    id = extract_id(arguments.url)\n",
    "\n",
    "    url = fetch_loom_download_url(id)\n",
    "    filename = arguments.out or f\"{id}.mp4\"\n",
    "    print(f\"Downloading video {id} and saving to {filename}\")\n",
    "    download_loom_video(url, filename)\n",
    "\n",
    "\n",
    "if __name__ == \"__main__\":\n",
    "    main()"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "7bca1e0b-ff5f-4e8e-b3d5-b1b83e241c3d",
   "metadata": {},
   "outputs": [],
   "source": []
  }
 ],
 "metadata": {
  "kernelspec": {
   "display_name": "Python 3 (ipykernel)",
   "language": "python",
   "name": "python3"
  },
  "language_info": {
   "codemirror_mode": {
    "name": "ipython",
    "version": 3
   },
   "file_extension": ".py",
   "mimetype": "text/x-python",
   "name": "python",
   "nbconvert_exporter": "python",
   "pygments_lexer": "ipython3",
   "version": "3.12.0"
  }
 },
 "nbformat": 4,
 "nbformat_minor": 5
}
