---
schema: qual/card@1
id: P-AMD-ZTLK4VHF
kind: problem
title: Nilpotents in commutative rings and perturbations of units
classification:
  areas:
  - algebra
  topics:
  - Nilpotence
  - Ideals
  - Rings
relations: []
review: draft
audit:
- event: source-checked
  by: gpt-5.6-sol
  date: 2026-09-07
  note: >-
    Checked against UCSD Math 200A Fall 2016 Homework 6, Exercise 4. Restored
    the three source parts, the binomial-formula hint, the nilradical
    terminology, the hint for the unit perturbation, and the request for a
    noncommutative counterexample. Replaced the corrupted normal-subgroup
    notation used where the source asks for an ideal.
- event: solution-written
  by: gpt-5.6-sol
  date: 2026-09-07
- event: solution-reviewed
  by: gpt-5.6-sol
  date: 2026-09-07
  note: >-
    If x^m=y^n=0, every term in (x+y)^(m+n-1) vanishes. This gives additive
    closure of the nilpotents, while (rx)^m=0 gives absorption, so the
    nilradical is an ideal. A nilpotent perturbation of 1 has the finite
    geometric-series inverse, and factoring out an arbitrary unit handles
    u+x. In M_2(Z), E_12 and E_21 are square-zero but their sum squares to I.
---

::: {.problem}
An element $x$ of a ring $R$ is **nilpotent** if $x^n=0$ for some $n\ge1$.

(a) Let $R$ be a commutative ring and let $x,y\in R$ be nilpotent.
Prove that $x+y$ is nilpotent.
Use this to prove that
\[
\sqrt{(0)}=\{x\in R:x\text{ is nilpotent}\}
\]
is an ideal of $R$, called the **nilradical**.

Hint: the binomial formula is valid in every commutative ring.

(b) Let $R$ be commutative, let $u\in R^\times$, and let $x\in R$ be nilpotent.
Prove that $u+x$ is a unit.

Hint: first consider the case $u=-1$.

(c) Give a noncommutative ring $R$ and nilpotent elements $x,y\in R$ such that $x+y$ is not nilpotent.
:::

::: {.solution}
<1>1. If $x^m=0$ and $y^n=0$ in a commutative ring, then
\[
(x+y)^{m+n-1}=0.
\]
::: {.proof}
By the binomial theorem,
\[
(x+y)^{m+n-1}
  =\sum_{k=0}^{m+n-1}
    \binom{m+n-1}{k}x^k y^{m+n-1-k}.
\]
For every $k$, either
\[
k\ge m
\]
or
\[
m+n-1-k\ge n.
\]
Indeed, if both inequalities failed, then $k\le m-1$ and $m+n-1-k\le n-1$, whose sum would give $m+n-1\le m+n-2$.

Thus every summand contains either $x^m$ or $y^n$ as a factor and is zero.
Hence the whole power is zero, so $x+y$ is nilpotent.
:::

<1>2. The set
\[
I=\{x\in R:x\text{ is nilpotent}\}
\]
is an additive subgroup of $R$.
::: {.proof}
The element $0$ is nilpotent.
If $x,y\in I$, then $x+y\in I$ by <1>1. If $x^m=0$, then
\[
(-x)^m=(-1)^m x^m=0,
\]
so $-x\in I$.
Therefore $I$ is an additive subgroup.
:::

<1>3. The set $I$ is an ideal of $R$.
::: {.proof}
Let $r\in R$ and $x\in I$, say $x^m=0$.
Since $R$ is commutative,
\[
(rx)^m=r^m x^m=0.
\]
Thus $rx\in I$.
Together with <1>2, this proves that $I$ is an ideal.
This completes part (a).
:::

<1>4. If $z$ is nilpotent, then $1+z$ is a unit.
::: {.proof}
Choose $n\ge1$ with
\[
z^n=0.
\]
Set
\[
v=1-z+z^2-\cdots+(-1)^{n-1}z^{n-1}.
\]
The finite geometric-series identity gives
\[
(1+z)v=v(1+z)=1+(-1)^{n-1}z^n=1.
\]
Hence $1+z$ is a unit with inverse $v$.
:::

<1>5. If $u\in R^\times$ and $x$ is nilpotent, then $u+x$ is a unit.
::: {.proof}
Factor
\[
u+x=u(1+u^{-1}x).
\]
Since $R$ is commutative and $x^n=0$ for some $n$,
\[
(u^{-1}x)^n=u^{-n}x^n=0.
\]
Thus $u^{-1}x$ is nilpotent, so $1+u^{-1}x$ is a unit by <1>4. The product of two units is a unit, hence $u+x$ is a unit.
This proves part (b).
:::

<1>6. The conclusion of part (a) fails for noncommutative rings.
::: {.proof}
Take
\[
R=M_2(\mathbb Z),
\qquad
x=\begin{pmatrix}0&1\\0&0\end{pmatrix},
\qquad
y=\begin{pmatrix}0&0\\1&0\end{pmatrix}.
\]
Then
\[
x^2=y^2=0,
\]
so both $x$ and $y$ are nilpotent.
But
\[
x+y=\begin{pmatrix}0&1\\1&0\end{pmatrix}
\]
satisfies
\[
(x+y)^2=I_2.
\]
Therefore no positive power of $x+y$ is zero, so $x+y$ is not nilpotent.
This proves part (c).
:::

<1>7. Q.E.D.
::: {.proof}
Parts (a), (b), and (c) are <1>3, <1>5, and <1>6.
:::
:::
