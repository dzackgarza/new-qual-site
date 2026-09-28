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
<1>1. (a) $(\QQ,+)$ is not finitely generated.

<2>1. For $a_1,\ldots,a_k\in\ZZ$ and $b_1,\ldots,b_k\in\ZZ_{>0}$, put $B=\prod_{i=1}^k b_i$. Then $\left\langle \frac{a_1}{b_1},\ldots,\frac{a_k}{b_k}\right\rangle\subseteq\frac1B\ZZ$.

::: {.proof}
Every element of the subgroup is an integer combination
$$x = \sum_{i=1}^k c_i \frac{a_i}{b_i} = \frac{1}{B} \sum_{i=1}^k c_i a_i \left(\prod_{j \ne i} b_j\right) \in \frac{1}{B}\ZZ.$$
:::

<2>2. For every $B\in\ZZ_{>0}$, $\frac1B\ZZ\ne\QQ$.

::: {.proof}
Let $p$ be a prime with $p>B$. If $\frac1p=\frac mB$ with $m\in\ZZ$, then $B=mp$, so $p\mid B$, which contradicts $0<B<p$. Hence $\frac1p\notin\frac1B\ZZ$.
:::

<2>3. Q.E.D.

::: {.proof}
Every finite subset of $\QQ$ can be written as $\left\{\frac{a_1}{b_1},\ldots,\frac{a_k}{b_k}\right\}$ with $b_i>0$. By steps <2>1 and <2>2 the subgroup it generates is a proper subgroup of $\QQ$.
:::

<1>2. (b) $(\QQ,+)$ is not a free abelian group.

<2>1. $(\QQ,+)$ has no basis with exactly one element.

::: {.proof}
A free abelian group with a one-element basis is cyclic, hence finitely generated, which contradicts step <1>1.
:::

<2>2. No two distinct elements of $\QQ$ are $\ZZ$-linearly independent.

::: {.proof}
Let $x=\frac ab$ and $y=\frac cd$ be distinct elements of a candidate basis, with $a,b,c,d\in\ZZ\setminus\{0\}$; basis elements are nonzero. Then
$$(b c) x - (a d) y = (b c) \left(\frac{a}{b}\right) - (a d) \left(\frac{c}{d}\right) = a c - a c = 0,$$
and the coefficients $bc$ and $-ad$ are nonzero.
:::

<2>3. Q.E.D.

::: {.proof}
By step <2>1 a basis of $(\QQ,+)$ cannot have exactly one element, and by step <2>2 it cannot have two or more elements.
:::

<1>3. (c) $(\QQ,+)$ is a torsion-free abelian group that is not free.

::: {.proof}
For $n \in \ZZ \setminus \{0\}$ and $\frac{a}{b} \in \QQ$, $n \cdot \frac{a}{b} = \frac{n a}{b} = 0$ implies $n a = 0$, hence $a = 0$ and $\frac{a}{b} = 0$. So $(\QQ,+)$ is torsion-free. By step <1>2 it is not free, and by step <1>1 it is not finitely generated. Hence the statement "every torsion-free abelian group is free" is false.
:::
:::
