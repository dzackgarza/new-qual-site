---
schema: qual/card@1
id: P-6VN3T
kind: problem
title: An entire function of modulus $1$ on the unit circle is $e^{i\theta}z^n$
classification:
  areas:
  - complex-analysis
  topics:
  - Maximum Modulus Principle
  - Blaschke Factors
  - Entire Functions
  - Zeros
relations: []
review: draft
---

::: {.problem}
Assume $f$ is an entire function such that $\abs{f(z)}=1$ on $\abs{z}=1$.
Prove that $f(z)=e^{i \theta} z^{n}$, where $\theta$ is a real number and $n$ a non-negative integer.

> Suggestion: First use the maximum and minimum modulus theorem to show
$$
f(z)=e^{i \theta} \prod_{k=1}^{n} \frac{z-z_{k}}{1-\bar{z_{k}} z}
$$ 
if $f$ has zeros.

:::

::: {.solution}

::: pf

::: {.pf-step #zeros}

$f$ has finitely many zeros in $\overline\DD$, all in $\DD$.

::: pf-proof

$f\not\equiv0$ because $\abs{f}=1$ on $\abs{z}=1$, so its zeros are isolated, and a compact set contains only finitely many of them. None lies on $\abs{z}=1$.

:::

:::

::: {.pf-step #blaschke}

Let $z_1,\dots,z_n$ be the zeros of $f$ in $\DD$, listed with multiplicity ($n=0$ is allowed), and $B(z)=\prod_{k=1}^n\frac{z-z_k}{1-\bar z_kz}$. Then $f=e^{i\theta}B$ on $\overline\DD$ for some real $\theta$.

::: pf-proof

Each factor of $B$ is holomorphic on $\abs{z}<1/\abs{z_k}$ and has modulus $1$ on $\abs{z}=1$, so $\abs{B}=1$ there, and $B$ has the same zeros as $f$ in $\overline\DD$, with the same multiplicities. Hence $h=f/B$ is holomorphic and zero-free on a neighborhood of $\overline\DD$, with $\abs{h}=1$ on $\abs{z}=1$. The maximum modulus principle applied to $h$ and to $1/h$ gives $\abs{h}\le1$ and $\abs{1/h}\le1$ on $\DD$, so $\abs{h}\equiv1$. A holomorphic function of constant modulus on a domain is constant by the open mapping theorem, so $h\equiv e^{i\theta}$.

:::

:::

::: {.pf-step #origin}

Every $z_k$ equals $0$.

::: pf-proof

The functions $f$ and $e^{i\theta}B$ are holomorphic on $\CC$ minus the finite set $P=\{1/\bar z_k:z_k\neq0\}$ and agree on $\DD$ by Step [](#blaschke){.pf-ref}, so they agree on the connected set $\CC\setminus P$. If some $z_k\neq0$, then $B$ has a pole at $1/\bar z_k$: the numerator of $B$ vanishes only at the points $z_j\in\DD$, and $\abs{1/\bar z_k}>1$. Then $f$ is unbounded near $1/\bar z_k$, which is impossible for the entire function $f$.

:::

:::

::: pf-qed

By Steps [](#blaschke){.pf-ref} and [](#origin){.pf-ref}, $B(z)=z^n$, so $f(z)=e^{i\theta}z^n$ on $\overline\DD$, and on $\CC$ by the identity theorem.

:::

:::

:::
