---
schema: qual/card@1
id: P-NORI-GT-3-05
kind: problem
title: Towers of cubic extensions of $\FF_{19}$
classification:
  areas: [algebra]
  topics: []
relations: []
review: draft
audit:
- event: source-checked
  by: gpt-5.6-sol
  date: 2026-09-12
  note: Checked against problem 3.5 of the retained Nori Galois Theory Problems PDF.
---

::: {.problem}
Explain how you would obtain a sequence of field extensions $E _ { n + 1 } / E _ { n }$ of degree three, with $E _ { 0 } = \FF _ { 1 9 }$
:::

::: {.solution}

The construction is the cubic analogue of the preceding square-root towers.

::: pf

::: pf-step

Since
\[
19-1=18
\]
is divisible by $3$, the field $\FF_{19}$ contains all cube roots of unity.


::: pf-proof

The cyclic group $\FF_{19}^\times$ has order $18$. Hence it contains an element of order $3$, so $X^3-1$ splits completely over $\FF_{19}$.

:::

:::

::: {.pf-step #s1-2}

Choose an element
\[
u_0\in\FF_{19}^\times
\]
that is not a cube.


::: pf-proof

The cube map on the cyclic group $\FF_{19}^\times$ has image of order
\[
18/\gcd(18,3)=6,
\]
so its image is a proper subgroup. Thus noncubes exist.

:::

:::

::: pf-step

Recursively, after $(E_n,u_n)$ is defined, choose $u_{n+1}$ with
\[
u_{n+1}^3=u_n
\]
and set
\[
E_{n+1}=E_n(u_{n+1}).
\]


::: pf-proof

This defines a field extension in an algebraic closure. It remains to show inductively that $u_n$ is never a cube in $E_n$, so that each polynomial $X^3-u_n$ is irreducible.

:::

:::

::: {.pf-step #s1-4}

If $u_n$ is not a cube in $E_n$ and $E_n$ contains the cube roots of unity, then
\[
X^3-u_n
\]
is irreducible over $E_n$.


::: pf-proof

A reducible cubic polynomial over a field has a root in that field. A root of $X^3-u_n$ would be an element whose cube is $u_n$, contrary to the assumption that $u_n$ is not a cube.

:::

:::

::: {.pf-step #s1-5}

Hence, as long as $u_n$ is a noncube,
\[
[E_{n+1}:E_n]=3
\]
and
\[
E_{n+1}\cong\FF_{19^{3^{n+1}}}.
\]


::: pf-proof

Step [](#s1-4){.pf-ref} gives irreducibility of the degree-three polynomial defining $u_{n+1}$. Inductively $[E_n:\FF_{19}]=3^n$, so $E_n$ has $19^{3^n}$ elements. A degree-three extension therefore has $19^{3^{n+1}}$ elements and is the unique finite field of that order.

:::

:::

::: {.pf-step #s1-6}

For every $n\ge0$,
\[
u_n^{3^n}=u_0.
\]


::: pf-proof

Iterate the defining relations $u_{j+1}^3=u_j$.

:::

:::

::: {.pf-step #s1-7}

Let
\[
Q_n=19^{3^n}.
\]
Then
\[
v_3(Q_n-1)=n+2.
\]


::: pf-proof

Since $19\equiv1\pmod3$, the lifting-the-exponent formula gives
\[
v_3(19^{3^n}-1)
=v_3(19-1)+v_3(3^n)
=2+n,
\]
because $19-1=18$ has $3$-adic valuation $2$.

:::

:::

::: {.pf-step #s1-8}

In a finite field $K=\FF_Q$ with $3\mid Q-1$, an element $a\in K^\times$ is a cube if and only if
\[
a^{(Q-1)/3}=1.
\]


::: pf-proof

The cyclic group $K^\times$ has order $Q-1$. Its subgroup of cubes has index $3$, hence order $(Q-1)/3$, and is exactly the kernel of the character $a\mapsto a^{(Q-1)/3}$ into the cube roots of unity.

:::

:::

::: {.pf-step #s1-9}

Since $u_0$ is a noncube in $\FF_{19}$,
\[
u_0^6\ne1.
\]


::: pf-proof

Here $(19-1)/3=6$. Apply step [](#s1-8){.pf-ref} with $Q=19$.

:::

:::

::: {.pf-step #s1-10}

Assume the construction has reached $E_n$. Then
\[
u_n^{(Q_n-1)/3}
=\left(u_0^6\right)^{M_n}
\]
for some integer $M_n$ not divisible by $3$.


::: pf-proof

By steps [](#s1-6){.pf-ref} through [](#s1-7){.pf-ref},
\[
\frac{Q_n-1}{3^{n+1}}
\]
is an integer with $3$-adic valuation $1$, the same as $6$. Thus
\[
\frac{Q_n-1}{3^{n+1}}=6M_n
\]
with $3\nmid M_n$. Since $u_n^{3^n}=u_0$,
\[
u_n^{(Q_n-1)/3}
=u_0^{(Q_n-1)/3^{n+1}}
=(u_0^6)^{M_n}.
\]

:::

:::

::: {.pf-step #s1-11}

The value in step [](#s1-10){.pf-ref} is not $1$, so $u_n$ is not a cube in $E_n$.


::: pf-proof

The element $u_0^6$ is a nontrivial cube root of unity: its cube is $u_0^{18}=1$, while step [](#s1-9){.pf-ref} says it is not $1$. Raising a nontrivial element of order $3$ to an exponent $M_n$ not divisible by $3$ remains nontrivial. Thus step [](#s1-10){.pf-ref} is not $1$, and step [](#s1-8){.pf-ref} shows $u_n$ is a noncube.

:::

:::

::: {.pf-step #s1-12}

Therefore the recursion continues indefinitely and satisfies
\[
\boxed{[E_{n+1}:E_n]=3\quad\text{for every }n\ge0.}
\]


::: pf-proof

Step [](#s1-2){.pf-ref} starts with a noncube. Steps [](#s1-5){.pf-ref} and [](#s1-11){.pf-ref} show inductively that adjoining a cube root gives a degree-three extension and that the new chosen cube root remains a noncube at the next stage.

:::

:::

::: pf-qed

Step [](#s1-12){.pf-ref} gives the requested sequence of cubic field extensions beginning at $E_0=\FF_{19}$.

:::

:::

:::
