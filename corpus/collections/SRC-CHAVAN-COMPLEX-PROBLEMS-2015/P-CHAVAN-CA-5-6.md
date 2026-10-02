---
schema: qual/card@1
id: P-CHAVAN-CA-5-6
kind: problem
title: Minimum modulus principle
classification: {areas: [complex-analysis], topics: []}
relations: []
review: draft
audit:
- event: source-checked
  by: gpt-5.6-sol
  date: 2026-09-14
  note: The deterministic extraction drops the closure bar in the continuity hypothesis; the public text rendering of the same source confirms continuity on the closure.
---

::: {.problem}
Let $f$ be a nonconstant holomorphic function on a bounded open set $\Omega$, continuous on $\overline\Omega$.
Show that either $f$ has a zero in $\Omega$ or $|f|$ assumes its minimum on $\partial\Omega$.
:::

::: {.solution}
<1>1. The function $|f|$ attains a minimum at some point
$a\in\overline\Omega$.

::: {.proof}
Because $f$ is nonconstant, $\Omega$ is nonempty. Since $\Omega$ is bounded,
$\overline\Omega$ is compact. The function $|f|$ is continuous on
$\overline\Omega$, so the extreme value theorem gives
$a\in\overline\Omega$ such that
$$
\abs{f(a)}\leq\abs{f(z)}
\qquad\text{for every }z\in\overline\Omega.
$$
:::

<1>2. If $f$ has a zero in $\Omega$, then the first alternative holds.

::: {.proof}
This is immediate.
:::

<1>3. Suppose that $f$ has no zero in $\Omega$. If $a\in\partial\Omega$, then
$|f|$ assumes its minimum on $\partial\Omega$.

::: {.proof}
The point $a$ is a global minimizer on $\overline\Omega$ by step <1>1, so if it
lies on $\partial\Omega$, its value is the required boundary minimum.
:::

<1>4. Suppose instead that $f$ has no zero in $\Omega$ and $a\in\Omega$. If $U$
is the connected component of $\Omega$ containing $a$, then $f$ is constant on
$U$.

::: {.proof}
Since $f$ has no zero on $U$, the function
$$
g=\frac1f
$$
is holomorphic on $U$. By step <1>1, for every $z\in U$,
$$
\abs{g(z)}=\frac1{\abs{f(z)}}
\leq
\frac1{\abs{f(a)}}
=\abs{g(a)}.
$$
Thus $|g|$ has a local maximum at the interior point $a$. The maximum modulus
principle makes $g$, and hence $f$, constant on the domain $U$.
:::

<1>5. Under the hypotheses of step <1>4, there is a point
$b\in\partial\Omega$ such that $|f(b)|=|f(a)|$.

::: {.proof}
The component $U$ is a nonempty bounded open subset of $\CC$, so
$\partial U\neq\varnothing$. Moreover,
$$
\partial U\subseteq\partial\Omega.
$$
Indeed, if $b\in\partial U\cap\Omega$, choose a disc $B(b,r)\subseteq\Omega$.
Because $b\in\overline U$, this disc meets $U$. The union
$U\cup B(b,r)$ is therefore a connected subset of $\Omega$ containing $U$, so
maximality of the connected component forces $B(b,r)\subseteq U$. Then
$b\in U$, contradicting $b\in\partial U$.

Choose $b\in\partial U$. Since $b\in\overline U\subseteq\overline\Omega$, there
is a sequence $z_n\in U$ with $z_n\to b$. Step <1>4 gives
$f(z_n)=f(a)$ for every $n$, while continuity of $f$ on $\overline\Omega$ gives
$$
f(b)=\lim_{n\to\infty}f(z_n)=f(a).
$$
Hence $b\in\partial\Omega$ and $\abs{f(b)}=\abs{f(a)}$.
:::

<1>6. If $f$ has no zero in $\Omega$, then $|f|$ assumes its minimum on
$\partial\Omega$.

::: {.proof}
Let $a$ be the minimizing point from step <1>1. If $a\in\partial\Omega$, apply
step <1>3. If $a\in\Omega$, step <1>5 produces a boundary point with the same
minimum value.
:::

<1>7. Q.E.D.

::: {.proof}
Step <1>2 gives the first alternative when $f$ has an interior zero. Otherwise
step <1>6 gives the second alternative.
:::
:::
