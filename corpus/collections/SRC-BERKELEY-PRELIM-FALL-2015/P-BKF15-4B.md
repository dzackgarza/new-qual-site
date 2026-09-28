---
schema: qual/card@1
id: P-BKF15-4B
kind: problem
title: The Schur algorithm step preserves Schur functions
classification:
  areas:
  - prelim
  topics: []
relations: []
review: draft
audit:
- event: source-checked
  by: chatgpt
  date: 2026-09-24
  note: >-
    Independently checked the retained Fall 2015 solution packet, including
    its explicit correction that the printed statement is false under the
    printed non-constant definition of a Schur function.
- event: solution-written
  by: chatgpt
  date: 2026-09-24
- event: solution-reviewed
  by: chatgpt
  date: 2026-09-24
  note: >-
    Checked the counterexample f(z)=z and the corrected Schwarz-lemma
    argument showing that the transform is holomorphic and disk-valued when
    constant outputs are allowed.
---

::: {.problem}
A Schur function is a non-constant holomorphic function defined in the open unit disk whose values have absolute value at most 1. Show that if f is a Schur function then

$$
\frac { f ( 0 ) - f ( z ) } { ( 1 - { \overline { { f ( 0 ) } } } f ( z ) ) z }
$$

is also a Schur function.
:::

::: {.solution}
Write
$$
\DD\coloneqq\{z\in\CC:\abs{z}<1\}.
$$

<1>1. The printed assertion is false with the printed definition of a
Schur function.

::: {.proof}
Take
$$
f(z)=z.
$$
This is nonconstant, holomorphic on $\DD$, and satisfies
$\abs{f(z)}<1$. Since $f(0)=0$, the displayed transform is
$$
\frac{0-z}{(1-0)z}
=
-1
$$
for $z\ne0$, and its removable extension at $0$ is also $-1$.
Thus the transform is constant. Under the printed definition, which
requires a Schur function to be nonconstant, the transform is not a
Schur function.
:::

<1>2. Call a holomorphic map
$$
\DD\to\overline{\DD}
$$
a Schur function in the wide sense, constants allowed. If $f$ is a
nonconstant Schur function, then its displayed transform is a Schur
function in the wide sense.

::: {.proof}
Steps <1>3--<1>8 prove this assertion. It differs from the printed
assertion only in allowing the transform to be constant; the input $f$
remains nonconstant.
:::

<1>3. For a nonconstant holomorphic function
$$
f:\DD\to\overline{\DD},
$$
one has
$$
\abs{f(z)}<1
$$
for every $z\in\DD$. In particular, if
$$
a\coloneqq f(0),
$$
then $\abs{a}<1$.

::: {.proof}
If $\abs{f(z_0)}=1$ at an interior point, then $\abs{f}$ attains its maximum
there. The maximum modulus principle would force $f$ to be constant,
contrary to the hypothesis.
:::

<1>4. For $\abs{a}<1$, define
$$
\varphi_a(w)
\coloneqq
\frac{a-w}{1-\overline a\,w}.
$$
Then
$$
\varphi_a:\DD\to\DD.
$$

::: {.proof}
For $\abs{w}<1$,
$$
\begin{aligned}
1-\abs{\varphi_a(w)}^2
&=
\frac{
\abs{1-\overline a\,w}^2-\abs{a-w}^2
}{
\abs{1-\overline a\,w}^2
}\\
&=
\frac{
(1-\abs{a}^2)(1-\abs{w}^2)
}{
\abs{1-\overline a\,w}^2
}
>
0.
\end{aligned}
$$
Thus $\abs{\varphi_a(w)}<1$.
:::

<1>5. The function
$$
h(z)\coloneqq\varphi_a(f(z))
$$
is holomorphic on $\DD$, maps $\DD$ into itself, and
satisfies
$$
h(0)=0.
$$

::: {.proof}
By step <1>3, $\abs{a}<1$ and $f(\DD)\subset\DD$. The
denominator
$$
1-\overline a\,f(z)
$$
cannot vanish because
$$
\abs{\overline a\,f(z)}<1.
$$
Hence $h$ is holomorphic. Step <1>4 shows that its values lie in
$\DD$, and
$$
h(0)
=
\varphi_a(a)
=
0.
$$
:::

<1>6. For every $z\in\DD$,
$$
\abs{h(z)}\le\abs{z}.
$$

::: {.proof}
This is Schwarz's lemma applied to the holomorphic self-map $h$ of
$\DD$ from step <1>5, which fixes the origin.
:::

<1>7. The function
$$
g(z)
\coloneqq
\frac{h(z)}z
$$
for $z\ne0$ extends holomorphically to $\DD$ and satisfies
$$
\abs{g(z)}\le1
$$
throughout the disk.

::: {.proof}
Since $h$ is holomorphic and $h(0)=0$, its Taylor expansion has the
form
$$
h(z)=zq(z)
$$
for a holomorphic function $q$ on $\DD$. Thus $g=q$ away from
$0$ and extends holomorphically by
$$
g(0)=q(0)=h'(0).
$$

For $z\ne0$, step <1>6 gives
$$
\abs{g(z)}
=
\frac{\abs{h(z)}}{\abs{z}}
\le1.
$$
Continuity of the extension gives the same inequality at $z=0$.
:::

<1>8. For $z\ne0$, the function in step <1>7 is exactly
$$
\frac{f(0)-f(z)}
{(1-\overline{f(0)}f(z))z}.
$$

::: {.proof}
By definition,
$$
h(z)
=
\varphi_{f(0)}(f(z))
=
\frac{f(0)-f(z)}
{1-\overline{f(0)}f(z)}.
$$
Dividing by $z$ gives the displayed expression.
:::

<1>9. Hence the printed assertion is false, while the assertion of
step <1>2 is true.

::: {.proof}
Step <1>1 disproves the printed assertion. Steps <1>7--<1>8 show that
the transform extends holomorphically to the disk and has absolute
value at most $1$, which is the wide-sense Schur condition of step
<1>2.
:::

<1>10. Q.E.D.

::: {.proof}
Step <1>9 gives both the counterexample to the printed assertion and
the proof of the assertion of step <1>2.
:::
:::
