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
    {
        "name": "Dr. Farhan Saif",
        "Designation": "Assistant Professor",
        "image_filename": "Dr.farhan.png",  # Store only the filename here
        "Qualifications":"M.Sc, Department of Physics QAU (Gold Medal) "
        "MPhil, Department of Electronics QAU (World Lab Fellow) "
        "Doctorate, Department of Physics, University of Ulm, Ulm, Germany "
        "Post Doc, University of Ulm, Germany; Univ. of Electro-Communication, Japan ",
        "Publications":"https://www.researchgate.net/profile/Farhan-Saif",
        "Area": "Quantum Physics, Quantum Computing, Quantum Information Theory, and Quantum Cryptography",
        "email": "Farhansaif@qau.pk",
        "office": "Room 103",
        "phone": "+92-51-7654321"
    },
    {
        "name": "Dr. Hasan Mehmood",
        "Designation": "Assistant Professor",
        "image_filename": "hss.jpeg",  # Store only the filename here
        "Qualifications":"Ph.D, Electrical Engineering, 2007 Stevens Institute of Technology Castle Point on Hudson, Hoboken NJ 07030, USA. "
        "M.Sc, Electrical Engineering/Communications Technology, 2002 University of Ulm, Ulm 89069, Germany ",
        "Publications":"https://www.researchgate.net/profile/Hasan-Mahmood",
        "Area": "Ad Hoc Networks, Channel Coding, Computer Architecture, Computer Architecture, Game theory, Information Theory, Wireless Networks",
        "email": "hasan@qau.pk",
        "office": "Room 104",
        "phone": "+92-51-7654321"
    },
    
]

research_data = [
    {
        "title": "Advanced Signal Processing Techniques",
        "description": "Research on novel signal processing algorithms for various applications.",
        "pi": "Naeem Bhatti",
        "keywords": "Signal Processing, Algorithms, Research"
    },
    {
        "title": "Low-Power VLSI Circuits",
        "description": "Design and implementation of energy-efficient VLSI circuits for portable devices.",
        "pi": "Dr. Musarat Abbas",
        "keywords": "VLSI, Low-Power, Circuits, Design"
    },
    {
        "title": "Wireless Sensor Networks",
        "description": "Development of efficient protocols and algorithms for wireless sensor networks.",
        "pi": "Dr. Arshad Hussain",
        "keywords": "Wireless Networks, Protocols, Algorithms"
    },
    {
        "title": "Nanophotonics",
        "description": "Study of light-matter interactions at the nanoscale for various applications.",
        "pi": "Dr. Qaisar Abbas",
        "keywords": "Photonics, Nanotechnology, Research"
    },
    {
        "title": "Quantum Physics",
        "description": "fundamental theory in physics that explains the behavior of matter and energy at the atomic and subatomic level.",
        "pi": "Dr. Farhan Saif",
        "keywords": "Entanglement, Superposition, Wave-particle duality, Quantum computing"
    }
]

programs_data = [
    {
        "name": "BS Electronics",
        "Prerequisite": " FSc (Pre-Eng) or equivalent with at least second division (45% marks).",
        "duration": "4 Years, 8 Semesters, Eight semesters of 16 weeks each.",
        "credits": "136, 130 (Coursework) + 6 (Project)",
        "description": "A comprehensive undergraduate program covering various aspects of electronics."
    },
    {
        "name": "MS Electronics",
        "Prerequisite":" Bachelor’s degree (B.Sc.) with Mathematics and Physics, "
        "2. Bsc(Electronics), "
        "3. B.Tech(Hons), "
        "4. BCS, "
        "5. BS.Ed(3-Years) from Pakistani University or an equivalent degree from a recognized University",
        "duration": "2 Years, 4 Semesters, Eight semesters of 16 weeks each.",
        "credits": "30, 18 (Coursework) + 12 (Thesis)",
        "description": "A graduate program with specializations in areas like Signal Processing, VLSI, and Communication Systems. with a research thesis."
    },
    {
        "name": "MPhil Electronics",
        "Prerequisite": "Shall possess an MA/MSc degree or its equivalent in the relevant discipline, "
        "Shall have obtained first division in MA/MSc, "
        "BA/BSc or at least 60% marks in BS (Hons) and all other 4-5 years degrees.",
        "duration": "2 Years, 4 Semesters, Eight semesters of 16 weeks each.",
        "credits": "30, 18 (Coursework) + 12 (Thesis)",
        "description": "A research-focused program for advanced studies in electronics. Emphasis on research and thesis work."
    },
    {
        "name": "PhD Electronics",
        "Prerequisite": "M. Phil degree in Electronics from a Pakistani University."
        "An equivalent degree from a recognized University, "
        "A college/university teacher or a member of research staff of a research organization holding a Master’s degree in Electronics, who has shown undoubted promise for research, may also be considered for admission. These candidates will, however, be required to complete the course work of 24 credit hours.",
        "duration": "3-5 Years",
        "credits": "18 (Coursework) + Thesis (Research) ",
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

