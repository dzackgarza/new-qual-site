---
schema: qual/card@1
id: P-EMQE3
kind: problem
title: Galois group of $x^4-2x^2+9$
classification:
  areas:
  - algebra
  topics:
  - Galois Theory
  - Splitting Fields
  - Polynomials
relations: []
review: draft
audit:
- event: solution-written
  by: OpenAI
  date: 2026-09-09
- event: solution-reviewed
  by: OpenAI
  date: 2026-09-09
---

::: problem
What is the Galois group of $x^4 - 2x^2 + 9$?
:::


::: {.solution}
Let
\[
f(x)=x^4-2x^2+9.
\]

<1>1. The polynomial $f$ is irreducible over $\QQ$.
::: {.proof}
By Gauss's lemma, if $f$ were reducible over $\QQ$, then since it is monic it would factor into monic polynomials in $\ZZ[x]$. It has no rational root, so any factorization would be into quadratics:
\[
f=(x^2+ax+b)(x^2+cx+d),
\qquad a,b,c,d\in\ZZ.
\]
Comparing the $x^3$-coefficient gives $c=-a$, and comparing the $x$-coefficient gives
\[
a(d-b)=0.
\]

If $a=0$, then $b+d=-2$ and $bd=9$, which has no integer solution. If $d=b$, then $b^2=9$. For $b=3$, the $x^2$-coefficient gives $6-a^2=-2$, so $a^2=8$, impossible in $\ZZ$; for $b=-3$, it gives $-6-a^2=-2$, so $a^2=-4$, also impossible. Hence $f$ is irreducible.
:::

<1>2. If $\alpha$ is any root of $f$, then $3/\alpha$ is also a root.
::: {.proof}
Since $\alpha\ne0$ and
\[
\alpha^4-2\alpha^2+9=0,
\]
we have
\[
\left(\frac3\alpha\right)^4
-2\left(\frac3\alpha\right)^2+9
=
\frac{9(\alpha^4-2\alpha^2+9)}{\alpha^4}=0.
\]
:::

<1>3. The field $\QQ(\alpha)$ already contains all four roots of $f$.
::: {.proof}
Because $f$ is even, $-\alpha$ is a root. By <1>2, $3/\alpha$ is a root, and then so is $-3/\alpha$. These four roots are distinct: equality $\alpha=\pm3/\alpha$ would imply $\alpha^2=\pm3$, neither of which satisfies $f$.

Thus the four roots are
\[
\pm\alpha,
\qquad
\pm\frac3\alpha,
\]
all of which lie in $\QQ(\alpha)$.
:::

<1>4. Therefore the splitting field is $L=\QQ(\alpha)$ and
\[
[L:\QQ]=4.
\]
::: {.proof}
By <1>1, the minimal polynomial of $\alpha$ has degree $4$, so $[\QQ(\alpha):\QQ]=4$. By <1>3 this field contains every root, hence is the splitting field.
:::

<1>5. The Galois group has at least two distinct nontrivial involutions.
::: {.proof}
Since $L$ is the splitting field of a separable polynomial over $\QQ$, $L/\QQ$ is Galois of degree $4$.

The embedding determined by
\[
\alpha\mapsto-\alpha
\]
is an automorphism $\tau$ of order $2$.
Likewise,
\[
\alpha\mapsto\frac3\alpha
\]
defines an automorphism $\sigma$ because $3/\alpha$ is another root and generates the same field. Moreover,
\[
\sigma^2(\alpha)
=
\frac{3}{3/\alpha}
=
\alpha,
\]
so $\sigma$ also has order $2$. These automorphisms are distinct.
:::

<1>6. Hence
\[
\operatorname{Gal}(f/\QQ)\cong C_2\times C_2.
\]
::: {.proof}
A group of order $4$ is either $C_4$ or $C_2\times C_2$. The cyclic group $C_4$ has exactly one element of order $2$, while <1>5 exhibits two distinct nontrivial involutions. Therefore the Galois group is the Klein four group.
:::
:::
