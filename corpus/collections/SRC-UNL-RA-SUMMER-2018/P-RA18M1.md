---
schema: qual/card@1
id: P-RA18M1
kind: problem
title: Convergence of $2n\cdot n!/n^n$ and of a series with $\cos(k!)/(k(k+1))$
classification:
  areas:
  - real-analysis
  topics:
  - Sequences of Numbers
  - Series of Numbers
  - Limits
relations: []
review: draft
---

:::{.problem}
Determine whether the following sequences converge and carefully justify your claims:
$$(i)\quad x_n=\frac{2n\cdot n!}{n^n};\qquad
(ii)\quad y_n=\sum_{k=1}^{n}\frac{\cos(k!)}{k(k+1)}.$$
:::

:::: {.solution}
> **AI-Generated Solution**
**Goal:** Determine convergence of (i) $x_n = \frac{2n\cdot n!}{n^n}$ and (ii) $y_n = \sum_{k=1}^n \frac{\cos(k!)}{k(k+1)}$.

<1>1. (i) $x_n \to 0$.
    <2>1. Split the product: $\frac{n!}{n^n} = \prod_{j=1}^{n}\frac{j}{n} \le \left(\frac12\right)^{\lfloor n/2\rfloor}$.
        Proof: for $j \le n/2$, $j/n \le 1/2$; there are at least $\lfloor n/2 \rfloor$ such factors, and the remaining factors are $\le 1$.
    <2>2. $0 \le x_n = 2n \cdot \frac{n!}{n^n} \le 2n \left(\frac12\right)^{n/2} \to 0$.
        Proof: <2>1 and the squeeze theorem (exponential decay $2^{-n/2}$ beats the linear factor $2n$).
    <2>3. Q.E.D.
        Proof: <2>2 shows $x_n \to 0$.

<1>2. (ii) $y_n$ converges.
    <2>1. $\left|\frac{\cos(k!)}{k(k+1)}\right| \le \frac{1}{k(k+1)}$.
        Proof: $|\cos| \le 1$.
    <2>2. $\sum_{k=1}^\infty \frac{1}{k(k+1)} = 1 < \infty$.
        Proof: telescoping: $\frac{1}{k(k+1)} = \frac1k - \frac{1}{k+1}$, so the partial sums are $1 - 1/(n+1) \to 1$.
    <2>3. $\sum_k \frac{\cos(k!)}{k(k+1)}$ converges absolutely, hence $y_n$ converges.
        Proof: comparison test with the convergent series of <2>2 using <2>1.
    <2>4. Q.E.D.
        Proof: <2>3 is convergence of $y_n$.

:::
