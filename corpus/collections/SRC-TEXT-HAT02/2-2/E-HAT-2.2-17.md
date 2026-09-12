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
---

Show the isomorphism between cellular and singular homology is natural in the following sense: A map $f: X \to Y$ that is cellular — satisfying $f(X^n) \subset Y^n$ for all $n$ — induces a chain map $f_*$ between the cellular chain complexes of $X$ and $Y$, and the map $f_*: H_n^{CW}(X) \to H_n^{CW}(Y)$ induced by this chain map corresponds to $f_*: H_n(X) \to H_n(Y)$ under the isomorphism $H_n^{CW} \approx H_n$.

::: {.solution}
The cellular chain group of a CW complex $X$ is
\[
C_n^{CW}(X)=H_n(X^n,X^{n-1}).
\]
Let $f:X\to Y$ be cellular, so $f(X^n)\subseteq Y^n$ for every $n$.

<1>1. For each $n$, $f$ induces a homomorphism
\[
f_n:H_n(X^n,X^{n-1})\longrightarrow H_n(Y^n,Y^{n-1}).
\]
::: {.proof}
Cellularity says precisely that
\[
f:(X^n,X^{n-1})\longrightarrow(Y^n,Y^{n-1})
\]
is a map of pairs. Relative homology is functorial, so the displayed map is defined.
:::

<1>2. The maps $f_n$ commute with the cellular boundary operators, hence form a chain map
\[
f_\#:C_*^{CW}(X)\to C_*^{CW}(Y).
\]
::: {.proof}
The cellular boundary is the composite
\[
H_n(X^n,X^{n-1})
\xrightarrow{\partial}
H_{n-1}(X^{n-1})
\longrightarrow
H_{n-1}(X^{n-1},X^{n-2}).
\]
Both arrows are natural with respect to maps of pairs: the first by naturality of the long exact sequence and the second by functoriality of relative homology. Therefore the square
\[
\begin{array}{ccc}
C_n^{CW}(X)&\xrightarrow{d_n}&C_{n-1}^{CW}(X)\\
\downarrow f_n&&\downarrow f_{n-1}\\
C_n^{CW}(Y)&\xrightarrow{d_n}&C_{n-1}^{CW}(Y)
\end{array}
\]
commutes.
:::

<1>3. Under the canonical isomorphisms
\[
H_n^{CW}(X)\cong H_n(X),
\qquad
H_n^{CW}(Y)\cong H_n(Y),
\]
the homomorphism induced by the cellular chain map is the ordinary singular-homology map $f_*$.
::: {.proof}
The cellular-homology isomorphism is constructed from the long exact sequences of the skeletal pairs and triples
\[
(X^n,X^{n-1},X^{n-2}).
\]
Every map appearing in that construction is a connecting homomorphism, inclusion-induced map, or quotient arising from exactness. All of these are natural. Applying $f$ gives a morphism between the entire systems of exact sequences for $X$ and $Y$, and the comparison maps defining
\[
H_n^{CW}(-)\xrightarrow{\cong}H_n(-)
\]
commute with this morphism. Consequently the diagram
\[
\begin{array}{ccc}
H_n^{CW}(X)&\xrightarrow{(f_\#)_*}&H_n^{CW}(Y)\\
\downarrow\cong&&\downarrow\cong\\
H_n(X)&\xrightarrow{f_*}&H_n(Y)
\end{array}
\]
commutes.
:::

Thus cellular homology is natural for cellular maps.
:::
