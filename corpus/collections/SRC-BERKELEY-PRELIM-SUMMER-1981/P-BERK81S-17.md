---
schema: qual/card@1
id: P-BERK81S-17
kind: problem
title: Entire functions satisfying $|f|\le|g|$ are constant multiples
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
  date: 2026-09-21
- event: solution-reviewed
  by: chatgpt
  date: 2026-09-21
  note: >-
    If g is identically zero, the inequality forces f to vanish as well.
    Otherwise h=f/g is holomorphic away from the isolated zeros of g and
    satisfies |h|<=1 there. Each zero of g is therefore a removable
    singularity of h. The resulting bounded entire function is constant by
    Liouville, and f=cg follows everywhere.
---

::: {.problem}
Suppose $f$ and $g$ are entire functions such that
\[
|f(z)|\le |g(z)|
\]
for every $z\in\mathbb C$.
Show that
\[
f(z)=c\,g(z)
\]
for some constant $c\in\mathbb C$.
:::

::: {.solution}
<1>1. If
$$
g\equiv0,
$$
then
$$
f\equiv0.
$$

::: {.proof}
The hypothesis gives
$$
\abs{f(z)}
\leq
\abs{g(z)}
=
0
$$
for every $z\in\CC$. Hence $f(z)=0$ for every $z$.
:::

<1>2. If $g\equiv0$, the required conclusion holds with
$$
\boxed{c=0}.
$$

::: {.proof}
By step <1>1,
$$
f\equiv0=0\cdot g.
$$
:::

<1>3. Assume henceforth that $g$ is not identically zero, and let
$$
Z=\{z\in\CC:g(z)=0\}.
$$
Then every point of $Z$ is isolated.

::: {.proof}
The function $g$ is entire and not identically zero. By the identity
theorem, its zeros have no accumulation point in $\CC$. Thus every zero is
isolated.
:::

<1>4. On $\CC\sm Z$, define
$$
h(z)=\frac{f(z)}{g(z)}.
$$
Then $h$ is holomorphic and satisfies
$$
\abs{h(z)}\leq1.
$$

::: {.proof}
On $\CC\sm Z$, the denominator $g(z)$ is nonzero, so the quotient of the
entire functions $f$ and $g$ is holomorphic. The given inequality gives
$$
\abs{h(z)}
=
\frac{\abs{f(z)}}{\abs{g(z)}}
\leq
1.
$$
:::

<1>5. Every point of $Z$ is a removable singularity of $h$.

::: {.proof}
Fix $z_0\in Z$. By step <1>3, there is a punctured disk
$$
0<\abs{z-z_0}<r
$$
containing no zero of $g$ other than $z_0$. Thus $h$ is holomorphic on this
punctured disk. Step <1>4 gives
$$
\abs{h(z)}\leq1
$$
there, so $h$ is bounded near $z_0$. The removable singularity theorem
therefore extends $h$ holomorphically across $z_0$.
:::

<1>6. The function $h$ extends to an entire function
$$
H:\CC\longrightarrow\CC
$$
such that
$$
\abs{H(z)}\leq1
$$
for every $z\in\CC$.

::: {.proof}
Step <1>5 removes each isolated singularity at a zero of $g$. The resulting
function $H$ is entire and agrees with $h$ on $\CC\sm Z$.

The bound
$$
\abs{H(z)}\leq1
$$
holds off $Z$ by step <1>4. At a point $z_0\in Z$, it follows by continuity
of $H$ from the same bound on the punctured neighborhood.
:::

<1>7. There is a constant $c\in\CC$ such that
$$
H\equiv c.
$$

::: {.proof}
By step <1>6, the function $H$ is bounded and entire. Liouville's theorem
therefore implies that $H$ is constant.
:::

<1>8. One has
$$
\boxed{
f(z)=c\,g(z)
}
$$
for every $z\in\CC$.

::: {.proof}
On $\CC\sm Z$, steps <1>4 and <1>7 give
$$
\frac{f(z)}{g(z)}
=
H(z)
=
c,
$$
so
$$
f(z)=c\,g(z).
$$
The entire function
$$
f-cg
$$
therefore vanishes on the nonempty open set $\CC\sm Z$. By the identity
theorem, it vanishes identically on $\CC$.
:::

<1>9. Q.E.D.

::: {.proof}
Step <1>2 handles the case $g\equiv0$, and step <1>8 handles the case in
which $g$ is not identically zero.
:::
:::
