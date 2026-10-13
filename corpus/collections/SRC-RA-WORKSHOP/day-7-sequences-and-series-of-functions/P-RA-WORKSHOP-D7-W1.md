---
schema: qual/card@1
id: P-RA-WORKSHOP-D7-W1
kind: problem
title: Stone–Weierstrass and a polynomial algebra with high-degree terms
classification:
  areas:
  - real-analysis
  topics:
  - Stone-Weierstrass
  - Polynomials
  - Function Spaces
relations:
- kind: uses
  target: T-RA-WORKSHOP-D7-6-7
review: draft
audit:
- event: solution-written
  by: gemini-3.7-flash
  date: 2026-08-25
---
::: {.problem}
Give a precise statement of the Stone–Weierstrass theorem for real-valued continuous functions.
Then, verify that the set of all polynomials of the form $$\left\{\sum_{j=2017}^{N}a_jx^j:N\in\mathbb N,\ N\ge2017,\ a_j\in\mathbb R\right\}$$ along with the zero function is an algebra over $[-2,2]\subset\mathbb R$.
:::

::: {.solution}
Write $X=[-2,2]$ and let $\mathcal A\subseteq C(X;\mathbb R)$ be the family of polynomial functions specified in the problem.

::: pf

::: {.pf-step #s1}

The real Stone–Weierstrass theorem states: if $K$ is compact Hausdorff and $B\subseteq C(K;\mathbb R)$ is an $\mathbb R$-subalgebra containing the constant functions and separating points of $K$, then $B$ is dense in $C(K;\mathbb R)$ in the uniform norm.

::: pf-proof

This is the unital real form of the Stone–Weierstrass theorem. Separation means that for every distinct $s,t\in K$ there exists $h\in B$ with $h(s)\ne h(t)$. The conclusion means that for every $u\in C(K;\mathbb R)$ and every $\varepsilon>0$ there exists $h\in B$ with $\|u-h\|_\infty<\varepsilon$.

:::

:::

::: {.pf-step #s2}

The family $\mathcal A$ consists precisely of the functions $x\mapsto x^{2017}q(x)$ for $q\in\mathbb R[x]$.

::: pf-proof

Every displayed polynomial in the problem factors as $x^{2017}\sum_{j=2017}^N a_jx^{j-2017}$. Conversely, multiplying any polynomial $q$ by $x^{2017}$ produces a polynomial with no terms of degree below $2017$. The choice $q=0$ includes the zero function.

:::

:::

::: {.pf-step #s3}

The family $\mathcal A$ is a (not necessarily unital) $\mathbb R$-subalgebra of $C(X;\mathbb R)$.

::: pf-proof

::: {.pf-step #s3-1}

The family $\mathcal A$ is an $\mathbb R$-vector subspace.

::: pf-proof

By step [](#s2){.pf-ref}, zero belongs to $\mathcal A$, and for polynomials $p,q$ and scalars $r,s\in\mathbb R$,
\[
r(x^{2017}p)+s(x^{2017}q)=x^{2017}(rp+sq)\in\mathcal A.
\]

:::

:::

::: {.pf-step #s3-2}

The family $\mathcal A$ is closed under pointwise multiplication.

::: pf-proof

For polynomials $p,q$,
\[
(x^{2017}p)(x^{2017}q)=x^{2017}(x^{2017}pq)\in\mathcal A
\]
by step [](#s2){.pf-ref}.

:::

:::

::: pf-qed

Steps [](#s3-1){.pf-ref} and [](#s3-2){.pf-ref} give the vector-space and multiplication axioms of an $\mathbb R$-subalgebra of $C(X;\mathbb R)$.

:::

:::

:::

::: {.pf-step #s4}

The algebra $\mathcal A$ is not unital and does not satisfy the hypotheses of step [](#s1){.pf-ref}.

::: pf-proof

Every member of $\mathcal A$ vanishes at $0$ by step [](#s2){.pf-ref}. Thus the constant function $1$ is not in $\mathcal A$. In particular, the unital hypothesis of step [](#s1){.pf-ref} fails. Indeed, $\mathcal A$ is not uniformly dense in $C(X;\mathbb R)$ because its uniform closure also consists of functions vanishing at $0$.

:::

:::

::: pf-qed

Step [](#s1){.pf-ref} supplies the requested theorem, and step [](#s3){.pf-ref} establishes that the displayed polynomial family is an algebra. Step [](#s4){.pf-ref} clarifies its nonunital status.

:::

:::

:::
