---
schema: qual/card@1
id: E-SS6.EX-2
kind: problem
title: "SS 6.2: A Gamma product identity and the reflection formula"
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
2. Prove that

$$
\prod_ {n = 1} ^ {\infty} \frac {n (n + a + b)}{(n + a) (n + b)} = \frac {\Gamma (a + 1) \Gamma (b + 1)}{\Gamma (a + b + 1)}
$$

whenever a and b are positive.
Using the product formula for sin πs, give another proof that $\Gamma ( s ) \Gamma ( 1 - s ) = \pi /$ sin πs.
:::

::: {.solution}
For $N\ge1$, set
\[
P_N=\prod_{n=1}^N\frac{n(n+a+b)}{(n+a)(n+b)}.
\]
Using $\Gamma(z+1)=z\Gamma(z)$,
\[
\prod_{n=1}^N(n+a)=\frac{\Gamma(N+a+1)}{\Gamma(a+1)},
\]
and similarly for the other factors. Hence
\[
P_N=
\frac{\Gamma(N+1)\Gamma(N+a+b+1)}
{\Gamma(N+a+1)\Gamma(N+b+1)}
\cdot
\frac{\Gamma(a+1)\Gamma(b+1)}{\Gamma(a+b+1)}.
\]
The standard gamma-ratio asymptotic
\[
\frac{\Gamma(N+c)}{\Gamma(N+d)}\sim N^{c-d}
\]
shows that the first factor tends to $1$. Therefore
\[
\boxed{
\prod_{n=1}^\infty\frac{n(n+a+b)}{(n+a)(n+b)}
=\frac{\Gamma(a+1)\Gamma(b+1)}{\Gamma(a+b+1)}}.
\]

For the reflection formula, Euler's product gives
\[
\frac1{\Gamma(s)}=s e^{\gamma s}
\prod_{n=1}^\infty\left(1+\frac{s}{n}\right)e^{-s/n},
\]
and replacing $s$ by $-s$ gives
\[
\frac1{\Gamma(-s)}=-s e^{-\gamma s}
\prod_{n=1}^\infty\left(1-\frac{s}{n}\right)e^{s/n}.
\]
Multiplying,
\[
\frac1{\Gamma(s)\Gamma(-s)}
=-s^2\prod_{n=1}^\infty\left(1-\frac{s^2}{n^2}\right).
\]
The sine product
\[
\frac{\sin\pi s}{\pi s}
=\prod_{n=1}^\infty\left(1-\frac{s^2}{n^2}\right)
\]
therefore yields
\[
\frac1{\Gamma(s)\Gamma(-s)}=-\frac{s\sin\pi s}{\pi}.
\]
Since $\Gamma(1-s)=(-s)\Gamma(-s)$,
\[
\boxed{\Gamma(s)\Gamma(1-s)=\frac{\pi}{\sin\pi s}},
\]
first away from the integers and then as an identity of meromorphic functions.
:::
