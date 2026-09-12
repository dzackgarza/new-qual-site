---
schema: qual/card@1
id: E-HAT-4.3-6
kind: problem
title: "H-space structure on $K(G,n)$"
classification:
  areas:
  - topology
  topics:
  - Higher Homotopy Groups
relations: []
review: draft
audit:
- event: source-checked
  by: gpt-5.6-sol
  date: 2026-09-09
  note: Checked against Hatcher, Algebraic Topology, Section 4.3, Exercise 6; the stored statement matches.
- event: solution-written
  by: gpt-5.6-sol
  date: 2026-09-09
- event: solution-reviewed
  by: gpt-5.6-sol
  date: 2026-09-09
---

Use Exercise 4 to construct a multiplication map $\mu: K(G, n) \times K(G, n) \to K(G, n)$ for any abelian group $G$, making a CW complex $K(G, n)$ into an H-space whose multiplication is commutative and associative up to homotopy and has a homotopy inverse.
Show also that the H-space multiplication $\mu$ is unique up to homotopy.

::: {.solution}
By Exercise 4, homotopy classes of maps
\[
K(G,n)\times K(G,n)\to K(G,n)
\]
are classified by homomorphisms
\[
\pi_n(K(G,n)\times K(G,n))=G\oplus G\to G.
\]
Choose \(\mu\) corresponding to addition
\[
(a,b)\mapsto a+b.
\]
Its restrictions to the two factors induce the identity on \(G\), hence are homotopic to the identity map. Thus \(\mu\) is an H-space multiplication.

The maps
\[
\mu(\mu\times1),\qquad \mu(1\times\mu):K^3\to K
\]
both induce \((a,b,c)\mapsto a+b+c\) on \(\pi_n\), so Exercise 4 makes them homotopic. Likewise \(\mu\) and \(\mu\tau\) both induce \(a+b\), so multiplication is homotopy-commutative. The map corresponding to
\[
a\mapsto-a
\]
is a homotopy inverse.

Finally any H-space multiplication on \(K(G,n)\) restricts to the identity on both factors, hence induces addition \(G\oplus G\to G\). Exercise 4 therefore implies that it is homotopic to \(\mu\). Thus
\[
\boxed{K(G,n)\text{ has a unique H-space multiplication up to homotopy, with the stated properties}.}
\]
:::
