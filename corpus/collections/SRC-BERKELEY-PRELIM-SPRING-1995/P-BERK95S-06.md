---
schema: qual/card@1
id: P-BERK95S-06
kind: problem
title: Finite-index subrings have the same quotient modulo coprime integers
classification:
  areas:
  - prelim
  topics: []
relations: []
review: draft
audit:
- event: source-checked
  by: gpt-5.6-sol
  date: 2026-09-13
- event: solution-written
  by: chatgpt
  date: 2026-09-23
---

::: {.problem}
Let $R$ be a subring of a commutative ring $S$, and suppose the additive index $[S:R]$ is finite and equal to $n$. Let $m$ be an integer relatively prime to $n$. Prove that the natural map
\[
R/mR\longrightarrow S/mS
\]
is a ring isomorphism.
:::

::: {.solution}
Let
$$
A\coloneqq S/R
$$
be the finite additive quotient group. Then $\abs A=n$.

::: pf

::: {.pf-step #s1}

Multiplication by $m$ is an automorphism of the additive group
$A$.

::: pf-proof

Since $\gcd(m,n)=1$, choose integers $u,v$ with
$$
um+vn=1.
$$
For every $a\in A$, Lagrange's theorem gives $na=0$. Hence
$$
u(ma)=uma=(1-vn)a=a.
$$
Thus multiplication by $u$ is an inverse to multiplication by $m$ on
$A$.

:::

:::

::: {.pf-step #s2}

The natural map
$$
\phi:R/mR\longrightarrow S/mS
$$
is surjective.

::: pf-proof

Let $s\in S$. By step [](#s1){.pf-ref}, multiplication by $m$ is surjective on
$A$, so there is $t\in S$ such that
$$
m(t+R)=s+R.
$$
Equivalently,
$$
r\coloneqq s-mt\in R.
$$
Then $s-r=mt\in mS$, so $s+mS=r+mS$. Thus every class in $S/mS$ is
the image of a class from $R/mR$.

:::

:::

::: {.pf-step #s3}

The map $\phi$ is injective.

::: pf-proof

Suppose $r\in R$ maps to zero in $S/mS$. Then
$$
r=ms
$$
for some $s\in S$. In $A=S/R$ this says
$$
m(s+R)=r+R=0.
$$
Multiplication by $m$ is injective on $A$ by step [](#s1){.pf-ref}, so
$s+R=0$, hence $s\in R$. Therefore
$$
r=ms\in mR,
$$
and the class of $r$ in $R/mR$ is zero.

:::

:::

::: {.pf-step #s4}

The natural map is a ring isomorphism.

::: pf-proof

The map is induced by the inclusion $R\hookrightarrow S$, so it is a
ring homomorphism. Steps [](#s2){.pf-ref} and [](#s3){.pf-ref} show that it is bijective.

:::

:::

::: pf-qed

Step [](#s4){.pf-ref} proves the assertion.

:::

:::

:::
