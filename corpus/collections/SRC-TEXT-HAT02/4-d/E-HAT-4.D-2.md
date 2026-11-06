---
schema: qual/card@1
id: E-HAT-4.D-2
kind: problem
title: Cohomology of $K(\ZZ_p, 1)$ via Leray--Hirsch
classification:
  areas:
  - topology
  topics:
  - Fiber Bundles
  - Cohomology
relations: []
review: draft
audit:
- event: source-checked
  by: gpt-5.6-sol
  date: 2026-09-09
  note: Checked against Hatcher, Algebraic Topology, Section 4.D, Exercise 2; the stored statement matches.
- event: solution-written
  by: gpt-5.6-sol
  date: 2026-09-09
- event: solution-reviewed
  by: gpt-5.6-sol
  date: 2026-09-09
---

::: {.problem}
Apply the Leray–Hirsch theorem to the bundle $S^1 \to S^\infty/\ZZ_p \to \CP^\infty$ to compute $H^*(K(\ZZ_p, 1); \ZZ_p)$ from $H^*(\CP^\infty; \ZZ_p)$.
:::

::: {.solution}
Consider
$$
S^1\longrightarrow S^\infty/\ZZ_p\xrightarrow{q}\CP^\infty.
$$
The inclusion of a fiber induces on fundamental groups the reduction map
$$
\ZZ=\pi_1(S^1)\longrightarrow\pi_1(S^\infty/\ZZ_p)=\ZZ_p.
$$
Here $S^\infty/\ZZ_p$ is a $K(\ZZ_p,1)$, since $\ZZ_p\subset S^1$ acts freely on the contractible space $S^\infty$. Because $H^1(-;\ZZ_p)=\operatorname{Hom}(\pi_1(-),\ZZ_p)$, the reduction $\ZZ\to\ZZ_p$ being onto means the generator
$$
a\in H^1(S^\infty/\ZZ_p;\ZZ_p)
$$
restricts to the generator of $H^1(S^1;\ZZ_p)$. The Leray--Hirsch theorem (Theorem 4D.1, p. 432) applies, since $H^*(S^1;\ZZ_p)$ is free with generator the restriction of $a$; it gives
$$
H^*(K(\ZZ_p,1);\ZZ_p)
\cong H^*(\CP^\infty;\ZZ_p)\{1,a\}
$$
as a module. If $b=q^*c$, where $c$ generates $H^2(\CP^\infty;\ZZ_p)$, then
$$
H^*(K(\ZZ_p,1);\ZZ_p)
\cong \ZZ_p[b]\{1,a\},
\qquad \gradeddegree{a}=1,\ \gradeddegree{b}=2.
$$
For odd $p$, graded commutativity gives $a^2=-a^2$, hence $a^2=0$, so
$$
\boxed{H^*(K(\ZZ_p,1);\ZZ_p)
\cong \Lambda(a)\otimes\ZZ_p[b]\qquad(p\text{ odd}).}
$$
The Bockstein associated to $0\to\ZZ_p\to\ZZ_{p^2}\to\ZZ_p\to0$ (defined in §3.E, p. 303) satisfies $\beta(a)=b$: by construction it detects whether the class lifts to $\ZZ_{p^2}$ coefficients, and $a$ does not, while $a$ generates $H^1$ of the fiber. For $p=2$ the Bockstein is $Sq^1$ (Theorem 4L.12(7), p. 504), and $Sq^1$ of a degree-one class is its square, so $b=a^2$. Hence
$$
\boxed{H^*(K(\ZZ_2,1);\ZZ_2)\cong\ZZ_2[a],\quad \gradeddegree{a}=1.}
$$
:::
