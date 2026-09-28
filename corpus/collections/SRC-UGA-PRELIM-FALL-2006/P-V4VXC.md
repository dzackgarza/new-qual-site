---
schema: qual/card@1
id: P-V4VXC
kind: problem
title: Maclaurin series of $xe^{2x}$ and a remainder bound on $[0,1/2]$
classification:
  areas:
  - prelim
  topics:
  - Taylor Series
  - Power Series
relations: []
review: draft
audit:
- event: solution-written
  by: gpt-5.6-sol
  date: 2026-09-10
---

::: {.problem}
a. Find the Maclaurin series expansion of $f(x) = xe^{2x}$ (that is, the Taylor series expansion of $f(x)$ about $a = 0$).
b. If $T_5(x)$ is the polynomial consisting of the terms of the Maclaurin series of $f(x)$ through degree 5, and $T_5(x)$ is used to approximate $f(x)$ on the interval $[0,1/2]$, find a bound for the maximum error $|f(x) - T_5(x)|$ on $[0,1/2]$.
:::

::: {.solution}
Since
\[
e^{2x}=\sum_{n=0}^\infty \frac{(2x)^n}{n!},
\]
we have
\[
xe^{2x}=\sum_{n=0}^\infty \frac{2^n}{n!}x^{n+1}.
\]
Thus
\[
T_5(x)=x+2x^2+2x^3+\frac43x^4+\frac23x^5.
\]

Taylor's theorem gives, for some $\xi$ between $0$ and $x$,
\[
f(x)-T_5(x)=\frac{f^{(6)}(\xi)}{6!}x^6.
\]
From the derivative formula,
\[
f^{(6)}(t)=64te^{2t}+192e^{2t}=(64t+192)e^{2t}.
\]
On $0\le t\le1/2$, this is increasing, so
\[
|f^{(6)}(t)|\le224e.
\]
Also $x^6\le(1/2)^6=1/64$. Therefore
\[
|f(x)-T_5(x)|\le \frac{224e}{6!\,64}=\frac{7e}{1440}
\]
for every $x\in[0,1/2]$.
:::
