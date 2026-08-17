---
schema: qual/card@1
id: P-UKZE6
kind: problem
title: "Let $R$ be a commutative ring with 1. some positive integer $n$."
classification:
  areas:
  - algebra
  topics:
  - jacobson-radical
  - maximal-ideals
  - nilpotence
relations: []
review: draft
solved: true
---
Let $R$ be a commutative ring with 1.

> Recall that $x \in R$ is nilpotent iff $xn = 0$ for
some positive integer $n$.

a.
Show that every proper ideal of $R$ is contained within a maximal ideal.

b.
Let $J(R)$ denote the intersection of all maximal ideals of $R$.
Show that $x \in J(R) \iff 1 + rx$ is a unit for all $r \in R$.

c.
Suppose now that $R$ is finite. Show that in this case $J(R)$ consists precisely
of the nilpotent elements in R.

:::{.concept}
\envlist

- Definitions:
\[
N(R) &\da \theset{x\in R \suchthat x^n = 0 \text{ for some } n} \\
J(R) &\da \intersect _{\mfm \in \mspec} \mfm
.\]

- Zorn's lemma: if $P$ is a poset in which every chain has an upper bound, $P$ contains a maximal element.


:::

:::{.solution}
\envlist

:::{.proof title="of a"}
Define the set of proper ideals
$$
S = \theset{J \suchthat I   \subseteq J < R}
,$$

which is a poset under set inclusion.

Given a chain $J_1 \subseteq \cdots$, there is an upper bound $J \definedas \union J_i$, so Zorn's lemma applies.


:::

:::{.proof title="of b, $\implies$"}
$\implies$:

- We will show that $x\in J(R) \implies 1+x \in R\units$, from which the result follows by letting $x=rx$.

- Let $x\in J(R)$, so it is in every maximal ideal, and suppose toward a contradiction that $1+x$ is **not** a unit.

- Then consider $I = \generators{1+x} \normal R$. 
Since $1+x$ is not a unit, we can't write $s(1+x) = 1$ for any $s\in R$, and so $1 \not\in I$ and $I\neq R$

- So $I < R$ is proper and thus contained in some maximal proper ideal $\mathfrak{m} < R$ by part (1), and so we have $1+x \in \mathfrak{m}$.
Since $x\in J(R)$, $x\in \mathfrak{m}$ as well.

- But then $(1+x) - x = 1 \in \mathfrak{m}$ which forces $\mathfrak{m} = R$.

:::

:::{.proof title="of b, $\impliedby$"}
$\impliedby$

- Fix $x\in R$, and suppose $1+rx$ is a unit for all $r\in R$.

 
- Suppose towards a contradiction that there is a maximal ideal $\mathfrak{m}$ such that $x\not \in \mathfrak{m}$ and thus $x\not\in J(R)$.

- Consider 
\[
M' \definedas \theset{rx + m \suchthat r\in R,~ m\in M}
.\]

- Since $\mathfrak{m}$ was maximal, $\mathfrak{m} \subsetneq M'$ and so $M' = R$.

- So every element in $R$ can be written as $rx + m$ for some $r\in R, m\in M$.
But $1\in R$, so we have 
\[
1 = rx + m
.\] 

- So let $s = -r$ and write $1 = sx - m$, and so $m = 1 + sx$.

- Since $s\in R$ by assumption $1+sx$ is a unit and thus $m \in \mathfrak{m}$ is a unit, a contradiction.

- So $x\in \mathfrak{m}$ for every $\mathfrak{m}$ and thus $x\in J(R)$.

:::

:::{.proof title="of c: $J(R) = \mathfrak N(R)$"}
$\mathfrak N(R) \subseteq J(R)$:

- Use the fact $x\in \mathfrak N(R) \implies x^n = 0 \implies 1 + rx$ is a unit $\iff x\in J(R)$ by (b):
$$
\sum_{k=1}^{n-1} (-x)^k = \frac{1 - (-x)^n}{1- (-x)} = (1+x)\inv
.$$

$J(R) \subseteq \mathfrak N(R)$:

- Let $x \in J(R) \setminus \mathfrak N(R)$.

- Since $R$ is finite, $x^m = x$ for some $m > 0$.

- Without loss of generality, we can suppose $x^2 = x$ by replacing $x^m$ with $x^{2m}$.

- If $1-x$ is not a unit, then $\generators{1-x}$ is a nontrivial proper ideal, which by (a) is contained in some maximal ideal $\mm$. 
But then $x\in \mm$ and $1-x \in \mm \implies x + (1-x) = 1 \in \mm$, a contradiction.

- So $1-x$ is a unit, so let $u = (1-x)\inv$.

- Then
\[
(1-x)x &= x - x^2 = x - x = 0 \\
&\implies u (1-x)x = x = 0 \\
&\implies x=0
.\]

:::

:::
