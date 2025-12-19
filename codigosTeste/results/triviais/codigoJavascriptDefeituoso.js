for (let i=0; i < 100; i++)
{
	console.log(i);
	if (i == 99)
	{
		throw new Error("Teste do stderr do javascript!")
	}
}
