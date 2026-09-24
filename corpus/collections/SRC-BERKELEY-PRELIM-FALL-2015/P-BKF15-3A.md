---
schema: qual/card@1
id: P-BKF15-3A
kind: problem
title: Darboux property of derivatives via difference quotients
classification:
  areas:
  - prelim
  topics: []
relations: []
review: draft
audit:
- event: source-checked
  by: claude-opus-5
  date: 2026-09-16
  note: Statement checked against F15_Exam.pdf problem 3A; the extraction read the derivative prime as f 0.
- event: source-checked
  by: chatgpt
  date: 2026-09-24
  note: >-
    Independently checked the retained Fall 2015 solution packet: the mean
    value theorem gives X subset Y, difference quotients tending to a
    derivative give Y subset closure(X), and connectedness of the
    difference-quotient domain yields Darboux's property.
- event: solution-written
  by: chatgpt
  date: 2026-09-24
- event: solution-reviewed
  by: chatgpt
  date: 2026-09-24
  note: >-
    Checked continuity of the two-variable difference quotient off the
    diagonal and the final interval argument for every set lying between an
    interval and its closure.
---

::: {.problem}
Let $f(x)$ be differentiable on an interval $(a, b)$.

(a) Prove that if $X$ is the range of $(f(u) - f(v))/(u - v)$ for $a < u < v < b$ and $Y$ is the range of $f'(x)$ on $(a, b)$, then $X \subseteq Y \subseteq \overline{X}$.

(b) Prove that the range of $f'(x)$ on $(a, b)$ is an interval (possibly unbounded).
Do not assume that $f'(x)$ is continuous.
:::

::: {.solution}
Define
$$
D\coloneqq\{(u,v)\in\RR^2:a<u<v<b\}
$$
and
$$
m(u,v)\coloneqq\frac{f(u)-f(v)}{u-v}.
$$
Thus
$$
X=m(D).
$$

<1>1. One has
$$
X\subseteq Y.
$$

::: {.proof}
Take any $s\in X$. Then
$$
s=\frac{f(u)-f(v)}{u-v}
$$
for some $a<u<v<b$. Since $f$ is differentiable, it is continuous on
$[u,v]$ and differentiable on $(u,v)$. The mean value theorem gives
$c\in(u,v)$ such that
$$
s
=
\frac{f(v)-f(u)}{v-u}
=
f'(c).
$$
Hence $s\in Y$.
:::

<1>2. One has
$$
Y\subseteq\overline X.
$$

::: {.proof}
Take $y\in Y$. Then
$$
y=f'(x)
$$
for some $x\in(a,b)$. Choose any sequence
$$
v_n\in(x,b)
$$
with $v_n\to x$. For every $n$,
$$
m(x,v_n)\in X,
$$
and by the definition of the derivative,
$$
\lim_{n\to\infty}m(x,v_n)
=
\lim_{n\to\infty}
\frac{f(v_n)-f(x)}{v_n-x}
=
f'(x)
=
y.
$$
Thus $y$ is a limit point of $X$, so $y\in\overline X$.
:::

<1>3. This proves part (a):
$$
\boxed{X\subseteq Y\subseteq\overline X}.
$$

::: {.proof}
Combine steps <1>1 and <1>2.
:::

<1>4. The set $D$ is connected.

::: {.proof}
The set $D$ is convex. Indeed, if
$$
(u_1,v_1),(u_2,v_2)\in D
$$
and $0\le t\le1$, then
$$
a<(1-t)u_1+tu_2<(1-t)v_1+tv_2<b.
$$
Every convex subset of $\RR^2$ is path connected, hence connected.
:::

<1>5. The function
$$
m:D\to\RR
$$
is continuous.

::: {.proof}
Differentiability of $f$ implies continuity of $f$. Therefore
$$
(u,v)\longmapsto f(u)-f(v)
$$
and
$$
(u,v)\longmapsto u-v
$$
are continuous on $D$. Since $u-v\ne0$ throughout $D$, their quotient
$m$ is continuous.
:::

<1>6. The set $X$ is an interval.

::: {.proof}
By step <1>4, $D$ is connected, and by step <1>5, $m$ is continuous.
Therefore its image
$$
X=m(D)
$$
is connected. The connected subsets of $\RR$ are exactly the
intervals.
:::

<1>7. Every subset $Z$ satisfying
$$
X\subseteq Z\subseteq\overline X
$$
is an interval.

::: {.proof}
By step <1>6, $X$ is an interval. Let $p,q\in Z$ with $p<q$, and let
$r$ satisfy
$$
p<r<q.
$$
Since $p,q\in\overline X$, every point strictly between $p$ and $q$
belongs to $X$: the closure of an interval can add only one or both
endpoints, not an interior gap. Hence $r\in X\subseteq Z$. Thus $Z$ is
an interval.
:::

<1>8. The range $Y$ of $f'$ is an interval.

::: {.proof}
By step <1>3,
$$
X\subseteq Y\subseteq\overline X.
$$
Apply step <1>7 with $Z=Y$.
:::

<1>9. Q.E.D.

::: {.proof}
Step <1>3 proves part (a), and step <1>8 proves part (b).
:::
:::
