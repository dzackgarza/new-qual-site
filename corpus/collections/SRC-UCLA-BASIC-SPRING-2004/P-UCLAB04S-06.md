---
schema: qual/card@1
id: P-UCLAB04S-06
kind: problem
title: Equivalence of norms and closedness of finite-dimensional subspaces
classification:
  areas: [prelim]
  topics: []
relations: []
review: draft
audit:
- event: source-checked
  by: gpt-5.6-sol
  date: 2026-09-14
  note: Checked against Problem 6 of the official UCLA Basic Exam Spring 2004 PDF. In part (b), the source writes merely "there exists a constant c"; the accompanying sphere-minimum hint makes the intended positive constant explicit.
---

::: {.problem}
Let $\|\cdot\|$ be any norm on $\RR^n$, and let $\|\cdot\|_2$ be the Euclidean norm.

(a) Prove that there exists $d>0$ such that
\[
\|x\|\leq d\|x\|_2
\]
for every $x\in\RR^n$, and use this to show that $N(x)=\|x\|$ is continuous in the usual topology on $\RR^n$.

(b) Prove that there exists $c>0$ such that
\[
\|x\|\geq c\|x\|_2
\]
for every $x\in\RR^n$.

Hint: use continuity of $N$ on the sphere $\{x:\|x\|_2=1\}$.

(c) Show that if $L$ is an $n$-dimensional subspace of an arbitrary normed vector space $V$, then $L$ is closed.
:::

::: {.solution}

Let
\[
e_1,\ldots,e_n
\]
be the standard basis of $\RR^n$.

::: pf

::: {.pf-step #s1-1}

For every
\[
x=(x_1,\ldots,x_n)\in\RR^n,
\]
one has
\[
\|x\|
\le
\sum_{j=1}^n|x_j|\,\|e_j\|.
\]


::: pf-proof

Write
\[
x=\sum_{j=1}^n x_je_j.
\]
Repeated use of the triangle inequality and absolute homogeneity gives
\[
\left\|
\sum_{j=1}^n x_je_j
\right\|
\le
\sum_{j=1}^n
\|x_je_j\|
=
\sum_{j=1}^n
|x_j|\,\|e_j\|.
\]

:::

:::

::: {.pf-step #s1-2}

There exists
\[
d>0
\]
such that
\[
\boxed{
\|x\|\le d\|x\|_2
}
\]
for every $x\in\RR^n$.


::: pf-proof

By Cauchy--Schwarz,
\[
\sum_{j=1}^n
|x_j|\,\|e_j\|
\le
\left(
\sum_{j=1}^n x_j^2
\right)^{1/2}
\left(
\sum_{j=1}^n\|e_j\|^2
\right)^{1/2}.
\]
Set
\[
d
=
\left(
\sum_{j=1}^n\|e_j\|^2
\right)^{1/2}.
\]
Then step [](#s1-1){.pf-ref} gives
\[
\|x\|
\le
d\|x\|_2.
\]
Because every basis vector is nonzero, $d>0$.

:::

:::

::: {.pf-step #s1-3}

The norm function
\[
N(x)=\|x\|
\]
is continuous in the Euclidean topology.


::: pf-proof

The reverse triangle inequality gives
\[
\bigl|\|x\|-\|y\|\bigr|
\le
\|x-y\|.
\]
By step [](#s1-2){.pf-ref},
\[
\|x-y\|
\le
d\|x-y\|_2.
\]
Hence
\[
|N(x)-N(y)|
\le
d\|x-y\|_2.
\]
Thus $N$ is Lipschitz with respect to the Euclidean norm, hence continuous.

:::

:::

::: {.pf-step #s1-4}

Let
\[
S^{n-1}
=
\{x\in\RR^n:\|x\|_2=1\}.
\]
Then there exists
\[
c>0
\]
such that
\[
\|u\|\ge c
\]
for every $u\in S^{n-1}$.


::: pf-proof

The Euclidean unit sphere is compact.
By step [](#s1-3){.pf-ref}, $N$ is continuous, so it attains a minimum
\[
c=\min_{u\in S^{n-1}}\|u\|.
\]
Since every $u\in S^{n-1}$ is nonzero and a norm is positive on nonzero vectors,
\[
\|u\|>0
\]
for every $u$ on the sphere.
Therefore the attained minimum satisfies
\[
c>0.
\]

:::

:::

::: {.pf-step #s1-5}

For every $x\in\RR^n$,
\[
\boxed{
\|x\|\ge c\|x\|_2
}.
\]


::: pf-proof

If $x=0$, the inequality is equality.
If $x\ne0$, set
\[
u=\frac{x}{\|x\|_2}.
\]
Then
\[
\|u\|_2=1,
\]
so step [](#s1-4){.pf-ref} gives
\[
\|u\|\ge c.
\]
By homogeneity,
\[
\|x\|
=
\|x\|_2\|u\|
\ge
c\|x\|_2.
\]

:::

:::

::: {.pf-step #s1-6}

Let $L$ be an $n$-dimensional subspace of an arbitrary normed vector space
\[
(V,\|\cdot\|_V),
\]
and choose a basis
\[
v_1,\ldots,v_n
\]
of $L$.
Define
\[
\Phi:\RR^n\to L
\]
by
\[
\Phi(a_1,\ldots,a_n)
=
\sum_{j=1}^n a_jv_j.
\]
Then there exists
\[
c_L>0
\]
such that
\[
\|\Phi(a)\|_V
\ge
c_L\|a\|_2
\]
for every $a\in\RR^n$.


::: pf-proof

Define a norm on $\RR^n$ by
\[
\|a\|_L
=
\|\Phi(a)\|_V.
\]
Because $v_1,\ldots,v_n$ is a basis, $\Phi$ is injective, so
\[
\|a\|_L=0
\]
only when $a=0$.
Thus $\|\cdot\|_L$ is a norm.
Apply part (b), proved in step [](#s1-5){.pf-ref}, to this norm.

:::

:::

::: {.pf-step #s1-7}

Let
\[
(x_k)
\]
be a sequence in $L$ converging in $V$ to some
\[
x\in V.
\]
Write
\[
x_k=\Phi(a^{(k)}).
\]
Then
\[
\bigl(a^{(k)}\bigr)
\]
is a Cauchy sequence in $\RR^n$.


::: pf-proof

Since $x_k\to x$ in $V$, the sequence $(x_k)$ is Cauchy.
By step [](#s1-6){.pf-ref},
\[
\begin{aligned}
c_L
\|a^{(k)}-a^{(\ell)}\|_2
&\le
\|\Phi(a^{(k)}-a^{(\ell)})\|_V\\
&=
\|x_k-x_\ell\|_V.
\end{aligned}
\]
The right side tends to zero as $k,\ell\to\infty$.
Hence the coordinate sequence is Cauchy in Euclidean space.

:::

:::

::: {.pf-step #s1-8}

There exists
\[
a\in\RR^n
\]
such that
\[
a^{(k)}\to a,
\]
and
\[
x=\Phi(a)\in L.
\]


::: pf-proof

Euclidean space is complete, so step [](#s1-7){.pf-ref} gives
\[
a^{(k)}\to a
\]
for some $a\in\RR^n$.

The map $\Phi$ is continuous because
\[
\|\Phi(b)\|_V
\le
\sum_{j=1}^n|b_j|\|v_j\|_V
\le
C\|b\|_2
\]
for some constant $C$.
Therefore
\[
x_k
=
\Phi(a^{(k)})
\to
\Phi(a).
\]
But also
\[
x_k\to x
\]
in the normed space $V$.
Limits are unique, so
\[
x=\Phi(a)\in L.
\]

:::

:::

::: {.pf-step #s1-9}

Therefore every finite-dimensional subspace of a normed vector space is closed.


::: pf-proof

Step [](#s1-8){.pf-ref} shows that every convergent sequence in $L$ whose limit lies in $V$ has its limit still in $L$.
Since normed spaces are metric spaces, sequential closedness is equivalent to closedness.
Hence
\[
\boxed{L\text{ is closed in }V}.
\]

:::

:::

::: pf-qed

Steps [](#s1-1){.pf-ref} through [](#s1-3){.pf-ref} prove part (a), steps [](#s1-4){.pf-ref} through [](#s1-5){.pf-ref} prove part (b), and steps [](#s1-6){.pf-ref} through [](#s1-9){.pf-ref} prove part (c).

:::

:::

:::
