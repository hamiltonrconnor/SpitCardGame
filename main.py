from Observer import Observer
from Board import Board
from StockPile import StockPile
from Pile import Pile
from Event import *

observer = Observer([])
board = Board(StockPile([]).newPile(5),StockPile([]).newPile(5),Pile([]),Pile([]),Pile([]),Pile([]))
board = board.setup()

while 1:
    ## Add

    observer = observer.registerObserver(Move(1,1,1))
    observer = observer.registerObserver(Spit(1))
    observer = observer.registerObserver(Bored())
    temp = observer.getObservers()
    
    for i in temp:

        if isinstance(i,Move):
            board = board.move(i.getStockPile(),i.getStockPileNum(),i.getSpitPile())
            observer = observer.unregisterOberserver(i)

        elif (isinstance(i,Bored)):
            board = board.bored()
            observer = observer.unregisterOberserver(i)

        elif(isinstance(i,Spit)):
            observer = observer.unregisterOberserver(i)
