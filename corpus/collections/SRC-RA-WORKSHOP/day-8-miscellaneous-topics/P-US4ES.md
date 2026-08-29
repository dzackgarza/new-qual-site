---
schema: qual/card@1
id: P-US4ES
kind: problem
title: Continuity equivalent to lower and upper semicontinuity, and sequential characterization
  of lower semicontinuity
classification:
  areas:
  - real-analysis
  topics:
  - Continuity
  - Metric Spaces
relations: []
review: draft
audit:
- event: solution-written
  by: gemini-3.7-flash
  date: 2026-08-25
---

::: problem
Let $(X,d)$ be a metric space. A function
$f \colon X \to \mathbb{R}$ is said to be lower semi-continuous
(l.s.c) if $f^{-1}(a,\infty)  = \{x \in X \, \colon \,  f(x)> a\}$
is open in $X$ for every $a \in \mathbb{R}$. Analogously, $f$ is
upper semi-continuous (u.s.c) if
$f^{-1}(-\infty, b) = \{x \in X \, \colon \,  f(x)<b\}$ is open in
$X$ for every $b \in \mathbb{R}$.


Prove that a function $f \colon X \to \mathbb{R}$ is continuous
if and only if $f$ is both l.s.c. and u.s.c.


Prove that $f$ is lower semi-continuous if and only if
$\liminf_{n \to \infty} f(x_n) \geq f(x)$ whenever
$\{x_n\}_{n=1}^\infty \subseteq X$ such that $x_n \to x$ in $X$.
:::
::: {.solution}
<1>1. Continuous $\Rightarrow$ l.s.c. and u.s.c.
    Proof: if $f$ is continuous, then $f^{-1}(a,\infty)$ and $f^{-1}(-\infty,b)$ are preimages of open sets, hence open.
<1>2. l.s.c. and u.s.c. $\Rightarrow$ continuous.
    Proof: every open set $U \subseteq \RR$ is a union of open intervals $(a,b)$; since $f^{-1}(a,b) = f^{-1}(a,\infty) \cap f^{-1}(-\infty,b)$ is open, $f^{-1}(U)$ is a union of open sets, hence open.
<1>3. (Part 2, $\Rightarrow$) If $f$ is l.s.c. and $x_n \to x$, then $\liminf_n f(x_n) \ge f(x)$.
    Proof: fix $a < f(x)$. Then $x \in f^{-1}(a,\infty)$, which is open, so $x_n \in f^{-1}(a,\infty)$ for all large $n$, i.e. $f(x_n) > a$ eventually; hence $\liminf_n f(x_n) \ge a$. Since $a < f(x)$ is arbitrary, $\liminf_n f(x_n) \ge f(x)$.
<1>4. (Part 2, $\Leftarrow$) If $\liminf_n f(x_n) \ge f(x)$ whenever $x_n \to x$, then $f$ is l.s.c.
    Proof: suppose $f$ were not l.s.c.: some $f^{-1}(a,\infty)$ is not open. Then there is $x$ with $f(x) > a$ and a sequence $x_n \to x$ with $f(x_n) \le a$ for all $n$ (points outside the set accumulating at $x$). Then $\liminf_n f(x_n) \le a < f(x)$, contradicting the hypothesis.
<1>5. Q.E.D.
:::
