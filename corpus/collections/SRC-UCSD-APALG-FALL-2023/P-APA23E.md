---
schema: qual/card@1
id: P-APA23E
kind: problem
title: Reynolds operator with conjugate character on an irreducible complex $G$-module
classification:
  areas:
  - applied-algebra
  topics:
  - Representation Theory
  - Character Theory
  - Invariant Theory
relations: []
review: draft
---

::: {.problem}
Let $G$ be a finite group and let $V$ be a finite-dimensional $G$-module over $\mathbb{C}$.
Let $\chi \colon G \to \mathbb{C}$ be the character of $V$ and consider the linear operator $\varphi \colon V \to V$ given by
\[
\varphi(v) := \sum_{g \in G} \overline{\chi}(g)\, (g \cdot v),
\]
where $\overline{\chi}(g)$ denotes the complex conjugate of $\chi(g)$.
Assume that $V$ is irreducible.

Prove that there exists a complex number $c \in \mathbb{C}$ such that $\varphi(v) = cv$ for all $v \in V$, and find the value of $c$.
:::

::: {.solution}
Let $\rho:G\to\operatorname{GL}(V)$ be the representation and set
\[
z:=\sum_{g\in G}\overline{\chi(g)}\,g\in\mathbb C[G].
\]
Then $\varphi=\rho(z)$.

<1>1. The element $z$ is central in $\mathbb C[G]$.
::: {.proof}
Characters are class functions, so for every $h,g\in G$,
\[
\chi(hgh^{-1})=\chi(g).
\]
Therefore
\[
hzh^{-1}
=\sum_{g\in G}\overline{\chi(g)}\,hgh^{-1}
=\sum_{x\in G}\overline{\chi(x)}\,x
=z,
\]
where we reindexed by $x=hgh^{-1}$.
:::

<1>2. There exists $c\in\mathbb C$ such that
\[
\varphi=cI_V.
\]
::: {.proof}
By <1>1, $\rho(z)$ commutes with $\rho(h)$ for every $h\in G$. Since $V$ is irreducible over $\mathbb C$, Schur's lemma implies that every such endomorphism is scalar. Hence $\varphi=cI_V$.
:::

<1>3. The trace of $\varphi$ is $|G|$.
::: {.proof}
Using linearity of trace,
\[
\operatorname{tr}(\varphi)
=\sum_{g\in G}\overline{\chi(g)}\operatorname{tr}(\rho(g))
=\sum_{g\in G}\overline{\chi(g)}\chi(g)
=\sum_{g\in G}|\chi(g)|^2.
\]
For an irreducible complex character,
\[
\langle\chi,\chi\rangle_G
=\frac1{|G|}\sum_{g\in G}|\chi(g)|^2=1.
\]
Thus $\operatorname{tr}(\varphi)=|G|$.
:::

<1>4. Therefore
\[
\boxed{c=\frac{|G|}{\dim V}}.
\]
::: {.proof}
Since $\varphi=cI_V$ by <1>2,
\[
\operatorname{tr}(\varphi)=c\dim V.
\]
Combining this with <1>3 gives
\[
c\dim V=|G|,
\]
and hence the stated value of $c$.
:::
:::
