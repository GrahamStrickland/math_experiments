#include <math.h>
#include <stdio.h>
#include <stdlib.h>
#include <time.h>

float Q_rsqrt(float);
void benchmark(float);

int main(int argc, char *argv[]) {
  benchmark(4.0);
  benchmark(2.0);
  benchmark(0.15625);
  benchmark(0.01);

  return EXIT_SUCCESS;
}

void benchmark(float number) {
  float fastinvsqrt, invsqrt, start, elapsed;

  char eqs[30] = "=====";
  char line[31];
  sprintf(line, "%s%s%s%s%s%s", eqs, eqs, eqs, eqs, eqs, eqs);
  printf("%s\n", line);
  printf("Benchmark for %.10f\n", number);
  printf("%s\n", line);

  start = (float)clock() / CLOCKS_PER_SEC;
  fastinvsqrt = Q_rsqrt(number);
  elapsed = (float)clock() / CLOCKS_PER_SEC - start;

  printf("Q_rsqrt(%.10f) = %.10f\n", number, fastinvsqrt);
  printf("Elapsed time: %.10f\n", elapsed);

  start = (float)clock() / CLOCKS_PER_SEC;
  invsqrt = 1.0 / sqrt(number);
  elapsed = (float)clock() / CLOCKS_PER_SEC - start;

  printf("1.0 / sqrt(%.10f) = %.10f\n", number, invsqrt);
  printf("Elapsed time: %.10f\n", elapsed);

  printf("Absolute error = %.10f\n", fabs(invsqrt - fastinvsqrt));
  printf("Relative error = %.10f\n\n",
         fabs(invsqrt - fastinvsqrt) / fabs(invsqrt));
}

float Q_rsqrt(float number) {
  long i;
  float x2, y;
  const float threehalfs = 1.5F;

  x2 = number * 0.5F;
  y = number;
  i = *(long *)&y;           // evil floating point bit level hacking
  i = 0x5f3759df - (i >> 1); // what the fuck?
  y = *(float *)&i;
  y = y * (threehalfs - (x2 * y * y)); // 1st iteration
  // y  = y * ( threehalfs - ( x2 * y * y ) ); // 2nd iteration, this can be removed

  return y;
}
