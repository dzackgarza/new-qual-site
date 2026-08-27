---
schema: qual/card@1
id: P-E33SA
kind: exercise
title: Uniform continuity, sets of discontinuities, and non-uniform limits of continuous
  functions
classification:
  areas:
  - real-analysis
  topics:
  - Uniform Continuity
  - Continuity
  - Counterexamples
relations: []
review: draft
audit:
- event: solution-written
  by: gemini-3.7-flash
  date: 2026-08-17
---

::: exercise
- What does it mean for a function to be **uniformly continuous** on a set?

- Is it possible for a function $f:\RR\to \RR$ to be discontinuous precisely on the rationals $\QQ$?
  If so, produce such a function, if not, why?

  - Can the set of discontinuities be precisely the irrationals $\RR\sm\QQ$?

- Find a sequence of continuous functions that does *not* converge uniformly, but still has a pointwise limit that is continuous.
:::
::: {.solution}
<1>1. Definition: $f$ is uniformly continuous on a set $E$ iff for every $\eps > 0$ there is a single $\delta > 0$ such that $|x - y| < \delta$, $x, y \in E$ $\Rightarrow$ $|f(x) - f(y)| < \eps$ (the same $\delta$ works for all pairs).
Proof: this is the definition, in contrast with pointwise continuity, where $\delta$ may depend on the point.

<1>2. A function can be discontinuous precisely on $\QQ$: yes — the Thomae function $f(x) = 1/q$ if $x = p/q$ in lowest terms, $f(x) = 0$ if $x$ is irrational, is continuous exactly at the irrationals, hence discontinuous exactly on $\QQ$.
<2>1. $f$ is continuous at every irrational $x$: given $\eps > 0$, only finitely many rationals $p/q$ in a bounded interval around $x$ have $1/q \ge \eps$, so a small neighborhood of $x$ contains no rational with $f \ge \eps$; and $f$ is $0$ at all irrationals there.
Proof: the set $\{p/q : |p/q - x| < 1,\ 1/q \ge \eps\}$ is finite; take $\delta$ smaller than the distance from $x$ to the nearest such point (and than $1$, so the neighborhood stays bounded).
<2>2. $f$ is discontinuous at every rational $p/q$: $f(p/q) = 1/q > 0$, but irrationals arbitrarily close to $p/q$ have $f = 0$.
Proof: density of the irrationals; the limit of $f$ along irrationals approaching $p/q$ is $0 \ne 1/q$.

<1>3. A function cannot be discontinuous precisely on $\RR \setminus \QQ$ (the irrationals).
<2>1. The set of discontinuities of any function is $F_\sigma$: a countable union of closed sets.
Proof: the points where the oscillation of $f$ is $\ge 1/n$ form a closed set, and the discontinuities are their union over $n$.
<2>2. $\RR \setminus \QQ$ is not $F_\sigma$.
Proof: if $\RR\setminus\QQ = \bigcup_n F_n$ with $F_n$ closed, then $\QQ = \bigcap_n (\RR \setminus F_n)$ would be a $G_\delta$.
But a countable dense set cannot be a $G_\delta$: if $\QQ = \bigcap_n U_n$ with $U_n$ open, each $U_n$ is dense (it contains $\QQ$), so by the Baire category theorem $\bigcap_n U_n$ is uncountable (indeed comeager), contradicting countability of $\QQ$.

<1>4. A sequence of continuous functions with a continuous pointwise limit but no uniform convergence: $f_n(x) = \dfrac{nx}{1 + n^2 x^2}$ on $[0,1]$.
<2>1. $f_n \to 0$ pointwise.
Proof: for $x = 0$, $f_n(0) = 0$; for $x > 0$, $f_n(x) \le \frac{nx}{n^2 x^2} = \frac{1}{nx} \to 0$.
<2>2. $f_n \not\to 0$ uniformly.
Proof: $\|f_n\|_\infty \ge f_n(1/n) = \frac{1}{2}$, so the uniform limit (if it existed) would be $\ge 1/2 \ne 0$; indeed $\|f_n - 0\|_\infty = 1/2 \not\to 0$.

<1>5. Q.E.D. Proof: <1>1–<1>4 answer each question.
(Second bullet: Thomae's function; third: the $F_\sigma$ obstruction; fourth: $nx/(1+n^2x^2)$.)
:::
