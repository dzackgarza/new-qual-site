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

::: {.solution}

Let $a=\sqrt[3]{11}$ and let $\omega$ be a primitive cube root of unity.

::: pf

::: {.pf-step #s1-1}

The splitting field $E=\QQ(a,\omega)$ has degree six and Galois group $S_3$.


::: pf-proof

Eisenstein's criterion at $11$ gives $[\QQ(a):\QQ]=3$. This cubic field is real, whereas $\omega$ is nonreal and has quadratic minimal polynomial $x^2+x+1$. Thus $[E:\QQ]=6$. The irreducible cubic has three distinct roots, and its Galois group is a transitive subgroup of $S_3$ of order six, hence equals $S_3$.

:::

:::

::: {.pf-step #s1-2}

No square root $\sqrt n$ with squarefree positive $n>1$ belongs to $E$.


::: pf-proof

The group $S_3$ has exactly one subgroup of index two, namely $A_3$. The Galois correspondence therefore gives exactly one quadratic field inside $E$. Since $\QQ(\omega)=\QQ(\sqrt{-3})$ is quadratic, it is that unique field. If $\sqrt n\in E$, the real quadratic field $\QQ(\sqrt n)$ would coincide with the nonreal field $\QQ(\sqrt{-3})$, a contradiction.

:::

:::

::: {.pf-step #s1-3}

The splitting field of $(x^3-11)(x^2-2)$ has Galois group
$$
\boxed{S_3\times C_2}.
$$


::: pf-proof

Its splitting field is $E(\sqrt2)$. By step [](#s1-2){.pf-ref}, $\QQ(\sqrt2)$ is not contained in $E$, so their intersection is $\QQ$. Both are finite Galois extensions of $\QQ$, and the restriction isomorphism for their compositum gives
$$
\operatorname{Gal}(E(\sqrt2)/\QQ)
\cong\operatorname{Gal}(E/\QQ)\times
\operatorname{Gal}(\QQ(\sqrt2)/\QQ)\cong S_3\times C_2.
$$

:::

:::

::: {.pf-step #s1-4}

The minimal polynomial of $\theta=\sqrt[3]{11}+\sqrt2$ has degree
$$
\boxed{[\QQ(\theta):\QQ]=6}.
$$


::: pf-proof

The cubic field $\QQ(a)$ cannot contain a quadratic extension of $\QQ$, by the tower law. Thus $[\QQ(a,\sqrt2):\QQ]=6$. Expanding $(\theta-\sqrt2)^3=11$ yields
$$
(3\theta^2+2)\sqrt2=\theta^3+6\theta-11.
$$
As $\theta$ is real, the factor $3\theta^2+2$ is nonzero. Therefore $\sqrt2=(\theta^3+6\theta-11)/(3\theta^2+2)\in\QQ(\theta)$ and $a=\theta-\sqrt2\in\QQ(\theta)$. Consequently $\QQ(\theta)=\QQ(a,\sqrt2)$ and has degree six.

:::

:::

::: pf-qed

Steps [](#s1-2){.pf-ref} and [](#s1-3){.pf-ref}, and [](#s1-4){.pf-ref} establish parts (a), (b), and (c), respectively.

:::

:::

:::
