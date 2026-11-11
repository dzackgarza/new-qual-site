---
schema: qual/card@1
id: E-WRMSX
kind: problem
title: Antipode-separating maps of the sphere are surjective
classification:
  areas:
  - topology
  topics:
  - Borsuk-Ulam Theorem
relations: []
review: draft
audit:
- event: source-checked
  by: gpt-5.6-sol
  date: 2026-09-10
- event: solution-written
  by: gpt-5.6-sol
  date: 2026-09-10
- event: solution-reviewed
  by: gpt-5.6-sol
  date: 2026-09-10
- event: source-checked
  by: claude
  date: 2026-11-11
  note: >-
    Checked line by line against Munkres, Topology (2000), Section 57 Exercise 2, printed p. 359,
    with Theorem 57.3 and the book's hint that $S^2-p$ is homeomorphic to $\RR^2$. The card composes $g$ with a homeomorphism $S^2-p\to\RR^2$ off a point missed by $g$ and applies Borsuk-Ulam, so the injectivity of that homeomorphism gives $g(x)=g(-x)$. No complete published solution was located for this exercise: dbFin's Chapter 9 pages run from Section 51 to Section 56 only, and every set searched is listed in the COMPLAINTS.md entry for Sections 57 to 60. The proof is the card's own and every step was checked against the book.
---

::: {.exercise}

Show that if $g: S^2 \to S^2$ is continuous and $g(x) \neq g(-x)$ for all $x$, then $g$ is surjective.
[Hint: If $p \in S^2$, then $S^2 - \theset{p}$ is homeomorphic to $\RR^2$.]
:::

::: {.solution}
Suppose, toward a contradiction, that $g$ is not surjective. Choose
$$
p\in S^2-g(S^2).
$$
Since $S^2-\{p\}$ is homeomorphic to $\RR^2$, choose a homeomorphism
$$
\phi:S^2-\{p\}\longrightarrow\RR^2.
$$
Then
$$
F=\phi\circ g:S^2\to\RR^2
$$
is continuous. By the Borsuk--Ulam theorem there exists $x\in S^2$ with
$$
F(x)=F(-x).
$$
Since $\phi$ is injective, this implies
$$
g(x)=g(-x),
$$
contrary to the hypothesis. Therefore $g$ must be surjective.
:::
