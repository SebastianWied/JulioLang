Julio Wants Bool: IsNumEven(Int num)
{
    is (num % 2 == 0) fr?
        Julio Gets YES;
    Julio Gets NO;
}

Julio Wants Int: Multiply(Int a, Int b)
{
    Julio Gets a * b;
}

Julio Wants None: main()
{
    Julio Lets Int a = 5;
    Julio Lets Int b = 4;

    Julio Lets Int c = Multiply(a, b);

    is (IsNumEven(c)) fr?
        Julio Says "c is an even number";
    
    Julio Says "Programs Ends Here";

    Julio Gets None;
}