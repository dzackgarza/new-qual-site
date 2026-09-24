---
schema: qual/card@1
id: P-BKS81-6
kind: problem
title: Smooth dependence of simple polynomial roots on coefficients
classification:
  areas: [prelim]
  topics: []
relations: []
review: draft
audit:
- event: source-checked
  by: gpt-5.6-sol
  date: 2026-09-13
- event: solution-written
  by: chatgpt
  date: 2026-09-24
- event: solution-reviewed
  by: chatgpt
  date: 2026-09-24
  note: Checked simplicity of each original root, invertibility of the real z-derivative, the common implicit-function neighborhood, and preservation of degree n.
---

::: {.problem}
Suppose the complex polynomial
\[
\sum_{k=0}^n a_k z^k
\]
has $n$ distinct roots $r_1,\ldots,r_n\in\mathbb C$.
Prove that if the coefficients $b_k$ are sufficiently close to the corresponding $a_k$, then
\[
\sum_{k=0}^n b_k z^k
\]
has $n$ roots which are smooth functions of $b_0,\ldots,b_n$.
:::

::: {.solution}
Write
$$
p_a(z)\coloneqq\sum_{k=0}^n a_kz^k
$$
and, for a coefficient vector
$$
b=(b_0,\ldots,b_n)\in\CC^{n+1},
$$
write
$$
p_b(z)\coloneqq\sum_{k=0}^n b_kz^k.
$$

<1>1. Each root $r_i$ of $p_a$ is simple, so
$$
p_a'(r_i)\ne0.
$$

::: {.proof}
The polynomial has $n$ distinct roots and degree at most $n$. Hence it has
degree exactly $n$, and the listed roots account for all its roots without
multiplicity. Thus every $r_i$ is simple, which is equivalent to
$p_a'(r_i)\ne0$.
:::

<1>2. For each $i$, there are neighborhoods
$$
U_i\subset\CC^{n+1}
\quad\text{of }a
$$
and
$$
V_i\subset\CC
\quad\text{of }r_i,
$$
together with a smooth function
$$
\rho_i:U_i\longrightarrow V_i
$$
such that
$$
p_b(\rho_i(b))=0
$$
and $\rho_i(a)=r_i$.

::: {.proof}
Regard $\CC^{n+1}\times\CC$ and $\CC$ as real vector spaces and define
$$
\Phi(b,z)\coloneqq p_b(z).
$$
This is a smooth map. Its derivative in the $z$ variable at $(a,r_i)$ is
complex multiplication by
$$
p_a'(r_i).
$$
By step <1>1 this complex number is nonzero, so that real-linear map
$\CC\to\CC$ is invertible. The implicit function theorem therefore gives
the stated neighborhoods and smooth root function $\rho_i$.
:::

<1>3. The neighborhoods $V_1,\ldots,V_n$ may be chosen pairwise disjoint,
and there is one neighborhood
$$
U\subseteq\bigcap_{i=1}^nU_i
$$
of $a$ on which all $\rho_i$ are defined and $b_n\ne0$.

::: {.proof}
The roots $r_1,\ldots,r_n$ are distinct, so choose pairwise disjoint small
neighborhoods around them before applying step <1>2. Also $a_n\ne0$ by
step <1>1, since $p_a$ has degree $n$. The condition $b_n\ne0$ is open.
Intersect the finitely many coefficient neighborhoods from step <1>2 with
a sufficiently small neighborhood on which $b_n\ne0$.
:::

<1>4. For every $b\in U$, the polynomial $p_b$ has the $n$ distinct roots
$$
\boxed{\rho_1(b),\ldots,\rho_n(b)},
$$
and each root is a smooth function of
$$
b_0,\ldots,b_n.
$$

::: {.proof}
By step <1>2, each $\rho_i(b)$ is a root of $p_b$. Step <1>3 places these
roots in pairwise disjoint sets $V_i$, so they are distinct. The same step
gives $b_n\ne0$, hence $p_b$ has degree $n$. A degree-$n$ complex
polynomial cannot have more than $n$ distinct roots, so these are exactly
its $n$ roots. Their smooth dependence is exactly the conclusion of the
implicit function theorem in step <1>2.
:::

<1>5. Q.E.D.

::: {.proof}
Step <1>4 is the required conclusion for all coefficient vectors
sufficiently close to $a$.
:::
:::
