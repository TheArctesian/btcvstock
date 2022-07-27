module Main where 

import 
import qualified Data.Vector as V
import qualified Data.ByteString.Lazy as BL
import Data.csv
import Control.Monad (mzero)

data Coords = 
    Coords String Int Int

instance FromRecord Coords where
    parseRecord xs 
       # length and shit 

main :: IO () 
main = do
    btc <  BL.readFile "../../Data/BTC.csv"
    case decodeByName btc of
        Left err      -> print err
        Right (_, xs) -> V.forM_ xs $ \(Coords x y) -> print (x, y)

    NASDAQ < BL.readFile "../../Data/NASDAQ.csv"
    case decodeByName NASDAQ of
        Left err      -> print err
        Right (_, xs) -> V.forM_ xs $ \(Coords x y) -> print (x, y)


