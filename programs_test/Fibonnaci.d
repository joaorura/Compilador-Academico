void fib(int n)                             
{                                          
	int fib1 = 1, fib2 = 1, soma;

	for (int i : (3, n, 1))           
	{    
		print("%d", fib1);
		                                    
		soma = fib1 + fib2;                    
		fib1 = fib2;                           
		fib2 = soma;                           
	}                                        
}                                          

int main()
{
	int n;
	scan("%d", n);
	fib(n);
	
	return 0;
}