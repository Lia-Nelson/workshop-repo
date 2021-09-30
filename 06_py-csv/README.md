# K06: StI/O: Divine your Destiny!

### The Nice Mice: Noakai Aronesty, Ryan Wang, Eliza Knapp

We opened the file and we read it into a `DictReader` (an iterable object that contains a dictionary of each line).

We then iterated through each line (each dictionary), separated the two values into two lists (`job_class`, `percentage`) and removed the last item from each list because it was a total.

Finally, we used `random.choices()`, which takes two lists: the values to choose from (`job_class`) and the corresponding probability of selection (`percentage`). 

`k=1` means we are only selecting once. 

This implements the weighted randomized selection.
