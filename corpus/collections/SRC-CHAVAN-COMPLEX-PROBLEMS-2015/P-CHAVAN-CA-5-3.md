---
schema: qual/card@1
id: P-CHAVAN-CA-5-3
kind: problem
title: Maximum modulus principle for open mappings
classification: {areas: [complex-analysis], topics: []}
relations: []
review: draft
audit:
- event: source-checked
  by: gpt-5.6-sol
  date: 2026-09-14
  note: The deterministic extraction drops the bars on the closures in part 2; the public text rendering of the same source confirms the clauses about the compact closure and continuity on the closure.
---

::: {.problem}
Let $f:\Omega\to\mathbb C$ be an open mapping on an open set $\Omega\subseteq\mathbb C$.
Define $|f|(z)=|f(z)|$.

1. Show that $|f|$ cannot have a local maximum at a point of $\Omega$.

2. If $\overline\Omega$ is compact and $f$ is continuous on $\overline\Omega$, show that $|f|$ attains its maximum on $\partial\Omega$.
:::

::: {.solution}
For part (2), the assertion necessarily presupposes that $\Omega$ is nonempty;
otherwise $|f|$ has no maximum. We interpret continuity on $\overline\Omega$ as
the existence of a continuous extension to $\overline\Omega$, denoted again by
$f$. For $c\in\CC$ and $r>0$, write
$$
B(c,r)=\{z\in\CC:\abs{z-c}<r\}.
$$

<1>1. The function $|f|$ cannot have a local maximum at any point of $\Omega$.

<2>1. Suppose, for contradiction, that $|f|$ has a local maximum at
$a\in\Omega$. Then there is an $r>0$ such that
$$
B(a,r)\subseteq\Omega
\qquad\text{and}\qquad
\abs{f(z)}\leq\abs{f(a)}
\quad\text{for every }z\in B(a,r).
$$

::: {.proof}
The local-maximum hypothesis gives a neighborhood of $a$ on which the displayed
inequality holds. Since $\Omega$ is open, that neighborhood may be shrunk to a
ball $B(a,r)$ contained in $\Omega$.
:::

<2>2. If $w=f(a)$, then $f(B(a,r))$ is an open neighborhood of $w$ contained in
$$
\{\zeta\in\CC:\abs{\zeta}\leq\abs{w}\}.
$$

::: {.proof}
The set $B(a,r)$ is open in $\Omega$, so the hypothesis that $f$ is an open
mapping makes $f(B(a,r))$ open in $\CC$. It contains $w=f(a)$. The containment
in the closed disc follows from the inequality in step <2>1.
:::

<2>3. No open neighborhood of $w$ is contained in
$\{\zeta\in\CC:\abs{\zeta}\leq\abs{w}\}$.

::: {.proof}
Let $\varepsilon>0$. If $w\neq0$, put $u=w/\abs{w}$; if $w=0$, put $u=1$.
Then
$$
\zeta=w+\frac{\varepsilon}{2}u
$$
satisfies $\abs{\zeta-w}=\varepsilon/2<\varepsilon$. If $w\neq0$, then
$\zeta=(\abs{w}+\varepsilon/2)u$, so
$\abs{\zeta}=\abs{w}+\varepsilon/2>\abs{w}$; if $w=0$, then
$\abs{\zeta}=\varepsilon/2>0=\abs{w}$. Thus every ball about $w$ contains a point
outside the closed disc.
:::

<2>4. Q.E.D.

::: {.proof}
Because $f(B(a,r))$ is an open neighborhood of $w$, step <2>2 gives some
$\varepsilon>0$ with $B(w,\varepsilon)\subseteq f(B(a,r))$. This contradicts
step <2>3. Hence the assumed local maximum cannot exist.
:::

<1>2. Under the hypotheses of part (2), $|f|$ attains a maximum at some
$b\in\overline\Omega$.

::: {.proof}
The set $\overline\Omega$ is nonempty and compact, and the continuous extension
of $f$ makes $|f|=\abs{f}$ continuous on $\overline\Omega$. The extreme value
theorem therefore gives $b\in\overline\Omega$ such that
$$
\abs{f(z)}\leq\abs{f(b)}
\qquad\text{for every }z\in\overline\Omega.
$$
:::

<1>3. Every such maximizing point $b$ belongs to $\partial\Omega$.

::: {.proof}
If $b\in\Omega$, then the inequality in step <1>2 shows that $|f|$ has a local
maximum at $b$, contradicting step <1>1. Since $\Omega$ is open,
$$
\overline\Omega\setminus\Omega=\partial\Omega,
$$
so $b\in\partial\Omega$.
:::

<1>4. Therefore $|f|$ attains its maximum on $\partial\Omega$.

::: {.proof}
Step <1>2 produces a maximizing point $b\in\overline\Omega$, and step <1>3
places that point on $\partial\Omega$.
:::

<1>5. Q.E.D.

::: {.proof}
Step <1>1 proves part (1), and step <1>4 proves part (2).
:::
:::

::: {.remark}
Part (2) needs $\Omega\neq\varnothing$. If $\Omega=\varnothing$, then
$\overline\Omega$ is compact and the empty map is open and continuous, but
$|f|$ has no maximum. The phrase "$f$ is continuous on $\overline\Omega$" is
understood as saying that $f$ extends continuously from $\Omega$ to
$\overline\Omega$.
:::
