---
schema: qual/card@1
id: E-L9XR0
kind: problem
title: Subspace topologies on lines in the Sorgenfrey plane
classification:
  areas:
  - topology
  topics:
  - Subspace Topology
  - Product Topology
relations: []
review: draft
audit:
- event: source-checked
  by: claude
  date: 2026-11-10
  note: >-
    Read against Munkres, Topology (2000), §16 Exercise 8, printed p. 92, with Lemma 16.1 on
    printed p. 89; the stored statement is the printed one.
- event: solution-written
  by: claude
  date: 2026-11-10
  note: >-
    Transcribed from the located published solution: "positron0802", "Solutions to Topology,
    Chapter 2" (1 January 2021), Exercise 16.8, PDF p. 5, with each entry proved on the card
    from the traces of the bases [a,b) x (c,d) and [a,b) x [c,d). The answer: over R_l x R a
    vertical line gives R and any other line gives R_l directed rightward and R_u directed
    leftward; over R_l x R_l a vertical line gives R_l upward and R_u downward, a line of
    non-negative slope gives R_l or R_u according to direction, and a negative-slope line
    gives the discrete topology, since a small product basis element at a point of it meets
    the line in that point alone. Two source defects are recorded: positron0802 misprints
    the leftward negative-slope case, and Whitman, printed pp. 154-155, states that his
    argument is informal. (tmp/sources/munkres-solutions-positron-ch2.pdf).
---

::: {.exercise}

If $L$ is a straight line in the plane, describe the topology $L$ inherits as a subspace of $\RR_\ell \times \RR$ and as a subspace of $\RR_\ell \times \RR_\ell$.
In each case it is a familiar topology.
:::

::: {.solution}
The complete published solution is **"positron0802", *Solutions to Topology, Chapter 2* (1 January 2021), Exercise 16.8, PDF p. 5** (`tmp/sources/munkres-solutions-positron-ch2.pdf`); the table of answers is his, and each entry is proved below. One misprint in his last sentence is corrected: for a line directed to the left he writes that the topology is that of $\RR_{u}$ when the slope is non-positive and that of $\RR_{d}$ when it is negative, whereas the discreteness comes from the negative slope and not from the direction. Whitman, printed pp. 154--155, gives the same table but says on p. 154 that he can only argue informally ("we do not yet have the tools to show formally"), so his answer is not used as the proof.

Identify $L$ with $\RR$ by a coordinate $x$ increasing in the chosen **direction** of $L$, and let $\RR_{d}$ denote $\RR$ with the discrete topology. The product $\RR_{\ell}\times\RR$ has basis the sets $[a,b)\times(c,d)$ and $\RR_{\ell}\times\RR_{\ell}$ has basis the sets $[a,b)\times[c,d)$; the subspace topology on $L$ has as a basis the traces of these (Lemma 16.1, printed p. 89). In the arguments below a half-open interval $[p,q)$ of $L$ is produced as a trace by taking the first coordinate interval $[p,q)$ and choosing the second coordinate interval so wide that $y=mx+k$ stays inside it for $x\in[p,q)$, which is possible because $x\mapsto mx+k$ is bounded on $[p,q)$.

**As a subspace of $\RR_{\ell}\times\RR$.**

*Vertical $L$.* A trace is $\{x_{0}\}\times(c,d)$ intersected with $L$, that is, an open interval of $L$; conversely every open interval of $L$ is such a trace with $a\le x_{0}<b$. The topology is that of $\RR$.

*$L$ not vertical, say $y=mx+k$.* The trace of $[a,b)\times(c,d)$ is $\{x\in[a,b)\mid c<mx+k<d\}$. Whatever the sign of $m$, the two conditions $c<mx+k$ and $mx+k<d$ cut out an open interval of $x$-values, so the trace is the intersection of $[a,b)$ with an open interval: it is an interval of $L$ with right end open and left end open or closed, hence a union of half-open intervals, hence open in the lower limit topology of $L$ when $L$ is directed to the right. Conversely every half-open $[p,q)$ of $L$ is a trace, as noted above. So the topology is that of $\RR_{\ell}$ when $L$ is directed to the right and that of $\RR_{u}$ when it is directed to the left, reversing the coordinate being a homeomorphism $\RR_{\ell}\to\RR_{u}$.

**As a subspace of $\RR_{\ell}\times\RR_{\ell}$.**

*Vertical $L$.* A trace is $\{x_{0}\}\times([c,d)\cap\RR)$ intersected with $L$, a half-open interval of $L$; conversely every half-open interval of $L$ is such a trace. The topology is $\RR_{\ell}$ when $L$ is directed upward and $\RR_{u}$ when it is directed downward.

*Horizontal $L$, or $L$ of positive slope.* Say $y=mx+k$ with $m\ge0$. The trace of $[a,b)\times[c,d)$ is $\{x\in[a,b)\mid c\le mx+k<d\}$, and with $m\ge0$ both conditions are lower or upper bounds on $x$ of the same kind, so the trace is a half-open interval $[x_{0},x_{1})$ of $L$; conversely every half-open interval of $L$ is a trace, as noted above. So the topology is $\RR_{\ell}$ when $L$ is directed to the right and $\RR_{u}$ when it is directed to the left.

*$L$ of negative slope.* Given $(x_{0},y_{0})\in L$, the trace of $[x_{0},x_{0}+\varepsilon)\times[y_{0},y_{0}+\varepsilon')$ consists of the points of $L$ with $x_{0}\le x<x_{0}+\varepsilon$ and $y_{0}\le y=y_{0}+m(x-x_{0})$, and since $m<0$ the second inequality forces $x\le x_{0}$; the trace is the single point $\{(x_{0},y_{0})\}$. Every point of $L$ is thus open in $L$ and the topology is the discrete one, $\RR_{d}$, in either direction.

**Answer.** As a subspace of $\RR_{\ell}\times\RR$: vertical lines give $\RR$; every other line gives $\RR_{\ell}$ when directed to the right and $\RR_{u}$ when directed to the left, independently of the slope. As a subspace of $\RR_{\ell}\times\RR_{\ell}$: vertical lines give $\RR_{\ell}$ directed upward and $\RR_{u}$ directed downward; horizontal and positive-slope lines give $\RR_{\ell}$ directed to the right and $\RR_{u}$ directed to the left; negative-slope lines give $\RR_{d}$.
:::
