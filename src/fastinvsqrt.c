#include <math.h>
#include <stdio.h>
#include <stdlib.h>
#include <time.h>

float Q_rsqrt(float);

int main(int argc, char *argv[]) {
  float fastinvsqrt, invsqrt, start, elapsed;

  start = (float)clock() / CLOCKS_PER_SEC;
  fastinvsqrt = Q_rsqrt(2.0);
  elapsed = (float)clock() / CLOCKS_PER_SEC - start;

  printf("Q_rsqrt(2.0) = %.10f\n", fastinvsqrt);
  printf("Elapsed time: %.10f\n", elapsed);

  start = (float)clock() / CLOCKS_PER_SEC;
  invsqrt = 1.0 / sqrt(2.0);
  elapsed = (float)clock() / CLOCKS_PER_SEC - start;

  printf("1.0 / sqrt(2.0) = %.10f\n", invsqrt);
  printf("Elapsed time: %.10f\n", elapsed);

  printf("Absolute error = %.10f\n", fabs(invsqrt - fastinvsqrt));
  printf("Relative error = %.10f\n",
         fabs(invsqrt - fastinvsqrt) / fabs(invsqrt));

  return EXIT_SUCCESS;
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
