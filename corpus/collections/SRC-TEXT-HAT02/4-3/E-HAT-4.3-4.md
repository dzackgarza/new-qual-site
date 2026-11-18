---
schema: qual/card@1
id: E-HAT-4.3-4
kind: problem
title: "Maps between Eilenberg--MacLane spaces"
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
  note: Checked against Hatcher, Algebraic Topology, Section 4.3, Exercise 4; the stored statement matches.
- event: solution-written
  by: gpt-5.6-sol
  date: 2026-09-09
- event: solution-reviewed
  by: gpt-5.6-sol
  date: 2026-09-09
- event: solution-reviewed
  by: claude
  date: 2026-11-02
  note: >-
    Cards read. Verdict record is m6__proofs-4-3-1-12.md (1-12: 10 correct, 5 a dimension slip, 9 a wrong assertion; both repaired) and m2__proofs-4-3-13-24.md (13-24: 10 correct, 20 a display misalignment repaired by identifying the principal fibration, 22 the missing converse of an iff, later restated and proved, and 24, whose whole proof was then written). No card in this slice has an unmet piece.

- event: solution-written
  by: claude
  date: 2026-11-18
  note: >-
    Lamport structure for the four steps of the identification, which is what Queue D asks for on this card. The representability theorem is named with its page; the Hurewicz input is one step covering both the degree-n isomorphism and the vanishing of the Ext term, including the n = 1 case where the Ext is that of a free group; the universal coefficient sequence is written out; and the last step says why the composite of the two bijections is f -> f_*, which the prose compressed into "by naturality". No retained set covers this exercise; the card now says so. Locators checked: Theorem 4.57 on printed p. 402, Theorem 3.2 on p. 195, the exercise on p. 419. No statement repair.
---

::: {.problem}
Given abelian groups $G$ and $H$ and CW complexes $K(G, n)$ and $K(H, n)$, show that the map $\langle K(G, n), K(H, n) \rangle \to \operatorname{Hom}(G, H)$ sending a homotopy class $[f]$ to the induced homomorphism $f_*: \pi_n(K(G, n)) \to \pi_n(K(H, n))$ is a bijection.
:::

::: {.solution}
No retained solution set covers this exercise: the Hatcher sets in the checkout hold nothing from §4.3. The argument is the card's own, checked against Hatcher, *Algebraic Topology* (2002), §4.3 Exercise 4, printed p. 419.

::: pf

::: {.pf-step #representability}
$\langle K(G,n),K(H,n)\rangle\cong H^n(K(G,n);H)$.

::: pf-proof
Theorem 4.57, printed p. 402, gives natural bijections $T:\langle X,K(H,n)\rangle\to H^n(X;H)$ for every CW complex $X$ and $n>0$, so the set of homotopy classes is in bijection with the cohomology of the source with coefficients in $H$.
:::

:::

::: {.pf-step #hurewicz}
$H_n(K(G,n);\ZZ)\cong G$ and $\operatorname{Ext}\bigl(H_{n-1}(K(G,n);\ZZ),H\bigr)=0$.

::: pf-proof
A $K(G,n)$ is $(n-1)$-connected by definition, so the Hurewicz theorem applies in degree $n$ and gives $H_n(K(G,n);\ZZ)\cong\pi_n(K(G,n))\cong G$; for $n>1$ it also gives $H_{n-1}(K(G,n);\ZZ)=0$, so that Ext group vanishes. For $n=1$ one has $H_0=\ZZ$ free, and the Ext of a free group vanishes too.
:::

:::

::: {.pf-step #uct}
$H^n(K(G,n);H)\cong\operatorname{Hom}(G,H)$.

::: pf-proof
The universal coefficient theorem, Theorem 3.2 printed p. 195, gives the split exact sequence
$$
0\to\operatorname{Ext}\bigl(H_{n-1}(K(G,n)),H\bigr)\to H^n(K(G,n);H)\to\operatorname{Hom}\bigl(H_n(K(G,n)),H\bigr)\to0,
$$
whose first term vanishes by step [](#hurewicz){.pf-ref} and whose last is $\operatorname{Hom}(G,H)$ by the same step.
:::

:::

::: {.pf-step #induced-map}
Under the identifications of steps [](#representability){.pf-ref} and [](#uct){.pf-ref}, the class of $f:K(G,n)\to K(H,n)$ corresponds to the induced homomorphism $f_*:G\to H$ on $\pi_n$.

::: pf-proof
The bijection of Theorem 4.57 has the form $T([f])=f^*(\alpha)$ for a distinguished class $\alpha\in H^n(K(H,n);H)$, and the universal coefficient isomorphism is natural in the space, so the class corresponding to $[f]$ is the image of $\alpha$ under $f^*$ followed by the identification $\operatorname{Hom}(H_n(K(H,n)),H)\cong\operatorname{Hom}(H,H)$. Naturality of the Hurewicz isomorphism identifies $f_*$ on $\pi_n$ with $f_*$ on $H_n$, so the composite sends $[f]$ to $f_*\in\operatorname{Hom}(G,H)$; the map $\langle K(G,n),K(H,n)\rangle\to\operatorname{Hom}(G,H)$ is therefore a bijection, which is the exercise.
:::

:::

:::
:::
