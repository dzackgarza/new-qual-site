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
- event: source-checked
  by: gpt-5.6-sol
  date: 2026-09-09
  note: Checked against Problem 2 of the official UCSD Fall 2018 real-analysis qualifying exam.
- event: solution-reviewed
  by: gpt-5.6-sol
  date: 2026-09-09
  note: Existing Bessel/weak-to-strong proof reviewed as correct; normalized legacy solution/proof block syntax.
---

::: {.problem}
Let $H$ be a Hilbert space and $\{\xi_n\}_n$ be a sequence of vectors in $H$ such that $\|\xi_n\| = 1$ for all $n$.

1. Assume that $\{\xi_n\}_n$ is an orthonormal set.
   Prove that $\xi_n$ converges weakly to $0$.

2. Assume that $\xi_n$ converges weakly to a vector $\xi \in H$ such that $\|\xi\| = 1$.
   Prove that $\lim_{n \to \infty} \|\xi_n - \xi\| = 0$.

Recall: $\xi_n$ converges weakly to $\xi$ iff $\langle \xi_n, \eta \rangle \to \langle \xi, \eta \rangle$ for every $\eta \in H$.
:::

::: {.solution}
**Part 1.**

::: pf

::: pf-step
For any $\eta \in H$, $\sum_{n} |\langle \xi_n, \eta \rangle|^2 \le \|\eta\|^2 < \infty$.

::: pf-proof
Bessel's inequality for the orthonormal set $\{\xi_n\}$.
:::

:::

::: {.pf-step #p1-s2}
Hence $\langle \xi_n, \eta \rangle \to 0$ for every $\eta \in H$.

::: pf-proof
the terms of a convergent series tend to $0$.
:::

:::

::: {.pf-step #p1-s3}
Therefore $\xi_n \rightharpoonup 0$ weakly.

::: pf-proof
step [](#p1-s2){.pf-ref} and the definition of weak convergence.
:::

:::

:::

**Part 2.**

::: pf

::: {.pf-step #p2-s1}
$\|\xi_n - \xi\|^2 = \|\xi_n\|^2 - 2\operatorname{Re}\langle \xi_n, \xi \rangle + \|\xi\|^2$.

::: pf-proof
expand the norm squared.
:::

:::

::: {.pf-step #p2-s2}
$\|\xi_n\|^2 = 1$ and $\|\xi\|^2 = 1$.

::: pf-proof
hypothesis.
:::

:::

::: {.pf-step #p2-s3}
$\langle \xi_n, \xi \rangle \to \langle \xi, \xi \rangle = \|\xi\|^2 = 1$.

::: pf-proof
weak convergence applied to $\eta = \xi$.
:::

:::

::: {.pf-step #p2-s4}
Hence $\|\xi_n - \xi\|^2 = 1 - 2\operatorname{Re}\langle \xi_n, \xi \rangle + 1 \to 1 - 2 + 1 = 0$.

::: pf-proof
step [](#p2-s1){.pf-ref}, step [](#p2-s2){.pf-ref}, and step [](#p2-s3){.pf-ref}.
:::

:::

::: {.pf-step #p2-s5}
Therefore $\|\xi_n - \xi\| \to 0$.

::: pf-proof
step [](#p2-s4){.pf-ref}.
:::

:::

::: pf-qed
step [](#p1-s3){.pf-ref} (part 1) and step [](#p2-s5){.pf-ref} (part 2).
:::

:::
:::
