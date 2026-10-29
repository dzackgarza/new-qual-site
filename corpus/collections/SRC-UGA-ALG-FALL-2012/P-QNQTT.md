---
schema: qual/card@1
id: P-QNQTT
kind: problem
title: Galois group over $\QQ$ of an irreducible quintic with all but two roots real
classification:
  areas:
  - algebra
  topics:
  - Galois Theory
  - Permutations
  - Polynomials
relations: []
review: draft
---

::: {.problem}
Let $f(x) \in \QQ[x]$ be an irreducible polynomial of degree 5. Assume that $f$ has all but two roots in $\RR$.
Compute the Galois group of $f(x)$ over $\QQ$ and justify your answer.
:::

::: {.solution}

Let $K$ be the splitting field of $f$ over $\QQ$ and $G=\operatorname{Gal}(K/\QQ)$, acting on its five roots.

::: pf

::: {.pf-step #s1-1}

The subgroup $G\leq S_5$ contains a $5$-cycle.


::: pf-proof

Because $f$ is irreducible in characteristic zero, its five roots are distinct and its Galois group acts transitively on them. The action is faithful since the roots generate $K$. By orbit–stabilizer, $5$ divides $|G|$, and Cauchy's theorem gives an element of order five. Every such element of $S_5$ is a $5$-cycle.

:::

:::

::: {.pf-step #s1-2}

The group $G$ contains a transposition.


::: pf-proof

Exactly three roots of $f$ are real; the remaining two form a nonreal conjugate pair because $f$ has rational coefficients. Complex conjugation restricts to an automorphism of the splitting field $K$, fixes the three real roots, and swaps the nonreal pair. Its action on the roots is a transposition.

:::

:::

::: {.pf-step #s1-3}

A subgroup of $S_5$ containing a $5$-cycle and a transposition is $S_5$.


::: pf-proof

Label the roots by $\ZZ/5\ZZ$ so that the $5$-cycle is $\sigma:i\mapsto i+1$. Let the transposition interchange $a$ and $b$, with $a\neq b$. Its conjugates by powers of $\sigma$ interchange $a+k$ and $b+k$ for $k\in\ZZ/5\ZZ$. These pairs form the edges of a connected graph: the difference $b-a$ generates the additive group of order five. Edge transpositions of a connected graph generate its full symmetric group, as follows by expressing any transposition along a path by conjugation. Hence the subgroup contains $S_5$.

:::

:::

::: {.pf-step #s1-4}

The Galois group is
\[
\boxed{\operatorname{Gal}(K/\QQ)\cong S_5}.
\]


::: pf-proof

Steps [](#s1-1){.pf-ref} and [](#s1-2){.pf-ref} supply a $5$-cycle and a transposition in $G$. By step [](#s1-3){.pf-ref}, $G=S_5$ in its faithful root action.

:::

:::

::: pf-qed

Step [](#s1-4){.pf-ref} identifies the requested Galois group.

:::

:::

:::
