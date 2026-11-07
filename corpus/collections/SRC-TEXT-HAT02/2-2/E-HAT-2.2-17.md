---
schema: qual/card@1
id: E-HAT-2.2-17
kind: problem
title: Cellular map induces chain map compatible with singular homology isomorphism
classification:
  areas:
  - topology
  topics:
  - Homology
  - CW Complexes
  - Cellular Homology
relations: []
review: draft
audit:
- event: source-checked
  by: gpt-5.6-sol
  date: 2026-09-09
  note: Checked against Hatcher, Algebraic Topology, Section 2.2, Exercise 17; the stored statement matches the current Cornell text.
- event: solution-written
  by: gpt-5.6-sol
  date: 2026-09-09
- event: solution-reviewed
  by: gpt-5.6-sol
  date: 2026-09-09
  note: Complete cellular-chain proof checked.
- event: solution-reviewed
  by: claude
  date: 2026-10-31
  note: >-
    Read the naturality argument: a cellular map is a map of the skeletal pairs, so it induces
    $f_n$ on the cellular chain groups and commutes with $d_n$ because both arrows of the composite
    boundary, the connecting map and the inclusion-induced map, are natural. The closing step is
    read at the level of the claim it makes: it asserts, rather than diagram-chases, that the
    comparison maps $H_n^{CW}\cong H_n$ are natural.
- event: solution-reviewed
  by: claude
  date: 2026-11-08
  note: >-
    Statement matches Exercise 17 as printed on p. 157. The naturality argument is correct and
    now names its construction: the cellular boundary is d_n = j_{n-1} partial_n of the diagram
    on p. 139; the two long exact sequences of pairs are Theorem 2.16 p. 117 with naturality as
    stated on p. 127; functoriality of relative homology is p. 115. The third step was rewritten:
    it had appealed to "long exact sequences of triples", which is not what Hatcher's proof of
    Theorem 2.35 uses — that proof (pp. 139-140) identifies H_n(X) with H_n(X^n)/Im partial_{n+1}
    via the pair (X^{n+1},X^n) and Lemma 2.34(c) p. 137, and H_n^CW with the same quotient through
    the injective maps j_n and j_{n-1}. What is not covered: naturality is argued at the level of
    the construction, as the book does; no certificate.
---

::: {.problem}
Show the isomorphism between cellular and singular homology is natural in the following sense: A map $f: X \to Y$ that is cellular — satisfying $f(X^n) \subset Y^n$ for all $n$ — induces a chain map $f_*$ between the cellular chain complexes of $X$ and $Y$, and the map $f_*: H_n^{CW}(X) \to H_n^{CW}(Y)$ induced by this chain map corresponds to $f_*: H_n(X) \to H_n(Y)$ under the isomorphism $H_n^{CW} \approx H_n$.
:::

::: {.solution}
The cellular chain group of a CW complex $X$ is
$$
C_n^{CW}(X)=H_n(X^n,X^{n-1}).
$$
Let $f:X\to Y$ be cellular, so $f(X^n)\subseteq Y^n$ for every $n$.

::: pf

::: pf-step

For each $n$, $f$ induces a homomorphism
$$
f_n:H_n(X^n,X^{n-1})\longrightarrow H_n(Y^n,Y^{n-1}).
$$

::: pf-proof

Cellularity says precisely that
$$
f:(X^n,X^{n-1})\longrightarrow(Y^n,Y^{n-1})
$$
is a map of pairs. A map of pairs induces a chain map of the relative chain groups, and hence a map on relative homology (p. 115); relative homology is functorial for this reason, so the displayed map is defined.

:::

:::

::: pf-step

The maps $f_n$ commute with the cellular boundary operators, hence form a chain map
$$
f_\#:C_*^{CW}(X)\to C_*^{CW}(Y).
$$

::: pf-proof

The cellular boundary is the composite
$$
H_n(X^n,X^{n-1})
\xrightarrow{\partial}
H_{n-1}(X^{n-1})
\longrightarrow
H_{n-1}(X^{n-1},X^{n-2}),
$$
that is, $d_n=j_{n-1}\partial_n$ in the notation of p. 139, where the diagram defining the cellular complex is drawn. Both arrows are natural with respect to maps of pairs: the first by naturality of the long exact sequence of Theorem 2.16 (p. 117), as stated in the subsection on naturality (p. 127), and the second by functoriality of relative homology (p. 115). Therefore the square
$$
\begin{array}{ccc}
C_n^{CW}(X)&\xrightarrow{d_n}&C_{n-1}^{CW}(X)\\
\downarrow f_n&&\downarrow f_{n-1}\\
C_n^{CW}(Y)&\xrightarrow{d_n}&C_{n-1}^{CW}(Y)
\end{array}
$$
commutes.

:::

:::

::: pf-step

Under the canonical isomorphisms
$$
H_n^{CW}(X)\cong H_n(X),
\qquad
H_n^{CW}(Y)\cong H_n(Y),
$$
the homomorphism induced by the cellular chain map is the ordinary singular-homology map $f_*$.

::: pf-proof

The comparison is the one made in the proof of Theorem 2.35 (pp. 139–140). There $H_n(X)$ is identified with $H_n(X^n)/\operatorname{Im}\partial_{n+1}$, using the exact sequence of the pair $(X^{n+1},X^n)$ together with the isomorphism $H_n(X^{n+1})\cong H_n(X)$ of Lemma 2.34(c) (p. 137), and $H_n^{CW}(X)=\ker d_n/\operatorname{Im}d_{n+1}$ is identified with that quotient through the injective maps $j_n$ and $j_{n-1}$; the isomorphism is $H_n^{CW}(X)\cong H_n(X)$ of Theorem 2.35 (p. 139).

Every object and every map in that computation is built from the long exact sequences of the three pairs
$$
(X^{n+1},X^n),\qquad (X^n,X^{n-1}),\qquad (X^{n-1},X^{n-2})
$$
by connecting homomorphisms, inclusion-induced maps, and the injective maps $j$ supplied by exactness. Each of these is natural: the long exact sequences by Theorem 2.16 (p. 117) and the subsection on naturality (p. 127), inclusions by functoriality (p. 115). A cellular $f$ maps each of the three sequences for $X$ to the corresponding one for $Y$, since $f(X^i)\subseteq Y^i$. Hence the comparison isomorphism commutes with the maps induced by $f$, and the diagram below commutes. Consequently the diagram
$$
\begin{array}{ccc}
H_n^{CW}(X)&\xrightarrow{(f_\#)_*}&H_n^{CW}(Y)\\
\downarrow\cong&&\downarrow\cong\\
H_n(X)&\xrightarrow{f_*}&H_n(Y)
\end{array}
$$
commutes.

:::

:::

:::

Thus cellular homology is natural for cellular maps.
:::
