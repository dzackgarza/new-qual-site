---
schema: qual/card@1
id: P-JIQVA
kind: problem
title: Zeros of the truncated exponential $P_n$ and of $P_n-1$ in $|z|<10$
classification:
  areas:
  - complex-analysis
  topics:
  - Rouché
  - Zeros
  - Polynomials
  - Uniform Convergence
relations: []
review: draft
audit:
- event: solution-written
  by: gemini-3.7-flash
  date: 2026-08-17
---

::: problem
For each $n\in \ZZ^{\geq 1}$, let
\[
P_n(z) = 1 + z + {1\over 2!} z^2 + \cdots + {1\over n!}z^n
.\]
Show that for sufficiently large $n$, the polynomial $P_n$ has no zeros in $\abs{z} < 10$, while the polynomial $P_n(z) - 1$ has precisely 3 zeros there.
:::

::: {.solution}
**Goal:** With $P_n(z) = \sum_{k=0}^n \frac{z^k}{k!}$, show that for all large $n$, $P_n$ has no zeros in $\abs{z} < 10$ and $P_n - 1$ has exactly 3 zeros there.

<1>1. $P_n \to e^z$ uniformly on the circle $\abs{z} = 10$.
    Proof: $e^z - P_n(z) = \sum_{k=n+1}^\infty \frac{z^k}{k!}$, and $\abs{e^z - P_n(z)} \leq \sum_{k=n+1}^\infty \frac{10^k}{k!} \to 0$ as $n \to \infty$ (the tail of the convergent series $e^{10} = \sum 10^k/k!$).

<1>2. On $\abs{z} = 10$, $\abs{e^z} \geq e^{-10} > 0$.
    Proof: $\abs{e^z} = e^{\Re z} \geq e^{-\abs{z}} = e^{-10}$.

<1>3. For all sufficiently large $n$, $P_n$ has no zeros in $\abs{z} < 10$.
    Proof: Choose $n$ so that $\abs{e^z - P_n(z)} < e^{-10} \leq \abs{e^z}$ on $\abs{z} = 10$ (possible by <1>1 and <1>2). Rouch\'e's theorem applied to $e^z$ and $P_n - e^z$ shows $P_n$ and $e^z$ have equally many zeros in $\abs{z} < 10$; $e^z$ has none, so neither does $P_n$.

<1>4. $e^z - 1$ has exactly 3 zeros in $\abs{z} < 10$, all simple.
    Proof: The zeros of $e^z - 1$ are $z = 2\pi i k$, $k \in \ZZ$; those with $\abs{z} < 10$ are $k = -1, 0, 1$, i.e. $z = 0, \pm 2\pi i$, and each is simple since $\dv{z}(e^z - 1) = e^z \neq 0$ at each.

<1>5. On $\abs{z} = 10$, $\abs{e^z - 1} \geq m$ for some $m > 0$.
    Proof: $e^z - 1$ is continuous on the compact circle and has no zeros there (all zeros lie strictly inside by <1>4, since $\abs{2\pi i} \approx 6.28 < 10$ and $\abs{4\pi i} \approx 12.57 > 10$), so its minimum $m$ on the circle is positive.

<1>6. For all sufficiently large $n$, $P_n - 1$ has exactly 3 zeros in $\abs{z} < 10$.
    Proof: Write $P_n - 1 = (e^z - 1) - (e^z - P_n)$. Choose $n$ so that $\abs{e^z - P_n} < m$ on $\abs{z} = 10$ (by <1>1); then Rouch\'e with $f = e^z - 1$ and $g = -(e^z - P_n)$ gives that $P_n - 1$ and $e^z - 1$ have equally many zeros in $\abs{z} < 10$, namely 3 by <1>4.

<1>7. Q.E.D.
    Proof: <1>3 and <1>6 together establish both claims for all sufficiently large $n$.

:::
