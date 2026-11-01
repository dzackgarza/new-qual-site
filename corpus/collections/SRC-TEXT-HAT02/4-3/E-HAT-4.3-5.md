---
schema: qual/card@1
id: E-HAT-4.3-5
kind: problem
title: "$[X, S^n] \\approx H^n(X; \\ZZ)$ for $n$-dimensional $X$"
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
  note: Checked against Hatcher, Algebraic Topology, Section 4.3, Exercise 5; the stored statement matches.
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
Show that $[X, S^n] \approx H^n(X; \ZZ)$ if $X$ is an $n$-dimensional CW complex. [Build a $K(\ZZ, n)$ from $S^n$ by attaching cells of dimension $\geq n + 2$.]
:::

::: {.solution}
Choose a map
$$
j:S^n\to K(\ZZ,n)
$$
representing the generator of $\pi_nK(\ZZ,n)$. It induces an isomorphism on $\pi_i$ for $i\le n$: both spaces have zero homotopy groups below $n$, and $j_*:\pi_n(S^n)\to\ZZ$ is an isomorphism.

If $X$ is $n$-dimensional, obstruction theory or cellular induction says that an $n$-equivalence of targets induces a bijection
$$
j_*:[X,S^n]\xrightarrow{\cong}[X,K(\ZZ,n)].
$$
Indeed, maps and homotopies from an $n$-dimensional CW complex depend only on the homotopy groups of the target through degree $n$.

Finally representability gives
$$
[X,K(\ZZ,n)]\cong H^n(X;\ZZ).
$$
Therefore
$$
\boxed{[X,S^n]\cong H^n(X;\ZZ).}
$$
:::
