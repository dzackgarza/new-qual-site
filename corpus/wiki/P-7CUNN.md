---
schema: qual/card@1
id: P-7CUNN
kind: problem
title: Integrals of rational functions by long division and partial fractions
classification:
  areas:
  - prelim
  topics:
  - Integrals
  - Partial Fractions
relations: []
review: draft
---

::: problem
1. $\displaystyle \int \frac {x^3 + 4x^2}{x^2 + 4x + 3} ~dx = \color{blue} {\frac {1}{2} x^2 - \frac {9}{2} \ln (x + 3) + \frac {3}{2} \ln (x+1)}$

- **Solution:** $\frac {x^3 + 4x^2}{x^2 + 4x + 3} = x - \frac {9}{2} \cdot \frac {1}{x + 3} + \frac {3}{2} \cdot \frac {1}{x + 1}$

2. $\displaystyle \int \frac {2x^3 + 2x^2 - 9x - 1}{x^2 + x - 6} ~dx = \color{blue} {x^2 +2 \ln (x + 3) + \ln (x - 2)}$

- **Solution:** $\frac {2x^3 + 2x^2 - 9x - 1}{x^2 + x - 6} = 2x + 2 \cdot \frac {1}{x + 3} + \frac {1}{x - 2}$

- **Used 2019**, *Unsolved*

3. $\displaystyle \int \frac {x^3 - x^2 -3x +1}{x^2 - x - 6} ~dx = \color{blue} {\frac {1}{2} x^2 + 2 \ln (x - 3) + \ln (x + 2)}$

- **Solution:** $\frac {x^3 - x^2 -3x +1}{x^2 - x - 6} = x + 2 \cdot \frac {1}{x - 3} + \frac {1}{x + 2}$

4. $\displaystyle \int \frac {3x^3 - 12x^2 + 15x - 5}{x^2 - 4x + 4} ~dx = \color{blue} {\frac {3}{2} x^2 + 3 \ln (x - 2) - \frac {1}{x - 2}}$

- **Solution:** $\frac {3x^3 - 12x^2 + 15x - 5}{x^2 - 4x + 4} = 3x + 3 \cdot \frac {1}{x - 2} + \frac {1}{(x - 2)^2}$

5. $\displaystyle \int \frac {x(x^2 - 3x + 5)}{x^2 - 2x + 1} ~dx = \color{blue} {\frac {1}{2} x^2 - x + \ln (x - 1) - \frac {3}{x - 1}}$

- **Solution:** $\frac {x(x^2 - 3x + 5)}{x^2 - 2x + 1} = x - 1 + 2 \cdot \frac {1}{x - 1} + 3 \cdot \frac {1}{(x - 1)^2}$

6. $\displaystyle \int \frac {x^3 -4x^2 + 2x - 3}{x+2} ~dx = \color{blue} {\frac 1 3 x^3 -3x^2 + 14x - 31\ln(x+2)}$

- **Solution:** $\frac {x^3 - 4x^2 + 2x - 3}{x+2} = x^2 - 6x + 14 - 31 \cdot \frac {1}{x + 2}$

- **Used 2018**, *Unsolved*

7. $\displaystyle \int \frac {x^4 - 2x^3 - 8x^2 + 2x + 10 }{x^2 - 2x - 8} ~dx =  \color{blue} {\frac {1}{3} x^3 + 3 \ln (x - 4) - \ln (x + 2)}$

- **Solution:** $\frac {x^4 - 2x^3 - 8x^2 + 2x + 10 }{x^2 - 2x - 8} = x^2 + 3 \cdot \frac {1}{x - 4} - \frac {1}{x + 2}$
:::

::: {.solution}
> **AI-Generated Solution** (Gemini 3.7 Flash)

**Goal:** Evaluate indefinite integrals of rational functions using polynomial long division and partial fraction decomposition.

<1>1. Evaluation of $\int \frac{x^3 + 4x^2}{x^2 + 4x + 3} \, dx$: Proof: <2>1. Long division: $x^3 + 4x^2 = x(x^2 + 4x + 3) - 3x$, so $\frac{x^3 + 4x^2}{x^2 + 4x + 3} = x - \frac{3x}{(x+1)(x+3)}$.
<2>2. Partial fractions: $-\frac{3x}{(x+1)(x+3)} = \frac{A}{x+1} + \frac{B}{x+3} \implies -3x = A(x+3) + B(x+1)$.
Setting $x = -1 \implies 3 = 2A \implies A = 3/2$.
Setting $x = -3 \implies 9 = -2B \implies B = -9/2$.
<2>3. Integrating: $\int \left(x + \frac{3/2}{x+1} - \frac{9/2}{x+3}\right) dx = \frac{1}{2}x^2 + \frac{3}{2}\ln|x+1| - \frac{9}{2}\ln|x+3| + C$.

<1>2. Evaluation of $\int \frac{2x^3 + 2x^2 - 9x - 1}{x^2 + x - 6} \, dx$: Proof: <2>1. Long division: $2x^3 + 2x^2 - 9x - 1 = 2x(x^2 + x - 6) + (3x - 1)$.
<2>2. Partial fractions: $\frac{3x-1}{(x+3)(x-2)} = \frac{A}{x+3} + \frac{B}{x-2} \implies 3x - 1 = A(x-2) + B(x+3)$.
Setting $x = 2 \implies 5 = 5B \implies B = 1$.
Setting $x = -3 \implies -10 = -5A \implies A = 2$.
<2>3. Integrating: $\int \left(2x + \frac{2}{x+3} + \frac{1}{x-2}\right) dx = x^2 + 2\ln|x+3| + \ln|x-2| + C$.

<1>3. Evaluation of $\int \frac{3x^3 - 12x^2 + 15x - 5}{(x-2)^2} \, dx$: Proof: <2>1. Substitute $u = x - 2 \implies x = u + 2, dx = du$.
<2>2. $3(u+2)^3 - 12(u+2)^2 + 15(u+2) - 5 = 3(u^3 + 6u^2 + 12u + 8) - 12(u^2 + 4u + 4) + 15(u+2) - 5 = 3u^3 + 6u^2 + 3u + 1$.
<2>3. Dividing by $u^2$: $3u + 6 + \frac{3}{u} + \frac{1}{u^2}$.
<2>4. Integrating: $\frac{3}{2}u^2 + 6u + 3\ln|u| - \frac{1}{u} + C = \frac{3}{2}(x-2)^2 + 6(x-2) + 3\ln|x-2| - \frac{1}{x-2} + C = \frac{3}{2}x^2 + 3\ln|x-2| - \frac{1}{x-2} + C'$.
Q.E.D.
:::
