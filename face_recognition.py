import cv2
import face_recognition as fr

# Load an image of the person you want to recognize
known_image = fr.load_image_file("/Users/niladridas/image/elon.jpg")
known_encoding = fr.face_encodings(known_image)[0]

# Open the webcam (you may need to change the argument to 1 if you have an external camera)
video_capture = cv2.VideoCapture(0)

while True:
    # Capture each frame from the webcam
    ret, frame = video_capture.read()

    # Find all face locations and face encodings in the current frame
    face_locations = fr.face_locations(frame)
    face_encodings = fr.face_encodings(frame, face_locations)

    for (top, right, bottom, left), face_encoding in zip(face_locations, face_encodings):
        # Check if the face matches the known person
        matches = fr.compare_faces([known_encoding], face_encoding)

        name = "Unknown"

        if matches[0]:
            name = "Elon Musk"

        # Draw a rectangle around the face and display the name
        cv2.rectangle(frame, (left, top), (right, bottom), (0, 255, 0), 2)
        font = cv2.FONT_HERSHEY_DUPLEX
        cv2.putText(frame, name, (left + 6, bottom - 6), font, 0.5, (255, 255, 255), 1)

    # Display the resulting frame
    cv2.imshow('Video', frame)

    # Break the loop when 'q' key is pressed
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

# Release the webcam and close all OpenCV windows
video_capture.release()
cv2.destroyAllWindows()

