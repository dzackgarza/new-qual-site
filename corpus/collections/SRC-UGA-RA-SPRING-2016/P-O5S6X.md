---
schema: qual/card@1
id: P-O5S6X
kind: problem
title: The overlap $m(E\cap(E+x))$ is $L^1$, uniformly continuous, and vanishes at
  infinity
classification:
  areas:
  - real-analysis
  topics:
  - Convolution
  - Uniform Continuity
  - Measure Theory
relations: []
review: draft
audit:
- event: solution-written
  by: gemini-3.7-flash
  date: 2026-08-25
---

::: problem
Let $E \subset \RR$ be measurable with $m(E) < \infty$.
Define
\[
f(x)=m(E \cap(E+x)).
\]

Show that

1. $f\in L^1(\RR)$.

2. $f$ is uniformly continuous.

3. $\lim _{|x| \to \infty} f(x) = 0$.

> Hint:
\[
\chi_{E \cap(E+x)}(y)=\chi_{E}(y) \chi_{E}(y-x)
\]
:::
::: {.solution}
<1>1. $f(x) = m(E \cap (E + x)) = \int \chi_E(y)\chi_E(y - x)\,dy = (\chi_E \ast \tilde\chi_E)(x)$ where $\tilde\chi_E(y) = \chi_E(-y)$.
Proof: the hint: $\chi_{E\cap(E+x)}(y) = \chi_E(y)\chi_E(y - x)$; integrating in $y$ gives the convolution identity ($\chi_E \ast \tilde\chi_E$: $\int\chi_E(y)\tilde\chi_E(x - y)\,dy = \int\chi_E(y)\chi_E(y - x)\,dy$).

<1>2. (1) $f \in L^1(\RR)$ with $\int f = m(E)^2$.
Proof: Tonelli: $\int_\RR f(x)\,dx = \int_\RR\int_\RR \chi_E(y)\chi_E(y-x)\,dy\,dx = \int_\RR\chi_E(y)\left(\int_\RR\chi_E(y-x)\,dx\right)dy = \int_\RR\chi_E(y)\,m(E)\,dy = m(E)^2 < \infty$ (since $m(E) < \infty$).

<1>3. (2) $f$ is uniformly continuous.
Proof: $f = \chi_E \ast \tilde\chi_E$ is the convolution of two $L^1$ functions ($\chi_E, \tilde\chi_E \in L^1$ since $m(E) < \infty$); convolution of $L^1$ functions is uniformly continuous: $|f(x) - f(x')| \le \int\chi_E(y)|\tilde\chi_E(x-y) - \tilde\chi_E(x'-y)|\,dy \le \|\chi_E\|_\infty\|\tau_{x-x'}\tilde\chi_E - \tilde\chi_E\|_1 \to 0$ as $|x - x'| \to 0$ (strong continuity of translation in $L^1$).

<1>4. (3) $\lim_{|x| \to \infty} f(x) = 0$.
Proof: given $\eps > 0$, choose $R$ with $m(E \setminus [-R, R]) < \eps$ (possible since $m(E) < \infty$). For $|x| > 2R$: if $y \in E \cap (E + x)$, then $y \in E$ and $y - x \in E$; if $y \in [-R,R]$, then $|y - x| \ge |x| - |y| > R$, so $y - x \notin [-R, R]$.
Hence $E \cap (E+x) \subseteq (E \setminus [-R,R]) \cup ((E + x) \setminus [-R,R])$, and $f(x) = m(E \cap (E+x)) \le m(E\setminus[-R,R]) + m((E+x)\setminus[-R,R]) = m(E\setminus[-R,R]) + m(E \setminus [-R,R] + x) < 2\eps$ (translation invariance).

<1>5. Q.E.D. Proof: <1>2, <1>3, <1>4 establish (1), (2), (3).
:::
