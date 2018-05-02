f (x:xs) | xs == [] = g x
         | xs /= [] = g x + f xs
         
g x | x `mod` 2 == 0 = 0
    | x `mod` 2 == 1 = x

-- This part handles the Input/Output and can be used as it is. Do not change or modify it.
main = do
  inputdata <- getContents
  putStrLn $ show $ f $ map (read :: String -> Int) $ lines inputdata
