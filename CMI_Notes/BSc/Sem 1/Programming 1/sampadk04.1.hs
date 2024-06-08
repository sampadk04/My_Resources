-- Skeleton Haskell file. I have given the type and
-- function name for each problem. Please do not change
-- the name or the type, since my evaluation script will
-- use these exact names. If you change and your program
-- does not compile or execute, you will get 0 marks.
--

-- You are allowed to define your own helper functions and
-- give any name to them that does not clash with the built-ins
-- and the following function names.
-- Uncomment the following line if you need to import Data.List.	

import Data.List
import Data.Char

-- Problem 1
isPOT :: Integer -> Bool
isPOT n = go 0
    where go m
            |(n `div` (3^m) == 1) && (n `mod` (3^m) == 0) = True
            | n `div` (3^m) >  1                          = go (m+1)
            | otherwise                                   = False


-- Problem 2

-- For this problem I will define functions called 'intlog' and 
-- 'largestdiv' and also use the 'isPOT' function from Problem 1 

intlog :: Integer -> Integer -> Integer
intlog n m = go 1
    where go k
            | m `div` n^k > 0 = go (k+1)
            | otherwise       = (k-1)


largestdiv :: Integer -> Integer
largestdiv n = go (n-1)
    where go m
            | (mod n m) == 0 = m
            | otherwise      = go (m-1)


isPPOT :: Integer -> Bool
isPPOT 1 = False
isPPOT 3 = False
isPPOT n = (isPOT n) && (go n)
    where go m
            | largestdiv (intlog 3 n) == 1 = True
            | otherwise                    = False


-- Problem 3
octall :: Int -> String
octall 0 = ""
octall n = chr((n `mod` 8)+48): octall (n `div` 8)

intToOct::Int -> String
intToOct n = reverse (octall n)


-- Problem 4
octToInt :: String -> Int
octToInt s
    | null        s = 0
    | null (tail s) = (ord (head s) - 48)
octToInt (x:xs)     = (ord x - 48) * (8 ^ (length xs)) + octToInt xs


-- Problem 5

-- For this problem I will define function called 'intLength'

intLength :: Integer -> Integer
intLength n
    | otherwise = 1 + intLength (n `div` 10) 


leftRotate :: Integer -> Integer
leftRotate m
    | m<0    = 0
leftRotate n = (n `mod` (10^(intLength n - 1))) * 10 + n `div` (10^(intLength n - 1))


-- Problem 6

-- For this problem I will use the function called 'intLength' as
-- defined in Problem 5 

rightRotate :: Integer -> Integer
rightRotate m
    | m < 0   = 0
rightRotate n = (n `mod` 10) * (10^(intLength n - 1)) + n `div` 10

-- Problem 7
collatz :: Int -> [Int]
collatz 0 = []
collatz 1 = [1]
collatz m
    | m < 0 = []
collatz n   = n:go n
    where go m
            | m == 1         = []
            | m `mod` 2 == 0 = (m `div` 2):go (m `div` 2)
            | m `mod` 2 == 1 = (3*m + 1):go (3*m + 1)

-- Problem 8
-- For this problem I will define a function 'switchlist' and 'collectTwo'

switchlist :: [Int] -> [Int]
switchlist []     = []
switchlist (x:xs) = (drop 2 (x:xs)) ++ [x]


collectTwo :: [Int] -> [(Int, Int)]
collectTwo (x:y:ys) = [(x,y)]


josephus :: Int -> [(Int, Int)]
josephus m
    | m <= 1 = []
josephus n   = pplAlive [1..n]
            where pplAlive l
                    | null (tail (tail l)) = [(head l , head (tail l))]
                    | otherwise            = (collectTwo l) ++ (pplAlive (switchlist  l))

josephusWinner :: Int -> Int
josephusWinner m
    | m < 0      = 0
josephusWinner n = nosAlive [1..n]
            where nosAlive l
                    | null (tail l)  = head l
                    | otherwise      = nosAlive (switchlist l)

