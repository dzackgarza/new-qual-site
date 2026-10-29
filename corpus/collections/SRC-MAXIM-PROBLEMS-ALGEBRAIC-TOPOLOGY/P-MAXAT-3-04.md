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
If there exists a division algebra on $\RR ^ { n }$ , then $\RP ^ { n - 1 }$ is orientable, hence $n = 2 ^ { r }$ , for some r.
:::

::: {.solution}

Let $A$ be an $n$-dimensional real division algebra. Only bilinearity of multiplication and the absence of zero divisors are needed.

::: pf

::: {.pf-step #s1-1}

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

::: {.pf-step #s1-2}

Choose a basis $e_1,\ldots,e_n$ of $A$. For every $x\in A\setminus\{0\}$, the vectors
\[
e_1x,\ldots,e_nx
\]
form a basis of $A$.


::: pf-proof

Use right multiplication $R_x(a)=ax$. The same argument as in step [](#s1-1){.pf-ref} shows that $R_x$ is a linear isomorphism. It therefore sends the chosen basis to a basis.

:::

:::

::: {.pf-step #s1-3}

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

With $e_1=1$, the first vector is $e_1x=x$, the radial direction. By step [](#s1-2){.pf-ref}, $x,e_2x,\ldots,e_nx$ is a basis of $A$. If a linear combination of the tangent projections of $e_2x,\ldots,e_nx$ vanished, then the same linear combination of $e_ix$ would be a multiple of $x$, contradicting linear independence of the displayed basis. Thus the $n-1$ projected vectors form a basis of $x^\perp$. Their dependence on $x$ is continuous.

:::

:::

::: {.pf-step #s1-4}

Under the antipodal map $x\mapsto-x$, each vector field satisfies
\[
v_i(-x)=-v_i(x).
\]


::: pf-proof

Bilinearity gives $e_i(-x)=-(e_ix)$. Also $(-x)^\perp=x^\perp$, and orthogonal projection is linear, so projecting preserves the minus sign.

:::

:::

::: {.pf-step #s1-5}

The frame from step [](#s1-3){.pf-ref} descends through
\[
S^{n-1}\to\RP^{n-1}
\]
to a frame of $T\RP^{n-1}$. In particular, $\RP^{n-1}$ is orientable.


::: pf-proof

The differential of the antipodal deck transformation is $-I$ on tangent spaces. Step [](#s1-4){.pf-ref} says exactly that
\[
d(-I)_x(v_i(x))=v_i(-x),
\]
so each $v_i$ is equivariant and descends to the quotient. The descended $n-1$ vector fields remain pointwise linearly independent, hence trivialize the tangent bundle. A parallelizable manifold is orientable.

:::

:::

::: {.pf-step #s1-6}

The existence of the division-algebra multiplication also gives a nonsingular bilinear map
\[
\mu:\RR^n\times\RR^n\to\RR^n,
\qquad
\mu(x,y)=xy,
\]
meaning $\mu(x,y)=0$ implies $x=0$ or $y=0$.


::: pf-proof

Bilinearity is part of the real algebra structure. The defining division property says that a product of two nonzero elements cannot be zero.

:::

:::

::: {.pf-step #s1-7}

By the classical Hopf--Stiefel theorem on nonsingular bilinear maps, such a map
\[
\RR^n\times\RR^n\to\RR^n
\]
can exist only if $n$ is a power of $2$.


::: pf-proof

The Hopf--Stiefel obstruction says that a nonsingular bilinear map $\RR^r\times\RR^s\to\RR^m$ forces the binomial coefficients in the formal inverse of $(1+x)^m$ to satisfy the corresponding mod-$2$ truncation obstruction. In the square case $r=s=m=n$, this is equivalent to the absence of a $1$ in the binary expansion of $n$ below its highest nonzero bit; hence
\[
n=2^r
\]
for some $r\ge0$. Applying it to the multiplication map of step [](#s1-6){.pf-ref} gives the claim.

:::

:::

::: {.pf-step #s1-8}

Therefore
\[
\boxed{
\RP^{n-1}\text{ is orientable and }n=2^r
\text{ for some }r.}
\]


::: pf-proof

Orientability is step [](#s1-5){.pf-ref}, and the power-of-two restriction is step [](#s1-7){.pf-ref}.

:::

:::

::: pf-qed

Step [](#s1-8){.pf-ref} is the required conclusion.

:::

:::

:::
