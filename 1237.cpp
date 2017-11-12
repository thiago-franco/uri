#include<iostream>
#include<string>

using namespace std;

int lcs(string X, string Y)
{
    int m = X.length();
    int n = Y.length();
    int c[m+1][n+1];
    for(int i = 0; i < m+1; i++)
        for(int j = 0; j < n+1; j++)
            c[i][j] = 0;
    for(int i = 1; i < m+1; i++)
    {
        for(int j = 1; j < n+1; j++)
        {
            if(i == 0 || j == 0)
                c[i][j] = 0;
            else if(X[i-1] == Y[j-1])
                c[i][j] = c[i-1][j-1] + 1;
            else if(c[i-1][j] >= c[i][j-1])
                c[i][j] = c[i-1][j];
            else
                c[i][j] = c[i][j-1];
        }
    }
    return c[m][n];
}

int lcs2(string X, string Y)
{
    int m = X.length();
    int n = Y.length();
    int z = 0;
    int c[m+1][n+1];

    for(int i = 1; i < m+1; i++)
    {
        for(int j = 1; j < n+1; j++)
        {
            if(i == 0 || j == 0)
                c[i][j] = 0;
            if(X[i-1] == Y[j-1])
            {
                if(i == 1 || j == 1)
                    c[i][j] = 1;
                else
                    c[i][j] = c[i-1][j-1] + 1;
                if(c[i][j] > z)
                    z = c[i][j];
            }
            else
                c[i][j] = 0;
        }
    }
    return z;
}

int main()
{
    int contador = 0;
    string texto, s1, s2;
    while(getline(cin, texto))
    {
        if(contador == 0)
        {
            s1 = texto;
            contador++;
        }
        else if(contador == 1)
        {
            s2 = texto;
            contador = 2;
        }
        if(contador == 2)
        {
            cout << lcs(s1,s2) << endl;
            contador = 0;
        }
    }

    return 0;
}
