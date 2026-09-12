---
schema: qual/card@1
id: E-SS3.EX-10
kind: problem
title: 'SS 3.10: $\int_0^\infty\frac{\log x}{x^2+a^2}\,dx$'
classification:
  areas:
  - complex-analysis
  topics: ['Meromorphic Functions', 'Residue Theorem', 'Argument Principle']
relations: []
review: draft
audit:
- event: solution-written
  by: gpt-5.6-sol
  date: 2026-09-11
---

::: exercise
10. Show that if $a > 0$ , then

$$
\int_ {0} ^ {\infty} \frac {\log x}{x ^ {2} + a ^ {2}} d x = \frac {\pi}{2 a} \log a.
$$

[Hint: Use the contour in Figure 10.]
:::

::: solution
Put $x=at$. Then
\[
I(a):=\int_0^\infty \frac{\log x}{x^2+a^2}\,dx
=\frac1a\int_0^\infty \frac{\log a+\log t}{1+t^2}\,dt.
\]
Now
\[
\int_0^\infty \frac{dt}{1+t^2}=\frac\pi2.
\]
Also, with $t=1/u$,
\[
\int_0^\infty \frac{\log t}{1+t^2}\,dt
=\int_\infty^0 \frac{-\log u}{1+u^{-2}}\frac{-du}{u^2}
=-\int_0^\infty \frac{\log u}{1+u^2}\,du,
\]
so this integral is $0$. Therefore
\[
I(a)=\frac1a\left(\log a\cdot\frac\pi2\right)=\frac{\pi}{2a}\log a.
\]
:::
