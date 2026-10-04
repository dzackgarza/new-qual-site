---
schema: qual/card@1
id: P-AMH-ALG-SG16-31
kind: problem
title: Reducibility of $x^2+3$ over $\mathbb F_7$ and an intermediate ideal
classification:
  areas:
  - algebra
  topics: []
relations: []
review: draft
audit:
- event: source-checked
  by: gpt-5.6-sol
  date: 2026-09-13
  note: Checked against the vendored Amherst College Study Guide for Algebra (September 2016).
---

::: {.problem}
(March 2008) Let $g(x)=x^2+3\in\mathbb{F}_7[x]$, where $\mathbb{F}_7=\{0,1,2,3,4,5,6\}$ is the field of seven elements.
(a) Prove that $g$ is reducible in $\mathbb{F}_7[x]$.
(b) Let $\langle g\rangle\subseteq\mathbb{F}_7[x]$ denote the principal ideal $\{gh\mid h\in\mathbb{F}_7[x]\}$.
Find an ideal $I\subseteq\mathbb{F}_7[x]$ such that $\langle g\rangle\subsetneq I\subsetneq\mathbb{F}_7[x]$.
:::

::: {.solution}
<1>1. In $\FF_7[x]$,
$$
g(x)=x^2+3=(x-2)(x+2).
$$

::: {.proof}
Expanding gives
$$
(x-2)(x+2)=x^2-4.
$$
Since $-4\equiv3\pmod7$, this equals $x^2+3$ in $\FF_7[x]$.
:::

<1>2. The polynomial $g$ is reducible in $\FF_7[x]$.

::: {.proof}
Step <1>1 expresses $g$ as a product of two nonconstant degree-$1$
polynomials, so the factorization is nontrivial.
:::

<1>3. Part (a) follows.

::: {.proof}
This is step <1>2.
:::

<1>4. Let
$$
I=\langle x-2\rangle.
$$
Then
$$
\langle g\rangle\subseteq I.
$$

::: {.proof}
By step <1>1,
$$
g=(x-2)(x+2).
$$
Thus every element of $\langle g\rangle$ has the form
$$
h g
=h(x-2)(x+2)
=(h(x+2))(x-2),
$$
which is a multiple of $x-2$ and hence belongs to $I$.
:::

<1>5. The inclusion
$$
\langle g\rangle\subseteq I
$$
is strict.

::: {.proof}
The polynomial $x-2$ belongs to $I$.  If $x-2\in\langle g\rangle$, then
there would exist $h\in\FF_7[x]$ with
$$
x-2=hg.
$$
If $h=0$, the right side is zero, impossible.  If $h\neq0$, then
$$
\deg(hg)=\deg h+\deg g\geq2,
$$
whereas $\deg(x-2)=1$.  Hence $x-2\notin\langle g\rangle$.
:::

<1>6. The ideal $I$ is a proper ideal of $\FF_7[x]$.

::: {.proof}
If $I=\FF_7[x]$, then $1\in I$, so
$$
1=h(x-2)
$$
for some $h\in\FF_7[x]$.  If $h=0$, the right side is zero.  If $h\neq0$,
then
$$
\deg(h(x-2))=\deg h+1\geq1,
$$
whereas $\deg1=0$.  Both cases are impossible.  Thus $1\notin I$, so
$I\subsetneq\FF_7[x]$.
:::

<1>7. Therefore
$$
\boxed{
\langle g\rangle
\subsetneq
\langle x-2\rangle
\subsetneq
\FF_7[x].
}
$$

::: {.proof}
Step <1>4 gives the first inclusion, step <1>5 makes it strict, and step <1>6
gives the strict second inclusion.
:::

<1>8. Part (b) follows.

::: {.proof}
Step <1>7 supplies the required intermediate ideal.
:::

<1>9. Q.E.D.

::: {.proof}
Steps <1>3 and <1>8 establish parts (a) and (b), respectively.
:::
:::
