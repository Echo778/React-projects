def main():
  a = 0
  b = 1
  print("0\n1")
  while True:
    c = a + b
    print(c)
    a = b
    b = c
    if c > 1000:
      break
    
 
main()