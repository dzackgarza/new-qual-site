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
- event: source-checked
  by: claude
  date: 2026-10-31
  note: Statement compared with Hatcher, Algebraic Topology, Section 3.1, Exercise 13; it matches the printed text. The card also states Proposition 1B.9, which the exercise refers to; that is extra context, not a change to the exercise.
- event: solution-reviewed
  by: claude
  date: 2026-10-31
  note: >-
    Read the composition: Proposition 1B.9 gives the bijection with $\operatorname{Hom}(\pi_1X,G)$;
    abelianness factors that through $\pi_1^{ab}=H_1(X)$; the universal coefficient sequence with
    $\operatorname{Ext}(H_0,G)=\operatorname{Ext}(\ZZ,G)=0$ identifies it with $H^1(X;G)$; and the
    induced map on $H_1$ is the abelianization of the induced map on $\pi_1$.
- event: solution-reviewed
  by: claude
  date: 2026-11-07
  note: >-
    Statement matches Exercise 13 (p.206), with Proposition 1B.9 restated as context. Rechecked the composition: Proposition 1B.9 p.90 gives the bijection with Hom(pi_1 X,G); abelian G factors it through pi_1^ab = H_1(X) by Theorem 2A.1 p.166; Theorem 3.2 p.195 with H_0 free identifies Hom(H_1,G) with H^1(X;G); and the composite sends f to f_* on H_1. Citations added at each step, including the page of Proposition 1B.9 and of Theorem 2A.1. Not covered: X not connected, which the exercise excludes.
---

::: {.problem}
Proposition 1B.9 reads: Let $X$ be a connected CW complex and let $Y$ be a $K(G,1)$.
Then every homomorphism $\pi_1(X, x_0) \to \pi_1(Y, y_0)$ is induced by a map $(X, x_0) \to (Y, y_0)$ that is unique up to homotopy fixing $x_0$.

Let $\langle X, Y \rangle$ denote the set of basepoint-preserving homotopy classes of basepoint-preserving maps $X \to Y$.
Using Proposition 1B.9, show that if $X$ is a connected CW complex and $G$ is an abelian group, then the map $\langle X, K(G, 1) \rangle \to H^1(X; G)$ sending a map $f: X \to K(G, 1)$ to the induced homomorphism $f_*: H_1(X) \to H_1(K(G, 1)) \approx G$ is a bijection, where we identify $H^1(X; G)$ with $\operatorname{Hom}(H_1(X), G)$ via the universal coefficient theorem.
:::

::: {.solution}
Let $Y=K(G,1)$ and fix basepoints throughout.

::: pf

::: {.pf-step #s1}

Proposition 1B.9 gives a bijection
$$
\langle X,K(G,1)\rangle
\xrightarrow{\cong}
\operatorname{Hom}(\pi_1(X),G),
\qquad
[f]\longmapsto f_*.
$$

::: pf-proof

Proposition 1B.9 (p.90) states that for a connected CW complex $X$ and a $K(G,1)$, every homomorphism $\pi_1(X,x_0)\to\pi_1(Y,y_0)$ is induced by a based map, unique up to based homotopy; with $\pi_1(K(G,1))=G$ this is the displayed bijection. Because maps and homotopies are based, there is no quotient by conjugation.

:::

:::

::: {.pf-step #s2}

Since $G$ is abelian, every homomorphism
$$
\pi_1(X)\to G
$$
factors uniquely through the abelianization
$$
\pi_1(X)^{\mathrm{ab}}\cong H_1(X;\ZZ).
$$
Hence
$$
\operatorname{Hom}(\pi_1(X),G)
\cong
\operatorname{Hom}(H_1(X),G).
$$

::: pf-proof

The commutator subgroup lies in the kernel of every homomorphism to an abelian group, and the universal property of abelianization gives the unique factorization. Theorem 2A.1 (p.166) identifies $\pi_1(X)^{\mathrm{ab}}$ with $H_1(X)$ for path-connected $X$, which a connected CW complex is.

:::

:::

::: {.pf-step #s3}

The universal coefficient theorem gives
$$
H^1(X;G)\cong\operatorname{Hom}(H_1(X),G).
$$

::: pf-proof

The cohomological universal coefficient sequence of Theorem 3.2 (p.195) is
$$
0\to\operatorname{Ext}(H_0(X),G)
\to H^1(X;G)
\to\operatorname{Hom}(H_1(X),G)\to0.
$$
Since $X$ is connected, $H_0(X)\cong\ZZ$ is free, so the Ext term vanishes and $H^1(X;G)\cong\operatorname{Hom}(H_1(X),G)$.

:::

:::

::: pf-step

Under the identifications in steps [](#s1){.pf-ref}, [](#s2){.pf-ref} and [](#s3){.pf-ref}, the bijection is exactly
$$
[f]\longmapsto f_*:H_1(X)\to H_1(K(G,1))\cong G.
$$

::: pf-proof

The induced homomorphism on $H_1$ is the abelianization of the induced homomorphism on $\pi_1$. Thus the composite of the first two identifications sends $f$ to precisely $f_*:H_1(X)\to G$, and step [](#s3){.pf-ref} identifies this homomorphism with the corresponding cohomology class.

:::

:::

:::

Therefore the map stated in the problem is a bijection.
:::
