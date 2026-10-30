---
schema: qual/card@1
id: P-UCLARA18F-05
kind: problem
title: Pointwise limits of continuous functions converge locally uniformly on a dense set
classification:
  areas:
  - real-analysis
  topics:
  - Baire Category
  - Uniform Convergence
relations: []
review: draft
audit:
- event: source-checked
  by: gpt-5.6-sol
  date: 2026-09-13
  note: Transcribed from the official UCLA Analysis Qualifying Exam, Fall 2018, and reconciled with the retained UCLA Analysis Qualifying Exam Solutions compendium.
---

::: {.problem}
Let $\{f_n\}$ be a sequence of continuous real-valued functions on $[0,1]$ and suppose $f_n(x)$ converges to another real-valued function $f(x)$ at every $x\in[0,1]$.

(a) Prove that for every $\varepsilon>0$ there is a dense subset $D_\varepsilon\subset[0,1]$ such that if $x\in D_\varepsilon$, then there are an open interval $I\ni x$ and a positive integer $N_x$ such that for all $n>N_x$,
$$
\sup_{y\in I}\abs{f_n(y)-f(y)}\le\varepsilon.
$$

Hint: Consider the closed sets
$$
F_{N,\varepsilon}=\{y\in[0,1]:\abs{f_n(y)-f_m(y)}\le\varepsilon\text{ for all }n,m>N\}.
$$

(b) Prove that $f$ cannot be the characteristic function $\chi_{\QQ\cap[0,1]}$, where $\QQ$ is the set of rational numbers.
:::

::: {.solution}

Fix $\varepsilon>0$. For $N\ge1$, set
$$
F_N=F_{N,\varepsilon}
=\left\{y\in[0,1]:\abs{f_n(y)-f_m(y)}\le\varepsilon
\text{ for all }n,m>N\right\}.
$$

::: pf

::: {.pf-step #s1-1}

Each $F_N$ is closed in $[0,1]$, the sequence $(F_N)$ is increasing, and
$$
\bigcup_{N=1}^\infty F_N=[0,1].
$$


::: pf-proof

For fixed $n,m$, continuity of $f_n-f_m$ shows that
$$
\{y:\abs{f_n(y)-f_m(y)}\le\varepsilon\}
$$
is closed. The set $F_N$ is the intersection of these closed sets over all $n,m>N$, so it is closed. The inclusions $F_N\subseteq F_{N+1}$ are immediate.

For each fixed $y\in[0,1]$, the scalar sequence $f_n(y)$ converges and hence is Cauchy. Therefore there is some $N$ for which $\abs{f_n(y)-f_m(y)}\le\varepsilon$ whenever $n,m>N$, so $y\in F_N$.

:::

:::

::: {.pf-step #s1-2}

The set
$$
D_\varepsilon=(0,1)\cap\bigcup_{N=1}^\infty\operatorname{Int}_{[0,1]}(F_N)
$$
is dense in $[0,1]$.


::: pf-proof

It is enough to show that $\bigcup_N\operatorname{Int}(F_N)$ meets every nonempty relatively open subset of $[0,1]$. Let $U\subseteq[0,1]$ be nonempty and relatively open. Choose a nondegenerate closed interval $J\subseteq U$. By step [](#s1-1){.pf-ref},
$$
J=\bigcup_{N=1}^\infty(F_N\cap J),
$$
where every $F_N\cap J$ is closed in the complete metric space $J$. By the [[FT-6WPJI|Baire category theorem]], some $F_N\cap J$ has nonempty interior relative to $J$. Since $J\subseteq U$, this yields a nonempty relatively open interval contained in $U\cap F_N$, hence a point of $U\cap\operatorname{Int}_{[0,1]}(F_N)$.

Thus the union of the interiors is dense. Intersecting it with the dense open set $(0,1)$ leaves a dense subset of $[0,1]$, proving the claim.

:::

:::

::: {.pf-step #s1-3}

If $x\in D_\varepsilon$, then there are an open interval $I\ni x$ with $I\subset(0,1)$ and an integer $N_x$ such that
$$
\sup_{y\in I}\abs{f_n(y)-f(y)}\le\varepsilon
\qquad(n>N_x).
$$


::: pf-proof

By the definition of $D_\varepsilon$, choose $N_x$ and an open interval $I\ni x$ such that $I\subseteq F_{N_x}\cap(0,1)$. Then, for every $y\in I$ and every $n,m>N_x$,
$$
\abs{f_n(y)-f_m(y)}\le\varepsilon.
$$
Fix $n>N_x$ and let $m\to\infty$. Since $f_m(y)\to f(y)$,
$$
\abs{f_n(y)-f(y)}\le\varepsilon
$$
for every $y\in I$. Taking the supremum over $I$ proves the assertion.

:::

:::

::: {.pf-step #s1-4}

Part (a) follows: for every $\varepsilon>0$, the dense set $\boxed{D_\varepsilon}$ from step [](#s1-2){.pf-ref} has the required local uniform-tail property.


::: pf-proof

This is exactly step [](#s1-3){.pf-ref} for every $x\in D_\varepsilon$.

:::

:::

::: {.pf-step #s1-5}

No continuous function $g$ on a nonempty open interval $I\subseteq[0,1]$ can satisfy
$$
\sup_{y\in I}\abs{g(y)-\chi_{\QQ\cap[0,1]}(y)}<\frac12.
$$


::: pf-proof

Suppose such a $g$ existed. Fix $x\in I$. There are sequences of rational points $q_j\in I$ and irrational points $r_j\in I$ with $q_j\to x$ and $r_j\to x$. The displayed bound gives
$$
g(q_j)>\frac12,
\qquad
g(r_j)<\frac12.
$$
More precisely, if the uniform error is $c<1/2$, then
$$
g(q_j)\ge1-c,
\qquad
g(r_j)\le c.
$$
Continuity at $x$ would imply simultaneously $g(x)\ge1-c$ and $g(x)\le c$, impossible because $1-c>c$.

:::

:::

::: {.pf-step #s1-6}

The pointwise limit $f$ cannot equal $\boxed{\chi_{\QQ\cap[0,1]}}$.


::: pf-proof

Assume otherwise and apply part (a), step [](#s1-4){.pf-ref}, with $\varepsilon=1/3$. Choose $x\in D_{1/3}$, and let $I\ni x$ and $N_x$ be supplied by step [](#s1-3){.pf-ref}. For any $n>N_x$, the continuous function $f_n$ satisfies
$$
\sup_{y\in I}\abs{f_n(y)-\chi_{\QQ\cap[0,1]}(y)}\le\frac13<\frac12,
$$
contradicting step [](#s1-5){.pf-ref}.

:::

:::

::: pf-qed

Step [](#s1-4){.pf-ref} proves part (a), and step [](#s1-6){.pf-ref} proves part (b).

:::

:::

:::
