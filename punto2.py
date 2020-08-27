
def esprimoono():
  p=0
  n=int(input(" Por favor Ingrese un numero ==>"))
  for j in range(1,n+1):
    if(n % j==0):
      p=p+1
  if(p!=2):
    print("Este numero No es primo")
  else:
    print("Este numero si es primo")
 
def main():
  esprimoono()
    

if __name__ == "__main__":
  main() 
        
        
    