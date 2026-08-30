---
schema: qual/card@1
id: P-KU6C3
kind: problem
title: Cubic formula for the roots of $x^3-3x+2$
classification:
  areas:
  - prelim
  topics:
  - Polynomials
relations: []
review: draft
audit:
- event: solution-written
  by: muse-spark-1.2
  date: 2026-08-30
---

::: {.problem}
For the cubic polynomial $x^3 - 3x + 2$, use the cubic formula described below to find the root $1$ (with multiplicity $2$) and $-2$.
You do not have to prove the validity of the cubic formula.]

For a cubic polynomial $x^3 + px + q$, the roots can all be found by the following formula, carried out in the complex number system.
Let $s$ be a square root of $q^2/4 + p^3/27$, set $A = -q/2 + s$, and then let $c$ be a cube root of $A$.
Then $c - p/3c$ is a root of $x^3 + px + q$.
:::

::: {.solution}
<1>1. Identification of parameters:
<2>1. For the cubic polynomial $x^3 - 3x + 2$, the coefficients are $p = -3$ and $q = 2$.
Proof: matching coefficients with $x^3 + px + q$.
<2>2. Compute the square root term $s$:
\[
s = \sqrt{\frac{q^2}{4} + \frac{p^3}{27}} = \sqrt{\frac{2^2}{4} + \frac{(-3)^3}{27}} = \sqrt{1 - 1} = 0.
\]
Proof: arithmetic evaluation.
<2>3. Compute $A$:
\[
A = -\frac{q}{2} + s = -\frac{2}{2} + 0 = -1.
\]
Proof: definition of $A$.

<1>2. The three complex cube roots of $A = -1$:
<2>1. The solutions to $c^3 = -1 = e^{i\pi}$ in $\mathbb{C}$ are:
- $c_1 = -1$,
- $c_2 = e^{i\pi/3} = \frac{1 + i\sqrt{3}}{2}$,
- $c_3 = e^{-i\pi/3} = \frac{1 - i\sqrt{3}}{2}$.
Proof: roots of unity multiplied by $-1$.

<1>3. Computation of roots via $x = c - \frac{p}{3c} = c + \frac{1}{c}$:
<2>1. **For $c_1 = -1$:**
\[
x_1 = c_1 + \frac{1}{c_1} = -1 + \frac{1}{-1} = -2.
\]
Proof: direct substitution.
<2>2. **For $c_2 = \frac{1 + i\sqrt{3}}{2}$:**
Since $\frac{1}{c_2} = \overline{c_2} = \frac{1 - i\sqrt{3}}{2}$:
\[
x_2 = c_2 + \frac{1}{c_2} = \frac{1 + i\sqrt{3}}{2} + \frac{1 - i\sqrt{3}}{2} = 1.
\]
Proof: sum of complex conjugate pair on unit circle.
<2>3. **For $c_3 = \frac{1 - i\sqrt{3}}{2}$:**
Since $\frac{1}{c_3} = \overline{c_3} = \frac{1 + i\sqrt{3}}{2}$:
\[
x_3 = c_3 + \frac{1}{c_3} = \frac{1 - i\sqrt{3}}{2} + \frac{1 + i\sqrt{3}}{2} = 1.
\]
Proof: sum of complex conjugate pair.

<1>4. Conclusion:
The cubic formula yields the roots $x = -2, 1, 1$, giving the root $1$ with multiplicity $2$ and the root $-2$, which factors $(x-1)^2(x+2) = x^3 - 3x + 2$. Q.E.D.
Proof: <1>1 through <1>3.
:::
