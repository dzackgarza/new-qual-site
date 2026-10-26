---
schema: qual/card@1
id: P-MAXAT-3-04
kind: problem
title: Maxim algebraic topology 3.4
classification:
  areas: [topology]
  topics: []
relations: []
review: draft
audit:
- event: source-checked
  by: gpt-5.6-sol
  date: 2026-09-12
  note: Checked against section 3, problem 4 of the retained Laurentiu Maxim Problems in Algebraic Topology PDF.
---

::: {.problem}
If there exists a division algebra on $\mathbb { R } ^ { n }$ , then $\mathbb { R } \mathbb { P } ^ { n - 1 }$ is orientable, hence $n = 2 ^ { r }$ , for some r.
:::

Let $A$ be an $n$-dimensional real division algebra. Only bilinearity of multiplication and the absence of zero divisors are needed.

::: pf

::: pf-step

For every nonzero $a\in A$, left multiplication
\[
L_a:A\to A,
\qquad x\longmapsto ax
\]
is a linear isomorphism.


::: pf-proof

Bilinearity makes $L_a$ linear. If $L_a(x)=0$, then $ax=0$. Since $A$ is a division algebra and $a\ne0$, this forces $x=0$, so $L_a$ is injective. A linear injective endomorphism of the finite-dimensional vector space $A$ is an isomorphism.

:::

:::

::: pf-step

Choose a basis $e_1,\ldots,e_n$ of $A$. For every $x\in A\setminus\{0\}$, the vectors
\[
e_1x,\ldots,e_nx
\]
form a basis of $A$.


::: pf-proof

Use right multiplication $R_x(a)=ax$. The same argument as in step <1>1 shows that $R_x$ is a linear isomorphism. It therefore sends the chosen basis to a basis.

:::

:::

::: pf-step

For $x\in S^{n-1}\subset A$, let $v_i(x)$ be the orthogonal projection of $e_ix$ to the tangent space
\[
T_xS^{n-1}=x^{\perp}.
\]
After choosing the basis with $e_1=1$ when the algebra is unital, the fields
\[
v_2,\ldots,v_n
\]
form a tangent frame of $S^{n-1}$.


::: pf-proof

With $e_1=1$, the first vector is $e_1x=x$, the radial direction. By step <1>2, $x,e_2x,\ldots,e_nx$ is a basis of $A$. If a linear combination of the tangent projections of $e_2x,\ldots,e_nx$ vanished, then the same linear combination of $e_ix$ would be a multiple of $x$, contradicting linear independence of the displayed basis. Thus the $n-1$ projected vectors form a basis of $x^\perp$. Their dependence on $x$ is continuous.

:::

:::

::: pf-step

Under the antipodal map $x\mapsto-x$, each vector field satisfies
\[
v_i(-x)=-v_i(x).
\]


::: pf-proof

Bilinearity gives $e_i(-x)=-(e_ix)$. Also $(-x)^\perp=x^\perp$, and orthogonal projection is linear, so projecting preserves the minus sign.

:::

:::

::: pf-step

The frame from step <1>3 descends through
\[
S^{n-1}\to\mathbb{RP}^{n-1}
\]
to a frame of $T\mathbb{RP}^{n-1}$. In particular, $\mathbb{RP}^{n-1}$ is orientable.


::: pf-proof

The differential of the antipodal deck transformation is $-I$ on tangent spaces. Step <1>4 says exactly that
\[
d(-I)_x(v_i(x))=v_i(-x),
\]
so each $v_i$ is equivariant and descends to the quotient. The descended $n-1$ vector fields remain pointwise linearly independent, hence trivialize the tangent bundle. A parallelizable manifold is orientable.

:::

:::

::: pf-step

The existence of the division-algebra multiplication also gives a nonsingular bilinear map
\[
\mu:\mathbb R^n\times\mathbb R^n\to\mathbb R^n,
\qquad
\mu(x,y)=xy,
\]
meaning $\mu(x,y)=0$ implies $x=0$ or $y=0$.


::: pf-proof

Bilinearity is part of the real algebra structure. The defining division property says that a product of two nonzero elements cannot be zero.

:::

:::

::: pf-step

By the classical Hopf--Stiefel theorem on nonsingular bilinear maps, such a map
\[
\mathbb R^n\times\mathbb R^n\to\mathbb R^n
\]
can exist only if $n$ is a power of $2$.


::: pf-proof

The Hopf--Stiefel obstruction says that a nonsingular bilinear map $\mathbb R^r\times\mathbb R^s\to\mathbb R^m$ forces the binomial coefficients in the formal inverse of $(1+x)^m$ to satisfy the corresponding mod-$2$ truncation obstruction. In the square case $r=s=m=n$, this is equivalent to the absence of a $1$ in the binary expansion of $n$ below its highest nonzero bit; hence
\[
n=2^r
\]
for some $r\ge0$. Applying it to the multiplication map of step <1>6 gives the claim.

:::

:::

::: pf-step

Therefore
\[
\boxed{
\mathbb{RP}^{n-1}\text{ is orientable and }n=2^r
\text{ for some }r.}
\]


::: pf-proof

Orientability is step <1>5, and the power-of-two restriction is step <1>7.

:::

:::

::: pf-qed

Step <1>8 is the required conclusion.

:::

:::
