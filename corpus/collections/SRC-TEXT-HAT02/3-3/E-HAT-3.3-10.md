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

- event: source-checked
  by: claude
  date: 2026-11-07
  note: >-
    A fuller published source now covers the gap omitted by Li: Stanford Math 215C Solution Set 3,
    printed p.1, Hatcher 3.3 #10. Its infinite-sheeted branch observes noncompactness of the total
    space and applies Proposition 3.29, as also used in the earlier version here; its finite branch
    has exactly the lift and multiplicativity argument. This supersedes relying on Li for the
    finite case alone.

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

The lifting and both sheet-count cases are in **Stanford Math 215C, Solution Set 3**, problem 10, printed p. 1, [`solution3.pdf`](https://math.stanford.edu/~ralph/math215c/solution3.pdf): the lift satisfies $\deg f=\deg p\deg\widetilde f$; finitely-sheeted covers have $|\deg p|$ equal to the sheet count by Exercises 9 and force that count to be $1$; and in an infinite-sheeted cover the total space is noncompact, so $H_n(\widetilde N;\ZZ)=0$ by Proposition 3.29, p. 239. The card's compact-discrete-fiber remark makes that noncompactness precise. The final passage to abelianizations is the one in the same set.

:::
