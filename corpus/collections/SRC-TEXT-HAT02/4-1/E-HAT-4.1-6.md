---
schema: qual/card@1
id: E-HAT-4.1-6
kind: problem
title: "Covering spaces and relative homotopy groups"
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
  note: Checked against Hatcher, Algebraic Topology, Section 4.1, Exercise 6; the stored statement matches.
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
    Read line by line. Correct. Surjectivity: a triple map `f : (D^n, S^{n-1}, s_0) -> (X, A, x_0)` lifts
    uniquely through `p` because `D^n` is simply connected, and since `f(S^{n-1}) subset A` the lift
    carries `S^{n-1}` into `p^{-1}(A) = A~`, so it represents a relative class upstairs. Injectivity: a
    relative homotopy of the projected maps lifts uniquely once its value at `(s_0,0)` is fixed, its two
    ends are the prescribed lifts by uniqueness, and its boundary stays in `p^{-1}(A)`; hence the two
    lifts were already relatively homotopic. The hypothesis `n > 1` is exactly what supplies the simple
    connectivity of `D^n` used in both halves. No correction was needed.
- event: solution-reviewed
  by: claude
  date: 2026-11-07
  note: >-
    Read against Hatcher, Algebraic Topology (2002), §4.1 Exercise 6, printed p. 358, with
    Proposition 4.1 and its proof on p. 342. Nothing false; two steps that were asserted are now
    derived: the existence of the lift of $f$ and of the lift of the relative homotopy is credited to
    the lifting criterion of Proposition 1.33 with the simply-connectedness of $D^n$, respectively of
    $D^n\times I$ (which the card had used without saying that existence, not only uniqueness, is at
    stake), and uniqueness with a prescribed value at one point is Proposition 1.34's uniqueness
    statement, p. 62. This is the relative form of Proposition 4.1 and the proof follows the book's
    argument for that proposition, with $D^n$ in place of $S^n$. No published exercise solution is in
    the retained sets; the book's own Proposition 4.1 proof covers the absolute case only.
---

::: {.problem}
If $p: (\tilde{X}, \tilde{A}, \tilde{x}_0) \to (X, A, x_0)$ is a covering space with $\tilde{A} = p^{-1}(A)$, show that the map $p_*: \pi_n(\tilde{X}, \tilde{A}, \tilde{x}_0) \to \pi_n(X, A, x_0)$ is an isomorphism for all $n > 1$.
:::

::: {.solution}
Represent an element of $\pi_n(X,A,x_0)$, $n>1$, by a map of triples
$$
f:(D^n,S^{n-1},s_0)\longrightarrow(X,A,x_0).
$$
Since $n>1$, the disk $D^n$ is simply connected, so the lifting criterion of Proposition 1.33 (p. 61) applies: a map from a simply connected space into $X$ lifts to $\widetilde X$ once the image of one point is chosen, because the image of its fundamental group is trivial and hence contained in $p_*\pi_1(\widetilde X,\widetilde x_0)$. Taking the value $\widetilde x_0$ at $s_0$, $f$ has a unique lift
$$
\widetilde f:(D^n,s_0)\longrightarrow(\widetilde X,\widetilde x_0),
$$
unique by the uniqueness of lifts of a connected space with a prescribed value at one point (p. 62).
Because $f(S^{n-1})\subset A$, we have
$$
\widetilde f(S^{n-1})\subset p^{-1}(A)=\widetilde A.
$$
Thus $\widetilde f$ represents a class in $\pi_n(\widetilde X,\widetilde A,\widetilde x_0)$, proving surjectivity of $p_*$.

If two lifted maps become relatively homotopic after applying $p$, there is a relative homotopy
$$
F:(D^n\times I,S^{n-1}\times I,\{s_0\}\times I)\to(X,A,x_0).
$$
The space $D^n\times I$ is contractible, hence simply connected, so Proposition 1.33 lifts $F$ to $\widetilde F:D^n\times I\to\widetilde X$ with $\widetilde F(s_0,0)=\widetilde x_0$; then $\widetilde F(S^{n-1}\times I)\subset p^{-1}(A)=\widetilde A$ and $\widetilde F(\{s_0\}\times I)=\widetilde x_0$. By uniqueness of lifts with a prescribed value, the two ends $\widetilde F(-,0)$ and $\widetilde F(-,1)$ are the prescribed lifted maps. So the two lifted maps were already relatively homotopic, which is injectivity.

Therefore
$$
\boxed{p_*:\pi_n(\widetilde X,\widetilde A,\widetilde x_0)\xrightarrow{\cong}\pi_n(X,A,x_0)}
\qquad(n>1).
$$
:::
