---
schema: qual/card@1
id: E-UB4PP
kind: problem
title: Extending $\cos(1/x)$ by enlarging the compactification
classification:
  areas:
  - topology
  topics:
  - Compactness
relations: []
review: draft
audit:
- event: source-checked
  by: gpt-5.6-sol
  date: 2026-09-09
- event: solution-written
  by: gpt-5.6-sol
  date: 2026-09-09
- event: solution-reviewed
  by: gpt-5.6-sol
  date: 2026-09-09
- event: solution-written
  by: claude
  date: 2026-11-10
  note: >-
    Transcribed from the located published solution: "Solutions to exercises for Mathematics 205A"
    (University of California, Riverside, Fall 2014; the file names no author), file solutions5a.pdf,
    section VI.4 "Local compactness and compactifications", "Problems from Munkres, §38, pp. 241-242",
    Exercise 2, printed p. 9 of that file (tmp/sources/munkres-solutions-ucr-math205A-solutions5a.pdf;
    the same section is collected at pp. 7-8 of its running numbering in
    tmp/sources/munkres-solutions-ucr-math205-gentop.pdf). Checked against Munkres, Topology (2000),
    Section 38 Exercise 2, printed p. 241, and Example 3 of §38 (printed p. 238). The set's
    non-extendability argument is the card's: the points (1/k pi, sin k pi) lie in the Example 3
    compactification and converge to (0,0), while cos(1/x) takes the values (-1)^k there, so no continuous
    extension to the compactification exists. What was corrected: the set imbeds (0,1) into [-1,1]^3 by
    h(x) = (x, sin(1/x), cos(1/x)), while the exercise prints the target [0,1]^3; the card rescales the
    second and third coordinates affinely to (1 + sin(1/x))/2 and (1 + cos(1/x))/2, and the extending
    functions are the two rescaled coordinate projections. The set's argument is otherwise unchanged. Not
    checked here: the set says nothing about the first coordinate's extension, which is the identity.
---

::: {.exercise}

Show that the bounded continuous function $g: (0, 1) \to \RR$ defined by $g(x) = \cos(1/x)$ cannot be extended to the compactification of Example 3 of §38. Define an imbedding $h: (0, 1) \to [0, 1]^3$ such that the functions $x$, $\sin(1/x)$, and $\cos(1/x)$ are all extendable to the compactification induced by $h$.
:::

::: {.solution}
In Example 3 the compactification is the closure of
$$
e:(0,1)\longrightarrow [0,1]\times[-1,1],
\qquad e(x)=(x,\sin(1/x)).
$$
Suppose $g(x)=\cos(1/x)$ extended continuously to this compactification. For
$$
x_n=\frac1{n\pi}
$$
we have
$$
e(x_n)=\left(\frac1{n\pi},0\right)\longrightarrow(0,0),
$$
but
$$
g(x_n)=\cos(n\pi)=(-1)^n
$$
has no limit. This contradicts continuity at $(0,0)$. Hence $g$ does not extend.

Now define
$$
h:(0,1)\longrightarrow [0,1]^3,
\qquad
h(x)=\left(x,\frac{1+\sin(1/x)}2,\frac{1+\cos(1/x)}2\right).
$$
The first coordinate recovers $x$, so $h$ is injective; its inverse on $h((0,1))$ is the restriction of the first-coordinate projection. Hence $h$ is an embedding.

Let
$$
Y=\overline{h((0,1))}\subset [0,1]^3.
$$
The ambient cube is compact Hausdorff, so $Y$ is a compactification of $(0,1)$. The continuous functions $\pi_1,2\pi_2-1,2\pi_3-1$ on $Y$ restrict respectively to
$$
x,\qquad \sin(1/x),\qquad \cos(1/x).
$$
Thus all three functions extend continuously to the compactification induced by $h$.
:::
