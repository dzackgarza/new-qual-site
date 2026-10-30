---
schema: qual/card@1
id: E-SS9.EX-1
kind: problem
title: A meromorphic function with two periods of real ratio
classification:
  areas:
  - complex-analysis
  topics:
  - Elliptic Functions
  - Lattices
relations: []
review: draft
audit:
- event: solution-written
  by: gpt-5.6-sol
  date: 2026-09-11
---

::: {.exercise}
Suppose that a meromorphic function $f$ has two periods $\omega_1$ and $\omega_2$, with $\omega_2/\omega_1 \in \RR$.

(a) Suppose $\omega_2/\omega_1$ is rational, say equal to $p/q$, where $p$ and $q$ are relatively prime integers. Prove that as a result the periodicity assumption is equivalent to the assumption that $f$ is periodic with the simple period $\omega_0 = \frac{1}{q}\omega_1$. [Hint: Since $p$ and $q$ are relatively prime, there exist integers $m$ and $n$ such that $mq + np = 1$ (Corollary 1.3, Chapter 8, Book I).]

(b) If $\omega_2/\omega_1$ is irrational, then $f$ is constant. To prove this, use the fact that $\{m - n\tau\}$ is dense in $\RR$ whenever $\tau$ is irrational and $m, n$ range over the integers.
:::

::: {.solution}
Write $\tau=\omega_2/\omega_1\in\RR$.

For (a), suppose $\tau=p/q$ with $(p,q)=1$. If $f$ has period $\omega_0=\omega_1/q$, then both
$$
\omega_1=q\omega_0,\qquad \omega_2=p\omega_0
$$
are periods. Conversely, if $\omega_1$ and $\omega_2$ are periods, choose integers $m,n$ with
$$
mq+np=1.
$$
Then
$$
m\omega_1+n\omega_2
=\left(m+\frac{np}{q}\right)\omega_1
=\frac{mq+np}{q}\omega_1
=\omega_0.
$$
Integer linear combinations of periods are periods, so $\omega_0$ is a period. Thus the two periodicity conditions are equivalent.

For (b), suppose $\tau$ is irrational. The additive subgroup
$$
G=\{m-n\tau:m,n\in\ZZ\}
$$
is dense in $\RR$. Hence there is a sequence of nonzero periods
$$
h_j=(m_j-n_j\tau)\omega_1\longrightarrow0.
$$
A meromorphic function cannot have a pole: if $p$ were a pole, then every $p+h_j$ would also be a pole, producing distinct poles accumulating at $p$, contrary to isolatedness of poles. Thus $f$ is entire.

For every $z\in\CC$,
$$
f'(z)=\lim_{j\to\infty}\frac{f(z+h_j)-f(z)}{h_j}=0,
$$
because each $h_j$ is a period. Therefore $f'\equiv0$, so $f$ is constant.
:::
