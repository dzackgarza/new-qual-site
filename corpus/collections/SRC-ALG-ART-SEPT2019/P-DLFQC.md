---
schema: qual/card@1
id: P-DLFQC
kind: problem
title: Density in affine varieties via the Nullstellensatz
classification:
  areas:
  - algebra
  topics:
  - Geometry
  - Commutative Algebra
  - Maximal Ideals
relations: []
review: draft
---

::: {.problem}
Work over an algebraically closed field $F$ of characteristic zero.

(a) Let $X$ be an affine variety with coordinate algebra $F[X]$. State the *Nullstellensatz*. Then use it to show that a subset $S \subseteq X$ is dense (in the Zariski topology) if and only if the following property holds for all $f \in F[X]$:
$$(f(s)=0 \text{ for all } s\in S) \Rightarrow f=0.$$

(b) Given affine varieties $X$ and $Y$ and dense subsets $S \subseteq X$ and $T \subseteq Y$, prove that $S\times T$ is dense in $X\times Y$.

(c) Show that the integer lattice $\ZZ^n$ is dense in $F^n$.
:::

::: {.solution}

::: pf

::: {.pf-step #s1}
(a) Nullstellensatz: the maps
$$
V: \{\text{radical ideals of }F[X]\} \leftrightarrow \{\text{closed subsets of }X\} : I,
$$
$V(J) = \{x\in X \mid f(x)=0\ \forall f\in J\}$ and $I(S) = \{f\in F[X] \mid f(x)=0\ \forall x\in S\}$, are mutually inverse inclusion-reversing bijections.

::: pf-proof
This is the statement of the theorem.
:::

:::

::: {.pf-step #s2}
(a) $\overline S = V(I(S))$ for every $S\subseteq X$.

::: pf-proof
$S \subseteq V(I(S))$ and $V(I(S))$ is closed, so $\overline S \subseteq V(I(S))$. Conversely, every closed set containing $S$ has the form $V(J)$ with $J=\sqrt J$, and $S\subseteq V(J)$ gives $J=I(V(J))\subseteq I(S)$ by step [](#s1){.pf-ref}, so $V(I(S)) \subseteq V(J)$. Hence $V(I(S)) \subseteq \overline S$.
:::

:::

::: {.pf-step #s3}
(a) $S$ is dense if and only if every $f\in F[X]$ vanishing on $S$ is $0$.

::: pf-proof
The stated property says $I(S)=(0)$. By steps [](#s1){.pf-ref} and [](#s2){.pf-ref}, $\overline S = X \iff V(I(S)) = X \iff I(S) = I(X) = (0)$.
:::

:::

::: {.pf-step #s4}
(b) $S\times T$ is dense in $X\times Y$.

::: pf-proof
The coordinate ring of the product is $F[X\times Y] = F[X]\otimes F[Y]$. Let $\theta \in F[X\times Y]$ vanish on $S\times T$, and write $\theta = \sum_i f_i\otimes g_i$ with the $f_i$ linearly independent. For any $t\in T$, $\sum_i g_i(t)f_i \in F[X]$ vanishes on $S$, hence is zero by step [](#s3){.pf-ref}. As the $f_i$ are linearly independent, $g_i(t)=0$ for all $t\in T$, so $g_i=0$ by step [](#s3){.pf-ref} for $T\subseteq Y$. Therefore $\theta=0$, and $S\times T$ is dense by step [](#s3){.pf-ref}.
:::

:::

::: {.pf-step #s5}
(c) $\ZZ^n$ is dense in $F^n$.

::: pf-proof
Since $\operatorname{char}F=0$, $\ZZ$ is an infinite subset of $F$, and a nonzero polynomial in $F[x]$ has finitely many roots, so $\ZZ$ is dense in $F$ by step [](#s3){.pf-ref}. Step [](#s4){.pf-ref} and induction on $n$ give density of $\ZZ^n=\ZZ^{n-1}\times\ZZ$ in $F^n$.
:::

:::

::: pf-qed
Steps [](#s3){.pf-ref}, [](#s4){.pf-ref} and [](#s5){.pf-ref} prove (a), (b) and (c).
:::

:::

:::
