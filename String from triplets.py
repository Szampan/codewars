import copy

def recoverSecret(triplets):
  chars = {c: [set(),set()] for col in triplets for c in col}

  for t in triplets * len(chars):
    print(t)
  print()

  # Update chars dictionary based on triplets

  for triplet in triplets:
    print(triplet)
    for i, letter in enumerate(triplet):
      # Add left & right letter counts
      if i != 0:
        chars[letter][0].update(triplet[:i]) 
      if i != len(triplet):
        chars[letter][1].update(triplet[i+1:])

  # Update chars dictionary based on current chars

  for char in chars:
    for left in copy.deepcopy(chars[char])[0]:
      chars[char][0].update(chars[left][0])
    for right in copy.deepcopy(chars[char])[1]:
      chars[char][1].update(chars[right][1])

  return sort_and_list(chars)

def sort_and_list(dictionary):
  output = "".join([char for char in sorted(dictionary, key=lambda x: (-len(dictionary[x][1]), len(dictionary[x][0])))])
  print(output)
  return output

###

secret = "whatisup"
triplets = [
  ['t','u','p'],
  ['w','h','i'],
  ['t','s','u'],
  ['a','t','s'],
  ['h','a','p'],
  ['t','i','s'],
  ['w','h','s']
]

recoverSecret(triplets)
