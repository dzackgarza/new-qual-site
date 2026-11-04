---
schema: qual/card@1
id: E-HAT-4.2-30
kind: problem
title: "Fiber bundle projections from subspaces of $\\RR^2$"
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
  note: Checked against Hatcher, Algebraic Topology, Section 4.2, Exercise 30; the stored statement matches.
- event: solution-written
  by: gpt-5.6-sol
  date: 2026-09-09
- event: solution-reviewed
  by: gpt-5.6-sol
  date: 2026-09-09
---

::: {.problem}
Let $E$ be a subspace of $\RR^2$ obtained by deleting a subspace of $\{0\} \times \RR$.
For which such spaces $E$ is the projection $E \to \RR$, $(x, y) \mapsto x$, a fiber bundle?
:::

::: {.solution}
Write
$$
E=\RR^2-\bigl(\{0\}\times A\bigr),
\qquad
p(x,y)=x.
$$
For $x\ne0$, the fiber is $\RR$, while
$$
p^{-1}(0)=\RR-A.
$$
If $p$ is a fiber bundle over the connected base $\RR$, all fibers are homeomorphic. Hence a necessary condition is
$$
\RR-A\cong\RR.
$$
As a subspace of $\RR$, a space homeomorphic to $\RR$ is a connected one-manifold without boundary, hence is an open interval, allowing infinite endpoints. Thus necessarily
$$
\RR-A=(a,b)
$$
for some
$$
-\infty\le a<b\le\infty.
$$

This condition is also sufficient. Put $I=(a,b)$. Away from $0$ the projection is already the trivial product. It remains to trivialize over a small interval $(-\varepsilon,\varepsilon)$.

For $t>0$, choose an increasing homeomorphism
$$
h_t:\RR\to I
$$
which equals the identity on the portion of $I$ at distance at least $t$ from each finite endpoint, compresses the left tail into $(a,a+t]$ when $a$ is finite, and compresses the right tail into $[b-t,b)$ when $b$ is finite. For example, at a finite left endpoint use
$$
h_t(y)=a+t\exp\!\left(\frac{y-a-t}{t}\right)
\qquad(y\le a+t),
$$
and use the identity for $y\ge a+t$ until the analogous right-end interpolation begins; at a finite right endpoint use
$$
h_t(y)=b-t\exp\!\left(-\frac{y-b+t}{t}\right)
\qquad(y\ge b-t).
$$
For sufficiently small $t$ the two transition regions are disjoint. If an endpoint is infinite no compression is needed there. These formulas give a jointly continuous family in $(t,y)$, with
$$
h_t(y)\longrightarrow y
$$
for every $y\in I$ as $t\to0$, and points outside $I$ are sent toward the corresponding missing endpoint.

Define
$$
H:p^{-1}(({-}\varepsilon,\varepsilon))\longrightarrow
(-\varepsilon,\varepsilon)\times I
$$
by
$$
H(x,y)=
\begin{cases}
(x,h_{\abs{x}}(y)),&x\ne0,\\
(0,y),&x=0.
\end{cases}
$$
The displayed limiting behavior gives continuity at the central fiber; the same argument for $h_t^{-1}$ gives continuity of the inverse. Thus $H$ is a fiber-preserving homeomorphism.

Therefore
$$
\boxed{p:E\to\RR\text{ is a fiber bundle exactly when }\RR-A\text{ is an open interval (possibly unbounded).}}
$$
:::
