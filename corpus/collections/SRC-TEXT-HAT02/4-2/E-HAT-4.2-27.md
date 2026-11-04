---
schema: qual/card@1
id: E-HAT-4.2-27
kind: problem
title: "Image of $\\pi_2(X) \\to \\pi_2(X,A)$ is central"
classification:
  areas:
  - topology
  topics:
  - Higher Homotopy Groups
relations: []
review: draft
audit:
- event: solution-reviewed
  by: claude
  date: 2026-11-02
  note: >-
    Cards read. Verdict record is m7__proofs-4-2-14-26.md (14-26: 11 correct, 16 and 26 each a single named step; both repaired) and m5__proofs-4-2-27-39.md (27-39: 10 correct, 28, 29 defective single cases, 34 a wrong intermediate assertion; all three repaired). No card in this slice has an unmet piece.

- event: source-checked
  by: gpt-5.6-sol
  date: 2026-09-09
  note: Checked against Hatcher, Algebraic Topology, Section 4.2, Exercise 27; the stored statement matches.
- event: solution-written
  by: gpt-5.6-sol
  date: 2026-09-09
- event: solution-reviewed
  by: gpt-5.6-sol
  date: 2026-09-09
- event: source-corrected
  by: claude
  date: 2026-11-01
  note: >-
    Statement repaired against Hatcher's printed text: the card had dropped printed matter
    (a bracketed hint or pointer, or a printed sentence) that an audit located by word-by-word
    comparison with tmp/hat/AT.txt, and that this session re-verified at the cited lines before
    applying the repair. The restored text is the printed wording and the mathematics of the
    statement is otherwise unchanged.
---

::: {.problem}
Show that the image of the map $\pi_2(X, x_0) \to \pi_2(X, A, x_0)$ lies in the center of $\pi_2(X, A, x_0)$. (This exercise should be in §4.1.)
:::

::: {.solution}
Let
$$
j_*:\pi_2(X,x_0)\to\pi_2(X,A,x_0)
$$
be the natural map, and let
$$
a\in\operatorname{im}j_*.
$$
Exactness of the long homotopy sequence of the pair gives
$$
\partial a=0\in\pi_1(A,x_0).
$$
For arbitrary $b\in\pi_2(X,A,x_0)$, Lemma 4.39 says
$$
a+b-a=(\partial a)b.
$$
Since $\partial a$ is the identity element of $\pi_1(A,x_0)$, its action on $b$ is trivial, so
$$
a+b-a=b.
$$
Hence
$$
a+b=b+a.
$$
Thus every element in the image of $j_*$ commutes with every element of the relative group:
$$
\boxed{\operatorname{im}\bigl(\pi_2(X)\to\pi_2(X,A)\bigr)
\subseteq Z\bigl(\pi_2(X,A)\bigr).}
$$
:::
