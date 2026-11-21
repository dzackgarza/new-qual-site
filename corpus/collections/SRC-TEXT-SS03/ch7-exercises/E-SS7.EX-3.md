---
schema: qual/card@1
id: E-SS7.EX-3
kind: problem
title: $\sum_n\mu(n)n^{-s}=1/\zeta(s)$ for the Möbius function
classification:
  areas:
  - complex-analysis
  topics:
  - Zeta Function
  - Prime Number Theorem
  - Dirichlet Series
relations: []
review: draft
audit:
- event: solution-written
  by: gpt-5.6-sol
  date: 2026-09-11
- event: solution-written
  by: claude
  date: 2026-11-19
  note: >-
    Structured both parts into numbered steps and supplied the two convergence facts the prose used
    in passing: that the Euler product converges absolutely and locally uniformly for Re s > 1, so
    its inverse product may be expanded term by term, and that a divisor of a squarefree number is
    squarefree, which is what makes the product formula in (b) cover exactly the nonzero terms.
    Also recorded the multiplicativity of mu used in the expansion. Every macro used is one the
    preamble defines. Not checked this session: the printed statement page.

---

::: {.exercise}
In line with the previous exercise, we consider the Dirichlet series for $1/\zeta$.

(a) Prove that for $\Re(s) > 1$
$$
\frac{1}{\zeta(s)} = \sum_{n=1}^{\infty} \frac{\mu(n)}{n^s},
$$
where $\mu(n)$ is the Möbius function defined by
$$
\mu(n) = \begin{cases} 1 & \text{if } n = 1, \\ (-1)^k & \text{if } n = p_1 \cdots p_k \text{, and the } p_j \text{ are distinct primes,} \\ 0 & \text{otherwise.} \end{cases}
$$
Note that $\mu(nm) = \mu(n)\mu(m)$ whenever $n$ and $m$ are relatively prime. [Hint: Use the Euler product formula for $\zeta(s)$.]

(b) Show that
$$
\sum_{k \divides n} \mu(k) = \begin{cases} 1 & \text{if } n = 1, \\ 0 & \text{otherwise.} \end{cases}
$$
:::

::: {.solution}

The argument is the card's own; the statement is the exercise stored on the card, and no source text or solution set is retained for it.

Recall $\mu(1)=1$, $\mu(n)=(-1)^{k}$ when $n$ is a product of $k$ distinct primes, and $\mu(n)=0$ otherwise; $\mu$ is multiplicative for coprime arguments, since a prime factorization of $nm$ with $\gcd(n,m)=1$ is the union of those of $n$ and $m$.

::: pf

::: {.pf-step #euler}
For $\Re s>1$ the Euler product $\zeta(s)=\prod_{p}(1-p^{-s})^{-1}$ converges absolutely and locally uniformly, and so does its reciprocal $\prod_{p}(1-p^{-s})$.

::: pf-proof
$\sum_{p}\abs{p^{-s}}=\sum_{p}p^{-\Re s}\leq\sum_{n\geq2}n^{-\Re s}<\infty$ for $\Re s>1$, and on the half-plane $\Re s\geq1+\varepsilon$ this bound is uniform. A product $\prod_{p}(1+a_{p})$ with $\sum_{p}\abs{a_{p}}$ convergent converges absolutely and locally uniformly, and is nonzero when no $1+a_{p}$ vanishes; here $a_{p}=-p^{-s}$ and $1-p^{-s}\neq0$ for $\Re s>1$. The reciprocal product is therefore $\sum_{n}\mu(n)n^{-s}$ expanded, as the next step shows.
:::

:::

::: {.pf-step #expand}
$\prod_{p}(1-p^{-s})=\sum_{n\geq1}\mu(n)n^{-s}$.

::: pf-proof
Expanding the absolutely convergent product over all primes, a term is obtained by choosing, for each prime, either $1$ or $-p^{-s}$; only finitely many choices contribute to the coefficient of any $n^{-s}$ because finitely many primes divide $n$. A product $-p_{1}^{-s}\cdots-p_{k}^{-s}$ contributes $(-1)^{k}n^{-s}$ with $n=p_{1}\cdots p_{k}$ squarefree, and every squarefree $n$ arises exactly once; integers divisible by the square of a prime arise from no choice, and these are exactly the $n$ with $\mu(n)=0$. So the coefficient of $n^{-s}$ is $\mu(n)$.
:::

:::

::: {.pf-step #a}
$1/\zeta(s)=\sum_{n\geq1}\mu(n)n^{-s}$ for $\Re s>1$.

::: pf-proof
By steps [](#euler){.pf-ref} and [](#expand){.pf-ref}, $\prod_{p}(1-p^{-s})=\sum_{n}\mu(n)n^{-s}$ and this product is the reciprocal of the Euler product of $\zeta$, which equals $\zeta(s)$; dividing gives the identity. Both series converge absolutely on $\Re s>1$.
:::

:::

::: {.pf-step #squarefree-divisors}
A divisor of a squarefree integer is squarefree, and if $n=p_{1}\cdots p_{r}$ with distinct primes then the squarefree divisors of $n$ are the products $\prod_{j\in J}p_{j}$ over subsets $J\subseteq\{1,\dots,r\}$.

::: pf-proof
If $d\mid n$ and some prime $q$ had $q^{2}\mid d$, then $q^{2}\mid n$, contradicting squarefreeness. Conversely each such product of distinct primes divides $n$; distinct subsets give distinct products by uniqueness of prime factorization.
:::

:::

::: {.pf-step #b}
$\sum_{k\mid n}\mu(k)=1$ for $n=1$ and $0$ otherwise.

::: pf-proof
For $n=1$ the only divisor is $1$ and $\sum_{k\mid1}\mu(k)=\mu(1)=1$. For $n=p_{1}^{e_{1}}\cdots p_{r}^{e_{r}}>1$ with $r\geq1$, the terms with $\mu(k)\neq0$ are those with $k$ squarefree, and by step [](#squarefree-divisors){.pf-ref} they are the products over subsets $J$; so
$$
\sum_{k\mid n}\mu(k)=\sum_{J\subseteq\{1,\dots,r\}}(-1)^{\abs{J}}=\prod_{j=1}^{r}(1-1)=0,
$$
the first equality because a subset $J$ contributes $\mu\bigl(\prod_{j\in J}p_{j}\bigr)=(-1)^{\abs{J}}$, and the middle factorization being the binomial expansion of $(1-1)^{r}$.
:::

:::

:::

:::
