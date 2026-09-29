---
schema: qual/card@1
id: P-WUWUT
kind: problem
title: $(\QQ,+)$ is torsion-free but neither finitely generated nor free
classification:
  areas:
  - algebra
  topics:
  - Abelian Groups
  - Free Modules
  - Counterexamples
relations: []
review: draft
audit:
- event: solution-written
  by: muse-spark-1.2
  date: 2026-08-30
---

::: {.problem}
(a) Show that the additive group of rationals $(\mathbb{Q}, +)$ is not finitely generated.

(b) Show that $(\mathbb{Q}, +)$ is not a free abelian group.

(c) Conclude that the statement "every torsion-free abelian group is free" is false if the hypothesis "finitely generated" is omitted.
:::

::: {.solution}

::: pf

::: {.pf-step #s1}

(a) $(\QQ,+)$ is not finitely generated.

::: pf-proof

::: {.pf-step #s1-1}

For $a_1,\ldots,a_k\in\ZZ$ and $b_1,\ldots,b_k\in\ZZ_{>0}$, put $B=\prod_{i=1}^k b_i$. Then $\left\langle \frac{a_1}{b_1},\ldots,\frac{a_k}{b_k}\right\rangle\subseteq\frac1B\ZZ$.

::: pf-proof

Every element of the subgroup is an integer combination
$$x = \sum_{i=1}^k c_i \frac{a_i}{b_i} = \frac{1}{B} \sum_{i=1}^k c_i a_i \left(\prod_{j \ne i} b_j\right) \in \frac{1}{B}\ZZ.$$

:::

:::

::: {.pf-step #s1-2}

For every $B\in\ZZ_{>0}$, $\frac1B\ZZ\ne\QQ$.

::: pf-proof

Let $p$ be a prime with $p>B$. If $\frac1p=\frac mB$ with $m\in\ZZ$, then $B=mp$, so $p\mid B$, which contradicts $0<B<p$. Hence $\frac1p\notin\frac1B\ZZ$.

:::

:::

::: pf-qed

Every finite subset of $\QQ$ can be written as $\left\{\frac{a_1}{b_1},\ldots,\frac{a_k}{b_k}\right\}$ with $b_i>0$. By steps [](#s1-1){.pf-ref} and [](#s1-2){.pf-ref} the subgroup it generates is a proper subgroup of $\QQ$.

:::

:::

:::

::: {.pf-step #s2}

(b) $(\QQ,+)$ is not a free abelian group.

::: pf-proof

::: {.pf-step #s2-1}

$(\QQ,+)$ has no basis with exactly one element.

::: pf-proof

A free abelian group with a one-element basis is cyclic, hence finitely generated, which contradicts step [](#s1){.pf-ref}.

:::

:::

::: {.pf-step #s2-2}

No two distinct elements of $\QQ$ are $\ZZ$-linearly independent.

::: pf-proof

Let $x=\frac ab$ and $y=\frac cd$ be distinct elements of a candidate basis, with $a,b,c,d\in\ZZ\setminus\{0\}$; basis elements are nonzero. Then
$$(b c) x - (a d) y = (b c) \left(\frac{a}{b}\right) - (a d) \left(\frac{c}{d}\right) = a c - a c = 0,$$
and the coefficients $bc$ and $-ad$ are nonzero.

:::

:::

::: pf-qed

A basis of $(\QQ,+)$ is nonempty, since the empty set generates $0\ne\QQ$. By step [](#s2-1){.pf-ref} it cannot have exactly one element, and by step [](#s2-2){.pf-ref} it cannot have two or more elements.

:::

:::

:::

::: pf-step

(c) $(\QQ,+)$ is a torsion-free abelian group that is not free.

::: pf-proof

For $n \in \ZZ \setminus \{0\}$ and $\frac{a}{b} \in \QQ$, $n \cdot \frac{a}{b} = \frac{n a}{b} = 0$ implies $n a = 0$, hence $a = 0$ and $\frac{a}{b} = 0$. So $(\QQ,+)$ is torsion-free. By step [](#s2){.pf-ref} it is not free, and by step [](#s1){.pf-ref} it is not finitely generated. Hence the statement "every torsion-free abelian group is free" is false.

:::

:::

:::

:::
