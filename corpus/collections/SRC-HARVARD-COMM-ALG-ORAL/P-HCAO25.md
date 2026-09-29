---
schema: qual/card@1
id: P-HCAO25
kind: problem
title: When the Hilbert function agrees with a polynomial
classification:
  areas:
  - algebra
  topics:
  - Hilbert Functions
  - Hilbert Polynomials
  - Graded Rings
relations: []
review: draft
audit:
- event: solution-written
  by: Codex 5.3 Spark Extra High
  date: 2026-08-30
---

::: {.problem}
Let $S=\bigoplus_{d=0}^{\infty} S_d$ be a graded ring.
State conditions on $S$ which ensure that its Hilbert function agrees with a polynomial for all sufficiently large $d$.
:::

::: {.solution}
A sufficient condition: $S_0=k$ is a field and $S$ is a \dfn{standard graded}
$k$-algebra, that is,
$$
S=k[x_1,\ldots,x_r],\qquad \deg x_i=1\quad(i=1,\ldots,r),
$$
for some $r\ge1$. The same proof applies with $S_0$ Artinian and $\dim_k$
replaced by length over $S_0$.

::: pf

::: pf-step
Each $S_d$ is a finite-dimensional $k$-vector space, so
$H(S,d)=\dim_kS_d$ is defined.

::: pf-proof
$S_d$ is spanned by the finitely many monomials of degree $d$ in
$x_1,\ldots,x_r$.
:::

:::

::: pf-step
There is $Q(t)\in\ZZ[t]$ with
$$
P(S,t)\coloneqq\sum_{d=0}^\infty(\dim_kS_d)\,t^d=\frac{Q(t)}{(1-t)^r}
\quad\text{in }\ZZ[[t]].
$$

::: pf-proof
This is the Hilbert--Serre theorem for a graded algebra generated over $k$ by
$r$ elements of degree $1$.
:::

:::

::: {.pf-step #hilbert-coefficient-formula}
Write $Q(t)=\sum_{j=0}^ma_jt^j$. For every $d\ge m$,
$$
\dim_kS_d=\sum_{j=0}^ma_j\binom{d-j+r-1}{r-1}.
$$

::: pf-proof
By the negative binomial expansion,
$$
\frac1{(1-t)^r}=\sum_{e=0}^\infty\binom{e+r-1}{r-1}t^e.
$$
Multiplying by $Q(t)$ and comparing coefficients of $t^d$ gives the formula;
for $d\ge m$ every index $d-j$ is nonnegative.
:::

:::

::: {.pf-step #hilbert-function-is-polynomial}
For $d\ge m$, $\dim_kS_d=P_S(d)$ for a single polynomial
$P_S\in\QQ[d]$, the Hilbert polynomial of $S$.

::: pf-proof
For each fixed $j$,
$$
\binom{d-j+r-1}{r-1}=\frac{(d-j+r-1)(d-j+r-2)\cdots(d-j+1)}{(r-1)!}
$$
is a polynomial in $d$ with rational coefficients. The finite sum in step
[](#hilbert-coefficient-formula){.pf-ref} is therefore a polynomial in $d$.
:::

:::

::: pf-qed
Step [](#hilbert-function-is-polynomial){.pf-ref} shows that the Hilbert function of a standard graded $k$-algebra
agrees with $P_S$ for all $d\ge\deg Q$.
:::

:::
:::
