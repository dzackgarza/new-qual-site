---
schema: qual/card@1
id: P-4KTFN
kind: problem
title: Fatou's lemma, the dominated convergence theorem, and a sequence with $f_n\to
  0$ a.e. but $\int f_n\to 1$
classification:
  areas:
  - real-analysis
  topics:
  - Fatou
  - Convergence of Integrals
  - Counterexamples
relations: []
review: draft
solved: true
---

::: {.problem title="?"}
For this problem, consider just Lebesgue measurable functions $f : [0,1] \to \mathbb{R}$, together with the Lebesgue measure.

a. State Fatou's lemma (no proof required).
b. State and prove the Dominated Convergence Theorem.
c. Give an example where $f_n(x) \to 0$ a.e., but $\int_{-\infty}^{+\infty} f_n(x)dx \to 1$.
:::
::: {.solution}
> **AI-Generated Solution**

<1>1. (a) Fatou's lemma.
Proof: if $(f_n)$ is a sequence of non-negative measurable functions, then \[ \int \liminf_{n\to\infty} f_n \le \liminf_{n\to\infty} \int f_n . \] (Equivalently, for $f_n \ge 0$: $\int \liminf f_n \le \liminf \int f_n$.)
<1>2. (b) Statement of the Dominated Convergence Theorem.
Proof: let $f_n$ be measurable, $f_n \to f$ pointwise a.e., and suppose there is $g \in L^1$ with $|f_n| \le g$ a.e. for all $n$.
Then $f \in L^1$ and $\int f_n \to \int f$ (and $\int|f_n - f| \to 0$). <1>3. (b) Proof of the DCT. Proof: $|f| \le g$ a.e. by passing to the a.e. limit, so $f \in L^1$.
Since $|f_n - f| \le 2g$, Fatou's lemma applied to the non-negative functions $2g - |f_n - f|$ gives \[ \int 2g \le \liminf_{n\to\infty}\int\big(2g - |f_n - f|\big) = \int 2g - \limsup_{n\to\infty}\int |f_n - f|, \] so $\limsup\int|f_n - f| \le 0$, hence $\int|f_n - f| \to 0$ and $|\int f_n - \int f| \le \int|f_n - f| \to 0$.
<1>4. (c) Example: $f_n \to 0$ a.e. but $\int f_n \to 1$.
Proof: take $f_n = n\chi_{(0,1/n)}$ on $\RR$: $f_n(x) \to 0$ for every $x \ne 0$, i.e. a.e., but $\int f_n = n\cdot(1/n) = 1$ for all $n$, so $\int f_n \to 1 \ne 0$.
(This shows the DCT's domination hypothesis is essential: $\sup_n f_n$ is not integrable.)
<1>5. Q.E.D.
:::
