---
schema: qual/card@1
id: P-G5MEU
kind: problem
title: Degree, Galois group, and intermediate fields of $\QQ(\sqrt{2}+\sqrt{5})/\QQ$
classification:
  areas:
  - algebra
  topics:
  - Galois Theory
  - Field Extensions
relations: []
review: draft
audit:
- event: solution-written
  by: gpt-5.6-sol
  date: 2026-09-10
---

::: {.problem}
Let $K = \QQ[\sqrt 2 + \sqrt 5]$.

a. Find $[K: \QQ]$.

b. Show that $K/\QQ$ is Galois, and find the Galois group $G$ of $K/\QQ$.

c. Exhibit explicitly the correspondence between subgroups of $G$ and intermediate fields between $\QQ$ and $K$.
:::

::: {.solution}
Set $\theta=\sqrt2+\sqrt5$.

<1>1. The extension has degree
\[
\boxed{[K:\mathbb Q]=4}.
\]

::: {.proof}
From $\theta^2=7+2\sqrt{10}$ follows $\sqrt{10}=(\theta^2-7)/2\in K$. Since $\theta\sqrt{10}=5\sqrt2+2\sqrt5$, subtracting $2\theta$ yields $3\sqrt2=\theta(\sqrt{10}-2)\in K$. Consequently $\sqrt5=\theta-\sqrt2\in K$, and $K=\mathbb Q(\sqrt2,\sqrt5)$. Were $\sqrt5=a+b\sqrt2$ for rational $a,b$, squaring would give $5=a^2+2b^2+2ab\sqrt2$, so $ab=0$. If $b=0$, $a^2=5$ is impossible in $\mathbb Q$; if $a=0$, $b^2=5/2$ is impossible in $\mathbb Q$. Therefore $\sqrt5\notin\mathbb Q(\sqrt2)$, and the tower law gives degree four.
:::

<1>2. The extension $K/\mathbb Q$ is Galois, with group
\[
\boxed{G\cong C_2\times C_2}.
\]

::: {.proof}
The field $K=\mathbb Q(\sqrt2,\sqrt5)$ is the splitting field of the separable polynomial $(x^2-2)(x^2-5)$, so it is Galois. Each automorphism independently sends $\sqrt2$ to $\pm\sqrt2$ and $\sqrt5$ to $\pm\sqrt5$. All four sign choices define automorphisms, since the field has degree four, and their composition is coordinatewise multiplication of signs. Hence $G$ is the Klein four group.
:::

<1>3. The complete Galois correspondence is
\[
\boxed{\begin{array}{c|c}
H&K^H\\ \hline
G&\mathbb Q\\
\langle\sigma_2\rangle&\mathbb Q(\sqrt5)\\
\langle\sigma_5\rangle&\mathbb Q(\sqrt2)\\
\langle\sigma_2\sigma_5\rangle&\mathbb Q(\sqrt{10})\\
\{1\}&K
\end{array}}
\]
where $\sigma_i$ changes the sign of $\sqrt i$ and fixes the other generator.

::: {.proof}
The displayed quadratic fields are fixed respectively by the indicated order-two subgroups. Each fixed field has degree two over $\mathbb Q$, by Galois correspondence, so the inclusions are equalities. The whole group fixes precisely $\mathbb Q$, and the trivial subgroup fixes $K$. These five subgroups exhaust the subgroups of $C_2\times C_2$.
:::

<1>4. Q.E.D.

::: {.proof}
Steps <1>1, <1>2, and <1>3 answer parts (a), (b), and (c).
:::
:::
