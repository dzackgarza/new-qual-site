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

- event: solution-written
  by: claude
  date: 2026-11-18
  note: >-
    Lamport structure for the two cases of the hint, which is what Queue D asks for on this card. The lift, the infinite-sheeted contradiction, the finite-sheeted degree count and the two conclusions are separate steps; the compact-discrete-fiber remark the prose used to justify noncompactness now sits inside the infinite-sheeted step together with the reason the total space is connected, and the import of deg f = 1 (that f_*[M] is a nonzero generator) is stated rather than left implicit. A trailing paragraph repeating the citation after the proof is folded into the lead sentence. No statement repair: the exercise is Hatcher §3.3 Exercise 10, printed p. 258, Proposition 3.29 is on printed p. 239, and the argument is the Stanford 215C set's (Solution Set 3, problem 10, printed p. 1).
---

::: {.problem}
Show that for a degree 1 map $f: M \to N$ of connected closed orientable manifolds, the induced map $f_*: \pi_1 M \to \pi_1 N$ is surjective, hence also $f_*: H_1(M) \to H_1(N)$.
[Lift $f$ to the covering space $\tilde N \to N$ corresponding to the subgroup $\operatorname{Im} f_* \subset \pi_1 N$, then consider the two cases that this covering is finite-sheeted or infinite-sheeted.]
:::

::: {.solution}
The published solution is **Stanford Math 215C, Spring 2009, Solution Set 3, problem 10, printed p. 1** ([`solution3.pdf`](https://math.stanford.edu/~ralph/math215c/solution3.pdf)): the lift, the two cases for the sheet number of the cover, and the passage to abelianizations are its. The statement is Hatcher, *Algebraic Topology* (2002), §3.3 Exercise 10, and the hint followed is the exercise's own.

::: pf

::: {.pf-step #lift}
With $H=\operatorname{im}\bigl(f_*:\pi_1(M)\to\pi_1(N)\bigr)$ and $p:\widetilde N\to N$ the connected covering corresponding to $H$, the map $f$ lifts to $\widetilde f:M\to\widetilde N$ with $p\circ\widetilde f=f$.

::: pf-proof
The lifting criterion applies: $M$ is a connected manifold, hence connected and locally path connected, and $f_*\bigl(\pi_1(M)\bigr)\subset H=p_*\bigl(\pi_1(\widetilde N)\bigr)$, the right side being $H$ by the choice of the cover. So a lift exists with the stated property.
:::

:::

::: {.pf-step #infinite}
$p$ does not have infinitely many sheets.

::: pf-proof
If it did, $\widetilde N$ would be a connected noncompact $n$-manifold: it is connected because it corresponds to the subgroup $H$, and if it were compact then a fiber, a discrete closed subset, would be finite. Hence $H_n(\widetilde N;\ZZ)=0$ by Proposition 3.29, which says $H_i$ vanishes for $i\ge n$ on a connected noncompact $n$-manifold. Then
$$
f_*[M]=p_*\widetilde f_*[M]=0 ,
$$
because $\widetilde f_*[M]\in H_n(\widetilde N;\ZZ)=0$; while $f_*[M]=\deg f\,[N]=[N]\ne0$, since $\deg f=1$ and $[N]$ generates $H_n(N;\ZZ)\cong\ZZ$. The contradiction rules out an infinite-sheeted cover.
:::

:::

::: {.pf-step #finite}
$p$ has one sheet, so $H=\pi_1(N)$.

::: pf-proof
By step [](#infinite){.pf-ref} the cover is finite-sheeted, say of degree $d$; then $d$ is the index $[\pi_1(N):H]$. A finite-sheeted cover of the closed orientable manifold $N$ is itself closed and orientable, and §3.3 Exercise 9 gives $\abs{\deg p}=d$. Degrees multiply under composition, so
$$
1=\abs{\deg f}=\abs{\deg p}\cdot\abs{\deg\widetilde f}=d\cdot\abs{\deg\widetilde f},
$$
which forces $d=1$. An index-one subgroup is the whole group, so $H=\pi_1(N)$.
:::

:::

::: {.pf-step #surjective}
$f_*:\pi_1(M)\to\pi_1(N)$ is surjective, and so is $f_*:H_1(M)\to H_1(N)$.

::: pf-proof
$H$ is by definition the image of $f_*: \pi_1(M)\to\pi_1(N)$, and step [](#finite){.pf-ref} gives $H=\pi_1(N)$; that is the surjectivity
$$
\boxed{f_*:\pi_1(M)\twoheadrightarrow\pi_1(N)} .
$$
Abelianization is a functor and $H_1=\pi_1^{\mathrm{ab}}$, so the surjection of fundamental groups induces a surjection $H_1(M)\twoheadrightarrow H_1(N)$, which is the second assertion.
:::

:::

:::
:::
