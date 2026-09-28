---
schema: qual/card@1
id: P-BKF88-3
kind: problem
title: Decay in a triangular system of linear differential equations
classification:
  areas: [prelim]
  topics: []
relations: []
review: draft
audit:
- event: source-checked
  by: gpt-5.6-sol
  date: 2026-09-14
  note: Checked against Problem 3 in the deterministic MinerU Flash extraction assets/attachments/Fall88_extracted.md.
---

::: {.problem}
Let real-valued functions $f_1,\ldots,f_{n+1}$ on $\mathbb R$ satisfy
\[
f_{k+1}'+f_k'=(k+1)f_{k+1}-kf_k,
\qquad k=1,\ldots,n,
\]
and
\[
f_{n+1}'=-(n+1)f_{n+1}.
\]
Prove that for every $k$,
\[
\lim_{t\to\infty}f_k(t)=0.
\]
:::

::: {.solution}
<1>1. For every $k=1,\ldots,n+1$, there are constants $c_{k,j}\in\RR$, $j=k,\ldots,n+1$, such that
$$
f_k(t)=\sum_{j=k}^{n+1}c_{k,j}e^{-jt}.
$$

<2>1. The asserted representation holds for $k=n+1$.

::: {.proof}
The last differential equation is
$$
f_{n+1}'=-(n+1)f_{n+1}.
$$
Hence
$$
f_{n+1}(t)=c_{n+1,n+1}e^{-(n+1)t}
$$
for some constant $c_{n+1,n+1}\in\RR$.
:::

<2>2. Suppose the representation holds for $f_{k+1}$, where $1\leq k\leq n$. Then it also holds for $f_k$.

::: {.proof}
The $k$th equation may be rewritten as
$$
f_k'+k f_k=(k+1)f_{k+1}-f_{k+1}'.
$$
By the induction hypothesis,
$$
f_{k+1}(t)
=
\sum_{j=k+1}^{n+1}c_{k+1,j}e^{-jt},
$$
and therefore
$$
f_{k+1}'(t)
=
-\sum_{j=k+1}^{n+1}j c_{k+1,j}e^{-jt}.
$$
Thus
$$
f_k'+k f_k
=
\sum_{j=k+1}^{n+1}(k+1+j)c_{k+1,j}e^{-jt}.
$$
Multiplying by $e^{kt}$ gives
$$
\left(e^{kt}f_k(t)\right)'
=
\sum_{j=k+1}^{n+1}(k+1+j)c_{k+1,j}e^{-(j-k)t}.
$$
Since $j-k>0$, integration yields
$$
e^{kt}f_k(t)
=
c_{k,k}
-\sum_{j=k+1}^{n+1}
\frac{k+1+j}{j-k}
c_{k+1,j}e^{-(j-k)t}
$$
for some constant $c_{k,k}\in\RR$. Multiplying by $e^{-kt}$ gives
$$
f_k(t)
=
c_{k,k}e^{-kt}
+\sum_{j=k+1}^{n+1}c_{k,j}e^{-jt}
$$
after renaming the constant coefficients. This is the required representation.
:::

<2>3. Q.E.D.

::: {.proof}
Step <2>1 is the base case, and step <2>2 propagates the representation from $k+1$ to $k$. Downward induction from $n+1$ to $1$ proves step <1>1.
:::

<1>2. For every $k=1,\ldots,n+1$,
$$
\lim_{t\to\infty}f_k(t)=0.
$$

::: {.proof}
By step <1>1, $f_k$ is a finite linear combination of the functions
$$
e^{-kt},e^{-(k+1)t},\ldots,e^{-(n+1)t}.
$$
Every exponent is negative, so each of these functions tends to $0$ as $t\to\infty$. Hence their finite linear combination $f_k(t)$ also tends to $0$.
:::

<1>3. Q.E.D.

::: {.proof}
Step <1>2 is the required conclusion for every $k$.
:::
:::
