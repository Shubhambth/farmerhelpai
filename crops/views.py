# crops/views.py
from django.shortcuts import render
import g4f
import markdown


def home(request):
    return render(request,"home.html")


def crop_suggestion(request):
    formatted_suggestion = None

    if request.method == "POST":
        location = request.POST['location']
        soil_type = request.POST['soil_type']
        weather = request.POST['weather']
        water_availability = request.POST['water_availability']
        additional_notes = request.POST.get('additional_notes', '')

        prompt = f"""
        You are an agricultural expert. Based on the following information about a farmer's land, suggest the most suitable crop to grow. Please provide a clear explanation for your suggestion.

        Information:
        - Location/Area: {location}
        - Soil Type: {soil_type}
        - Weather: {weather}
        - Water Availability: {water_availability}
        - Additional Notes: {additional_notes}

        Your output should include:
        1. Recommended crop(s)
        2. Reason for the recommendation
        3. Any tips or precautions for better yield
        """

        # Use g4f to get response
        response = g4f.ChatCompletion.create(
            model="gpt-4o-mini",  # or another supported model
            messages=[{"role": "user", "content": prompt}]
        )

        # Extract AI content (assuming OpenAI-style response format)
        raw_suggestion = response


        # Convert Markdown to safe HTML
        formatted_suggestion = markdown.markdown(raw_suggestion)

    return render(request, "crops/form.html", {
        "suggestion": formatted_suggestion
    })
