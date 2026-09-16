---
schema: qual/card@1
id: E-HAT-3.1-13
kind: problem
title: Maps to $K(G,1)$ represent $H^1(X;G)$
classification:
  areas:
  - topology
  topics:
  - Cohomology
relations: []
review: draft
audit:
- event: source-checked
  by: gpt-5.6-sol
  date: 2026-09-09
  note: Checked against Hatcher, Algebraic Topology, Section 3.1, Exercise 13; the stored statement matches.
- event: solution-written
  by: gpt-5.6-sol
  date: 2026-09-09
- event: solution-reviewed
  by: gpt-5.6-sol
  date: 2026-09-09
  note: Verified the cochain, exact-sequence, and universal-coefficient calculations directly.
- event: source-checked
  by: claude-opus-5
  date: 2026-09-16
  note: Moved the statement into a problem block and stated Proposition 1B.9 from Hatcher, Algebraic Topology, p. 90.
---

::: {.problem}
Proposition 1B.9 reads: Let $X$ be a connected CW complex and let $Y$ be a $K(G,1)$.
Then every homomorphism $\pi_1(X, x_0) \to \pi_1(Y, y_0)$ is induced by a map $(X, x_0) \to (Y, y_0)$ that is unique up to homotopy fixing $x_0$.

Let $\langle X, Y \rangle$ denote the set of basepoint-preserving homotopy classes of basepoint-preserving maps $X \to Y$.
Using Proposition 1B.9, show that if $X$ is a connected CW complex and $G$ is an abelian group, then the map $\langle X, K(G, 1) \rangle \to H^1(X; G)$ sending a map $f: X \to K(G, 1)$ to the induced homomorphism $f_*: H_1(X) \to H_1(K(G, 1)) \approx G$ is a bijection, where we identify $H^1(X; G)$ with $\operatorname{Hom}(H_1(X), G)$ via the universal coefficient theorem.
:::

::: {.solution}
Let $Y=K(G,1)$ and fix basepoints throughout.

<1>1. Proposition 1B.9 gives a bijection
\[
\langle X,K(G,1)\rangle
\xrightarrow{\cong}
\operatorname{Hom}(\pi_1(X),G),
\qquad
[f]\longmapsto f_*.
\]
::: {.proof}
For a connected CW complex $X$, Proposition 1B.9 classifies based homotopy classes of based maps into a $K(G,1)$ by the induced homomorphism on fundamental groups. Because maps and homotopies are based, there is no quotient by conjugation.
:::

<1>2. Since $G$ is abelian, every homomorphism
\[
\pi_1(X)\to G
\]
factors uniquely through the abelianization
\[
\pi_1(X)^{\mathrm{ab}}\cong H_1(X;\mathbb Z).
\]
Hence
\[
\operatorname{Hom}(\pi_1(X),G)
\cong
\operatorname{Hom}(H_1(X),G).
\]
::: {.proof}
The commutator subgroup lies in the kernel of every homomorphism to an abelian group. The universal property of abelianization gives the unique factorization. The Hurewicz theorem in degree one identifies the abelianization with $H_1(X)$.
:::

<1>3. The universal coefficient theorem gives
\[
H^1(X;G)\cong\operatorname{Hom}(H_1(X),G).
\]
::: {.proof}
The cohomological universal coefficient sequence is
\[
0\to\operatorname{Ext}(H_0(X),G)
\to H^1(X;G)
\to\operatorname{Hom}(H_1(X),G)\to0.
\]
Since $X$ is connected, $H_0(X)\cong\mathbb Z$ is free, so the Ext term vanishes.
:::

<1>4. Under the identifications in <1>1--<1>3, the bijection is exactly
\[
[f]\longmapsto f_*:H_1(X)\to H_1(K(G,1))\cong G.
\]
::: {.proof}
The induced homomorphism on $H_1$ is the abelianization of the induced homomorphism on $\pi_1$. Thus the composite of the first two identifications sends $f$ to precisely $f_*:H_1(X)\to G$, and <1>3 identifies this homomorphism with the corresponding cohomology class.
:::

Therefore the map stated in the problem is a bijection.
:::
