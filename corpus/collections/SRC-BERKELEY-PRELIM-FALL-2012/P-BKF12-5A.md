---
schema: qual/card@1
id: P-BKF12-5A
kind: problem
title: Blaschke factors and removing the zeros of a holomorphic function from the disk
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
    Checked against Problem 5A in the retained Fall 2012 Berkeley prelim exam
    and its retained solution packet F12_Solutions.pdf.
- event: solution-written
  by: chatgpt
  date: 2026-09-24
- event: solution-reviewed
  by: chatgpt
  date: 2026-09-24
  note: >-
    Checked the Blaschke-factor boundary modulus, finiteness and
    multiplicities of the interior zeros, and the zero-free quotient.
---

::: {.problem}
(a) Show that if $\abs z<1$ then there is a holomorphic function
defined on some neighborhood of the unit disk whose only zero is at
$z$ and that has absolute value $1$ on the unit circle.

(b) Suppose that $f$ is a holomorphic function on the complex plane
and is not identically zero. Show that there is a holomorphic function
$g$ defined in some open set containing the unit disk such that
$\abs{f(z)}=\abs{g(z)}$ whenever $\abs z=1$, and such that $g$
has no zeros in the open unit disk.
:::

::: {.solution}
Write
$$
\DD\coloneqq\{w\in\CC:\abs w<1\}.
$$

<1>1. For every $a\in\DD$, the function
$$
\boxed{
B_a(w)\coloneqq\frac{w-a}{1-\overline{a}w}
}
$$
is holomorphic on a neighborhood of the closed unit disk, has its
only zero there at $w=a$, and satisfies
$$
\abs{B_a(w)}=1
\qquad(\abs w=1).
$$

::: {.proof}
If $a=0$, then $B_a(w)=w$, so all assertions are immediate. Suppose
$a\ne0$. The only zero of the denominator is
$$
w=\frac1{\overline a},
$$
whose modulus is $1/\abs a>1$. Hence one may choose $R>1$ with
$R<1/\abs a$; then $B_a$ is holomorphic on $\abs w<R$. Its
numerator has the unique zero $w=a$, while the denominator is nonzero
there, so this is the only zero.

If $\abs w=1$, then
$$
\begin{aligned}
\abs{w-a}^2
&=(w-a)(\overline w-\overline a)\\
&=1-w\overline a-a\overline w+\abs a^2\\
&=(1-\overline a w)(1-a\overline w)\\
&=\abs{1-\overline a w}^2.
\end{aligned}
$$
Thus $\abs{B_a(w)}=1$ on the unit circle.
:::

<1>2. A nonzero entire function $f$ has only finitely many zeros in
the closed unit disk.

::: {.proof}
The zeros of a nonzero holomorphic function are isolated. If $f$ had
infinitely many zeros in the compact closed unit disk, those zeros
would have an accumulation point in that disk. The identity theorem
would then imply $f\equiv0$, contrary to the hypothesis.
:::

<1>3. List the zeros of $f$ in $\DD$, repeated according to
multiplicity, as
$$
a_1,\ldots,a_m.
$$
Then there is an entire function $h$ with no zeros in $\DD$ such
that
$$
f(w)=\prod_{j=1}^m(w-a_j)h(w).
$$

::: {.proof}
Step <1>2 shows that the list is finite. At a zero of multiplicity
$r$, the local factorization theorem for holomorphic functions writes
$f(w)=(w-a)^r q(w)$ with $q(a)\ne0$. Dividing successively by the
finite collection of linear factors therefore produces an entire
function $h$. All zeros of $f$ in $\DD$ have been removed with their
full multiplicities, so $h$ has no zeros there.
:::

<1>4. Define
$$
\boxed{
g(w)\coloneqq
h(w)\prod_{j=1}^m(1-\overline{a_j}w)
}.
$$
Then $g$ is entire, has no zeros in $\DD$, and
$$
\abs{g(w)}=\abs{f(w)}
\qquad(\abs w=1).
$$

::: {.proof}
The displayed expression is a finite product of entire functions, so
$g$ is entire. For $w\in\DD$ and each $j$,
$$
\abs{\overline{a_j}w}<1,
$$
so $1-\overline{a_j}w\ne0$. Step <1>3 says that $h$ is also
nonzero in $\DD$, hence $g$ has no zeros there.

For $\abs w=1$, step <1>1 gives
$$
\abs{w-a_j}=\abs{1-\overline{a_j}w}
$$
for every $j$. Using the product formulas from step <1>3 and the
definition of $g$,
$$
\begin{aligned}
\abs{f(w)}
&=\abs{h(w)}
  \prod_{j=1}^m\abs{w-a_j}\\
&=\abs{h(w)}
  \prod_{j=1}^m\abs{1-\overline{a_j}w}\\
&=\abs{g(w)}.
\end{aligned}
$$
This also covers points where $f(w)=g(w)=0$ on the unit circle.
:::

<1>5. Q.E.D.

::: {.proof}
Step <1>1 proves part (a), and step <1>4 constructs the function
required in part (b).
:::
:::
