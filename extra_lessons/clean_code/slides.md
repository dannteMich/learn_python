---
theme : "moon"
transition: "slide"
# highlightTheme: "monokai"
# slideNumber: true
title: "Clean Code"
---

# Clean Code

> Based mostly on Robert C. Martin, chapters 1-5{.fragment}

---

## Before we start:
## What are we writing?

> Based on the Mythical Man-month by A. brooks {.fragment}

--

### program

A piece of code that is written to solve a problem.

--

### programming product

A piece of code written for a **CLIENT** (not necessary a programmer) to solve his problem.

Possibly includes:

1. User interface{.fragment} 
2. Documentation{.fragment} 
3. Acceptance tests{.fragment} 
4. Support{.fragment} 

--

### programming system

**MULTIPLE** pieces of code written in **COLLABORATION** with others, **OVER TIME**, to solve an (evolving) problem.

Possibly includes:

1. Design and interfaces (between the different parts){.fragment} 
2. Internal Documentation{.fragment} 
3. Unit tests{.fragment} 

This is where clean code becomes important, as time spent reading is 10x the time spent writing (according to uncle Bob){.fragment}

--

### programming system product

You get the idea: a combination of the programming system and product

--

In a chart:

![](programs.png)


---

## So, Why do we need clean code?


- Because code is written once and read many times (1:10 ratio according to uncle Bob).{.fragment}
- Because code is written over time, and by different people.{.fragment}
- Because code changes. Constantly. And a lot.{.fragment}


---

# Chapter 1:

## What is clean code and how do you measure it?

--

![](wtf_pm.jpg)

> Write your code as if the man maintaining it is a psychopath with a chainsaw who knows where you live{.fragment}

--

What I used to tell my team:

The grade for you're code is 60%-80% from the next developer to work on it, the rest from the client that uses it.{.fragment}

--

### Some useful metrics and ideas:

1. No surprises - does what you expect
2. Clearly explains ideas

--

### Some others

1. Written by someone that cares
2. Expresses the design ideas
3. Minimum dependency (this is in design)

---

## Some comments before we're getting prescriptive:

::: {.incremental}
- Guidelines over dogma{.fragment}
- Conventions trump strict adherence{.fragment}
- Don't forget your tools: the IDE, git, etc..{.fragment}
- Communication, that is making your ideas *clear and distinct*, takes effort.{.fragment}
  - Don't count on the first draft

---

Most important rule is _the boy (and girl) scout rule_:

### Leave the trail/playground/code cleaner than it was when you found it{.fragment}




---

# Chapter 2: Meaningful Names

--

## Basic guidelines


* You should spend more time picking good names. They save a lot of time.
* Don't be afraid of long names. Long names are better than long comments.
  * It's ok to use standards (like `i` a   nd `j` for indexes in loops).
* These things are debatable - come to the table with some modesty.

--

## The basic rules:

* Provide meaningful information:
  * Intention reveling names
  * Meaningful distinctions
* Avoid disinformation

---

#### Example 1

What is the problem here:

```python
def is_document_relevant(c):
  if c > 864000
    return False
  return True
```

What is `c`? what is `864000`?{.fragment}


```python{.fragment}
SECONDS_IN_DAY = 86400

def is_document_relevant(seconds_since_creation):
  if seconds_since_creation > SECONDS_IN_DAY * 10
    return False
  return True
```

---

#### Example 2

The most blatant example is lying. What is the lie here?

```python
def my_functions(players):
  active_players_set = []
  for player in players:
    if player.is_active():
      active_players_set.append(player)
```
players is a list, not a set{.fragment}

--

#### Example 4

```python
def check_if_exists(elem, array):
  # some code here
```
There are no arrays in python, only lists.{.fragment}


--

#### Example 5

This is not miss-information, but it will create bugs

```python
class Player()

  def __init__(self, name: str):
    self._name = name
    self._score = 0

  # Some more code

class Players()

  def __init__(self):
    self._players = []

  # Some more code
```
`Player` and `Players` are too similar{.fragment}

--

#### Example 6

```python
# A class definition
class Player:
  def __init__(self, name: str):
    self._name = name
    self._score = 0
  # more code...
```

And down the line, in the same file, I see this:

```python
current_player = 0
```

I expected the type of `current_player` to be a `Player` {.fragment}

--

#### Example 7

```python
def expand_lists(list1, list2):
  """Merge one list into the other"""
  #some code
```
Which list is merged into which?

```python{.fragment}
def expand_lists(source_list, destination_list):
  #same code
```

--

#### Example 8 (real life)

```js
function get_transactions(start_period_millies: number) {...}
```

Seems like a good name with a good units clarification (millis) but:

1. Not written in the language standard (variables in js are in `camelCase`).{.fragment}
2. The whole system uses seconds and not milliseconds. It's not a bad name, just a bad decision{.fragment}
3. When you look at the code, you see it's NOT a period. Its a timestamp. So the name is misleading{.fragment}

---

## More rules:

- Pick on word per concept{.fragment}
  - Are you `get`ting data or `fetch`ing it?
  - Do you have `manager`s or `controller`s?
- Classes and objects should have **noun** names{.fragment}
- Methods and functions should have **verb** names{.fragment}
  - with some standards for classes: `get_` for getters, `is_` for boolean getters, `set_` for setters etc.

--

## Solution Domain Names

Use solution domain names - these are "programmatic" or "mathematic" concepts\words, that the client may not understand, but explain a lot to a programmer.

`Factory`, `Set`, `Visitor`, `geometrical_distribution`, algorithms, data structures, etc {.fragment}
Make sure you use it correctly - not every list is an array {.fragment}

--

## Problem Domain Names

Use concepts and words closer to the problem domain (accounts, addresses, players, etc)

This is useful when communicating with the clients and it's representatives

--

## Solution Domain vs Problem Domain

You will probably use both. You will need to understand when to use which, and when to combine the two.

Different pieces of code are at different "distances" or "depths" from the users, moving farther from problem domain and closer to solution domain.{.fragment}

---



## The rules you don't think about

- Use pronounceable names
- Use searchable names
- Don't be cute/use puns

---

# Functions

---

# Comments

1. The basic truth: when we update the code, we often forget to update the comments
   * the great "continental drifts" of comments away from their original lines
2. Don't write comments that explain what the code already explains
3. comments becomes a noise that I learn to ignore
4. Comments should explain ***why*** and maybe ***how***. never ***what***.

---

# Classes & Objects vs. Data Structures

---

# Formatting

---

# Additional guidelines

--

Interface inheritance vs implementation inheritance