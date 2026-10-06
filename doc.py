import streamlit as st
import json
from datetime import date

# -----------------------------
# Page Configuration
# -----------------------------
st.set_page_config(
    page_title="AI Patient Appointment Assistant",
    page_icon="🏥",
    layout="wide"
)

# -----------------------------
# Title
# -----------------------------
st.title("🏥 AI Patient Appointment Assistant")
st.write("Welcome! Book and manage your hospital appointment.")

# -----------------------------
# Hospital Data
# -----------------------------
hospitals = {
    "Hyderabad": [
        "Apollo Hospital",
        "Yashoda Hospital",
        "CARE Hospital"
    ],
    "Warangal": [
        "MGM Hospital",
        "Kakatiya Hospital"
    ],
    "Nizamabad": [
        "Government Hospital",
        "Medicare Hospital"
    ]
}

# -----------------------------
# Doctors Data
# -----------------------------
doctors = {
    "General Medicine": [
        "Dr. Ravi Kumar",
        "Dr. Priya Sharma"
    ],
    "Cardiology": [
        "Dr. Arjun Rao",
        "Dr. Sneha Reddy"
    ],
    "Dermatology": [
        "Dr. Kiran Kumar",
        "Dr. Anjali"
    ],
    "Neurology": [
        "Dr. Suresh",
        "Dr. Meena"
    ],
    "Orthopedics": [
        "Dr. Rajesh",
        "Dr. Kavya"
    ],
    "Pediatrics": [
        "Dr. Anitha",
        "Dr. Rahul"
    ]
}

# -----------------------------
# Load Appointments
# -----------------------------
def load_appointments():
    try:
        with open("appointments.json", "r") as file:
            return json.load(file)
    except (FileNotFoundError, json.JSONDecodeError):
        return []


# -----------------------------
# Save Appointments
# -----------------------------
def save_appointments(appointments):
    with open("appointments.json", "w") as file:
        json.dump(appointments, file, indent=4)


# -----------------------------
# Sidebar
# -----------------------------
option = st.sidebar.radio(
    "Menu",
    [
        "Book Appointment",
        "View Appointments",
        "Cancel Appointment"
    ]
)

# =========================================================
# BOOK APPOINTMENT
# =========================================================

if option == "Book Appointment":

    st.header("📅 Book Appointment")

    # Patient Name
    patient_name = st.text_input("Patient Name")

    # Gender
    gender = st.selectbox(
        "Gender",
        ["Male", "Female"]
    )

    # Age
    age = st.number_input(
        "Age",
        min_value=1,
        max_value=120,
        value=18
    )

    # Phone
    phone = st.text_input("Phone Number")

    # Place
    place = st.selectbox(
        "Select Place",
        list(hospitals.keys())
    )

    # Hospital
    hospital = st.selectbox(
        "Select Hospital",
        hospitals[place]
    )

    # Department
    department = st.selectbox(
        "Select Department",
        list(doctors.keys())
    )

    # Doctor
    doctor = st.selectbox(
        "Select Doctor",
        doctors[department]
    )

    # Date
    appointment_date = st.date_input(
        "Appointment Date",
        min_value=date.today()
    )

    # Time
    appointment_time = st.selectbox(
        "Appointment Time",
        [
            "09:00 AM",
            "10:00 AM",
            "11:00 AM",
            "12:00 PM",
            "02:00 PM",
            "03:00 PM",
            "04:00 PM"
        ]
    )

    # Reason
    reason = st.text_area(
        "Reason for Appointment"
    )

    # Book Button
    if st.button("📅 Book Appointment"):

        if patient_name.strip() == "":
            st.error("Please enter patient name.")

        elif phone.strip() == "":
            st.error("Please enter phone number.")

        elif reason.strip() == "":
            st.error("Please enter reason for appointment.")

        else:

            appointments = load_appointments()

            # Check slot
            slot_available = True

            for appointment in appointments:

                if (
                    appointment["doctor"] == doctor
                    and appointment["date"] == str(appointment_date)
                    and appointment["time"] == appointment_time
                ):
                    slot_available = False
                    break

            if not slot_available:

                st.error(
                    "❌ This doctor is already booked "
                    "for this date and time."
                )

            else:

                new_appointment = {
                    "patient_name": patient_name,
                    "gender": gender,
                    "age": age,
                    "phone": phone,
                    "place": place,
                    "hospital": hospital,
                    "department": department,
                    "doctor": doctor,
                    "date": str(appointment_date),
                    "time": appointment_time,
                    "reason": reason
                }

                appointments.append(new_appointment)

                save_appointments(appointments)

                st.success(
                    "✅ Appointment booked successfully!"
                )

                st.subheader("📋 Appointment Details")

                st.write(
                    "Patient Name:",
                    patient_name
                )

                st.write(
                    "Gender:",
                    gender
                )

                st.write(
                    "Age:",
                    age
                )

                st.write(
                    "Phone:",
                    phone
                )

                st.write(
                    "Place:",
                    place
                )

                st.write(
                    "Hospital:",
                    hospital
                )

                st.write(
                    "Department:",
                    department
                )

                st.write(
                    "Doctor:",
                    doctor
                )

                st.write(
                    "Date:",
                    appointment_date
                )

                st.write(
                    "Time:",
                    appointment_time
                )

                st.write(
                    "Reason:",
                    reason
                )


# =========================================================
# VIEW APPOINTMENTS
# =========================================================

elif option == "View Appointments":

    st.header("📋 View Appointments")

    appointments = load_appointments()

    if len(appointments) == 0:

        st.info("No appointments found.")

    else:

        for index, appointment in enumerate(appointments):

            st.subheader(
                f"Appointment {index + 1}"
            )

            st.write(
                "Patient Name:",
                appointment["patient_name"]
            )

            st.write(
                "Gender:",
                appointment["gender"]
            )

            st.write(
                "Age:",
                appointment["age"]
            )

            st.write(
                "Phone:",
                appointment["phone"]
            )

            st.write(
                "Place:",
                appointment["place"]
            )

            st.write(
                "Hospital:",
                appointment["hospital"]
            )

            st.write(
                "Department:",
                appointment["department"]
            )

            st.write(
                "Doctor:",
                appointment["doctor"]
            )

            st.write(
                "Date:",
                appointment["date"]
            )

            st.write(
                "Time:",
                appointment["time"]
            )

            st.write(
                "Reason:",
                appointment["reason"]
            )

            st.divider()


# =========================================================
# CANCEL APPOINTMENT
# =========================================================

elif option == "Cancel Appointment":

    st.header("❌ Cancel Appointment")

    appointments = load_appointments()

    if len(appointments) == 0:

        st.info("No appointments available.")

    else:

        appointment_list = []

        for index, appointment in enumerate(appointments):

            text = (
                f"{index + 1}. "
                f"{appointment['patient_name']} - "
                f"{appointment['doctor']} - "
                f"{appointment['date']} - "
                f"{appointment['time']}"
            )

            appointment_list.append(text)

        selected = st.selectbox(
            "Select Appointment",
            appointment_list
        )

        selected_index = appointment_list.index(selected)

        if st.button("❌ Cancel Appointment"):

            appointments.pop(selected_index)

            save_appointments(appointments)

            st.success(
                "✅ Appointment cancelled successfully."
            )

            st.rerun()