---
schema: qual/card@1
id: E-HAT-3.3-35
kind: problem
title: Poincaré duality for noncompact manifolds with boundary
classification:
  areas:
  - topology
  topics:
  - Poincaré Duality
  - Manifolds
  - Cohomology
relations: []
review: draft
audit:
- event: source-checked
  by: gpt-5.6-sol
  date: 2026-09-09
  note: Checked against Hatcher, Algebraic Topology, Section 3.3, Exercise 35; the stored statement matches the current online text and diagram where applicable.
- event: solution-written
  by: gpt-5.6-sol
  date: 2026-09-09
- event: solution-reviewed
  by: gpt-5.6-sol
  date: 2026-09-09
- event: source-checked
  by: claude
  date: 2026-10-31
  note: Statement compared with Hatcher, Algebraic Topology, Section 3.3, Exercise 35; it matches the printed text. The diagram is transcribed as printed.
- event: solution-reviewed
  by: claude
  date: 2026-10-31
  note: >-
    Read the argument and repaired one sentence: the four neighbouring vertical maps in Hatcher's
    diagram are isomorphisms by the noncompact duality applied to the interior and to $\partial M$,
    and the five lemma then makes the middle map $D_M$ an isomorphism. The stored text broke off
    mid-sentence ("The middle map is ... are isomorphisms"), which is corrected.
---

::: {.problem}
If $M$ is a noncompact $R$-orientable $n$-manifold with boundary $\partial M$ having a collar neighborhood in $M$, show that there are Poincaré duality isomorphisms $H_c^k(M;R)\approx H_{n-k}(M,\partial M;R)$ for all $k$, using the five-lemma and the following diagram:

$$
\begin{array}{ccccccc}
\cdots\to H_c^{k-1}(\partial M;R)&\to&H_c^k(M,\partial M;R)&\to&H_c^k(M;R)&\to&H_c^k(\partial M;R)\to\cdots\\
\downarrow D_{\partial M}&&\downarrow D_M&&\downarrow D_M&&\downarrow D_{\partial M}\\
\cdots\to H_{n-k}(\partial M;R)&\to&H_{n-k}(M;R)&\to&H_{n-k}(M,\partial M;R)&\to&H_{n-k-1}(\partial M;R)\to\cdots
\end{array}
$$
:::

::: {.solution}
Because $\partial M$ has a collar, compactly supported cohomology has the long exact sequence
$$
\cdots\to H_c^{k-1}(\partial M;R)
\to H_c^k(M,\partial M;R)
\to H_c^k(M;R)
\to H_c^k(\partial M;R)\to\cdots.
$$
The homology long exact sequence of the pair is
$$
\cdots\to H_{n-k}(\partial M;R)
\to H_{n-k}(M;R)
\to H_{n-k}(M,\partial M;R)
\to H_{n-k-1}(\partial M;R)\to\cdots.
$$
Cap product with the fundamental classes gives the vertical maps in Hatcher's diagram, and Exercise 34's cap-product/naturality argument shows the diagram commutes up to sign.

Now $M-\partial M$ is an $R$-orientable noncompact manifold without boundary. By excision through the collar,
$$
H_c^k(M,\partial M;R)\cong H_c^k(M-\partial M;R),
$$
and the already-proved noncompact Poincaré duality theorem gives
$$
H_c^k(M,\partial M;R)\xrightarrow{\cong}H_{n-k}(M;R).
$$
Similarly, $\partial M$ is an $R$-orientable $(n-1)$-manifold without boundary, so
$$
H_c^{k-1}(\partial M;R)\xrightarrow{\cong}H_{n-k}(\partial M;R)
$$
and
$$
H_c^k(\partial M;R)\xrightarrow{\cong}H_{n-k-1}(\partial M;R).
$$
The same interior duality also gives $H_c^{k+1}(M,\partial M;R)\cong H_{n-k-1}(M;R)$. Thus, in the five-term segment displayed in the diagram, the four vertical maps other than the middle one are isomorphisms, the middle one being
$$
D_M:H_c^k(M;R)\longrightarrow H_{n-k}(M,\partial M;R).
$$
The five-lemma applied to this segment therefore makes $D_M$ an isomorphism as well. Hence
$$
\boxed{H_c^k(M;R)\cong H_{n-k}(M,\partial M;R)}
$$
for every $k$.
:::
