---
schema: qual/card@1
id: E-YERPP
kind: problem
title: Order-preserving surjections are homeomorphisms
classification:
  areas:
  - topology
  topics:
  - Order Topology
  - Homeomorphisms
relations: []
review: draft
audit:
- event: source-checked
  by: claude
  date: 2026-11-10
  note: >-
    Read against Munkres, Topology (2000), §24 Exercise 7, printed p. 158, with Theorem
    24.1; the three parts are stored as printed.
- event: solution-written
  by: claude
  date: 2026-11-10
  note: >-
    Transcribed from the located published solution: "positron0802", "Solutions to Topology,
    Chapter 3" (1 January 2021), Exercise 24.7, PDF p. 5. An order-preserving surjection is
    injective and carries open rays to open rays both ways, hence is a continuous open
    bijection; x -> x^n on R_+ is order preserving and onto, so its inverse is continuous;
    and the example of (c) is order preserving and onto but not a homeomorphism, because its
    domain's subspace topology is not its order topology. (tmp/sources/munkres-solutions-
    positron-ch3.pdf).
---

::: {.exercise}

(a) Let $X$ and $Y$ be ordered sets in the order topology.
Show that if $f: X \to Y$ is order preserving and surjective, then $f$ is a homeomorphism.

(b) Let $X = Y = \RR_+$.
Given a positive integer $n$, show that the function $f(x) = x^n$ is order preserving and surjective.
Conclude that its inverse, the $n$th root function, is continuous.

(c) Let $X$ be the subspace $(-\infty, -1) \cup [0, \infty)$ of $\RR$.
Show that the function $f: X \to \RR$ defined by setting $f(x) = x + 1$ if $x < -1$, and $f(x) = x$ if $x \geq 0$, is order preserving and surjective.
Is $f$ a homeomorphism?
Compare with (a).
:::

::: {.solution}
The complete published solution is **"positron0802", *Solutions to Topology, Chapter 3* (1 January 2021), Exercise 24.7, PDF p. 5** (`tmp/sources/munkres-solutions-positron-ch3.pdf`); all three parts are theirs.

(a) Let $X,Y$ be ordered sets in the order topology and let $f:X\to Y$ be order preserving and surjective; it is then injective, hence a bijection. For $b\in Y$ write $x=f^{-1}(b)$; the open rays satisfy
$$
f^{-1}\big((b,+\infty)\big)=(x,+\infty),\qquad f^{-1}\big((-\infty,b)\big)=(-\infty,x),
$$
because $f$ is order preserving and surjective (a point maps above $b$ exactly when it lies above $x$). Open rays form a subbasis for the order topology, so $f$ is continuous. Likewise
$$
f\big((c,+\infty)\big)=\big(f(c),+\infty\big),\qquad f\big((-\infty,d)\big)=\big(-\infty,f(d)\big)
$$
are open in $Y$, so $f$ carries a subbasis of $X$ to open sets and is an open map. Hence $f$ is a homeomorphism.

(b) Let $X=Y=\RR_{+}$ and $f(x)=x^{n}$ for a fixed positive integer $n$. It is surjective: given $y>0$, the set $\{t\ge0\mid t^{n}<y\}$ is nonempty and bounded above, so its supremum $s$ satisfies $s^{n}=y$ by completeness, and $f(s)=y$. It is order preserving: if $0<x<y$ then $x^{2}<xy<y^{2}$ and inductively $x^{k}<y^{k}$. By (a), $f$ is a homeomorphism, so its inverse, the $n$-th root, is continuous.

(c) Let $X=(-\infty,-1)\cup[0,\infty)\subset\RR$ and $f(x)=x+1$ for $x<-1$, $f(x)=x$ for $x\ge0$. It is surjective: for $y<0$, $f(y-1)=y$; for $y\ge0$, $f(y)=y$. It is order preserving (it is strictly increasing on each piece, and every point of the first piece is below every point of the second, as is every image). But $f$ is not a homeomorphism: $\RR$ is connected while $X$ is separated by $(-\infty,-1)$ and $[0,\infty)$. The hypothesis of (a) is not met, because $X$ is given the subspace topology of $\RR$, not the order topology of $X$ — and the two differ here, since $[0,\infty)$ is open in the subspace topology but not in the order topology of $X$.
:::
