---
schema: qual/card@1
id: P-CAFA15F
kind: problem
title: "Periods of meromorphic functions form a discrete subgroup"
classification:
  areas:
  - complex-analysis
  topics:
  - Complex Analysis
relations: []
review: draft
---

::: problem
Let $f(z)$ be a nonconstant meromorphic function.
A complex number $\omega$ is called a period of $f$ if $f(z + \omega) = f(z)$ for all $z$.

(i) Show that if $\omega_1$ and $\omega_2$ are periods of $f$, then $n_1\omega_1 + n_2\omega_2$ is a period of $f$ for all integers $n_1$ and $n_2$.

(ii) Show that there are at most finitely many periods of $f$ in any bounded subset of the complex plane.
:::

::: {.remark}
The official Fall 2015 exam omits the word "nonconstant." Without it, part (ii) is false: every complex number is a period of a constant meromorphic function.
:::

::: solution
Let
\[
\Lambda=\{\omega\in\mathbb C:f(z+\omega)=f(z)\text{ for all }z\}.
\]

For (i), $0\in\Lambda$, and if $\omega,\eta\in\Lambda$, then
\[
f(z+\omega+\eta)=f(z+\omega)=f(z),
\]
so $\omega+\eta\in\Lambda$. Also
\[
f(z-\omega)=f((z-\omega)+\omega)=f(z),
\]
so $-\omega\in\Lambda$. Thus $\Lambda$ is an additive subgroup of $\mathbb C$, and in particular every integer combination $n_1\omega_1+n_2\omega_2$ is a period.

For (ii), suppose a bounded set contained infinitely many periods. Then there is a convergent sequence of distinct periods $\omega_n\to\omega$. By continuity at every point where $f$ is finite,
\[
f(z+\omega)=\lim_{n\to\infty}f(z+\omega_n)=f(z),
\]
so $\omega$ is itself a period. Therefore
\[
\tau_n:=\omega_n-\omega
\]
are nonzero periods with $\tau_n\to0$.

Choose a regular point $z_0$ of $f$ and a disk $B(z_0,r)$ containing no pole. For every $z$ in a smaller disk and all sufficiently large $n$,
\[
f(z+\tau_n)=f(z).
\]
Hence
\[
f'(z)=\lim_{n\to\infty}\frac{f(z+\tau_n)-f(z)}{\tau_n}=0.
\]
Thus $f$ is constant on a nonempty open disk, hence constant everywhere by the identity theorem for meromorphic functions, contradicting the hypothesis. Therefore the period group is discrete, so every bounded subset of $\mathbb C$ contains only finitely many periods.
:::
