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

Because code is written once (max 3 times) and read many times.

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

## Some comments before we begin:

- Guidelines over dogma{.fragment}
- Conventions trump strict adherence{.fragment}
- Don't forget your tools: the IDE, git, etc..{.fragment}
- Communication, making your ideas *clear and distinct*, takes effort.{.fragment}
  - Don't count on the first draft

---

Most important rule _the boy scout rule_:

## Leave the code cleaner than it was when you found it{.fragment}




---

# Chapter 2: Meaningful Names

--


```python [1|2]

def my_func(h, w):
    return h * w

```


---

# Functions

---

# Comments

---

# Classes & Objects vs. Data Structures

---

# Formatting

---

# Additional guidelines

--

Interface inheritance vs implementation inheritance