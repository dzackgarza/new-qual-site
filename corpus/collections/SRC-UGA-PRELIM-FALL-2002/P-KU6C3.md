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
- event: solution-written
  by: claude
  date: 2026-11-19
  note: >-
    Every step now carries a pf-proof: the two containers state why their subclaims suffice, and the 7
    leaf steps that asserted a claim with no justification each carry a sentence deriving it. The
    arithmetic was recomputed: p = -3 and q = 2 give q^2/4 + p^3/27 = 1 - 1 = 0, hence s = 0 and
    A = -q/2 = -1; the three cube roots of -1 are -1, e^{i pi/3} and e^{-i pi/3}; and c + 1/c (since
    p = -3) gives -2, 1 and 1. Expanding (x-1)^2(x+2) returns x^3 - 3x + 2, so the three values are
    exactly the roots, the root 1 arising twice as the exercise says it should. The validity of the
    cubic formula is not proved, as the exercise instructs. Nothing in the statement was changed.
---

::: {.problem}
For the cubic polynomial $x^3 - 3x + 2$, use the cubic formula described below to find the root $1$.
[The roots of this cubic are $1$ (with multiplicity $2$) and $-2$.
You do not have to prove the validity of the cubic formula.]

For a cubic polynomial $x^3 + px + q$, the roots can all be found by the following formula, carried out in the complex number system.
Let $s$ be a square root of $q^2/4 + p^3/27$, set $A = -q/2 + s$, and then let $c$ be a cube root of $A$.
Then $c - p/3c$ is a root of $x^3 + px + q$.
:::

::: {.solution}

::: pf

::: pf-step
Identification of parameters:

::: pf-proof
The subclaims read off the coefficients and compute the two quantities the formula asks for.

::: pf-step
For the cubic polynomial $x^3 - 3x + 2$, the coefficients are $p = -3$ and $q = 2$.

::: pf-proof
Comparing with $x^3+px+q$: the coefficient of $x$ is $-3$ and the constant term is $2$; the coefficient of $x^2$ is $0$, which is what the formula requires.
:::

:::

::: pf-step
Compute the square root term $s$:
$$
s = \sqrt{\frac{q^2}{4} + \frac{p^3}{27}} = \sqrt{\frac{2^2}{4} + \frac{(-3)^3}{27}} = \sqrt{1 - 1} = 0.
$$

::: pf-proof
Substituting $q=2$ and $p=-3$ gives $q^2/4=4/4=1$ and $p^3/27=-27/27=-1$, so the radicand is $0$ and its square root is $0$.
:::

:::

::: pf-step
Compute $A$:
$$
A = -\frac{q}{2} + s = -\frac{2}{2} + 0 = -1.
$$

::: pf-proof
Substituting $q=2$ and $s=0$ into the definition $A=-q/2+s$.
:::

:::

:::

:::

::: pf-step
The three complex cube roots of $A = -1$:

::: pf-proof
The solutions to $c^3 = -1 = e^{i\pi}$ in $\CC$ are:

- $c_1 = -1$,
- $c_2 = e^{i\pi/3} = \frac{1 + i\sqrt{3}}{2}$,
- $c_3 = e^{-i\pi/3} = \frac{1 - i\sqrt{3}}{2}$.
:::

:::

::: pf-step
Computation of roots via $x = c - \frac{p}{3c} = c + \frac{1}{c}$:

::: pf-proof
The subclaims apply the formula to each of the three cube roots; the simplification $c-p/(3c)=c+1/c$ uses $p=-3$.

::: pf-step
**For $c_1 = -1$:**
$$
x_1 = c_1 + \frac{1}{c_1} = -1 + \frac{1}{-1} = -2.
$$

::: pf-proof
Substituting $c_1=-1$ into $c+1/c$.
:::

:::

::: pf-step
**For $c_2 = \frac{1 + i\sqrt{3}}{2}$:**
Since $\frac{1}{c_2} = \overline{c_2} = \frac{1 - i\sqrt{3}}{2}$:
$$
x_2 = c_2 + \frac{1}{c_2} = \frac{1 + i\sqrt{3}}{2} + \frac{1 - i\sqrt{3}}{2} = 1.
$$

::: pf-proof
$c_2=e^{i\pi/3}$ has modulus $1$, so $1/c_2=\overline{c_2}$; the sum of the two conjugates is twice the real part, namely $1$, and the imaginary parts cancel.
:::

:::

::: pf-step
**For $c_3 = \frac{1 - i\sqrt{3}}{2}$:**
Since $\frac{1}{c_3} = \overline{c_3} = \frac{1 + i\sqrt{3}}{2}$:
$$
x_3 = c_3 + \frac{1}{c_3} = \frac{1 - i\sqrt{3}}{2} + \frac{1 + i\sqrt{3}}{2} = 1.
$$

::: pf-proof
The same computation with the conjugate root, whose modulus is also $1$.
:::

:::

:::

:::

::: pf-step
Conclusion:
The cubic formula yields the roots $x = -2, 1, 1$, giving the root $1$ with multiplicity $2$ and the root $-2$, which factors $(x-1)^2(x+2) = x^3 - 3x + 2$.

::: pf-proof
The three values were produced by the formula from the three cube roots of $A$; expanding $(x-1)^2(x+2)=x^3+2x^2-2x^2-4x+x+2=x^3-3x+2$ confirms that they are exactly the roots, and the value $1$ asked for arises from $c_2$ and again from $c_3$.
:::

:::

:::

:::
