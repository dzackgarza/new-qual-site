---
schema: qual/card@1
id: P-CAFA23F
kind: problem
title: "Zeros of partial sums of the exponential function"
classification:
  areas:
  - complex-analysis
  topics:
  - Complex Analysis
relations: []
review: draft
audit:
- event: solution-written
  by: Gemini 3.7 Flash
  date: 2026-08-30
---

::: problem
For each $N \in \mathbb{N}$, let $P_N(z) = \sum_{n=0}^{N} \frac{z^n}{n!}$.

(a) Show that the set $Z = \{z \in \mathbb{C} \mid P_N(z) = 0 \text{ for some } N \in \mathbb{N}\}$ is **discrete** (has no accumulation points in $\mathbb{C}$).

(b) Find a constant $c > 0$ such that $P_N(z)$ has no zeros in $\{z \in \mathbb{C} \mid |z| < cN\}$.
*(You may use the inequality $n! > e^{-n} n^n$.)*
:::

::: solution
**Goal:** Prove that the union of roots of all Taylor polynomials of $e^z$ is discrete by showing that roots escape to infinity at rate proportional to $N$.

<1>1. Remainder of the Exponential Series:
    *Proof:*
    <2>1. For any $z \in \mathbb{C}$, write $e^z = P_N(z) + R_N(z)$, where:
        $$R_N(z) = \sum_{n=N+1}^\infty \frac{z^n}{n!}.$$
    <2>2. If $P_N(z) = 0$, then:
        $$|e^z| = |R_N(z)|.$$
    <2>3. We estimate $|R_N(z)|$ from above when $|z| \le c N$ for some $0 < c < 1$:
        $$|R_N(z)| \le \sum_{n=N+1}^\infty \frac{|z|^n}{n!} = \frac{|z|^{N+1}}{(N+1)!} \left( 1 + \frac{|z|}{N+2} + \frac{|z|^2}{(N+2)(N+3)} + \cdots \right).$$
    <2>4. For $|z| \le c N$ where $c < 1$, each ratio satisfies $\frac{|z|}{N+k} \le \frac{cN}{N+k} \le c$, so the geometric series converges:
        $$1 + \frac{|z|}{N+2} + \frac{|z|^2}{(N+2)(N+3)} + \cdots \le \sum_{j=0}^\infty c^j = \frac{1}{1 - c}.$$
    <2>5. Using the given Stirling-type inequality $(N+1)! > e^{-(N+1)} (N+1)^{N+1}$:
        $$|R_N(z)| \le \frac{|z|^{N+1}}{(N+1)!} \frac{1}{1-c} < \frac{(cN)^{N+1}}{e^{-(N+1)} (N+1)^{N+1}} \frac{1}{1-c} \le \frac{1}{1-c} (c e)^{N+1}.$$

<1>2. Part (b): Finding the Constant $c > 0$:
    *Proof:*
    <2>1. On the other hand, for any $z = x + iy$ with $|z| \le c N$:
        $$|e^z| = e^{\operatorname{Re}(z)} = e^x \ge e^{-|z|} \ge e^{-cN}.$$
    <2>2. If $P_N(z) = 0$, then $|e^z| = |R_N(z)|$, which would force:
        $$e^{-cN} \le |R_N(z)| < \frac{1}{1-c} (ce)^{N+1}.$$
    <2>3. Multiplying both sides by $e^{cN}$:
        $$1 < \frac{ce}{1-c} (c e \cdot e^c)^N = \frac{ce}{1-c} (c e^{1+c})^N.$$
    <2>4. Consider the function $\phi(c) = c e^{1+c}$.
        - At $c = 0$, $\phi(0) = 0$.
        - Since $\phi$ is continuous, choose $c > 0$ sufficiently small so that $\phi(c) < 1$.
        - For example, choosing $c = 1/e^2 \approx 0.1353$:
          $$\phi(1/e^2) = \frac{1}{e^2} e^{1 + 1/e^2} = e^{-1 + 1/e^2} < e^{-1 + 0.5} = e^{-0.5} < 1.$$
    <2>5. For any such $c > 0$ with $c e^{1+c} < 1$, as $N \to \infty$, the term $(c e^{1+c})^N \to 0$, so for all $N \ge N_0$, $P_N(z)$ has no zeros with $|z| < cN$.
    <2>6. For small $N < N_0$, since $P_N(0) = 1 \ne 0$, $P_N$ has no zero in a ball around 0, so by shrinking $c$ if necessary (e.g. $c = 1/e^2$), $P_N(z) \ne 0$ for all $|z| < cN$ and all $N \ge 1$.

<1>3. Part (a): Discreteness of the Root Set $Z$:
    *Proof:*
    <2>1. To show that $Z$ has no accumulation points in $\mathbb{C}$, let $K \subset \mathbb{C}$ be any compact subset.
    <2>2. Since $K$ is bounded, there exists $R > 0$ such that $K \subseteq B(0, R)$.
    <2>3. By Part (b), if $N > R/c$, then all zeros of $P_N(z)$ satisfy $|z| \ge cN > R$, so $P_N(z)$ has **no zeros in $B(0, R)$**.
    <2>4. Therefore, the only polynomials that can have zeros in $K \subseteq B(0, R)$ are those with $N \le R/c$.
    <2>5. There are only finitely many such integers $N \in \{1, 2, \dots, \lfloor R/c \rfloor\}$.
    <2>6. Each $P_N(z)$ is a non-zero polynomial of degree $N$, so it has at most $N$ zeros.
    <2>7. Thus, $Z \cap K$ is a subset of the zeros of finitely many polynomials, which is a **finite set**.
    <2>8. Since the intersection of $Z$ with every compact set $K$ is finite, $Z$ has no accumulation points, so $Z$ is discrete.

<1>4. Conclusion:
    $Z$ is discrete and $P_N(z) \ne 0$ for $|z| < cN$ with $c = 1/e^2 > 0$. Q.E.D.
:::
