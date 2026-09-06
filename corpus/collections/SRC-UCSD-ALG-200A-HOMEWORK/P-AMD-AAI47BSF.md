---
schema: qual/card@1
id: P-AMD-AAI47BSF
kind: problem
title: If $N\normal G$ and $(|H|,[G:N])=1$, then $H\leq N$
classification:
  areas:
  - algebra
  topics:
  - Cosets and Lagrange
  - Normal Subgroups
  - Subgroups
relations: []
review: draft
audit:
- event: source-checked
  by: gpt-5.6-sol
  date: 2026-09-06
  note: >-
    Checked against the source-audited UCSD Math 200A Homework 1 occurrence and independently corroborated by the standard quotient-map proof of the coprime order/index lemma.
- event: solution-written
  by: gpt-5.6-sol
  date: 2026-09-06
- event: solution-reviewed
  by: gpt-5.6-sol
  date: 2026-09-06
  note: >-
    Restricted the quotient map G -> G/N to H. Its image is simultaneously a quotient of H and a subgroup of G/N, so its order divides both coprime integers |H| and [G:N]; the image is trivial and H lies in the kernel N.
---

::: {.problem}
Given: $|G| < \infty, \quad H \leq G, \quad N \normal G, (|H|, [G:N]) = 1$

Show: $H \leq N$
:::

::: {.solution}
Let
\[
\pi:G\longrightarrow G/N,
\qquad
\pi(g)=gN,
\]
be the quotient homomorphism, and restrict it to $H$.

<1>1. The integer $|\pi(H)|$ divides $|H|$.
::: {.proof}
The restriction
\[
\pi|_H:H\longrightarrow G/N
\]
has kernel
\[
\ker(\pi|_H)=H\cap N.
\]
By the first isomorphism theorem,
\[
\pi(H)\cong H/(H\cap N).
\]
Since $H$ is finite,
\[
|\pi(H)|=[H:H\cap N],
\]
which divides $|H|$ by Lagrange's theorem.
:::

<1>2. The integer $|\pi(H)|$ divides $[G:N]$.
::: {.proof}
The image $\pi(H)$ is a subgroup of the finite quotient group $G/N$.
Therefore Lagrange's theorem gives
\[
|\pi(H)|\mid|G/N|=[G:N].
\]
:::

<1>3. The image $\pi(H)$ is trivial.
::: {.proof}
By <1>1 and <1>2, $|\pi(H)|$ divides both $|H|$ and $[G:N]$.
The hypothesis says
\[
\gcd(|H|,[G:N])=1.
\]
Hence
\[
|\pi(H)|=1.
\]
Thus
\[
\pi(H)=\{N\}.
\]
:::

<1>4. Therefore $H\le N$.
::: {.proof}
By <1>3, every $h\in H$ satisfies
\[
\pi(h)=N,
\]
so $h\in\ker\pi=N$.
Hence
\[
H\subseteq N,
\]
that is,
\[
H\le N.
\]
:::
:::
