---
schema: qual/card@1
id: E-HAT-4.2-22
kind: problem
title: "$H_{n+1}(K(G,n); \\ZZ) = 0$ for $n > 1$"
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
  note: Checked against Hatcher, Algebraic Topology, Section 4.2, Exercise 22; the stored statement matches.
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
Show that $H_{n+1}(K(G, n); \ZZ) = 0$ if $n > 1$. [Build a $K(G, n)$ from a Moore space $M(G, n)$ by attaching cells of dimension $> n + 1$.]
:::

::: {.solution}
For $n>1$, choose an $(n-1)$-connected Moore space $M(G,n)$, so
$$
\widetilde H_i(M(G,n);\ZZ)=
\begin{cases}
G,&i=n,\\
0,&i\ne n.
\end{cases}
$$
By Hurewicz, $\pi_n(M(G,n))\cong G$.

Construct a $K(G,n)$ from $M(G,n)$ by killing $\pi_{n+1},\pi_{n+2},\dots$ successively. To kill $\pi_k$ one attaches $(k+1)$-cells. Thus the first cells added have dimension $n+2$, and all later cells have still larger dimension. No $(n+1)$-cells are added.

Initially
$$
H_{n+1}(M(G,n))=0.
$$
Attaching cells of dimension $n+2$ can only quotient $H_{n+1}$ by images of new cellular boundaries; it cannot create a new $(n+1)$-cycle. Cells of still higher dimension do not affect $H_{n+1}$. Therefore the resulting Eilenberg--MacLane space satisfies
$$
\boxed{H_{n+1}(K(G,n);\ZZ)=0\qquad(n>1).}
$$
:::
