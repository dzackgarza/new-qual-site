---
schema: qual/card@1
id: P-E33SA
kind: problem
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

::: {.exercise}
- What does it mean for a function to be **uniformly continuous** on a set?

- Is it possible for a function $f:\RR\to \RR$ to be discontinuous precisely on the rationals $\QQ$?
  If so, produce such a function, if not, why?

  - Can the set of discontinuities be precisely the irrationals $\RR\sm\QQ$?

- Find a sequence of continuous functions that does *not* converge uniformly, but still has a pointwise limit that is continuous.
:::
::: {.solution}
A function $f$ is \dfn{uniformly continuous} on $E$ if for every $\eps > 0$ there is $\delta > 0$ such that $|f(x) - f(y)| < \eps$ for all $x, y \in E$ with $|x - y| < \delta$.

<1>1. Thomae's function, $f(p/q) = 1/q$ for $p/q$ in lowest terms with $q \geq 1$ and $f(x) = 0$ for irrational $x$, is discontinuous exactly on $\QQ$.

<2>1. $f$ is continuous at every irrational $x$.

::: {.proof}
Given $\eps > 0$, the set $\theset{p/q : |p/q - x| < 1,\ 1/q \ge \eps}$ is finite and does not contain $x$. Choose $\delta < 1$ smaller than the distance from $x$ to each of its points. Then $|f(y)| < \eps = \eps + |f(x)|$ for $|y - x| < \delta$.
:::

<2>2. $f$ is discontinuous at every rational $p/q$.

::: {.proof}
$f(p/q) = 1/q > 0$, while irrationals $y \to p/q$ have $f(y) = 0$.
:::

<2>3. Q.E.D.

::: {.proof}
Steps <2>1 and <2>2.
:::

<1>2. No function $f\colon \RR \to \RR$ is discontinuous exactly on $\RR \setminus \QQ$.

<2>1. The set of discontinuities of $f$ is an $F_\sigma$ set.

::: {.proof}
Let $\omega_f(x) = \inf_{\delta > 0}\sup\theset{|f(y) - f(z)| : y, z \in B(x,\delta)}$ be the oscillation of $f$ at $x$. The set $\theset{\omega_f < 1/n}$ is open, so $\theset{\omega_f \ge 1/n}$ is closed, and $f$ is discontinuous at $x$ exactly when $\omega_f(x) \geq 1/n$ for some $n$.
:::

<2>2. $\RR \setminus \QQ$ is not an $F_\sigma$ set.

::: {.proof}
If $\RR\setminus\QQ = \bigcup_n F_n$ with $F_n$ closed, then $\QQ = \bigcap_n U_n$ with $U_n = \RR \setminus F_n$ open and dense, since $U_n \supseteq \QQ$. The sets $U_n$ and $\RR \setminus \theset q$, $q \in \QQ$, are countably many open dense sets with empty intersection, contradicting the Baire category theorem.
:::

<2>3. Q.E.D.

::: {.proof}
Steps <2>1 and <2>2.
:::

<1>3. $f_n(x) = \dfrac{nx}{1 + n^2 x^2}$ on $[0,1]$ are continuous and converge pointwise, but not uniformly, to the continuous function $0$.

::: {.proof}
$f_n(0) = 0$, and for $x > 0$, $0 \le f_n(x) \le \frac{nx}{n^2 x^2} = \frac{1}{nx} \to 0$. But $f_n(1/n) = \frac12$ for every $n$, so $\sup_{[0,1]}|f_n - 0| \ge \frac12$.
:::
:::
