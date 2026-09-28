---
schema: qual/card@1
id: P-AZOFF-H06
kind: problem
title: Local $m$-to-one behavior of an analytic function at a zero of order $m$
classification:
  areas: [complex-analysis]
  topics: []
relations: []
review: draft
audit:
- event: source-checked
  by: gpt-5.6-sol
  date: 2026-09-14
  note: Checked against Rouché’s theorem, Problem 6, in the deterministic MinerU Flash extraction assets/attachments/Azoff Problems by Topic_extracted.md.
- event: solution-written
  by: chatgpt
  date: 2026-09-21
- event: solution-reviewed
  by: chatgpt
  date: 2026-09-21
  note: >-
    Factored f(z)-w_0=(z-z_0)^m g(z) with g(z_0) nonzero and chose a small
    disk on which both g and m g+(z-z_0)g' are nonzero. Rouché then preserves
    the multiplicity-m zero count for nearby target values. Because f' is
    nonzero off z_0 in that disk and w differs from w_0, all counted zeros
    are simple, hence distinct.
---

::: {.problem}
Let $f$ be analytic in a domain $D$. Fix $z_0 \in D$ and let $w_0 = f(z_0)$. Suppose $z_0$ is a zero of finite multiplicity $m$ for $f(z) - w_0 = 0$. Show that there exist $\delta > 0$ and $\varepsilon > 0$ such that for each $w$ with $0 < \abs{w - w_0} < \varepsilon$, the equation $f(z) - w = 0$ has exactly $m$ distinct solutions inside the disk $\abs{z - z_0} < \delta$.
:::

::: {.solution}
Because $z_0$ is a zero of multiplicity $m$ of $f-w_0$, write
$$
f(z)-w_0
=
(z-z_0)^m g(z),
$$
where $g$ is analytic near $z_0$ and
$$
g(z_0)\neq0.
$$

<1>1. There is $\delta>0$ such that the closed disk
$$
\overline{B}(z_0,\delta)
$$
lies in $D$ and, throughout that disk,
$$
g(z)\neq0
$$
and
$$
m g(z)+(z-z_0)g'(z)\neq0.
$$

::: {.proof}
Since $D$ is open, some closed disk centered at $z_0$ lies in $D$.
Moreover,
$$
g(z_0)\neq0
$$
and
$$
m g(z_0)+(z_0-z_0)g'(z_0)
=
m g(z_0)
\neq0.
$$
Both displayed functions are continuous. Shrinking the disk if necessary
therefore makes both nonzero on its closure.
:::

<1>2. On the punctured disk
$$
0<\abs{z-z_0}\leq\delta,
$$
one has
$$
f'(z)\neq0.
$$

::: {.proof}
Differentiate the factorization above:
$$
f'(z)
=
(z-z_0)^{m-1}
\left(
m g(z)+(z-z_0)g'(z)
\right).
$$
For $z\neq z_0$, the first factor is nonzero, and the second factor is
nonzero by step <1>1.
:::

<1>3. Define
$$
\varepsilon
=
\min_{\abs{z-z_0}=\delta}
\abs{f(z)-w_0}.
$$
Then
$$
\varepsilon>0.
$$

::: {.proof}
On the boundary circle,
$$
f(z)-w_0
=
(z-z_0)^m g(z).
$$
Step <1>1 gives $g(z)\neq0$, so this expression never vanishes on the
circle. Its modulus is continuous on the compact circle, hence attains a
strictly positive minimum.
:::

<1>4. If
$$
0<\abs{w-w_0}<\varepsilon,
$$
then $f(z)-w$ has exactly $m$ zeros in
$$
\abs{z-z_0}<\delta,
$$
counting multiplicity.

::: {.proof}
On the boundary circle,
$$
\abs{
(f(z)-w)-(f(z)-w_0)
}
=
\abs{w-w_0}
<
\varepsilon
\leq
\abs{f(z)-w_0}.
$$
Rouché's theorem implies that $f-w$ and $f-w_0$ have the same number of
zeros in the disk, counting multiplicity.

By step <1>1,
$$
f(z)-w_0=(z-z_0)^m g(z)
$$
with $g$ nonzero throughout the disk. Hence $f-w_0$ has exactly the one
zero $z_0$, of multiplicity $m$. Thus $f-w$ has exactly $m$ zeros counting
multiplicity.
:::

<1>5. Every zero of $f-w$ in the disk from step <1>4 is simple.

::: {.proof}
Because $w\neq w_0$,
$$
f(z_0)-w
=
w_0-w
\neq0.
$$
Thus none of the zeros counted in step <1>4 is $z_0$. Every such zero lies
in the punctured disk, where step <1>2 gives $f'(z)\neq0$. Therefore the
derivative of $f(z)-w$ is nonzero at each zero, so each zero is simple.
:::

<1>6. For every $w$ satisfying
$$
0<\abs{w-w_0}<\varepsilon,
$$
the equation
$$
f(z)=w
$$
has exactly $m$ distinct solutions in
$$
\abs{z-z_0}<\delta.
$$

::: {.proof}
Step <1>4 gives $m$ solutions counted with multiplicity. Step <1>5 says
that every counted zero has multiplicity one. Hence there are exactly $m$
distinct solutions.
:::

<1>7. Q.E.D.

::: {.proof}
Steps <1>1, <1>3, and <1>6 provide the required positive numbers
$\delta$ and $\varepsilon$ and establish the conclusion.
:::
:::
