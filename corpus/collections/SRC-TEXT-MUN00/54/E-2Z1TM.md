---
schema: qual/card@1
id: E-2Z1TM
kind: problem
title: Lifting paths in the polar covering of the punctured plane
classification:
  areas:
  - topology
  topics:
  - Covering Spaces
relations: []
review: draft
audit:
- event: solution-written
  by: Gemini 3.7 Flash
  date: 2026-08-29
- event: source-checked
  by: claude
  date: 2026-11-11
  note: >-
    Checked against the located published solution: dbFin, "Section 54: Problem 4 Solution",
    https://dbfin.com/topology/munkres/chapter-9/section-54-the-fundamental-group-of-the-circle/problem-4-solution/
    (read 2026-11-11; kept at tmp/sources/dbfin/section-54-the-fundamental-group-of-the-circle/problem-4-solution.txt), and against Munkres,
    Topology (2000), Section 54 Exercise 4, printed p. 348. dbFin gives the three lifts in closed form, $\tilde f=(z,2-t)$, $\tilde g=(t+z,1+t)$ and $\tilde h=(\max(0,2t-1)+z,\,1+|1-2t|)$, and a figure; the card computes the same three and identifies the initial points in the fibre. Nothing needed repair.
- event: source-corrected
  by: claude
  date: 2026-11-19
  note: >-
    Rewrote the solution on 2026-11-19. Its three steps carried run-in titles and
    "Proof:" labels over unlabelled substeps, and its last block, "Geometric
    description / sketches", had no proof block at all: the bullets that were
    meant to be its content stood outside the step, below a stray terminator,
    with "Q.E.D." inside a list item. It is now three labelled steps whose
    claims are the lifts, each proved, and the sketch the exercise asks for is a
    remark after the proof. The lifts are unchanged and agree with dbFin's
    closed forms: (z, 2 - t), (t + z, 1 + t) and (max(0, 2t - 1) + z,
    1 + |1 - 2t|). Read for this repair in
    tmp/sources/dbfin/section-54-the-fundamental-group-of-the-circle/problem-4-solution.txt
    (read 2026-11-11) and checked against
    tmp/sources/munkres-2000-topology.md and the retained PDF: the exercise on
    printed p. 348 (PDF p. 363, printed page = PDF page - 15), Example 6 of §53 on
    printed p. 340 (PDF p. 355) and Lemma 54.1 on printed p. 342 (PDF p. 357). No
    statement changes.

---

::: {.exercise}

Consider the covering map $p: \RR \times \RR_+ \to \RR^2 - 0$ of Example 6 of §53. Find liftings of the paths

$$
f(t) = (2 - t, 0),
$$

$$
g(t) = ((1 + t) \cos 2\pi t, (1 + t) \sin 2\pi t),
$$

$$
h(t) = f * g.
$$

Sketch these paths and their liftings.
:::

::: {.solution}
The lifts are those of the published solution of dbFin, "Section 54: Problem 4 Solution", which writes the covering as $p(\alpha,r)=(r\cos2\pi\alpha,r\sin2\pi\alpha)$ and gives $\tilde f(t)=(z,2-t)$, $\tilde g(t)=(t+z,1+t)$ and $\tilde h(t)=(\max(0,2t-1)+z,\,1+\abs{1-2t})$ for $z\in\ZZ$. The exercise is Munkres, *Topology* (2000), Section 54, Exercise 4, printed p. 348; the covering is Example 6 of §53, printed p. 340, and the uniqueness of lifts used below is Lemma 54.1, printed p. 342.

Throughout, $p\colon\RR\times\RR_+\to\RR^2\setminus\{0\}$ is $p(\theta,r)=(r\cos2\pi\theta,r\sin2\pi\theta)$; the fibre over $(2,0)$ is $\{(n,2):n\in\ZZ\}$ and the fibre over $(1,0)$ is $\{(m,1):m\in\ZZ\}$.

::: pf

::: {.pf-step #lift-f}
For every $n\in\ZZ$, $\tilde f_n(t)=(n,2-t)$ is the lift of $f$ on $[0,1]$ with $\tilde f_n(0)=(n,2)$.

::: pf-proof
Since $2-t>0$ on $[0,1]$, $p(\tilde f_n(t))=((2-t)\cos2\pi n,(2-t)\sin2\pi n)=(2-t,0)=f(t)$. The lift of a path with a prescribed initial point is unique (Lemma 54.1), so this is the only one.
:::

:::

::: {.pf-step #lift-g}
For every $m\in\ZZ$, $\tilde g_m(t)=(m+t,1+t)$ is the lift of $g$ on $[0,1]$ with $\tilde g_m(0)=(m,1)$.

::: pf-proof
$p(\tilde g_m(t))=((1+t)\cos2\pi(m+t),(1+t)\sin2\pi(m+t))=((1+t)\cos2\pi t,(1+t)\sin2\pi t)=g(t)$, since $\cos$ and $\sin$ have period $1$ in the variable $\theta$; and $\tilde g_m(0)=(m,1)$.
:::

:::

::: {.pf-step #lift-h}
The lift of $h=f*g$ with $\tilde h_n(0)=(n,2)$ is
$$
\tilde h_n(t)=\begin{cases}(n,2-2t) & 0\le t\le\tfrac12,\\[2pt] (n+2t-1,2t) & \tfrac12\le t\le1.\end{cases}
$$

::: pf-proof
By the definition of the path product, $h(t)=f(2t)$ for $0\le t\le\tfrac12$ and $h(t)=g(2t-1)$ for $\tfrac12\le t\le1$. On the first half $\tilde h_n(t)=\tilde f_n(2t)$ lifts $f(2t)$ by step [](#lift-f){.pf-ref}, and it ends at $\tilde f_n(1)=(n,1)$; on the second half $\tilde h_n(t)=\tilde g_n(2t-1)$ lifts $g(2t-1)$ by step [](#lift-g){.pf-ref} and begins at $\tilde g_n(0)=(n,1)$. The two pieces agree at $t=\tfrac12$, so the concatenation is continuous and lifts $h$; the lift with a prescribed initial point is unique (Lemma 54.1). Its second half, expanded, is $(n+(2t-1),1+(2t-1))=(n+2t-1,2t)$, and $\max(0,2t-1)+n$ and $1+\abs{1-2t}$ are the same two functions on $[0,1]$, which is dbFin's closed form.
:::

:::

:::

:::

::: {.remark title="The paths and their liftings"}
In $\RR^2\setminus\{0\}$ the path $f$ runs along the positive $x$-axis from $(2,0)$ in to $(1,0)$, the path $g$ spirals once counterclockwise from $(1,0)$ out to $(2,0)$, and $h$ traces the inward segment and then the outward spiral. In the covering space $\RR\times\RR_+$, $\tilde f_0$ is the vertical segment from $(0,2)$ down to $(0,1)$, $\tilde g_0$ the diagonal segment from $(0,1)$ out to $(1,2)$, and $\tilde h_0$ their concatenation, from $(0,2)$ to $(0,1)$ and then to $(1,2)$.
:::
