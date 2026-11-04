---
schema: qual/card@1
id: P-AKYLF
kind: problem
title: Residue fields of $\ZZ[x_1,\ldots,x_n]$ at maximal ideals are finite
classification:
  areas:
  - algebra
  topics:
  - Commutative Algebra
  - Fields
relations: []
review: draft
audit:
- event: source-checked
  by: claude
  date: 2026-11-01
  note: >-
    Statement read from the card in `corpus/collections/SRC-UW-ALG-2016`; it is the standard statement
    and no correction is claimed.
- event: solution-written
  by: claude
  date: 2026-11-01
  note: >-
    Proved that the residue field is finite, with the characteristic-zero case shown impossible: if
    $\operatorname{char}F=0$ then $F$ is a finitely generated $\QQ$-algebra, hence a number field by
    Zariski's lemma, and then $F=\ZZ[a_1,\dots,a_n]\subseteq\mathcal O_F[1/D]$ while $1/p\in F$ for a
    prime $p\nmid D$, a contradiction. In characteristic $p$, Zariski's lemma makes $F$ finite over
    $\FF_p$. Nothing is left in outline.
---

::: {.problem}
Let $\mathfrak m\subset\ZZ[x_1,\ldots,x_n]$ be a maximal ideal.
Show that $\ZZ[x_1,\ldots,x_n]/\mathfrak m$ is a finite field.
:::

::: {.solution}

Let $R=\ZZ[x_1,\dots,x_n]$, let $\mathfrak m$ be a maximal ideal, and put $F=R/\mathfrak m$, a field. Write $a_i$ for the image of $x_i$ in $F$, so that $F=\ZZ[a_1,\dots,a_n]$.

::: pf

::: {.pf-step #s1}

Zariski's lemma: if $k$ is a field and $A$ is a finitely generated $k$-algebra that is a field, then $A$ is a finite extension of $k$. A field that is finitely generated as a $\ZZ$-algebra is therefore finite.

::: pf-proof

The first statement is Zariski's lemma (Atiyah--Macdonald, *Introduction to Commutative Algebra*, Corollary 5.24), quoted here rather than reproved.

For the second: let $F$ be a field finitely generated as a $\ZZ$-algebra. Then $F$ has a characteristic, which is $0$ or a prime $p$. If $\operatorname{char}F=p$, then $\FF_p\subseteq F$ and $F$ is a finitely generated $\FF_p$-algebra that is a field, so $F$ is a finite extension of $\FF_p$ by Zariski's lemma, in particular $F$ is finite.

It remains to exclude $\operatorname{char}F=0$; this is done in step [](#s3){.pf-ref}.

:::

:::

::: {.pf-step #s2}

If $F$ has characteristic $0$, then $F$ is a finite extension of $\QQ$.

::: pf-proof

Since $\operatorname{char}F=0$ the prime field of $F$ is $\QQ$, so $\QQ\subseteq F$, and $F=\ZZ[a_1,\dots,a_n]=\QQ[a_1,\dots,a_n]$ is a finitely generated $\QQ$-algebra. Being a field, it is a finite extension of $\QQ$ by Zariski's lemma.

:::

:::

::: {.pf-step #s3}

$F$ cannot have characteristic $0$.

::: pf-proof

Suppose $\operatorname{char}F=0$. By step [](#s2){.pf-ref}, $F$ is a number field, so each $a_i$ is algebraic over $\QQ$. Choose a positive integer $D$ with $D\,a_i$ integral over $\ZZ$ for every $i$, for instance a common multiple of the denominators of the $a_i$ with respect to the ring of integers $\mathcal O_F$ of $F$; this is possible because each $a_i$ satisfies a monic polynomial with rational coefficients, whose clearing of denominators makes a suitable multiple integral.

Then
$$
F=\ZZ[a_1,\dots,a_n]\subseteq\mathcal O_F\Bigl[\frac1D\Bigr]=\Bigl\{\frac{x}{D^k}:x\in\mathcal O_F,\ k\ge0\Bigr\}\subseteq F .
$$
Choose a prime $p$ with $p\nmid D$; such a prime exists. Since $\operatorname{char}F=0$ we have $1/p\in F$. But $1/p\notin\mathcal O_F[1/D]$: if $1/p=x/D^k$ with $x\in\mathcal O_F$, then $D^k=px$, so $px\in\mathcal O_F\cap\QQ=\ZZ$, and $x\in\ZZ$; then $p\mid D^k$, hence $p\mid D$, contrary to the choice of $p$.

Thus $F=\ZZ[a_1,\dots,a_n]\subseteq\mathcal O_F[1/D]$ with $1/p\in F\setminus\mathcal O_F[1/D]$, a contradiction.

:::

:::

::: {.pf-step #s4}

$F$ is a finite field, i.e. the residue field of $\mathfrak m$ is finite.

::: pf-proof

By step [](#s3){.pf-ref}, $\operatorname{char}F=p$ for some prime $p$. Then $\FF_p\subseteq F$ and $F=R/\mathfrak m$ is generated as an $\FF_p$-algebra by the $a_i$, so by Zariski's lemma (step [](#s1){.pf-ref}) $F$ is a finite extension of $\FF_p$. A finite extension of a finite field is finite, so $F$ is a finite field.

:::

:::

:::

:::
