from flask_restx import Namespace, Resource, fields
from models import Note 
from flask import request 

note_ns = Namespace("note", description = "A namespace for Notes")

#model (serializer)
note_model = note_ns.model(
    "Note",
    {
        "id":fields.Integer(),
        "title":fields.String(),
        "description":fields.String()
    }
)

@note_ns.route("/notes")
class NotesResource(Resource):

    @note_ns.marshal_list_with(note_model)
    def get(self):
        """Get all notes"""
        notes = Note.query.all() #return sql query object
        return notes 

    @note_ns.marshal_with(note_model)
    @note_ns.expect(note_model)
    def post(self):
        """Create a note"""
        data = request.get_json()

        new_note = Note(
            title = data.get("title"),
            description = data.get("description")
        ) 

        new_note.save()

        return new_note, 201

@note_ns.route("/note/<int:id>")
class NoteResource(Resource):
    def get(self, id):
        """Get a note by id"""
        pass 

    def put(self, id):
        """Update a note by id"""
        pass 

    def delete(self, id):
        """Delete a note by id"""
        pass 