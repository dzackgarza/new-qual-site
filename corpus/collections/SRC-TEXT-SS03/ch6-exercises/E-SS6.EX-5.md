---
schema: qual/card@1
id: E-SS6.EX-5
kind: problem
title: "SS 6.5: The absolute value of Gamma on the critical line"
classification:
  areas:
  - complex-analysis
  topics: ['Gamma Function', 'Zeta Function', 'Mellin Transform']
relations: []
review: draft
audit:
- event: solution-written
  by: gpt-5.6-sol
  date: 2026-09-11
---

::: {.exercise}
5. Use the fact that $\Gamma ( s ) \Gamma ( 1 - s ) = \pi /$ sin πs to prove that

$$
| \Gamma (1 / 2 + i t) | = \sqrt {\frac {2 \pi}{e ^ {\pi t} + e ^ {- \pi t}}}, \quad \mathrm{whenever} t \in \mathbb {R}.
$$
:::

::: {.solution}
Put
\[
s=\frac12+it.
\]
Then $1-s=\frac12-it=\overline s$. Since $\Gamma(\overline s)=\overline{\Gamma(s)}$,
\[
\Gamma(s)\Gamma(1-s)=|\Gamma(s)|^2.
\]
The reflection formula gives
\[
|\Gamma(1/2+it)|^2
=\frac{\pi}{\sin\pi(1/2+it)}.
\]
Now
\[
\sin\left(\frac\pi2+i\pi t\right)=\cosh(\pi t)
=\frac{e^{\pi t}+e^{-\pi t}}2.
\]
Therefore
\[
|\Gamma(1/2+it)|^2
=\frac{2\pi}{e^{\pi t}+e^{-\pi t}},
\]
and taking the positive square root yields
\[
\boxed{|\Gamma(1/2+it)|
=\sqrt{\frac{2\pi}{e^{\pi t}+e^{-\pi t}}}}.
\]
:::
