---
schema: qual/card@1
id: P-RAF18B
kind: problem
title: "Weak convergence of unit vectors in a Hilbert space"
classification:
  areas:
  - real-analysis
  topics:
  - Real Analysis
relations: []
review: draft
audit:
- event: solution-written
  by: gemini-3.7-flash
  date: 2026-08-29
---

::: problem
Let $H$ be a Hilbert space and $\{\xi_n\}_n$ be a sequence of vectors in $H$ such that $\|\xi_n\| = 1$ for all $n$.

1. Assume that $\{\xi_n\}_n$ is an orthonormal set.
   Prove that $\xi_n$ converges weakly to $0$.

2. Assume that $\xi_n$ converges weakly to a vector $\xi \in H$ such that $\|\xi\| = 1$.
   Prove that $\lim_{n \to \infty} \|\xi_n - \xi\| = 0$.

Recall: $\xi_n$ converges weakly to $\xi$ iff $\langle \xi_n, \eta \rangle \to \langle \xi, \eta \rangle$ for every $\eta \in H$.
:::

::: {.solution}
**Part 1.**

<1>1. For any $\eta \in H$, $\sum_{n} |\langle \xi_n, \eta \rangle|^2 \le \|\eta\|^2 < \infty$.
Proof: Bessel's inequality for the orthonormal set $\{\xi_n\}$.

<1>2. Hence $\langle \xi_n, \eta \rangle \to 0$ for every $\eta \in H$.
Proof: the terms of a convergent series tend to $0$.

<1>3. Therefore $\xi_n \rightharpoonup 0$ weakly.
Proof: <1>2 and the definition of weak convergence.

**Part 2.**

<1>1. $\|\xi_n - \xi\|^2 = \|\xi_n\|^2 - 2\operatorname{Re}\langle \xi_n, \xi \rangle + \|\xi\|^2$.
Proof: expand the norm squared.

<1>2. $\|\xi_n\|^2 = 1$ and $\|\xi\|^2 = 1$.
Proof: hypothesis.

<1>3. $\langle \xi_n, \xi \rangle \to \langle \xi, \xi \rangle = \|\xi\|^2 = 1$.
Proof: weak convergence applied to $\eta = \xi$.

<1>4. Hence $\|\xi_n - \xi\|^2 = 1 - 2\operatorname{Re}\langle \xi_n, \xi \rangle + 1 \to 1 - 2 + 1 = 0$.
Proof: <1>1–<1>3.

<1>5. Therefore $\|\xi_n - \xi\| \to 0$.
Proof: <1>4.

<1>6. Q.E.D.
Proof: <1>3 (part 1) and <1>5 (part 2).
:::
