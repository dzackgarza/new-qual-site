---
schema: qual/card@1
id: E-HAT-3.3-10
kind: problem
title: Degree 1 implies surjection on $\pi_1$
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
  note: Checked against Hatcher, Algebraic Topology, Section 3.3, Exercise 10; the stored statement matches.
- event: solution-written
  by: gpt-5.6-sol
  date: 2026-09-09
- event: solution-reviewed
  by: gpt-5.6-sol
  date: 2026-09-09
- event: source-checked
  by: claude
  date: 2026-10-31
  note: Statement compared with Hatcher, Algebraic Topology, Section 3.3, Exercise 10; it matches the printed text. The printed bracketed hint about lifting $f$ to the covering space corresponding to $\operatorname{Im} f_*$ was missing and is restored.
- event: solution-reviewed
  by: claude
  date: 2026-10-31
  note: >-
    Read the argument: lift $f$ to the covering corresponding to $\operatorname{Im} f_*$; an
    infinite-sheeted cover is a connected noncompact $n$-manifold with trivial $H_n$, which would
    force $f_*[M]=0$, so the cover is finite of degree $d$, and $1=\pm\deg f=d\cdot\deg\tilde f$
    forces $d=1$.
- event: solution-written
  by: claude
  date: 2026-11-07
  note: >-
    Published-source citation and an actual gap repair. The finite-sheeted lifting/multiplicativity
    argument is Guanyu Li, Hatcher.pdf, Exercise 3.3.5 (Hatcher 3.3 #10), printed p.57: integer
    degrees force the lift and covering both to have degree +-1, hence one sheet and surjectivity
    on pi_1, followed by abelianization. Li omits infinite-sheeted covers; the card proves that an
    infinite-sheeted total space is noncompact (a compact one has finite compact discrete fibers)
    and applies Proposition 3.29 p.239 to get top homology zero, contradicting degree one. The
    source file is not claimed complete or error-free.

---

::: {.problem}
Show that for a degree 1 map $f: M \to N$ of connected closed orientable manifolds, the induced map $f_*: \pi_1 M \to \pi_1 N$ is surjective, hence also $f_*: H_1(M) \to H_1(N)$.
[Lift $f$ to the covering space $\tilde N \to N$ corresponding to the subgroup $\operatorname{Im} f_* \subset \pi_1 N$, then consider the two cases that this covering is finite-sheeted or infinite-sheeted.]
:::

::: {.solution}
Let
$$
H=\operatorname{Im}\bigl(f_*:\pi_1(M)\to\pi_1(N)\bigr).
$$
Let
$$
p:\widetilde N\to N
$$
be the connected covering corresponding to $H$. By the lifting criterion, $f$ lifts to
$$
\widetilde f:M\to\widetilde N,
\qquad p\circ\widetilde f=f.
$$

If $p$ has infinitely many sheets, then $\widetilde N$ is a connected noncompact $n$-manifold: were $\widetilde N$ compact, a fiber would be compact and discrete, hence finite. Hence by Proposition 3.29, p. 239,
$$
H_n(\widetilde N;\ZZ)=0.
$$
Therefore
$$
f_*[M]=p_*\widetilde f_*[M]=0,
$$
contradicting $\deg f=1$.

Thus $p$ is finite-sheeted, say of degree $d=[\pi_1(N):H]$. Since $N$ is orientable, so is $\widetilde N$, and Exercise 9 gives
$$
\abs{\deg p}=d.
$$
Degrees multiply under composition, so
$$
1=\abs{\deg f}=\abs{\deg p}\,\abs{\deg\widetilde f}=d\,\abs{\deg\widetilde f}.
$$
Hence $d=1$. Therefore $H=\pi_1(N)$ and
$$
\boxed{f_*:\pi_1(M)\twoheadrightarrow\pi_1(N)}.
$$
Passing to abelianizations gives the surjection
$$
f_*:H_1(M)\twoheadrightarrow H_1(N).
$$

The finite-sheeted part is the argument in Guanyu Li, [`Hatcher.pdf`](https://guanyulee.github.io/Hatcher.pdf), Exercise 3.3.5 (Hatcher §3.3 #10), printed p. 57, also held locally as `tmp/sources/hatcher-solutions-guanyu-li.pdf`: after lifting, the multiplicativity of degree gives $1=\deg\widetilde f\,\deg p$, so the two integers are $\pm1$ and the covering has one sheet. Li's displayed argument does not treat infinitely many sheets, so the noncompact $H_n(\widetilde N;\ZZ)=0$ step above is the required separate case; it is not omitted from this card.
:::
