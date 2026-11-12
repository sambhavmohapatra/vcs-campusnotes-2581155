"""Utility functions for CampusNotes."""


def count_notes(notes):
    """Return the number of notes, or zero if notes is None."""
    if notes is None:
        return 0
    return len(notes)
