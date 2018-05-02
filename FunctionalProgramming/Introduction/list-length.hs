len :: Eq a => [a] -> Int
len (x:xs) | xs == [] = 1
           | xs /= [] = 1 + len xs
