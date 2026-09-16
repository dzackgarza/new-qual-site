---
schema: qual/card@1
id: P-JHUSP07ANB
kind: problem
title: "The Poisson kernel integral by residues"
classification:
  areas:
  - complex-analysis
  topics:
  - Contour Integration
  - Poisson Kernel
relations: []
review: draft
audit:
- event: source-checked
  by: chatgpt
  date: 2026-09-10
  note: "Compared the denominator and strict parameter range with Spring 2007 problem 2 in the retained JHU source; removed the trailing parenthesis."
- event: solution-written
  by: chatgpt
  date: 2026-09-10
- event: solution-reviewed
  by: chatgpt
  date: 2026-09-10
  note: "Checked positivity of the real denominator, the unit-circle substitution, and the unique enclosed pole and its residue."
---

::: {.problem}
2) Calculate the integral $\textstyle \int _ { 0 } ^ { 2 \pi } { \frac { d \theta } { 1 - 2 a \cos \theta + a ^ { 2 } } }$ , where $0 < a < 1$
:::

::: {.solution}
The integral is $\boxed{2\pi/(1-a^2)}$.

<1>1. The unit-circle substitution produces a rational contour integral.

::: {.proof}
Since $0<a<1$, the real denominator is
$$
1-2a\cos\theta+a^2=|e^{i\theta}-a|^2\geq(1-a)^2>0,
$$
so the integral is an ordinary integral of a continuous
function. Put $z=e^{i\theta}$, which traverses the unit
circle counterclockwise, and use $d\theta=dz/(iz)$.
The denominator becomes
$1-a(z+z^{-1})+a^2=(z-a)(1-az)/z$. Therefore
$$
I=\int_{|z|=1}\frac{dz}{i(z-a)(1-az)}.
$$
:::

<1>2. The pole at $a$ gives the value.

::: {.proof}
The two poles are $a$ and $1/a$. Only $a$ lies inside
the unit circle, and neither lies on it. The enclosed
pole is simple, with residue $1/(i(1-a^2))$.
The residue theorem consequently gives
$$
I=2\pi i\frac1{i(1-a^2)}=\frac{2\pi}{1-a^2}
$$
[@SS03], as required.
:::
:::
