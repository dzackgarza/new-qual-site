---
schema: qual/card@1
id: P-RA-WORKSHOP-D8-METRIC2
kind: problem
title: 'Characterize lower and upper semicontinuity by open inverse images and limits'
classification:
  areas:
  - real-analysis
  topics:
  - continuity
  - metric-spaces
relations: []
review: draft
solved: true
---

::: {.problem title="?"}
(May 2017, 6) Let $(X,d)$ be a metric space.
A function $f:X\to\mathbb R$ is said to be lower semi-continuous (l.s.c.) if $f^{-1}(a,\infty)=\{x\in X:f(x)>a\}$ is open in $X$ for every $a\in\mathbb R$.
Analogously, $f$ is upper semi-continuous (u.s.c.) if $f^{-1}(-\infty,b)=\{x\in X:f(x)<b\}$ is open in $X$ for every $b\in\mathbb R$.

(a) Prove that a function $f:X\to\mathbb R$ is continuous if and only if $f$ is both l.s.c. and u.s.c.

(b) Prove that $f$ is lower semi-continuous if and only if
$$
\liminf_{n\to\infty}f(x_n)\ge f(x)
$$
whenever $\{x_n\}_{n=1}^{\infty}\subseteq X$ is such that $x_n\to x$ in $X$.
:::

:::: {.solution}
> **AI-Generated Solution** **Goal:** (a) Prove $f$ is continuous iff $f$ is both l.s.c. and u.s.c.; (b) prove $f$ is l.s.c. iff $\liminf_{n} f(x_n) \ge f(x)$ whenever $x_n \to x$.

<1>1. (a) $f$ is continuous iff $f$ is both l.s.c. and u.s.c. <2>1. If $f$ is continuous, then $f$ is both l.s.c. and u.s.c. Proof: $f^{-1}(a, \infty)$ and $f^{-1}(-\infty, b)$ are preimages of open sets under a continuous map, hence open.
<2>2. If $f$ is both l.s.c. and u.s.c., then $f$ is continuous.
Proof: every open set $U \subseteq \mathbb R$ is a union of open intervals; for an interval $(a,b)$, $f^{-1}(a,b) = f^{-1}(a,\infty) \cap f^{-1}(-\infty, b)$ is open (intersection of two open sets, by the two hypotheses).
Preimages of open sets are open, so $f$ is continuous.
<2>3. Q.E.D. Proof: <2>1 and <2>2.

<1>2. (b) $f$ is l.s.c. iff $\liminf_n f(x_n) \ge f(x)$ for every $x_n \to x$.
<2>1. ($\Rightarrow$) If $f$ is l.s.c. and $x_n \to x$, then $\liminf_n f(x_n) \ge f(x)$.
Proof: let $L = \liminf_n f(x_n) < f(x)$ lead to a contradiction: choose $a$ with $L < a < f(x)$.
Then $f(x) > a$, so $x \in f^{-1}(a, \infty)$, an open set; since $x_n \to x$, eventually $x_n \in f^{-1}(a,\infty)$, i.e. $f(x_n) > a$ for all large $n$, contradicting $L = \liminf f(x_n) < a$.
<2>2. ($\Leftarrow$) If $\liminf_n f(x_n) \ge f(x)$ for all $x_n \to x$, then $f$ is l.s.c. Proof: show $f^{-1}(a, \infty)$ is open: suppose $x \in f^{-1}(a, \infty)$ but $x$ is not an interior point.
Then there is a sequence $x_n \to x$ with $x_n \notin f^{-1}(a,\infty)$, i.e. $f(x_n) \le a$ for all $n$.
Then $\liminf_n f(x_n) \le a < f(x)$, contradicting the hypothesis.
<2>3. Q.E.D. Proof: <2>1 and <2>2 establish the equivalence.
:::
