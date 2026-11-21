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
- event: solution-reviewed
  by: claude
  date: 2026-11-18
  note: >-
    Restructured into Lamport steps, with the retained set now cited in the solution section
    as well as here. Pages verified: Example 3 of §38 on printed p. 238, where the map is
    e(x) = (x, sin(1/x)) from (0,1) into the square [-1,1]^2; §38 Exercise 2 on printed
    p. 241, whose target is [0,1]^3, which is why the card rescales the second and third
    coordinates; the definition of a compactification on printed p. 237; Theorem 21.3 on
    printed p. 130, continuity implying that convergent sequences map to convergent
    sequences, which is the tool of the first part, with the sequence lemma on the same
    page; and Theorem 26.2, Theorem 26.7 and Theorem 27.1 on printed pp. 165, 167 and 172 for
    the compactness of [0,1]^3 and of its closed subsets. Two details written out that the
    prose left to the reader: that (0,0) lies in the compactification, because it is a limit
    of points of the dense copy, and that (-1)^n has no limit, its even and odd terms being
    the constants 1 and -1. No repair to the statement.
---

::: {.exercise}

Show that the bounded continuous function $g: (0, 1) \to \RR$ defined by $g(x) = \cos(1/x)$ cannot be extended to the compactification of Example 3 of §38. Define an imbedding $h: (0, 1) \to [0, 1]^3$ such that the functions $x$, $\sin(1/x)$, and $\cos(1/x)$ are all extendable to the compactification induced by $h$.
:::

::: {.solution}
The argument is the retained published solution, **"Solutions to exercises for Mathematics 205A" (University of California, Riverside, Fall 2014), section VI.4, "Problems from Munkres, §38", Exercise 2, printed p. 9 of the file** (`tmp/sources/munkres-solutions-ucr-math205A-solutions5a.pdf`), restructured into steps; the rescaled imbedding below is the card's, the exercise's target $[0,1]^3$ being too small for the unrescaled $(\sin,\cos)$.

Throughout, $e:(0,1)\to[-1,1]^2$ is the map $e(x)=(x,\sin(1/x))$ of Example 3 of §38 (printed p. 238), whose image's closure $Y_0$ is the compactification of $(0,1)$ used there, and a compactification of a space $X$ is a compact Hausdorff space containing a dense homeomorphic copy of $X$ (§38, printed p. 237). The exercise is §38 Exercise 2 (printed p. 241).

::: pf

::: {.pf-step #no-extension}
$g(x)=\cos(1/x)$ does not extend continuously to $Y_0$.

::: pf-proof

::: {.pf-step #sequence-in-y0}
With $x_n=1/(n\pi)$ the points $e(x_n)=(1/(n\pi),0)$ lie in $e((0,1))\subset Y_0$ and converge to $(0,0)$, which therefore lies in $Y_0$.

::: pf-proof
$\sin(n\pi)=0$ for every $n$, so $e(x_n)=(1/(n\pi),0)$, and $1/(n\pi)\to0$; a limit of points of a set lies in its closure (Lemma 21.2, printed p. 130), and $Y_0$ is a closed subset of the compact cube $[-1,1]^2$, so it is closed in $\RR^2$.
:::

:::

::: {.pf-step #contradiction}
If $G:Y_0\to\RR$ extended $g$, then $G(e(x_n))=(-1)^n$ would converge.

::: pf-proof
The sequence $e(x_n)$ converges to $(0,0)$, so by Theorem 21.3 (printed p. 130) the sequence $G(e(x_n))$ converges, to $G(0,0)$. But $G(e(x_n))=g(x_n)=\cos(n\pi)=(-1)^n$, a sequence whose even and odd terms are the constants $1$ and $-1$; a sequence in the Hausdorff space $\RR$ with two distinct subsequential limits has no limit. This contradiction at the single point $(0,0)$ shows that no such $G$ exists.
:::

:::

:::

:::

::: {.pf-step #imbedding}
$h:(0,1)\to[0,1]^3$, $h(x)=\big(x,\frac{1+\sin(1/x)}2,\frac{1+\cos(1/x)}2\big)$, is an imbedding.

::: pf-proof

::: {.pf-step #into-cube}
$h$ is continuous and takes its values in $[0,1]^3$.

::: pf-proof
Each coordinate is continuous on $(0,1)$, and $\sin$ and $\cos$ take values in $[-1,1]$, so $(1+\sin(1/x))/2$ and $(1+\cos(1/x))/2$ lie in $[0,1]$, while $x\in(0,1)\subset[0,1]$.
:::

:::

::: {.pf-step #inverse}
$h$ is injective and its inverse on $h((0,1))$ is the restriction of the first-coordinate projection, hence continuous.

::: pf-proof
The first coordinate of $h(x)$ is $x$, so $h(x)=h(x')$ gives $x=x'$. The projection $\pi_1:[0,1]^3\to[0,1]$ is continuous, and $\pi_1\circ h$ is the identity of $(0,1)$, so $\pi_1$ restricted to $h((0,1))$ is the inverse of $h$. A continuous injection whose inverse on its image is continuous is an imbedding.
:::

:::

:::

:::

::: {.pf-step #compactification}
$Y=\overline{h((0,1))}\subset[0,1]^3$ is a compactification of $(0,1)$ induced by $h$.

::: pf-proof
$[0,1]$ is compact (Theorem 27.1, printed p. 172), so $[0,1]^3$ is compact as a finite product of compact spaces (Theorem 26.7, printed p. 167) and Hausdorff as a subspace of $\RR^3$. A closed subset $Y$ of a compact space is compact (Theorem 26.2, printed p. 165), it is Hausdorff as a subspace, and $h((0,1))$ is dense in it by definition of the closure; with step [](#imbedding){.pf-ref} this makes $Y$ a compactification of $(0,1)$.
:::

:::

::: {.pf-step}
$x$, $\sin(1/x)$ and $\cos(1/x)$ all extend continuously to $Y$.

::: pf-proof
Let $\pi_i$ be the coordinate projections of $[0,1]^3$ and restrict them to $Y$; they are continuous on $Y$. On $h((0,1))$,
$$
\pi_1\big(h(x)\big)=x,\qquad \big(2\pi_2-1\big)\big(h(x)\big)=\sin(1/x),\qquad \big(2\pi_3-1\big)\big(h(x)\big)=\cos(1/x),
$$
so each of the three continuous functions $\pi_1$, $2\pi_2-1$, $2\pi_3-1$ on $Y$ extends the corresponding function on $(0,1)$, which is exactly extendability to the compactification induced by $h$.
:::

:::

:::
:::
