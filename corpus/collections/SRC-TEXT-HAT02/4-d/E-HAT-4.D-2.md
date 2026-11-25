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
- event: source-checked
  by: claude
  date: 2026-11-19
  note: >-
    Read against Hatcher, Exercise 2 of §4.D, printed p. 447, with the Leray--Hirsch theorem on
    printed p. 432 and the Bockstein of §3.E (p. 303). Correct: $S^\infty/\ZZ_p$ is a $K(\ZZ_p,1)$
    and the bundle $S^1\to S^\infty/\ZZ_p\to\CP^\infty$ has fibre $S^1/\ZZ_p\cong S^1$; the
    restriction of the degree-one class $a$ generates $H^1$ of the fibre because
    $H^1(-;\ZZ_p)=\operatorname{Hom}(\pi_1(-),\ZZ_p)$ and $\ZZ\to\ZZ_p$ is onto, so Leray--Hirsch
    gives $H^*=\ZZ_p[b]\{1,a\}$ with $|a|=1$, $|b|=2$. For odd $p$, $a^2=-a^2$ by graded
    commutativity, so the ring is $\Lambda(a)\otimes\ZZ_p[b]$; for $p=2$, $a^2\ne0$ and the
    Bockstein is $Sq^1$, which on a degree-one class is the square, so $b=a^2$ and the ring is
    $\ZZ_2[a]$. Nothing changed. Not claimed: a published solution, and no certificate.
- event: solution-reviewed
  by: claude
  date: 2026-11-22
  note: >-
    Read against Hatcher, §4.D Exercise 2. A provenance record is added, the card having carried
    none: no retained solution set covers the exercise. The proof reads correct; the one unjustified
    sentence, "$\beta(a)=b$", is recorded in the audit and is not used by the argument.
- event: solution-reviewed
  by: claude
  date: 2026-11-22
  note: >-
    The sentence "$\beta(a)=b$" is now derived rather than asserted, from a referee report: Hatcher's
    theorem of §4.L on $H^*(K(\ZZ_p,n);\ZZ_p)$ specializes at $n=1$ to
    $\Lambda_{\ZZ_p}[\iota]\otimes\ZZ_p[\beta\iota]$, so the even generator is $\beta\iota$ by
    construction, which is $b$; and for $p=2$ it gives $\ZZ_2[\iota]$, where $Sq^1$ is the Bockstein
    for that coefficient sequence (Theorem 4L.12(7)) and $Sq^1$ of a degree-one class is its square,
    so $b=a^2$. The earlier audit remark that the sentence was unused is withdrawn: the live
    conclusion uses it.
---

::: {.problem}
Apply the Leray–Hirsch theorem to the bundle $S^1 \to S^\infty/\ZZ_p \to \CP^\infty$ to compute $H^*(K(\ZZ_p, 1); \ZZ_p)$ from $H^*(\CP^\infty; \ZZ_p)$.
:::

::: {.solution}
No retained solution set covers this exercise: Sam's set ends at §4.3, Koukpari's §4.D heading carries no solutions, and Proudfoot's sheets are §4.1 and §4.2. The argument is the card's own.

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
restricts to the generator of $H^1(S^1;\ZZ_p)$. The Leray--Hirsch theorem (Theorem 4D.1) applies, since $H^*(S^1;\ZZ_p)$ is free with generator the restriction of $a$; it gives
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
The Bockstein associated to $0\to\ZZ_p\to\ZZ_{p^2}\to\ZZ_p\to0$ (defined in §3.E) satisfies $\beta(a)=b$, and this is Hatcher's own computation rather than an inference about lifting: the theorem of §4.L on $H^*(K(\ZZ_p,n);\ZZ_p)$ specializes at $n=1$ to $H^*(K(\ZZ_p,1);\ZZ_p)=\Lambda_{\ZZ_p}[\iota]\otimes\ZZ_p[\beta\iota]$ with $\iota$ of degree one, so the even generator is $\beta\iota=\beta(a)$ by definition of the second factor, and it is the class $b$ here. For $p=2$ the same place gives $H^*(K(\ZZ_2,1);\ZZ_2)=\ZZ_2[\iota]$ with $\iota$ of degree one; $Sq^1$ is the Bockstein for that coefficient sequence (Theorem 4L.12(7)) and $Sq^1$ of a degree-one class is its square, so $b=a^2$. Hence
$$
\boxed{H^*(K(\ZZ_2,1);\ZZ_2)\cong\ZZ_2[a],\quad \gradeddegree{a}=1.}
$$
:::
