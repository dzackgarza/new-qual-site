---
schema: qual/card@1
id: E-HAT-4.2-16
kind: problem
title: "Surfaces with infinite $\\pi_1$ are $K(\\pi, 1)$'s"
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
  note: Checked against Hatcher, Algebraic Topology, Section 4.2, Exercise 16; the stored statement matches.
- event: solution-written
  by: gpt-5.6-sol
  date: 2026-09-09
- event: solution-reviewed
  by: gpt-5.6-sol
  date: 2026-09-09
- event: solution-reviewed
  by: claude
  date: 2026-11-01
  note: >-
    Proof read against Hatcher Sec. 4.2 Exercise 16 (AT.txt 19378-19380) and repaired. The card had
    asserted that a connected noncompact 2-manifold has vanishing top-dimensional integral homology
    without proof or citation, which is the crux of the argument. It is Proposition 3.29 (AT.txt
    11890-11891), "a connected noncompact n-manifold has H_i(M;R)=0 for i>=n", and the printed hint
    directs the reader to precisely that section. The step now cites it and states its n=2, R=Z
    instance. Verified as correct and left unchanged: the least-k argument (minimality gives
    (k-1)-connectivity, Hurewicz gives pi_k = H_k, contradicting acyclicity), H_1 = 0 from simple
    connectivity, and the use of Whitehead's theorem via CW type. Not re-derived: the half-page proof
    of Proposition 3.29 itself, which is the book's.

---

::: {.problem}
Show that the closed surfaces with infinite fundamental group are $K(\pi, 1)$'s by showing that their universal covers are contractible, via the Hurewicz theorem and results of §3.3.
:::

::: {.solution}
Let $M$ be a closed surface with infinite fundamental group, and let
$$
p:\widetilde M\to M
$$
be its universal cover. Then $\widetilde M$ is a simply-connected surface. Since $\pi_1(M)$ is infinite, the covering has infinitely many sheets, so $\widetilde M$ is noncompact.

By Proposition 3.29 of §3.3, a connected noncompact $n$-manifold $N$ has $H_i(N;R)=0$ for $i\ge n$; with $n=2$ and $R=\ZZ$ this gives $H_i(\widetilde M;\ZZ)=0$ for $i\ge2$, in particular
$$
H_2(\widetilde M;\ZZ)=0.
$$
Also
$$
H_1(\widetilde M;\ZZ)=0
$$
because $\widetilde M$ is simply connected. Thus $\widetilde M$ is acyclic.

If some higher homotopy group of $\widetilde M$ were nonzero, choose the least $k\ge2$ with $\pi_k(\widetilde M)\ne0$. Then $\widetilde M$ would be $(k-1)$-connected, and Hurewicz would give
$$
\pi_k(\widetilde M)\cong H_k(\widetilde M),
$$
contradicting acyclicity. Hence all homotopy groups of $\widetilde M$ vanish. Since $\widetilde M$ has CW type, Whitehead's theorem gives
$$
\widetilde M\simeq *.
$$
Therefore
$$
\boxed{M\text{ is a }K(\pi_1(M),1).}
$$
:::
