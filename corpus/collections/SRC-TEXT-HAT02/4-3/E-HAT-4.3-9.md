---
schema: qual/card@1
id: E-HAT-4.3-9
kind: problem
title: "Linear projection is fibration but not fiber bundle"
classification:
  areas:
  - topology
  topics:
  - Higher Homotopy Groups
relations: []
review: draft
audit:
- event: source-corrected
  by: claude
  date: 2026-11-21
  note: >-
    Citation convention. Every locator of the form "printed page N" or "PDF page N" written into
    this card before today, here and in the events below, is superseded: sources are cited by
    chapter, section and numbered statement only. The events below are left as their sessions wrote
    them, as QUAL-11 requires, so their locators stand as a historical record; the statement and the
    solution above are the current text and cite by number. This event records the convention and no
    further reading: the mathematics of the card is as the events below describe it.
- event: solution-written
  by: claude
  date: 2026-11-20
  note: >-
    Restructured under #2, transcribing the retained solution of Steven V. Sam, Solutions to
    Algebraic Topology (2008), §4.3 Exercise 9, printed p. 26 of
    tmp/sources/hatcher-solutions-sam-2008.pdf (PDF p. 27). Sam's route is kept: a section of
    pi: Delta^I -> Delta_p, then Exercise 8. Two defects in his text are repaired on the card.
    His section is displayed as s(x,gamma)(t) = gamma(t), which is the base path and not a path
    in the simplex; the card writes the lift (gamma(t), min{y_0, lambda(gamma(t))}) and checks
    it. His reason for not being a bundle, "the fibers over the vertices of the edge are
    points", fails when the third vertex projects over an endpoint; the card's lambda model
    covers the endpoint cases, as the 2026-11-01 event already required. Checked against
    Exercise 8, printed p. 419, and the sentence defining a fiber bundle on printed p. 375
    ("All the subspaces p^{-1}(b) ... are homeomorphic"). Not checked: no certificate.
- event: source-checked
  by: gpt-5.6-sol
  date: 2026-09-09
  note: Checked against Hatcher, Algebraic Topology, Section 4.3, Exercise 9; the stored statement matches.
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
- event: solution-reviewed
  by: claude
  date: 2026-11-01
  note: >-
    Proof read against Hatcher Sec. 4.3 Exercise 9 (AT.txt 20779-20780) and repaired. The fibration half
    is correct: in the card's own coordinates the fibre-preserving retraction r(x,y) = (x, min{y,
    lambda(x)}) of a product bundle onto the simplex gives homotopy lifting. The reason given for "not
    a fiber bundle" was false as stated: the card claimed the fibres over both endpoints are points,
    but if the third vertex projects to an endpoint of the base edge there is no such thing -- for
    p(x,y) = x on conv{(0,0),(1,0),(0,1)} the fibre over 0 is the edge {0} x [0,1]. The card now argues
    from its own model: the fibre over x is the interval {x} x [0, lambda(x)], the third vertex gives
    some s with lambda(s) > 0, and at least one endpoint x_0 differs from s, where the fibre is the
    single vertex of the base edge. A point is not homeomorphic to a nondegenerate interval, and the
    fibres of a bundle over the connected edge are all homeomorphic (AT.txt 20067-20068). Not checked:
    nothing outside this exercise.

- event: source-checked
  by: claude
  date: 2026-11-19
  note: >-
    Read against Hatcher, Exercise 9 of §4.3, printed p. 419, with the preceding exercise's
    criterion. Correct, and the repair of 2026-11-01 is confirmed: the fibres of $p(x,y)=x$ on
    $\Delta=\{(x,y):0\le y\le\lambda(x)\}$ are $\{x\}\times[0,\lambda(x)]$, the fibre over the
    projection $s$ of the third vertex is a nondegenerate interval, and for an endpoint
    $x_0\ne s$ the fibre is the single base vertex, so the fibres are not all homeomorphic while
    the base is connected. The fibration half is right because $r(x,y)=(x,\min\{y,\lambda(x)\})$
    is a fibre-preserving retraction of the trivial bundle $I\times[0,M]\to I$ onto $\Delta$ over
    $I$, and a retract of a fibration over the same base is a fibration. Nothing changed.
    Not claimed: a published solution, and no certificate.
---

::: {.solution}
The argument is that of the retained solution set: **Steven V. Sam, *Solutions to Algebraic Topology* (2008), §4.3 Exercise 9** of `tmp/sources/hatcher-solutions-sam-2008.pdf`. Sam's route is kept: exhibit a section of $\pi\colon\Delta^I\to\Delta_p$, $\pi(\sigma)=(\sigma(0),p\sigma)$, and apply Exercise 8. His displayed section is the base path where the lifted path is meant, and step [](#section){.pf-ref} writes the lift; his reason for the failure of the bundle property assumes that the third vertex projects to an interior point of the edge, and step [](#notbundle){.pf-ref} covers the endpoint cases as well.

::: pf

::: {.pf-step #model}
In affine coordinates the simplex is $\Delta=\{(x,y):0\le x\le1,\ 0\le y\le\lambda(x)\}$ and $p(x,y)=x$, where $\lambda\ge0$ is continuous and piecewise linear, $\lambda(s)=h>0$ at the image $s$ of the third vertex, and $\lambda(x)=0$ at each endpoint $x\in\{0,1\}$ with $x\ne s$.

::: pf-proof
Identify the target edge with $I=[0,1]$ by $p$. In coordinates $(x,y)$ with $x=p$ the third vertex is $v=(s,h)$ with $h>0$ and $s\in[0,1]$, and $\Delta$ is the convex hull of $(0,0)$, $(1,0)$ and $(s,h)$. For $x\in[0,1]$ the points of $\Delta$ over $x$ form the interval $\{x\}\times[0,\lambda(x)]$, where $\lambda$ is affine on $[0,s]$ and on $[s,1]$ because those are the projections of the two edges through $v$; thus $\lambda$ is continuous and piecewise linear, $\lambda(s)=h$, and $\lambda$ vanishes at an endpoint unless $v$ projects to that endpoint.
:::

:::

::: {.pf-step #section}
$\pi\colon\Delta^I\to\Delta_p$ has a section.

::: pf-proof
For $x=(x_0,y_0)\in\Delta$ and $\gamma\colon I\to I$ with $\gamma(0)=x_0$, set $s(x,\gamma)(t)=(\gamma(t),\min\{y_0,\lambda(\gamma(t))\})$. Since $0\le y_0\le\lambda(x_0)$ and $0\le\min\{y_0,\lambda(\gamma(t))\}\le\lambda(\gamma(t))$, the path lies in $\Delta$ by step [](#model){.pf-ref}; it is continuous in $(x,\gamma,t)$ because evaluation $(\gamma,t)\mapsto\gamma(t)$ is continuous and $\lambda$ and $\min$ are continuous; at $t=0$ it is $(x_0,\min\{y_0,\lambda(x_0)\})=(x_0,y_0)=x$; and $p\,s(x,\gamma)(t)=\gamma(t)$. Hence $\pi\,s=\id$.
:::

:::

::: {.pf-step #fibration}
$p\colon\Delta\to I$ is a fibration.

::: pf-proof
Exercise 8 states that $p$ is a fibration if and only if $\pi\colon E^I\to E_p$ has a section; step [](#section){.pf-ref} provides one for $E=\Delta$, $B=I$.
:::

:::

::: {.pf-step #fibres}
The fibre of $p$ over $x\in I$ is $\{x\}\times[0,\lambda(x)]$.

::: pf-proof
Immediate from the description of $\Delta$ in step [](#model){.pf-ref}: a point of $\Delta$ over $x$ is a pair $(x,y)$ with $0\le y\le\lambda(x)$.
:::

:::

::: {.pf-step #notbundle}
$p$ is not a fibre bundle.

::: pf-proof
By step [](#model){.pf-ref}, $\lambda(s)=h>0$, so the fibre over $s$ is a nondegenerate interval. Choose an endpoint $x_0\in\{0,1\}$ with $x_0\ne s$, possible since $\{0,1\}$ has two elements; then $\lambda(x_0)=0$, so the fibre over $x_0$ is the single point $(x_0,0)$. A point is not homeomorphic to a nondegenerate interval, so the fibres of $p$ are not all homeomorphic, whereas the fibres of a fibre bundle are all homeomorphic. Hence $p$ is not a fibre bundle.
:::

:::

::: {.pf-step}
A linear projection of a $2$-simplex onto one of its edges is a fibration and not a fibre bundle.

::: pf-proof
Step [](#fibration){.pf-ref} gives the fibration, step [](#notbundle){.pf-ref} the failure of the bundle property.
:::

:::

:::
:::
