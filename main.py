from BoardRecognition import BoardRecognition
import cv2


board_img = cv2.imread("chessboard.png")
boardRec = BoardRecognition(board_img)
board = boardRec.initialize_Board()
board.assignState()

cv2.imshow("Chess board with lines", board)
cv2.waitKey(0)
