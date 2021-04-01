int fib(int n)                             
{                                          
	int fib1 = 1, fib2 = 1, soma;

	for (int i = 3; i <= n; i = i + 1)           
	{                                        
		soma = fib1 + fib2;                    
		fib1 = fib2;                           
		fib2 = soma;                           
	}                                        
	
	return fib2;                             
}                                          

int main()
{
	int n, fib_result;
	scan(n);

	fib_result = fib(n);
	
	print(fib_result);
	return 0;
}