"""views representing library functions"""
from django.shortcuts import render,get_object_or_404
from .models import Book, Student


def index(request):
    """handlies return"""
    return render(request, "library/index.html")


def book_list(request):
    """book list"""
    books = Book.objects.all()

    return render(request, "library/book_list.html", {"books": books})


def book_detail(request, book_id):
    """book detail"""
    book = Book.objects.get(id=book_id)
    return render(request, "library/book_detail.html", {"book": book})


def student_list(request):
    """student list"""
    students = Student.objects.all()
    return render(request, "library/student_list.html", {"students": students})


# def student_detail(request, student_id):
#     """student detail"""
#     student = Student.objects.get(id=student_id)
#     return render(request, "library/student_detail.html", {"student": student})
def student_detail(request, student_id):
    """student detail"""
    student = get_object_or_404(Student, id=student_id)
    book = None
    if student.transaction_set.exists():  # Check if any transactions exist for the student
        book = student.transaction_set.first().book # Assuming each student has only one transaction
    context = {"student": student, "book": book}
    return render(request, "library/student_detail.html", context)
