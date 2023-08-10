void pow_related_errors_001()
{

	double num=10^2;
	double exponent=10^2;
	double ans;
	ans=pow(num,exponent); /*Tool should not detect this line as error*/ /*No ERROR:Data Overflow*/
        dsink = ans;
}