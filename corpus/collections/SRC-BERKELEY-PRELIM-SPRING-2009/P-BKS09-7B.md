---
schema: qual/card@1
id: P-BKS09-7B
kind: problem
title: Odd univalent function $\sqrt{f(z^2)}$ from a normalized univalent $f$
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
  note: Cleaned LaTeX and added a remark that the source itself omits the function name f, checked on s09solutions.pdf page 6 problem 7B.
- event: source-checked
  by: chatgpt
  date: 2026-09-25
  note: >-
    Rechecked the retained PDF and found that its solution incorrectly prints
    g=1/sqrt(f(z^2)); the correct branch constructed from f(z^2)=z^2 phi(z)
    is g=z sqrt(phi(z)).
- event: solution-written
  by: chatgpt
  date: 2026-09-25
- event: solution-reviewed
  by: chatgpt
  date: 2026-09-25
  note: Independently checked the nonvanishing factor, analytic square-root branch, evenness, oddness, and injectivity argument.
---

::: {.problem}
If is a univalent (1-1 analytic) function with domain the unit disc such that $f(z) = z + \sum_{n=2}^{\infty} a_n z^n$, then prove that

$$
g(z) = \sqrt{f(z^2)}
$$

is an odd analytic univalent function on the unit disc.
:::

::: {.solution}
Since
$$
f(w)
=
w+\sum_{n=2}^{\infty}a_nw^n,
$$
define
$$
\phi(z)
\coloneqq
1+\sum_{n=2}^{\infty}a_n z^{2n-2}.
$$

<1>1. The function $\phi$ is analytic, even, and nonvanishing on the unit
disk, and
$$
f(z^2)=z^2\phi(z).
$$

::: {.proof}
Substituting $w=z^2$ in the power series for $f$ gives
$$
f(z^2)
=
z^2+\sum_{n=2}^{\infty}a_nz^{2n}
=
z^2\phi(z).
$$
The displayed power series for $\phi$ contains only even powers of $z$, so
$\phi$ is analytic and even, with $\phi(0)=1$.

If $z\neq0$ and $\phi(z)=0$, then
$$
f(z^2)=0=f(0).
$$
Since $f$ is univalent, this would imply $z^2=0$, a contradiction. At
$z=0$, one has $\phi(0)=1$. Hence $\phi$ has no zeros in the unit disk.
:::

<1>2. There is an analytic function $h$ on the unit disk such that
$$
h(z)^2=\phi(z)
$$
and $h(0)=1$.

::: {.proof}
The unit disk is simply connected, and step <1>1 shows that $\phi$ is a
nonvanishing analytic function there. Hence $\phi$ admits an analytic
square root. Choosing the sign of that square root so that its value at $0$
is $1$ gives $h$.
:::

<1>3. The function $h$ is even.

::: {.proof}
Because $h^2=\phi$ and $\phi$ is even,
$$
h(-z)^2
=
\phi(-z)
=
\phi(z)
=
h(z)^2.
$$
The function $h$ is nonvanishing, so
$$
q(z)\coloneqq\frac{h(-z)}{h(z)}
$$
is analytic and satisfies $q(z)^2=1$. Thus its values lie in the discrete
set $\{1,-1\}$. Since the unit disk is connected, $q$ is constant. At
$z=0$,
$$
q(0)=1,
$$
so $q\equiv1$ and therefore $h(-z)=h(z)$.
:::

<1>4. The analytic square-root branch
$$
g(z)\coloneqq zh(z)
$$
satisfies
$$
g(z)^2=f(z^2)
$$
and is odd and analytic on the unit disk.

::: {.proof}
Steps <1>1 and <1>2 give
$$
g(z)^2
=
z^2h(z)^2
=
z^2\phi(z)
=
f(z^2).
$$
Thus $g$ is an analytic choice of the square root in the statement. Since
$h$ is analytic, so is $g$. By step <1>3,
$$
g(-z)
=
-z\,h(-z)
=
-z\,h(z)
=
-g(z),
$$
so $g$ is odd.
:::

<1>5. The function $g$ is univalent on the unit disk.

::: {.proof}
Suppose
$$
g(z_1)=g(z_2).
$$
Squaring and using step <1>4 gives
$$
f(z_1^2)=f(z_2^2).
$$
Since $f$ is univalent,
$$
z_1^2=z_2^2,
$$
so either $z_1=z_2$ or $z_1=-z_2$.

In the second case, oddness from step <1>4 and the assumed equality give
$$
g(z_1)
=
g(-z_1)
=
-g(z_1),
$$
so $g(z_1)=0$. Then
$$
0=g(z_1)^2=f(z_1^2)=f(0).
$$
Univalence of $f$ implies $z_1^2=0$, hence $z_1=z_2=0$. Thus in every case
$z_1=z_2$.
:::

<1>6. Q.E.D.

::: {.proof}
Step <1>4 proves that the intended square-root branch is analytic and odd,
and step <1>5 proves that it is univalent.
:::
:::

::: {.remark}
The source statement reads "If is a univalent (1-1 analytic) function", omitting the name of the function; the formula $f(z) = z + \sum_{n=2}^{\infty} a_n z^n$ and the definition of $g$ show that the function meant is $f$.
:::
