---
schema: qual/card@1
id: E-E79BA
kind: problem
title: Euclidean spaces of different dimensions are not homeomorphic
classification:
  areas:
  - topology
  topics:
  - Fundamental Group
relations: []
review: draft
audit:
- event: solution-written
  by: gemini-3.7-flash
  date: 2026-08-29
- event: source-checked
  by: claude
  date: 2026-11-11
  note: >-
    Checked line by line against Munkres, Topology (2000), Section 59 Exercise 3, printed p. 370,
    with the invariance of connectedness and of the fundamental group under homeomorphism, with Theorem 58.2 and Theorem 59.3. Part (a) removes a point; part (b) compares $\pi_1(\RR^2-0)=\ZZ$ with $\pi_1(\RR^n-0)=0$ for $n>2$. No complete published solution was located for this exercise: dbFin's Chapter 9 pages run from Section 51 to Section 56 only, and every set searched is listed in the COMPLAINTS.md entry for Sections 57 to 60. The proof is the card's own and every step was checked against the book.
- event: source-checked
  by: claude
  date: 2026-11-14
  note: >-
    A published proof has now been located: Pearse, *Topology (2nd ed.) — James R. Munkres*,
    solutions, Cornell 2005, §59 Exercise 3, his pp. 24-25, read in the MinerU extraction
    tmp/sources/cornell-erin-munkres.md. The solution is that proof transcribed: for (a), that
    $\RR^n_0$ is path connected while $\RR^1_0$ is a separation, so a homeomorphism would match a
    connected space with a disconnected one; for (b), that $\RR^n_0$ deformation retracts onto
    $S^{n-1}$ by the formula the source writes, so $\pi_1(\RR^2_0)\cong\ZZ$ while
    $\pi_1(\RR^n_0)$ is trivial for $n\ge3$. The source is correct and needed no repair. Checked
    against the book: the exercise on printed p. 370, Theorem 23.5 on printed p. 150, the
    definition of path connectedness on printed p. 155, Theorem 58.3 on printed p. 361, Theorem
    58.7 on printed p. 364, Theorem 54.5 on printed p. 345 and Theorem 59.3 on printed p. 369. Not
    claimed: that the source writes more than one sentence for the detour through a point off the
    line -- the card spells that case out.
- event: solution-written
  by: claude
  date: 2026-11-14
  note: >-
    The solution was rewritten as the transcription above, in Lamport form, with the source and the
    book's pages named in its own text.
- event: solution-written
  by: claude
  date: 2026-11-14
  note: >-
    Part (b) corrected: it called $u\mapsto u+q$ a homeomorphism of $\RR^n-\theset q$ onto
    $\RR^n_0$, but translation by $q$ carries $\RR^n-\theset q$ onto $\RR^n-\theset{2q}$; the map
    that removes $q$ is $u\mapsto u-q$, and that is what the card now uses, so the composite $g$ is
    $u\mapsto h(u)-q$ as intended. The same map appears in part (a) in the other direction, from
    $\RR^n_0$ onto $\RR^n-\theset q$, where $u\mapsto u+q$ is correct; that clause now says which
    translation it is, carrying $\mathbf 0$ to $q$, so the two directions are not confused. Nothing
    else on the card changed. Checked against the book: the exercise on printed p. 370, Theorem
    58.3 on printed p. 361, Theorem 58.7 on printed p. 364 and Theorem 59.3 on printed p. 369.
---

::: {.exercise}

(a) Show that $\RR^1$ and $\RR^n$ are not homeomorphic if $n > 1$.

(b) Show that $\RR^2$ and $\RR^n$ are not homeomorphic if $n > 2$.

It is, in fact, true that $\RR^m$ and $\RR^n$ are not homeomorphic if $n \neq m$, but the proof requires more advanced tools of algebraic topology.
:::

::: {.solution}
The exercise is §59 Exercise 3, printed p. 370. The proof is transcribed from
Pearse, *Topology (2nd ed.) — James R. Munkres*, solutions, Cornell 2005, §59
Exercise 3, his pp. 24--25, read in `tmp/sources/cornell-erin-munkres.md`: part
(a) uses connectedness and part (b) the fundamental group, in each case applied
not to $\RR^n$ itself but to $\RR^n$ with one point deleted. Write
$\RR^n_0=\RR^n-\theset{\mathbf 0}$.

::: pf

::: {.pf-step #punctured-connected}
For $n\ge2$, $\RR^n_0$ is path connected, hence connected.

::: pf-proof
Let $x,y\in\RR^n_0$. If the straight segment $(1-t)x+ty$ never passes through
$\mathbf 0$, the path $t\mapsto(1-t)x+ty$ joins $x$ to $y$ inside $\RR^n_0$.
Otherwise $y$ is a negative multiple of $x$; choose $z\in\RR^n_0$ not on the line
through $x$ and $y$, which is possible because $n\ge2$ and a line is a proper
subset of $\RR^n$. Neither segment from $x$ to $z$ nor from $z$ to $y$ passes
through $\mathbf 0$: a point of the first segment is $\mathbf 0$ only if $z$ is on
the line through $\mathbf 0$ and $x$, which is the line through $x$ and $y$, and
likewise for the second. So the two segments give a path from $x$ to $y$ inside
$\RR^n_0$, and $\RR^n_0$ is path connected; a path connected space is connected, as the
definition of path connectedness and Theorem 23.5 give (printed pp. 155 and 150).
:::

:::

::: {.pf-step #one-dimensional}
(a) $\RR^1$ and $\RR^n$ are not homeomorphic if $n>1$.

::: pf-proof
Suppose $h:\RR^1\to\RR^n$ were a homeomorphism, $n>1$, and put $q=h(0)$. Then
$h$ restricts to a bijection of $\RR^1-\theset 0$ onto $\RR^n-\theset q$, and that
restriction is a homeomorphism, being continuous with continuous inverse
$\restrictionof{h^{-1}}{\RR^n-\theset q}$.

Now $\RR^1-\theset 0=(-\infty,0)\cup(0,\infty)$ is a separation: both parts are
nonempty, open in $\RR^1-\theset 0$, and disjoint. And $\RR^n-\theset q$ is
connected: the map $u\mapsto u+q$, translation carrying $\mathbf 0$ to $q$, is a
homeomorphism of $\RR^n$ carrying $\RR^n_0$ onto $\RR^n-\theset q$, and
$\RR^n_0$ is connected by step
[](#punctured-connected){.pf-ref}. A homeomorphism carries a separation of one
space to a separation of the other, so $\RR^n-\theset q$ is connected; equally, by
Theorem 23.5 (printed p. 150) a continuous image of a connected space is
connected. A connected space cannot be homeomorphic to a disconnected one, so no
such $h$ exists.
:::

:::

::: {.pf-step}
(b) $\RR^2$ and $\RR^n$ are not homeomorphic if $n>2$.

::: pf-proof
For every $n\ge2$ the map $H(x,t)=(1-t)x+t\,x/\norm x$ on $\RR^n_0$ is continuous,
satisfies $H(x,0)=x$, and carries $\RR^n_0$ onto $S^{n-1}$ at $t=1$, fixing
$S^{n-1}$ pointwise; so $S^{n-1}$ is a deformation retract of $\RR^n_0$ and
$\pi_1(\RR^n_0)\cong\pi_1(S^{n-1})$ by Theorem 58.3 (printed p. 361).

For $n=2$ this gives $\pi_1(\RR^2_0)\cong\pi_1(S^1)\cong\ZZ$ by Theorem 54.5.
For $n\ge3$ the sphere $S^{n-1}$ has dimension at least $2$, so it is simply
connected by Theorem 59.3 (printed p. 369), and $\pi_1(\RR^n_0)$ is trivial.

Suppose $n>2$ and $h:\RR^2\to\RR^n$ were a homeomorphism, and let $q=h(0)$. The
restriction of $h$ is a homeomorphism of $\RR^2-\theset 0$ onto
$\RR^n-\theset q$, and $u\mapsto u-q$ is a homeomorphism of $\RR^n-\theset q$
onto $\RR^n_0$; their composite is a homeomorphism $g:\RR^2_0\to\RR^n_0$, which
therefore induces an isomorphism $g_*:\pi_1(\RR^2_0, x_0)\to
\pi_1(\RR^n_0,g(x_0))$ by Theorem 58.7 (printed p. 364). But
$\pi_1(\RR^2_0)\cong\ZZ$ and $\pi_1(\RR^n_0)$ is trivial, and no group isomorphism
carries an infinite cyclic group onto a one-element group. So no such
homeomorphism exists.
:::

:::

:::
:::
