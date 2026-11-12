# CampusNotes - Note Statistics Guide

## Overview
The note_stats.py module provides a reusable utility
for counting notes in the CampusNotes project.

## Function
count_notes(notes)

## Features
- Counts notes in a list.
- Returns zero for an empty list.
- Safely handles None values.

## Example
from note_stats import count_notes

notes = ["Math", "Science", "English"]
print(count_notes(notes))

Expected output: 3
