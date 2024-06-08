import System.IO
import Control.Monad
import System.Exit
import Data.Char


--Problem 1


processText :: IO ()
processText = interact (unlines.map g.lines)

g :: String -> String
g s
    | s == ":r" = "\n"
    | (dropWhile (==' ') s) == ":r" = "\n"
    | (take 3 (dropWhile (==' ') s)) == ":r " = c++"\n"++c
    | otherwise = s
        where c = drop 2 (dropWhile (==' ') s)



--Problem 2


runningTotals :: IO ()
runningTotals = sumList [0]

sumList :: [Int] -> IO ()
sumList l = do {
    exitCond <- isEOF;
    if exitCond then return ();
        else do {
        n <- readLn :: IO Int;
        print $ sum $ take 2 (n:l);
        sumList ((n + head l):l);
    }
}



--Problem 3

-- In this problem inorder to get the req result type in ->
-- main = fizzBuzz 10 30

fizzBuzz :: Int -> Int -> IO ()
fizzBuzz m n = putStrLn $ unlines $ map f [m..n]
    where
        f x 
            | (x `mod` 15 == 0) = "FizzBuzz"
            | (x `mod` 3 == 0) && (x `mod` 5 /= 0) = "Fizz"
            | (x `mod` 3 /= 0) && (x `mod` 5 == 0)= "Buzz"
            | otherwise = show x



--Problem 4


reverseCapitalizeHalf :: IO ()
reverseCapitalizeHalf = do {
    x <- getLine;
    case x of
        "R" -> do {y <- getLine; putStrLn $ reverse y; reverseCapitalizeHalf;}
        "C" -> do {y <- getLine; putStrLn $ map toUpper y; reverseCapitalizeHalf;}
        "H" -> do {y <- getLine; putStrLn $ take ((length y) `div` 2) y; reverseCapitalizeHalf;}
        _   -> do {putStrLn "Haskell is awesome. Bye!";}
}