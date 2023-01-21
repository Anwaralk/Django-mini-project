from django.shortcuts import render
# from django.http import HttpResponse
from .models import Note


def display_notes(request):
    queryset = Note.objects.all()
    note_list = []
    context = { 'subject_notes': queryset}
    
    for n in queryset:
            note_list.append({
                'subject': Note.subject,
                'rate_of_understanding': Note.rate_understanding,
                'explanation': Note.explanation,
                
            })
    context = {'my_notes' : note_list}
    return render(request, 'base.html', queryset)
    
def get_note_id(request, note_id):
    noteid = noteid.get(id=note_id)

    return render(request, "note-id.html", {"note": noteid})

# note = Notes()
#     notes_list = []
#     for n in note:
#         note = {
#             "name": note.subject,
#             "explanation": note.explanation,
#             "rate_understanding": note.rate_understanding,
#         }

#         notes_list.append(note)

#         context = {"notes": notes_list}
#         print(context)
#         return render(request, "note-list.html", context)



 