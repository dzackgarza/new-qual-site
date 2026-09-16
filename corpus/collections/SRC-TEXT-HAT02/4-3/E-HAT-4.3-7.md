---
schema: qual/card@1
id: E-HAT-4.3-7
kind: problem
title: "Addition in $\\langle X, K(G,n) \\rangle$ matches cohomology"
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
  note: Checked against Hatcher, Algebraic Topology, Section 4.3, Exercise 7; the stored statement matches.
- event: solution-written
  by: gpt-5.6-sol
  date: 2026-09-09
- event: solution-reviewed
  by: gpt-5.6-sol
  date: 2026-09-09
---

::: {.problem}
Using an H-space multiplication $\mu$ on $K(G, n)$, define an addition in $\langle X, K(G, n) \rangle$ by $[f] + [g] = [\mu(f, g)]$ and show that under the bijection $H^n(X; G) \approx \langle X, K(G, n) \rangle$ this addition corresponds to the usual addition in cohomology.
:::

::: {.solution}
Let
\[
u\in H^n(K(G,n);G)
\]
be the universal class corresponding to the identity homomorphism of \(G\). For the H-space multiplication \(\mu\), Exercise 6 says that \(\mu_*\) on \(\pi_n=G\oplus G\) is addition. Hence, under the Künneth/representability identification,
\[
\mu^*u=\operatorname{pr}_1^*u+\operatorname{pr}_2^*u.
\]

If \(f,g:X\to K(G,n)\), then
\[
(\mu(f,g))^*u
=(f,g)^*\mu^*u
=f^*u+g^*u.
\]
The representing-space bijection
\[
\langle X,K(G,n)\rangle\xrightarrow{\cong}H^n(X;G)
\]
sends \([f]\) to \(f^*u\). Therefore the multiplication-induced addition satisfies
\[
\boxed{[f]+[g]\longleftrightarrow f^*u+g^*u,}
\]
which is exactly the usual addition in cohomology.
:::
