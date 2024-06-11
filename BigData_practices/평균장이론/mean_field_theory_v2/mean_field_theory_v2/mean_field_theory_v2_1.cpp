#include <iostream>
#include <math.h>
#include <iomanip>
#include <fstream>

int main()
{
    const int N = 199; // 200 - 1

    const double Tl = 0.;
    const double Th = 2.;
    const double dT = (Th - Tl) / (N + 1);
    double arr_T[N], arr_S[N], arr_E[N], arr_C[N];

    for (int i = 0; i < N; ++i) arr_T[i] = Tl + (i + 1) * dT;

    /* create and open a file, write up to 6 decimal points */
    std::ofstream of("Ising_mean_field_T.txt");
    of << std::setprecision(6) << std::fixed;

    double S = -0.1; // initial starting point
    const int N_lim = 100; // max number of iteration
    const double E_lim = 1.0e-8; // stop iteration if E_lim is reached

    /* T increasing */
    for (int i = 0; i < N; ++i)
    {
        for (int j = 1; j < N_lim; ++j)
        {
            double S_temp = S;
            S = std::tanh(S / arr_T[i]);
            if (std::fabs(S - S_temp) < E_lim) break;
        }

        arr_S[i] = S;
        arr_E[i] = -S * S;
    }

    for (int i = 0; i < N - 1; ++i)
    {
        arr_C[i] = (arr_E[i + 1] - arr_E[i]) / dT;
        of << arr_T[i] << ' ' << arr_S[i] << ' ' << arr_E[i] << ' ' << arr_C[i] << std::endl;
    }

    return 0;
}