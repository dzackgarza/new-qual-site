---
schema: qual/card@1
id: P-TATE85-X7-01
kind: problem
title: Galois groups of degree 7 polynomials with square discriminant and three real roots
classification:
  areas:
  - algebra
  topics:
  - Galois Groups of Polynomials
  - Simple Groups
  - Alternating Groups
relations: []
review: draft
audit:
- event: source-checked
  by: claude-opus-5
  date: 2026-09-16
  note: Retranscribed part (I) from the page headed X^7 - 7X + 3 in Tate_Galois_Theory_Problems.pdf; the OCR had glued math delimiters to words and dropped TeX into prose.
---

::: {.problem}
Suppose $f(X) \in \ZZ[X]$ is monic irreducible of degree $7$, has a square discriminant, and has exactly three real roots.
Prove that $G_f$ is isomorphic either to $A_7$ or to the group $G_{168} = \mathrm{GL}(3, \FF_2) \cong \mathrm{PSL}(2, \FF_7)$.
Note that $G_{168}$ is isomorphic to a subgroup of $S_7$, in fact of $A_7$, via the action of $G_{168} = \mathrm{GL}_3(\FF_2)$ on the $7$ nonzero vectors in $\FF_2^3$.

(By considering Sylow subgroups, especially the ones for $7$, this can be done from scratch without too much trouble.
But it is even easier if you know that the only non-abelian simple groups of order $< 1000$ are $A_5$ of order $60 = 2^2 \cdot 3 \cdot 5$, $G_{168}$ of order $168 = 2^3 \cdot 3 \cdot 7$, $A_6$ of order $360 = 2^3 \cdot 3^2 \cdot 5$, $\mathrm{PSL}(2, \FF_8)$ of order $504 = 2^3 \cdot 3^2 \cdot 7$, and $\mathrm{PSL}(2, \FF_{11})$ of order $660 = 2^2 \cdot 3 \cdot 5 \cdot 11$.)
:::

::: {.solution}

Let $L$ be the splitting field of $f$, let
$$
G=G_f=\operatorname{Gal}(L/\QQ),
$$
and identify $G$ with its faithful permutation action on the seven roots of $f$.

::: pf

::: {.pf-step #s1-1}

The group $G$ is a transitive subgroup of $A_7$ and contains a double transposition.


::: pf-proof

Since $f$ is irreducible over $\QQ$, the Galois group acts transitively on its roots.

If the roots are $\alpha_1,\ldots,\alpha_7$, put
$$
V=\prod_{i<j}(\alpha_i-\alpha_j).
$$
Then $V^2=\operatorname{disc}(f)$, and a permutation of the roots sends $V$ to its sign times $V$. By hypothesis the discriminant is a square in $\QQ$, so $V\in\QQ$. Every element of $G$ therefore fixes $V$, hence has sign $+1$. Thus
$$
G\le A_7.
$$

The polynomial has exactly three real roots, so its remaining four roots form two nonreal complex-conjugate pairs. Complex conjugation fixes the three real roots and exchanges each of the two nonreal pairs. Its action on the roots is therefore a product of two disjoint transpositions. In particular $G$ contains a nontrivial element of order $2$.

:::

:::

::: {.pf-step #s1-2}

The degree-$7$ action of $G$ is primitive, and every nontrivial normal subgroup of $G$ is transitive.


::: pf-proof

In a transitive action of prime degree, every block has size dividing the degree. Since the degree is $7$, the only block sizes are $1$ and $7$, so the action is primitive.

If $1\ne N\trianglelefteq G$, then the $N$-orbits form a $G$-invariant block system. Primitivity forces those orbits either to be singletons or to consist of all seven points. The first alternative would make $N$ act trivially; the action of $G$ is faithful, so this would give $N=1$. Hence every nontrivial normal subgroup $N$ is transitive.

:::

:::

::: {.pf-step #s1-3}

A minimal nontrivial normal subgroup $N\trianglelefteq G$ cannot be abelian.


::: pf-proof

Choose $N$ minimal among the nontrivial normal subgroups of $G$. By step [](#s1-2){.pf-ref}, $N$ is transitive, so $7\mid \cardinality{N}$.

If $N$ were abelian, minimal normality would make it an elementary abelian $q$-group for some prime $q$. Since $7\mid \cardinality{N}$, one would have $q=7$. But
$$
N\le G\le A_7,
\qquad
\cardinality{A_7}=2520=2^3\cdot3^2\cdot5\cdot7,
$$
so the $7$-part of $\cardinality{N}$ is at most $7$. Hence
$$
N\cong C_7.
$$
Its transitive action is regular.

Because $N\trianglelefteq G$, one has
$$
G\le N_{S_7}(N).
$$
For a regular $7$-cycle, its normalizer is the affine group
$$
N_{S_7}(N)\cong \FF_7\rtimes\FF_7^\times
$$
of order $42$: the centralizer of a $7$-cycle is $N$ itself, conjugation identifies the quotient of the normalizer by $N$ with a subgroup of $\operatorname{Aut}(C_7)\cong C_6$, and the six affine multipliers $x\mapsto ax$ realize all six automorphisms. This normalizer contains an odd permutation: the affine map $x\mapsto-x$ fixes $0$ and acts on the other six points as three transpositions. Consequently
$$
\cardinality{N_{S_7}(N)\cap A_7}=21.
$$
Since $G\le A_7$, it follows that $G$ is contained in a group of odd order $21$. This contradicts step [](#s1-1){.pf-ref}, which gives an element of order $2$ in $G$. Therefore $N$ is nonabelian.

:::

:::

::: {.pf-step #s1-4}

The minimal normal subgroup $N$ is isomorphic either to $A_7$ or to $G_{168}$.


::: pf-proof

A finite minimal normal subgroup is characteristically simple, hence is a direct product
$$
N\cong S^k
$$
of isomorphic simple groups. By step [](#s1-3){.pf-ref}, $S$ is nonabelian.

If $N=A_7$, there is nothing to prove in this step. Suppose instead that $N$ is a proper subgroup of $A_7$. A proper subgroup of $A_7$ has index at least $7$: if $H<A_7$ had index $j<7$, the action of the simple group $A_7$ on the $j$ cosets of $H$ would have trivial kernel and would embed $A_7$ into $S_j$, impossible because
$$
\cardinality{A_7}=2520>\cardinality{S_j}
\qquad(j\le6).
$$
Hence
$$
\cardinality{N}\le \frac{2520}{7}=360.
$$

The smallest nonabelian simple group has order $60$. Therefore $k\ge2$ would give
$$
\cardinality{N}\ge60^2=3600,
$$
contrary to $\cardinality{N}\le360$. Thus $k=1$, so $N$ itself is nonabelian simple.

By step [](#s1-2){.pf-ref}, $N$ is transitive, and therefore $7\mid \cardinality{N}$. From the list of nonabelian simple groups of order below $1000$ supplied in the problem, the only group of order at most $360$ whose order is divisible by $7$ is
$$
G_{168}\cong\operatorname{GL}_3(\FF_2)
\cong\operatorname{PSL}_2(\FF_7).
$$
Thus a proper $N$ is isomorphic to $G_{168}$.

:::

:::

::: {.pf-step #s1-5}

One has
$$
\boxed{G\cong A_7\quad\text{or}\quad G\cong G_{168}}.
$$


::: pf-proof

If $N=A_7$, then
$$
A_7=N\le G\le A_7,
$$
so $G=A_7$.

Now suppose $N\cong G_{168}$. Since $N\trianglelefteq G\le A_7$,
$$
[G:N]\mid[A_7:N]
=\frac{2520}{168}
=15.
$$
Thus
$$
[G:N]\in\{1,3,5,15\}.
$$
If the index were $3$ or $5$, then $G$ would have index $5$ or $3$, respectively, in $A_7$, contradicting the fact proved in step [](#s1-4){.pf-ref} that $A_7$ has no proper subgroup of index less than $7$. If $[G:N]=15$, then $G=A_7$, but this would make the proper nontrivial subgroup $N$ normal in the simple group $A_7$, again impossible. Hence $[G:N]=1$, so
$$
G=N\cong G_{168}.
$$
These are exactly the two asserted possibilities.

:::

:::

::: pf-qed

Step [](#s1-5){.pf-ref} gives the required classification of $G_f$.

:::

:::

:::
