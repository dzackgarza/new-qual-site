---
schema: qual/card@1
id: P-BKF79-2
kind: problem
title: Sharp bound for a bounded upper-half-plane function vanishing at $i$
classification: {areas: [prelim], topics: []}
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
    Conjugating by the Cayley map from the upper half-plane to the unit
    disk gives a disk self-map vanishing at 0. Schwarz's lemma yields
    |f(2i)| at most |(2i-i)/(2i+i)|=1/3, and the Cayley map itself
    attains equality.
---

::: {.problem}
Suppose $f$ is holomorphic on the open upper half-plane, satisfies
\[
|f(z)|\le1
\]
there, and $f(i)=0$. How large can $|f(2i)|$ be?
:::

::: {.solution}
Define
$$
\phi(z)=\frac{z-i}{z+i}.
$$

::: pf

::: {.pf-step #cayley-map}
The map $\phi$ is a biholomorphism from the open upper
half-plane onto the unit disk, with
$$
\phi(i)=0.
$$

::: pf-proof
For $z=x+iy$ with $y>0$,
$$
\abs{z-i}^2=x^2+(y-1)^2
<
x^2+(y+1)^2
=
\abs{z+i}^2,
$$
so $\abs{\phi(z)}<1$. Solving
$$
w=\frac{z-i}{z+i}
$$
for $z$ gives
$$
z=i\frac{1+w}{1-w},
$$
and, for $\abs w<1$,
$$
\im\left(i\frac{1+w}{1-w}\right)
=
\frac{1-\abs w^2}{\abs{1-w}^2}
>
0.
$$
Thus this formula maps the unit disk into the upper half-plane and is
the inverse of $\phi$. Finally, $\phi(i)=0$.
:::

:::

::: {.pf-step #g-def}
The function
$$
g(w)=f\left(i\frac{1+w}{1-w}\right)
$$
is holomorphic on the unit disk, satisfies $\abs{g(w)}\leq1$, and
$g(0)=0$.

::: pf-proof
By step [](#cayley-map){.pf-ref}, the argument of $f$ lies in the upper half-plane for
$\abs w<1$, so $g$ is holomorphic there and inherits the bound
$\abs g\leq1$. Also
$$
g(0)=f(i)=0.
$$
:::

:::

::: {.pf-step #schwarz-bound}
For every $w$ in the unit disk,
$$
\abs{g(w)}\leq\abs w.
$$

::: pf-proof
This is Schwarz's lemma applied to the function in step [](#g-def){.pf-ref}.
:::

:::

::: {.pf-step #upper-bound}
Every function satisfying the hypotheses obeys
$$
\abs{f(2i)}\leq\frac13.
$$

::: pf-proof
We have
$$
\phi(2i)
=
\frac{2i-i}{2i+i}
=
\frac13.
$$
Since $g(\phi(z))=f(z)$, step [](#schwarz-bound){.pf-ref} gives
$$
\abs{f(2i)}
=
\abs{g(1/3)}
\leq
\frac13.
$$
:::

:::

::: {.pf-step #bound-attained}
The bound in step [](#upper-bound){.pf-ref} is attained.

::: pf-proof
Take
$$
f(z)=\phi(z)=\frac{z-i}{z+i}.
$$
By step [](#cayley-map){.pf-ref}, this function is holomorphic on the upper half-plane,
has modulus strictly less than $1$ there, and satisfies $f(i)=0$.
Moreover,
$$
\abs{f(2i)}=\frac13.
$$
:::

:::

::: {.pf-step #sharp-value}
The largest possible value is
$$
\boxed{\frac13}.
$$

::: pf-proof
Step [](#upper-bound){.pf-ref} gives the upper bound, and step [](#bound-attained){.pf-ref} shows that equality is
possible.
:::

:::

::: pf-qed
Step [](#sharp-value){.pf-ref} is the requested sharp value.
:::

:::
:::
