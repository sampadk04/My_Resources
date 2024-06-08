import Data.List
import Data.Char
import Data.Ratio

-- Problem 1
add :: (Int,Int) -> (Int,Int) -> (Int,Int)
add (a,b) (c,d) = (a+c,b+d)

move :: [(Int,Int)] -> [(Int,Int)] -> [(Int,Int)]
move [] l = []
move (x:xs) l = (map (add x) l) ++ (move xs l)

filterrange :: (Int,Int) -> Bool
filterrange (x,y) = (x>=0) && (x<=7) && (y>=0) && (y<=7)

filterdup :: [(Int,Int)] -> [(Int,Int)]
filterdup [] = []
filterdup (x:xs)
    | x `elem` xs = filterdup xs
    | otherwise = x : filterdup xs

knightMove :: (Int, Int) -> Int -> [(Int, Int)]
knightMove i n = if (n<=5) then sort (kMove [i] n) else if n `mod` 2 == 0 then sort (kMove[i] 6) else sort (kMove[i] 5)
    where
        kMove :: [(Int, Int)] -> Int -> [(Int, Int)]
        kMove l 0 = l
        kMove l n = kMove l' (n-1)
            where
                l' = filterdup (filter filterrange x)
                    where
                        x = move l [(1,2),(2,1),(-1,2),(2,-1),(1,-2),(-2,1),(-1,-2),(-2,-1)]

-- Problem 2

frac :: Rational -> Rational
frac x = fromRational ((toRational x) - (toRational (floor x)))

cf :: Rational -> [Integer]
cf x = if (numerator (frac x) == 1) then ((floor x):(denominator (frac x)):[]) else (floor x):(cf (1/(frac x)))

computeRat :: [Integer] -> Rational
computeRat (x:xs)
    | null xs = (x%1)
    | otherwise = (x%1) + (1/(computeRat xs))


-- Problem 3

phi :: Double
phi = (1 + sqrt 5) / 2

computeFrac :: Rational -> Double
computeFrac x = fromIntegral (numerator x)/fromIntegral (denominator x)

approxGR :: Double -> Rational
approxGR e = check 1 e
    where
        check :: Int -> Double -> Rational
        check n e = if (abs (computeFrac (computeRat (replicate n 1)) - phi) < e) then (computeRat (replicate n 1)) else check (n+1) e

-- Problem 4
editDistance :: String -> String -> Int
editDistance as bs = last (last editDistanceTab)
    where
        editDistanceTab = firstList : zipWith nextList as editDistanceTab
        firstList = [0..length bs]
        nextList a l = (head l + 1): zipWith (g a) bs (zip3 l (tail l) (nextList a l))
            where 
                g a b (d,u,l) = if a == b then  d else 1 + minimum [l,u,d]