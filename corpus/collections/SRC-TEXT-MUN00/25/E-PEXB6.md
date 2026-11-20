---
schema: qual/card@1
id: E-PEXB6
kind: problem
title: A rational fan and a nowhere locally connected path-connected set
classification:
  areas:
  - topology
  topics:
  - Connectedness
relations: []
review: draft
audit:
- event: source-checked
  by: claude
  date: 2026-11-10
  note: >-
    Read against Munkres, Topology (2000), §25 Exercise 5, printed p. 162; both parts are
    stored as printed.
- event: solution-written
  by: claude
  date: 2026-11-10
  note: >-
    Transcribed from the located published solution: "positron0802", "Solutions to Topology,
    Chapter 3" (1 January 2021), Exercise 25.5, PDF p. 9. The fan is a union of segments
    through p, hence path connected and locally connected only at p; adjoining a second fan
    at another point gives a path-connected set locally connected nowhere.
    (tmp/sources/munkres-solutions-positron-ch3.pdf).
- event: solution-written
  by: claude
  date: 2026-11-20
  note: >-
    The card stood in queue D: its solution was prose with no numbered step. It is now a `pf` with
    ten steps covering both parts, each carrying a `pf-proof`. Cited by numbered statement only:
    Munkres, Topology, §25 Exercise 5, and Exercise 24.8(d) (a union of path-connected subspaces
    with a common point is path connected). The transcription is from positron0802, Solutions to
    Topology, Chapter 3, Exercise 25.5. The one place that answer compresses is written out here:
    that a small neighbourhood of a point of $T-\{p\}$ has infinitely many components. The card
    proves it through the base-coordinate map $\beta$, continuous on $T-\{p\}$ because the height
    is, and total disconnectedness of $X$ then puts every connected set avoiding $p$ inside a
    single segment; a neighbourhood of $q$ meets infinitely many other segments, so no connected
    neighbourhood of $q$ can fit in a ball about $q$ avoiding $p$. Checked: that $\beta$ is well
    defined on $T-\{p\}$, that its continuity holds at every point of positive height below $1$,
    that the rational cut point separates two distinct points of $X$, and that $1\times0$ lies in
    both $R$ and $T$.
---

::: {.exercise}

Let $X$ denote the rational points of the interval $[0, 1] \times 0$ of $\RR^2$.
Let $T$ denote the union of all line segments joining the point $p = 0 \times 1$ to points of $X$.

(a) Show that $T$ is path connected, but is locally connected only at the point $p$.

(b) Find a subset of $\RR^2$ that is path connected but is locally connected at none of its points.
:::

::: {.solution}

The argument is "positron0802", *Solutions to Topology, Chapter 3*, Exercise 25.5, read in the retained text `tmp/sources/munkres-solutions-positron-ch3.md`. The step where that answer compresses — that a small neighbourhood of a point of $T-\{p\}$ has infinitely many components — is written out here through the base-coordinate map, which is what makes the finitely many components impossible rather than merely implausible.

::: pf

::: {.pf-step #base-map}
Write a point of $T-\{p\}$ as $(\delta x,\delta)$ with $\delta=1-h$ and $x\in X$, where $h$ is the height coordinate; then $\beta(\delta x,\delta)=x$ defines a continuous map $\beta:T-\{p\}\to X$.

::: pf-proof
Every point of $T-\{p\}$ lies on exactly one segment $\overline{px}$ with $x\in X$ and has height $h<1$; the point of that segment at height $h$ is $((1-h)x,\,h)$, so $\beta$ is well defined and $h$ is continuous because it is the restriction of a coordinate function of $\RR^2$. For continuity of $\beta$ at $y=(\delta x_0,\delta)$ with $\delta>0$, let $y_n\to y$ in $T-\{p\}$ and write $y_n=(\delta_nx_n,\delta_n)$. Height is continuous, so $\delta_n\to\delta$ and hence $\delta_n>\delta/2$ eventually; then $x_n=(\delta_nx_n)/\delta_n\to(\delta x_0)/\delta=x_0$ because both coordinates converge and $\delta_n$ is bounded away from $0$. So $x_n\to x_0$ in $X$, as required.
:::

:::

::: {.pf-step #X-totally-disconnected}
$X=\QQ\cap[0,1]$ is totally disconnected, and more precisely: given distinct $x,x'\in X$ there is a separation $X=(X\cap[0,r))\cup(X\cap(r,1])$ of $X$ into nonempty open sets with $x$ and $x'$ in different parts, for a suitable $r\in X$.

::: pf-proof
Let $x<x'$ and choose a rational $r$ with $x<r<x'$, which exists because $x,x'$ are rational; then $r\in X$. The interval $[0,r)$ and $(r,1]$ cut $X$ into two nonempty pieces, both open in $X$, each carrying one of $x,x'$. So no connected subset of $X$ meets both $x$ and $x'$, which is total disconnectedness.
:::

:::

::: {.pf-step #path-connected}
(a) $T=\bigcup_{x\in X}\overline{px}$ is path connected.

::: pf-proof
For $x\in X$ the segment $\overline{px}$ is homeomorphic to $[0,1]$, hence path connected, and $p$ lies in every segment. A union of path-connected subspaces with a common point is path connected (Munkres, Exercise 24.8(d)), so any two points of $T$ are joined through $p$.
:::

:::

::: {.pf-step #connected-in-one-segment}
A connected subset $C\subseteq T$ with $p\notin C$ is contained in a single segment.

::: pf-proof
$C\subseteq T-\{p\}$ and $\beta$ is continuous by step [](#base-map){.pf-ref}, so $\beta(C)$ is connected in $X$. If $C$ met two segments $\overline{px},\overline{px'}$ with $x\ne x'$, then $\beta(C)$ would contain $x$ and $x'$, contradicting the total disconnectedness of step [](#X-totally-disconnected){.pf-ref}. Hence $\beta(C)$ is a single point and $C$ lies in the segment over it.
:::

:::

::: {.pf-step #cluster}
Distinct segments meet only in $p$, and for $q\in T-\{p\}$ on $\overline{px_0}$ and any neighbourhood $U$ of $q$ with $p\notin U$ there are infinitely many $x\in X$ distinct from $x_0$ with $\overline{px}\cap U\ne\varnothing$.

::: pf-proof
Two distinct lines through $p$ meet only in $p$, which proves the first claim. For the second write $q=(\delta x_0,\delta)$ with $0<\delta\le1$; since $U$ is open in $\RR^2$ and contains $q$, some $\varepsilon>0$ gives the ball $B(q,\varepsilon)\subseteq U$. For $x\in X$ with $\abs{x-x_0}<\varepsilon/(2\delta)$ the point $(\delta x,\delta)$ of $\overline{px}$ is within $2\delta\abs{x-x_0}<\varepsilon$ of $q$, hence lies in $U$. The rationals $x\in X$ with $\abs{x-x_0}<\varepsilon/(2\delta)$ and $x\ne x_0$ are infinitely many.
:::

:::

::: {.pf-step #not-locally-connected}
(a) $T$ is not locally connected at any $q\in T-\{p\}$.

::: pf-proof
Let $U$ be a neighbourhood of $q$ with $p\notin U$, and suppose $W$ is a connected neighbourhood of $q$ with $W\subseteq U$. By step [](#connected-in-one-segment){.pf-ref} $W$ lies in the single segment $\overline{px_0}$ through $q$. But $W$ is a neighbourhood of $q$ in $T$, so it contains $T\cap O$ for some open $O\subseteq\RR^2$ with $q\in O$. The set $T\cap O\cap U$ is then a neighbourhood of $q$ in $T$ avoiding $p$, and step [](#cluster){.pf-ref} applied to it gives a point of $T\cap O\cap U\subseteq W$ lying on a segment $\overline{px}$ with $x\ne x_0$, so that point is not in $\overline{px_0}$. This contradicts $W\subseteq\overline{px_0}$, so no connected neighbourhood of $q$ lies inside $U$.
:::

:::

::: {.pf-step #locally-connected-at-p}
(a) $T$ is locally connected at $p$.

::: pf-proof
Let $U$ be a neighbourhood of $p$ and choose a ball $B(p,\varepsilon)$ about $p$ with $B(p,\varepsilon)\subseteq U$; the set $V=T\cap B(p,\varepsilon)$ is a neighbourhood of $p$ in $T$ contained in $U$, and it is path connected, being the union over $x\in X$ of the subsegments $\overline{px}\cap B(p,\varepsilon)$, each path connected and each containing $p$ (Munkres, Exercise 24.8(d)). So $V$ is a connected neighbourhood of $p$ inside $U$.
:::

:::

::: {.pf-step #second-fan}
(b) Let $Y=\QQ\cap([0,1]\times\{1\})$ and let $R$ be the union of the segments joining $1\times0$ to the points of $Y$. Then $R$ is path connected, and $1\times0$ lies in $R\cap T$.

::: pf-proof
Each segment of $R$ is path connected and all of them contain $1\times0$, so $R$ is path connected by the union argument of step [](#path-connected){.pf-ref}. The point $1\times0$ lies in $T$ because $1\in X$ and it lies in $R$ as an endpoint of every segment of $R$; in particular $R\cap T\ne\varnothing$.
:::

:::

::: {.pf-step #second-fan-nowhere}
(b) $R\cup T$ is locally connected at none of its points.

::: pf-proof
Let $q\in R\cup T$ and let $U$ be an open neighbourhood of $q$ small enough to avoid the vertex of whichever fan does not contain $q$, and to avoid both vertices when $q$ is one of them. The argument of step [](#not-locally-connected){.pf-ref} applies with the fan containing $q$ in place of $T$: a connected neighbourhood $W\subseteq U$ of $q$ would lie in one segment of that fan by the argument of step [](#connected-in-one-segment){.pf-ref}, applied to that fan with its own vertex, while $W$ also meets infinitely many other segments of it by the argument of step [](#cluster){.pf-ref}. So $R\cup T$ is locally connected at none of its points.
:::

:::

::: {.pf-step #both-parts}
(a) and (b) hold: $T$ is path connected and locally connected only at $p$, and $R\cup T$ is a path-connected subset of $\RR^2$ that is locally connected at none of its points.

::: pf-proof
Step [](#path-connected){.pf-ref} gives path connectedness of $T$; steps [](#not-locally-connected){.pf-ref} and [](#locally-connected-at-p){.pf-ref} place local connectedness at $p$ alone; steps [](#second-fan){.pf-ref} and [](#path-connected){.pf-ref} with the union argument give path connectedness of $R\cup T$, and step [](#second-fan-nowhere){.pf-ref} denies local connectedness at every one of its points. That answers both parts.
:::

:::

:::

:::
