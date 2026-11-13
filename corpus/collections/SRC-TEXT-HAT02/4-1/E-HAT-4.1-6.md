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
- event: solution-reviewed
  by: claude
  date: 2026-11-13
  note: >-
    The exercise is on printed p. 358, and it is exactly the statement of Hatcher's Proposition 4.1, printed p. 342, whose proof the book prints there: a covering space $p:(\tilde X,\tilde A,\tilde x_0)\to(X,A,x_0)$ with $\tilde A=p^{-1}(A)$ induces an isomorphism on $\pi_n$ for $n\ge2$, first for $\tilde X\to X$ by lifting a homotopy of maps of $S^n$ through the covering homotopy property, then for the pair by applying the five-lemma to the long exact sequences of the two pairs. The card's proof is that proof, with the lifting criterion of Proposition 1.33 (printed p. 61) named where the book names it. Checked against the book: the printed statement of Proposition 4.1 including the hypothesis $\tilde A=p^{-1}(A)$ and the path-connectedness of $\tilde X$, and the long exact sequence of Theorem 4.3 on p. 344 that the five-lemma step uses.
- event: source-corrected
  by: claude
  date: 2026-11-13
  note: >-
    The preceding note's claim that Exercise 6 "is exactly the statement of Hatcher's Proposition
    4.1" is false and is withdrawn. Proposition 4.1, printed p. 342, is the absolute statement
    $p_*:\pi_n(\tilde X,\tilde x_0)\to\pi_n(X,x_0)$, with proof by the lifting criterion and the
    covering homotopy property. The exercise, printed p. 358, is the relative statement
    $p_*:\pi_n(\tilde X,\tilde A,\tilde x_0)\to\pi_n(X,A,x_0)$ for the pair with
    $\tilde A=p^{-1}(A)$, which the book does not print. The card's remark now says what is printed
    where, and records why the relative case is not Proposition 4.1 plus the five-lemma: in the
    ladder of Theorem 4.3 the map $p_*:\pi_1(\tilde A)\to\pi_1(A)$ is injective and not in general
    surjective, so at $\pi_2$ the five-lemma gives injectivity only. The proof itself is unchanged
    and is the book's lifting argument for triples $(D^n,S^{n-1},s_0)$. Not established here: a
    published proof of the relative statement. Searched for one without result in the retained
    sets (Sam, Li, DeMason, Poulsen, Stanford Math 215C Solution Sets 1--5, the UCR Math 205B help
    file, May's *Concise Course* §4, Bredon Chapters III and VII, Maxim's Math 752 notes) and in
    Hatcher's printed text and its errata.
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

::: {.remark title="Source"}
The exercise is Exercise 6 of §4.1, printed p. 358. Hatcher's Proposition 4.1, printed p. 342 with its proof there, is the absolute statement only: for a covering space projection $p:(\tilde X,\tilde x_0)\to(X,x_0)$, the map $p_*:\pi_n(\tilde X,\tilde x_0)\to\pi_n(X,x_0)$ is an isomorphism for all $n\ge2$, by the lifting criterion of Proposition 1.33 (printed p. 61) for surjectivity and the covering homotopy property for injectivity. The relative statement for a pair, with $\tilde A=p^{-1}(A)$, is not printed in the book, and it does not follow from Proposition 4.1 by the five-lemma: in the ladder of the two long exact sequences of Theorem 4.3 (printed p. 344) the map at $\pi_1$ is only injective, so at $\pi_2$ the five-lemma yields injectivity of $p_*:\pi_2(\tilde X,\tilde A)\to\pi_2(X,A)$ and not surjectivity. The proof above is the book's argument carried out directly for triples $(D^n,S^{n-1},s_0)$ instead of $S^n$: $D^n$ and $D^n\times I$ are simply connected, so Proposition 1.33 lifts the disk and the relative homotopy, whose boundary then lands in $p^{-1}(A)=\tilde A$.
:::
