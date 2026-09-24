from django.contrib.auth.decorators import login_required
from django.shortcuts import get_object_or_404, render, redirect
from .models import Course, Submission


def course_details(request, course_id):
    course = get_object_or_404(Course, id=course_id)
    return render(
        request,
        "course/course_details_bootstrap.html",
        {"course": course}
    )


@login_required
def submit(request, course_id):
    course = get_object_or_404(Course, id=course_id)

    if request.method == "POST":
        questions = course.questions.all()
        total_questions = questions.count()
        correct_answers = 0

        for question in questions:
            selected_choice = request.POST.get(f"question_{question.id}")

            if selected_choice:
                choice = question.choices.filter(
                    id=selected_choice,
                    is_correct=True
                ).first()

                if choice:
                    correct_answers += 1

        score = 0
        if total_questions > 0:
            score = round((correct_answers / total_questions) * 100)

        Submission.objects.create(
            user=request.user,
            course=course,
            score=score
        )

        return redirect("show_exam_result", course_id=course.id)

    return redirect("course_details", course_id=course.id)


@login_required
def show_exam_result(request, course_id):
    course = get_object_or_404(Course, id=course_id)

    submission = Submission.objects.filter(
        user=request.user,
        course=course
    ).order_by("-submitted_at").first()

    return render(
        request,
        "course/exam_result.html",
        {
            "course": course,
            "submission": submission
        }
    )