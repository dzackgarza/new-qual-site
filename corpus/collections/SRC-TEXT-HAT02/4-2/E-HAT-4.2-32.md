---
schema: qual/card@1
id: E-HAT-4.2-32
kind: problem
title: "Fiber bundles $S^k \to S^m \to S^n$"
classification:
  areas:
  - topology
  topics:
  - Higher Homotopy Groups
relations: []
audit:
- event: solution-reviewed
  by: claude
  date: 2026-11-02
  note: >-
    Cards read. Verdict record is m7__proofs-4-2-14-26.md (14-26: 11 correct, 16 and 26 each a single named step; both repaired) and m5__proofs-4-2-27-39.md (27-39: 10 correct, 28, 29 defective single cases, 34 a wrong intermediate assertion; all three repaired). No card in this slice has an unmet piece.

- event: solution-written
  by: Codex 5.3 Spark Extra High
  date: 2026-08-30
- event: source-corrected
  by: claude
  date: 2026-11-01
  note: >-
    Statement repaired against Hatcher's printed text: the card had dropped printed matter
    (a bracketed hint or pointer, or a printed sentence) that an audit located by word-by-word
    comparison with tmp/hat/AT.txt, and that this session re-verified at the cited lines before
    applying the repair. The restored text is the printed wording and the mathematics of the
    statement is otherwise unchanged.
review: draft
---

::: {.problem}
Show that if $S^k \to S^m \to S^n$ is a fiber bundle, then $k = n-1$ and $m = 2n-1$. [Look at the long exact sequence of homotopy groups.]
:::

::: {.solution}
Suppose first that $n\ge2$. The fiber cannot be $S^0$: a two-sheeted cover of the simply connected sphere $S^n$ is disconnected, while $S^m$ is connected. Thus $k\ge1$. A local trivialization is a product of a $k$-manifold and an $n$-manifold, so $m=n+k$.

The bundle's homotopy exact sequence in degree $n$ contains
$$
\pi_n(S^m)\longrightarrow\pi_n(S^n)\longrightarrow\pi_{n-1}(S^k).
$$
Since $m>n$, the first group is zero and the second is $\ZZ$. Hence the last group is nonzero, which requires $n-1\ge k$.

In degree $k+1$ the sequence contains
$$
\pi_{k+1}(S^n)\longrightarrow\pi_k(S^k)\longrightarrow\pi_k(S^m).
$$
Since $m>k$, the last group is zero and the middle group is $\ZZ$. Thus the first group is nonzero, which requires $k+1\ge n$. The two inequalities give $k=n-1$, and therefore $m=n+k=2n-1$.

For $n=1$, a connected fiber $S^k$ with $k\ge1$ would make $\pi_1(S^m)\to\pi_1(S^1)$ surjective. The dimension equation gives $m=k+1\ge2$, so this is impossible. Thus $k=0$ and $m=1$, as asserted.
:::
