from flask import Flask, render_template, request, jsonify, url_for

app = Flask(__name__, static_folder='static')

# Sample data (replace with your actual data)
faculty_data = [
    {
        "name": "Dr. Musarat Abaas",
        "Designation": "Associate Professor",
        "image_filename": "DSC_0159.jpeg",  # Store only the filename here
        "Qualifications":"BS in Electronics, MS in Electrical Engineering & PhD in Digital Design",
        "Publications":"https://www.researchgate.net/profile/Musarat-Abbas-3",
        "Area": "Digital Design, VLSI Design, Embedded Systems, FPGA Design, Verilog, System Verilog, and Computer Architecture",
        "email": "Musarat.Abbas@qau.edu.pk",
        "office": "Room 101",
        "phone": "+92-51-1234567"
    },
    {
        "name": "Dr. Qaisar Abbas", 
        "Designation": "Head of Department",
        "image_filename": "DSC_0016.jpeg",  # Store only the filename here
        "Qualifications":"BS in Electronics, MS in Electrical Engineering & PhD in Electronics",
        "Publications":"https://www.researchgate.net/profile/Q-Naqvi",
        "Area": "Metamaterials, Antennas, Photonics, Optoelectronics, Nanotechnology, and Microwave Engineering",
        "email": "Q.Abbas@qau.edu.pk",
        "office": "Room 102",
        "phone": "+92-51-9876543"
    },
    # Add more faculty members...
]

research_data = [
    {
        "title": "Advanced Signal Processing Techniques",
        "description": "Research on novel signal processing algorithms for various applications.",
        "pi": "Dr. John Doe",
        "keywords": "Signal Processing, Algorithms, Research"
    },
    {
        "title": "Low-Power VLSI Circuits",
        "description": "Design and implementation of energy-efficient VLSI circuits for portable devices.",
        "pi": "Dr. Jane Smith",
        "keywords": "VLSI, Low-Power, Circuits, Design"
    },
    # Add more research areas...
]

programs_data = [
    {
        "name": "BS Electronics",
        "duration": "4 Years",
        "credits": "136",
        "description": "A comprehensive undergraduate program covering various aspects of electronics."
    },
    {
        "name": "MS Electronics",
        "duration": "2 Years",
        "credits": "30",
        "description": "A graduate program with specializations in areas like Signal Processing, VLSI, and Communication Systems."
    },
    {
        "name": "MPhil Electronics",
        "duration": "2 Years",
        "credits": "30",
        "description": "A research-focused program for advanced studies in electronics."
    },
    {
        "name": "PhD Electronics",
        "duration": "3-5 Years",
        "credits": "18 (Coursework) + Thesis",
        "description": "A doctoral program for cutting-edge research and specialization in electronics."
    },
    # Add more programs...
]
@app.route("/")
def index():
    return render_template("index.html")

@app.route("/api/faculty", methods=["GET"])
def get_faculty():
    updated_faculty_data = []
    for faculty in faculty_data:
        faculty_with_image = faculty.copy()
        # Generate image URL using url_for and the stored filename
        faculty_with_image["image"] = url_for('static', filename=f'images/{faculty["image_filename"]}')
        updated_faculty_data.append(faculty_with_image)
    return jsonify(updated_faculty_data)

@app.route("/api/research", methods=["GET"])
def get_research():
    # If you want to add images to research data, process them here similarly to faculty data
    return jsonify(research_data)

@app.route("/api/programs", methods=["GET"])
def get_programs():
    return jsonify(programs_data)

@app.route("/api/contact", methods=["POST"])
def contact():
    name = request.form.get("name")
    email = request.form.get("email")
    message = request.form.get("message")

    # In a real application, you'd send an email or save to a database here
    print(f"Received contact form: Name: {name}, Email: {email}, Message: {message}")

    return jsonify({"message": "Message received!"})

if __name__ == "__main__":
    app.run(debug=True)
