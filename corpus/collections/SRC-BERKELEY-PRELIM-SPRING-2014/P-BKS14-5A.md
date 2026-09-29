---
schema: qual/card@1
id: P-BKS14-5A
kind: problem
title: Dominated meromorphic functions are proportional
classification:
  areas:
  - prelim
  topics: []
relations: []
review: draft
audit:
- event: source-checked
  by: gpt-5.6-sol
  date: 2026-09-13
  note: Checked against the vendored UC Berkeley Spring 2014 preliminary examination PDF.
- event: solution-written
  by: chatgpt
  date: 2026-09-25
- event: solution-reviewed
  by: chatgpt
  date: 2026-09-25
  note: Independently checked the zero case, meromorphic quotient, removability of every bounded singularity, and the final Liouville argument.
---

::: {.problem}
Let $f,g$ be meromorphic on $\CC$ and suppose $|f(z)|\le |g(z)|$ at every point where both are defined.
Show that there is $c\in\CC$ such that $f(z)=c\,g(z)$ wherever both are defined.
:::

::: {.solution}

::: pf

::: {.pf-step #s1}

If
$$
g\equiv0,
$$
then
$$
f\equiv0.
$$

::: pf-proof

At every point where $f$ is finite, the hypothesis gives
$$
\abs{f(z)}
\leq
\abs{g(z)}
=
0,
$$
so $f(z)=0$.

Moreover, $f$ cannot have a pole. If $p$ were a pole, then on a punctured
neighborhood of $p$ the function $f$ would be finite and nonzero at some
points, contradicting the preceding conclusion. Thus $f$ has no poles and
vanishes everywhere.

:::

:::

::: {.pf-step #s2}

In the case $g\equiv0$, the required conclusion holds with
$$
c=0.
$$

::: pf-proof

Step [](#s1){.pf-ref} gives
$$
f=0=0\cdot g.
$$

:::

:::

::: pf-step

Now suppose
$$
g\not\equiv0.
$$
Then
$$
h\coloneqq\frac{f}{g}
$$
is a meromorphic function on $\CC$.

::: pf-proof

The quotient of two meromorphic functions is meromorphic provided the
denominator is not identically zero.

:::

:::

::: {.pf-step #s4}

Every singularity of $h$ is removable.

::: pf-proof

Let $p$ be a possible singularity of $h$. Since zeros and poles of
nonzero meromorphic functions are isolated, choose a punctured disk
$$
0<\abs{z-p}<r
$$
containing no other zero or pole of $f$ or $g$.

At every point of this punctured disk, both $f$ and $g$ are finite and
$g(z)\neq0$. Hence the given inequality gives
$$
\abs{h(z)}
=
\frac{\abs{f(z)}}{\abs{g(z)}}
\leq
1.
$$
Thus $h$ is bounded on a punctured neighborhood of $p$. The removable
singularity theorem shows that $p$ is removable.

:::

:::

::: {.pf-step #s5}

After filling in all removable singularities, $h$ is an entire
function satisfying
$$
\abs{h(z)}\leq1
$$
for every $z\in\CC$.

::: pf-proof

Step [](#s4){.pf-ref} removes every possible singularity of the meromorphic function
$h$. The bound holds away from the removed points by hypothesis and at the
removed points by continuity of the extension.

:::

:::

::: {.pf-step #s6}

The function $h$ is constant:
$$
h(z)=c
$$
for some
$$
c\in\CC.
$$

::: pf-proof

By step [](#s5){.pf-ref}, $h$ is a bounded entire function. Liouville's theorem
therefore makes it constant.

:::

:::

::: {.pf-step #s7}

Consequently,
$$
\boxed{
f(z)=c\,g(z)
}
$$
at every point where both meromorphic functions are defined.

::: pf-proof

At every point where $f$ and $g$ are finite and $g(z)\neq0$, step [](#s6){.pf-ref}
gives
$$
\frac{f(z)}{g(z)}=c,
$$
hence $f(z)=cg(z)$.

If $g(z)=0$ at a point where both functions are finite, the original
inequality gives
$$
\abs{f(z)}\leq0,
$$
so $f(z)=0=cg(z)$. Thus the identity holds everywhere that both are
defined.

:::

:::

::: pf-qed

Step [](#s2){.pf-ref} handles $g\equiv0$, and step [](#s7){.pf-ref} handles
$g\not\equiv0$.

:::

:::

:::
