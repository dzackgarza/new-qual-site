---
schema: qual/card@1
id: P-CHAVAN-CA-5-3
kind: problem
title: Maximum modulus principle for open mappings
classification: {areas: [complex-analysis], topics: [Open Mapping Theorem, Maximum Modulus Principle]}
relations: []
review: draft
audit:
  - event: source-checked
    by: gpt-5.6-sol
    date: 2026-09-14
    note: The deterministic extraction drops the bars on the closures in part 2; the public text rendering of the same source confirms the clauses about the compact closure and continuity on the closure.
---

::: {.problem}
Let $f:\Omega\to\CC$ be an open mapping on an open set $\Omega\subseteq\CC$.
Define $\abs{f}(z)=\abs{f(z)}$.

(a) Show that $\abs{f}$ cannot have a local maximum at a point of $\Omega$.

(b) If $\overline\Omega$ is compact and $f$ is continuous on $\overline\Omega$, show that $\abs{f}$ attains its maximum on $\partial\Omega$.
:::

::: {.solution}

For part (b), the assertion necessarily presupposes that $\Omega$ is nonempty;
otherwise $\abs{f}$ has no maximum. We interpret continuity on $\overline\Omega$ as
the existence of a continuous extension to $\overline\Omega$, denoted again by
$f$. For $c\in\CC$ and $r>0$, write
$$
B(c,r)=\{z\in\CC:\abs{z-c}<r\}.
$$

::: pf

::: {.pf-step #s1}

The function $\abs{f}$ cannot have a local maximum at any point of $\Omega$.


::: pf-proof

::: {.pf-step #s1-1}

Suppose, for contradiction, that $\abs{f}$ has a local maximum at
$a\in\Omega$. Then there is an $r>0$ such that
$$
B(a,r)\subseteq\Omega
\qquad\text{and}\qquad
\abs{f(z)}\leq\abs{f(a)}
\quad\text{for every }z\in B(a,r).
$$


::: pf-proof

The local-maximum hypothesis gives a neighborhood of $a$ on which the displayed
inequality holds. Since $\Omega$ is open, that neighborhood may be shrunk to a
ball $B(a,r)$ contained in $\Omega$.

:::

:::

::: {.pf-step #s1-2}

If $w=f(a)$, then $f(B(a,r))$ is an open neighborhood of $w$ contained in
$$
\{\zeta\in\CC:\abs{\zeta}\leq\abs{w}\}.
$$


::: pf-proof

The set $B(a,r)$ is open in $\Omega$, so the hypothesis that $f$ is an open
mapping makes $f(B(a,r))$ open in $\CC$. It contains $w=f(a)$. The containment
in the closed disc follows from the inequality in step [](#s1-1){.pf-ref}.

:::

:::

::: {.pf-step #s1-3}

No open neighborhood of $w$ is contained in
$\{\zeta\in\CC:\abs{\zeta}\leq\abs{w}\}$.


::: pf-proof

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

:::

::: pf-qed

Because $f(B(a,r))$ is an open neighborhood of $w$, step [](#s1-2){.pf-ref} gives some
$\varepsilon>0$ with $B(w,\varepsilon)\subseteq f(B(a,r))$. This contradicts
step [](#s1-3){.pf-ref}. Hence the assumed local maximum cannot exist.

:::

:::

:::

::: {.pf-step #s2}

Under the hypotheses of part (b), $\abs{f}$ attains a maximum at some
$b\in\overline\Omega$.


::: pf-proof

The set $\overline\Omega$ is nonempty and compact, and the continuous extension
of $f$ makes $\abs{f}=\abs{f}$ continuous on $\overline\Omega$. The extreme value
theorem therefore gives $b\in\overline\Omega$ such that
$$
\abs{f(z)}\leq\abs{f(b)}
\qquad\text{for every }z\in\overline\Omega.
$$

:::

:::

::: {.pf-step #s3}

Every such maximizing point $b$ belongs to $\partial\Omega$.


::: pf-proof

If $b\in\Omega$, then the inequality in step [](#s2){.pf-ref} shows that $\abs{f}$ has a local
maximum at $b$, contradicting step [](#s1){.pf-ref}. Since $\Omega$ is open,
$$
\overline\Omega\setminus\Omega=\partial\Omega,
$$
so $b\in\partial\Omega$.

:::

:::

::: {.pf-step #s4}

Therefore $\abs{f}$ attains its maximum on $\partial\Omega$.


::: pf-proof

Step [](#s2){.pf-ref} produces a maximizing point $b\in\overline\Omega$, and step [](#s3){.pf-ref}
places that point on $\partial\Omega$.

:::

:::

::: pf-qed

Step [](#s1){.pf-ref} proves part (a), and step [](#s4){.pf-ref} proves part (b).

:::

:::

:::

::: {.remark}
Part (b) needs $\Omega\neq\varnothing$. If $\Omega=\varnothing$, then
$\overline\Omega$ is compact and the empty map is open and continuous, but
$\abs{f}$ has no maximum. The phrase "$f$ is continuous on $\overline\Omega$" is
understood as saying that $f$ extends continuously from $\Omega$ to
$\overline\Omega$.
:::
