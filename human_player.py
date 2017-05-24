


class Human_player:


    def make_move(self, mouse, board):
        ((mx,my),clicked) = mouse
        xoff,yoff,gap = 180,100,140
        for i in range(3):
            for j in range(3):
                if xoff + i*gap <= mx <= xoff + (i+1)*gap and yoff + j*gap <= my <= yoff + (j+1)*gap \
                        and clicked == 1 and board[j][i] == 0:
                    print j,i
                    return (j,i)

        return (-1,-1)
