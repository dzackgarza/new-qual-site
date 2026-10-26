---
schema: qual/card@1
id: P-3UTDH
kind: problem
title: Galois theory of $x^3-11$ and $11^{1/3}+\sqrt{2}$
classification:
  areas:
  - algebra
  topics:
  - Galois Theory
  - Splitting Fields
  - Field Extensions
relations: []
review: draft
audit:
- event: solution-written
  by: gpt-5.6-sol
  date: 2026-09-10
---

::: {.problem}
Let $E\subset \CC$ denote the splitting field over $\QQ$ of the polynomial $x^3 - 11$.

a.
Prove that if $n>1$ is a squarefree positive integer, then $\sqrt{n}\not\in E$.

  > Hint: you can describe all quadratic extensions of $\QQ$ contained in $E$.

b.
Find the Galois group of $(x^3 - 11)(x^2 - 2)$ over $\QQ$.

c.
Prove that the minimal polynomial of $11^{1/3} + 2^{1/2}$ over $\QQ$ has degree 6.
:::

Let $a=\sqrt[3]{11}$ and let $\omega$ be a primitive cube root of unity.

::: pf

::: pf-step

The splitting field $E=\mathbb Q(a,\omega)$ has degree six and Galois group $S_3$.


::: pf-proof

Eisenstein's criterion at $11$ gives $[\mathbb Q(a):\mathbb Q]=3$. This cubic field is real, whereas $\omega$ is nonreal and has quadratic minimal polynomial $x^2+x+1$. Thus $[E:\mathbb Q]=6$. The irreducible cubic has three distinct roots, and its Galois group is a transitive subgroup of $S_3$ of order six, hence equals $S_3$.

:::

:::

::: pf-step

No square root $\sqrt n$ with squarefree positive $n>1$ belongs to $E$.


::: pf-proof

The group $S_3$ has exactly one subgroup of index two, namely $A_3$. The Galois correspondence therefore gives exactly one quadratic field inside $E$. Since $\mathbb Q(\omega)=\mathbb Q(\sqrt{-3})$ is quadratic, it is that unique field. If $\sqrt n\in E$, the real quadratic field $\mathbb Q(\sqrt n)$ would coincide with the nonreal field $\mathbb Q(\sqrt{-3})$, a contradiction.

:::

:::

::: pf-step

The splitting field of $(x^3-11)(x^2-2)$ has Galois group
\[
\boxed{S_3\times C_2}.
\]


::: pf-proof

Its splitting field is $E(\sqrt2)$. By step <1>2, $\mathbb Q(\sqrt2)$ is not contained in $E$, so their intersection is $\mathbb Q$. Both are finite Galois extensions of $\mathbb Q$, and the restriction isomorphism for their compositum gives
\[
\operatorname{Gal}(E(\sqrt2)/\mathbb Q)
\cong\operatorname{Gal}(E/\mathbb Q)\times
\operatorname{Gal}(\mathbb Q(\sqrt2)/\mathbb Q)\cong S_3\times C_2.
\]

:::

:::

::: pf-step

The minimal polynomial of $\theta=\sqrt[3]{11}+\sqrt2$ has degree
\[
\boxed{[\mathbb Q(\theta):\mathbb Q]=6}.
\]


::: pf-proof

The cubic field $\mathbb Q(a)$ cannot contain a quadratic extension of $\mathbb Q$, by the tower law. Thus $[\mathbb Q(a,\sqrt2):\mathbb Q]=6$. Expanding $(\theta-\sqrt2)^3=11$ yields
\[
(3\theta^2+2)\sqrt2=\theta^3+6\theta-11.
\]
As $\theta$ is real, the factor $3\theta^2+2$ is nonzero. Therefore $\sqrt2=(\theta^3+6\theta-11)/(3\theta^2+2)\in\mathbb Q(\theta)$ and $a=\theta-\sqrt2\in\mathbb Q(\theta)$. Consequently $\mathbb Q(\theta)=\mathbb Q(a,\sqrt2)$ and has degree six.

:::

:::

::: pf-qed

Steps <1>2, <1>3, and <1>4 establish parts (a), (b), and (c), respectively.

:::

:::
