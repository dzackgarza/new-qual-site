---
schema: qual/card@1
id: E-HAT-4.J-1
kind: problem
title: "Reduction of $\\Omega\\Sigma X$ to the connected case"
classification:
  areas:
  - topology
  topics:
  - Homotopy Theory
  - Loop Spaces
relations: []
review: draft
audit:
- event: source-checked
  by: claude
  date: 2026-11-06
  note: >-
    Read on the printed page: Hatcher, Algebraic Topology, Section 4.J, Exercise 1,
    book page 475, read from a 300 dpi render of PDF page 484 (the printed page is
    not marked in the text extraction, whose two layers garble the statement).
    The statement is stored verbatim.
- event: solution-written
  by: claude
  date: 2026-11-06
  note: >-
    Proved from the book: the reduced suspension is the smash product with $S^1$
    (Example 0.10, p. 13), and collapsing an interval in a suspension is a homotopy
    equivalence by Proposition 0.17 (p. 15). The one case in which the printed claim
    fails is recorded in the solution: a non-base component consisting of a single
    point leaves an extra $S^1$ summand, and the counterexample is worked out there.
---

::: {.problem}
Show that $\Omega\Sigma X$ for a nonconnected CW complex $X$ reduces to the connected case by showing that each path-component of $\Omega\Sigma X$ is homotopy equivalent to $\Omega\Sigma(\bigvee_\alpha X_\alpha)$ where the $X_\alpha$'s are the components of $X$.
:::

::: {.solution}
Choose a $0$-cell $*_\alpha\in X_\alpha$ in every component, with $*_{\alpha_0}=x_0$ the basepoint of $X$, and regard $X_\alpha$ as a based space. By Example 0.10 (p. 12), which also identifies the reduced suspension with the smash product, the reduced suspension is
$$
\Sigma X=X\wedge S^1=(X\times S^1)\big/\big(X\times\{s_0\}\cup\{x_0\}\times S^1\big),
$$
so it is computed componentwise. The piece belonging to $X_\alpha$ is the quotient of $X_\alpha\times S^1$ by $X_\alpha\times\{s_0\}$ and, for $\alpha=\alpha_0$ only, by $\{x_0\}\times S^1$:

* for $\alpha=\alpha_0$ the piece is $X_{\alpha_0}\wedge S^1=\Sigma X_{\alpha_0}$;
* for $\alpha\ne\alpha_0$ the piece is $X_\alpha\times S^1$ with $X_\alpha\times\{s_0\}$ collapsed, that is the *unreduced* suspension $S(X_\alpha)=X_\alpha\times I/(X_\alpha\times\partial I)$, with $I$ a circle with basepoint $s_0$ cut open there.

All pieces meet in the single basepoint, so
$$
\Sigma X\ =\ \Sigma X_{\alpha_0}\ \vee\bigvee_{\alpha\ne\alpha_0}S(X_\alpha)
\tag{1}
$$
as spaces.

Now suppose first that no component of $X$ is a single point. Then for $\alpha\ne\alpha_0$ the pair $\big(S(X_\alpha),\{*_\alpha\}\times I\big)$ is a CW pair whose second term is a contractible interval, so collapsing that interval — which is exactly the passage from $S(X_\alpha)$ to $\Sigma X_\alpha$ — is a homotopy equivalence by Proposition 0.17 (p. 15). Applying this to (1) gives
$$
\Sigma X\ \simeq\ \bigvee_\alpha\Sigma X_\alpha\ =\ \Sigma\Big(\bigvee_\alpha X_\alpha\Big),
\tag{2}
$$
the last equality because the reduced suspension of a wedge of based spaces is the wedge of the suspensions. Hence
$$
\Omega\Sigma X\ \simeq\ \Omega\Sigma\Big(\bigvee_\alpha X_\alpha\Big).
\tag{3}
$$
The right side is a loop space, hence path-connected, and $\bigvee_\alpha X_\alpha$ is connected because the components are path-connected and share the basepoint. Therefore $\Omega\Sigma X$ is path-connected by (3): it has a single path-component, namely itself, and (3) is the statement of the exercise.

That is the sense in which the nonconnected case reduces to the connected one: the replacement $X\rightsquigarrow\bigvee_\alpha X_\alpha$ produces a *connected* CW complex, so Theorem 4J.1 (p. 471), whose hypothesis is that the complex be connected, applies to it, and (3) carries its conclusion — the weak equivalence $J(\bigvee_\alpha X_\alpha)\to\Omega\Sigma(\bigvee_\alpha X_\alpha)$ — over to $\Omega\Sigma X$ componentwise.

It remains to record the one case in which the printed statement fails. If $\alpha\ne\alpha_0$ and $X_\alpha$ consists of a single point, then $X_\alpha$ is degenerate at $*_\alpha$, Proposition 0.17 does not apply to the pair $\big(S(X_\alpha),\{*_\alpha\}\times I\big)$ — its second term *is* the whole space — and indeed $S(X_\alpha)=S^1$ while $\Sigma X_\alpha=*$. Taking $X=S^1\sqcup\{\mathrm{pt}\}$ with the basepoint on the circle, (1) gives
$$
\Sigma X=S^2\vee S^1,\qquad\text{while}\qquad \Sigma\Big(\bigvee_\alpha X_\alpha\Big)=\Sigma S^1=S^2,
$$
and these are not homotopy equivalent. Consequently the component of the constant loop in $\Omega\Sigma X$ is not homotopy equivalent to $\Omega\Sigma(\bigvee_\alpha X_\alpha)$: its fundamental group is $\pi_2(S^2\vee S^1)$, and the universal cover of $S^2\vee S^1$ is homotopy equivalent, by Proposition 0.17 (p. 15) applied to its subcomplex $\mathbb{R}$, to the infinite wedge $\bigvee_{\mathbb{Z}}S^2$, whose $\pi_2$ is the direct sum of countably many copies of $\pi_2(S^2)\cong\ZZ$; whereas $\pi_1(\Omega S^2)=\pi_2(S^2)\cong\ZZ$. So the printed statement holds for every nonconnected CW complex whose components are not single points, and fails for $S^1\sqcup\{\mathrm{pt}\}$; with the extra summand displayed in (1), the general statement is that each path-component of $\Omega\Sigma X$ is homotopy equivalent to $\Omega\Sigma$ of $\Sigma(\bigvee_\alpha X_\alpha)\vee\bigvee_{\alpha\in D}S^1$, where $D$ is the set of non-base components that are single points.
:::
