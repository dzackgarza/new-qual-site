---
schema: qual/card@1
id: P-BERK87S-03
kind: problem
title: If $f^2$ and $f^3$ are analytic, then $f$ is analytic
classification:
  areas: [prelim]
  topics: []
relations: []
review: draft
audit:
- event: source-checked
  by: gpt-5.6-sol
  date: 2026-09-13
- event: solution-written
  by: chatgpt
  date: 2026-09-22
- event: solution-reviewed
  by: chatgpt
  date: 2026-09-22
  note: >-
    Wrote f as f^3/f^2 away from the zeros of f^2. At each isolated zero,
    the identity |f|^2=|f^2| forces the quotient to tend to zero, so the
    removable-singularity theorem extends it holomorphically with the original
    value of f.
---

::: {.problem}
Let $f$ be complex-valued on the open unit disk $D$. Suppose
\[
f^2
\quad\text{and}\quad
f^3
\]
are both analytic on $D$. Prove that $f$ is analytic on $D$.
:::

::: {.solution}
Set
$$
g\coloneqq f^2,
\qquad
h\coloneqq f^3.
$$

<1>1. If $g\equiv0$, then $f$ is analytic on $D$.

::: {.proof}
For every $z\in D$,
$$
f(z)^2=g(z)=0,
$$
so $f\equiv0$, which is analytic.
:::

<1>2. Assume $g\not\equiv0$. On
$$
U\coloneqq\{z\in D:g(z)\ne0\},
$$
one has
$$
f=\frac{h}{g},
$$
so $f$ is analytic on $U$.

::: {.proof}
If $z\in U$, then $g(z)=f(z)^2\ne0$, hence $f(z)\ne0$. Therefore
$$
\frac{h(z)}{g(z)}
=
\frac{f(z)^3}{f(z)^2}
=
f(z).
$$
Since $g$ and $h$ are analytic and $g$ does not vanish on $U$, the quotient
$h/g$ is analytic on $U$.
:::

<1>3. Let $a\in D$ satisfy $g(a)=0$. Then $f$ is analytic in a neighborhood
of $a$.

::: {.proof}
Because $g$ is analytic and not identically zero, its zeros are isolated.
Choose $r>0$ such that
$$
\{z:0<\abs{z-a}<r\}\subseteq U.
$$
On this punctured disk, step <1>2 gives
$$
\frac{h(z)}{g(z)}=f(z).
$$
Moreover,
$$
\abs{f(z)}^2
=
\abs{f(z)^2}
=
\abs{g(z)}.
$$
Since $g$ is continuous and $g(a)=0$,
$$
\abs{f(z)}
=
\sqrt{\abs{g(z)}}
\longrightarrow0
$$
as $z\to a$. Hence $h/g$ is bounded near the isolated singularity $a$ and
in fact tends to $0$. By the removable-singularity theorem, $h/g$ extends
analytically across $a$ with value $0$.

Finally,
$$
f(a)^2=g(a)=0,
$$
so $f(a)=0$. Thus the analytic extension agrees with the original function
$f$ at $a$, proving that $f$ is analytic near $a$.
:::

<1>4. The function $f$ is analytic on all of $D$.

::: {.proof}
By step <1>2, $f$ is analytic at every point where $g$ is nonzero. By step
<1>3, it is analytic at every zero of $g$. These two sets cover $D$.
:::

<1>5. Q.E.D.

::: {.proof}
Step <1>1 handles the case $g\equiv0$, and step <1>4 handles the case
$g\not\equiv0$.
:::
:::
