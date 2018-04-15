import markovify

# Get raw text as string.
with open("captions.txt") as f:
    text = f.read()

# Build the model.
text_model = markovify.NewlineText(text)

# Print three randomly-generated sentences of no more than 140 characters
newCaptions = []
for i in range(50):
    newCaption = text_model.make_short_sentence(140)
    print(text_model.make_short_sentence(140,tries=1000))
    newCaptions.append(newCaption)

def remove_dupes(l):
    return list(set(l))

newCaptions = remove_dupes(newCaptions)

newCaptions
with open('new_captions.txt', 'w') as file_handler:
    for item in newCaptions:
        file_handler.write("{}\n".format(item))