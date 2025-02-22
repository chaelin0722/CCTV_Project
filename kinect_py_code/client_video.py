import socket
import cv2

UDP_IP = '127.0.0.1'
UDP_PORT = 9505

sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

cap = cv2.VideoCapture(0)

while True:
    ret, frame = cap.read()
    d = frame.flatten()
    s = d.tostring()

    for i in range(20):
        sock.sendto(bytes([i]) + s[i * 46080:(i + 1) * 46080], (UDP_IP, UDP_PORT))

        if cv2.waitKey(1) & 0xFF == ord('q'):
            break

cap.release()
cv2.destroyAllWindows()