
let notes = JSON.parse(localStorage.getItem("campusNotes")) || [];

const titleInput = document.getElementById("noteTitle");
const contentInput = document.getElementById("noteContent");
const addButton = document.getElementById("addNoteBtn");
const searchInput = document.getElementById("searchInput");
const notesContainer = document.getElementById("notesContainer");

let editIndex = -1;

function saveNotes() {
    localStorage.setItem("campusNotes", JSON.stringify(notes));
}

function displayNotes(filteredNotes = notes) {
    notesContainer.innerHTML = "";

    filteredNotes.forEach((note) => {
        const card = document.createElement("div");
        card.className = "note-card";

        const heading = document.createElement("h3");
        heading.textContent = note.title;

        const paragraph = document.createElement("p");
        paragraph.textContent = note.content;

        const editButton = document.createElement("button");
        editButton.textContent = "Edit";
        editButton.style.marginRight = "10px";

        const deleteButton = document.createElement("button");
        deleteButton.textContent = "Delete";
        deleteButton.className = "delete-btn";

        editButton.onclick = () => editNote(note);

        deleteButton.onclick = () => deleteNote(note);

        card.append(heading, paragraph, editButton, deleteButton);
        notesContainer.appendChild(card);
    });
}

function addNote() {
    const title = titleInput.value.trim();
    const content = contentInput.value.trim();

    if (title === "" || content === "") {
        alert("Please enter both title and content.");
        return;
    }

    if (editIndex === -1) {
        notes.push({ title, content });
    } else {
        notes[editIndex] = { title, content };
        editIndex = -1;
        addButton.textContent = "Add Note";
    }

    saveNotes();
    displayNotes();

    titleInput.value = "";
    contentInput.value = "";
}

function editNote(note) {
    editIndex = notes.indexOf(note);

    titleInput.value = note.title;
    contentInput.value = note.content;

    addButton.textContent = "Update Note";
}

function deleteNote(note) {
    notes = notes.filter(item => item !== note);

    saveNotes();
    displayNotes();
}

function searchNotes() {
    const keyword = searchInput.value.toLowerCase();

    const filteredNotes = notes.filter(note =>
        note.title.toLowerCase().includes(keyword) ||
        note.content.toLowerCase().includes(keyword)
    );

    displayNotes(filteredNotes);
}

addButton.addEventListener("click", addNote);
searchInput.addEventListener("input", searchNotes);

displayNotes();
