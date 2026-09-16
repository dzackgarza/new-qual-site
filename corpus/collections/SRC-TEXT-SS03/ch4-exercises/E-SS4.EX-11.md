---
schema: qual/card@1
id: E-SS4.EX-11
kind: problem
title: "One can give a neater formulation of the result in Exercise 10 by proving the fo"
classification:
  areas:
  - complex-analysis
  topics: ['Fourier Transform', 'Poisson Summation']
relations: []
review: draft
audit:
- event: solution-written
  by: gpt-5.6-sol
  date: 2026-09-11
---

::: {.exercise}
11. One can give a neater formulation of the result in Exercise 10 by proving the following fact.

Suppose $f ( z )$ is an entire function of strict order 2, that is,

$$
f (z) = O (e ^ {c _ {1} | z | ^ {2}})
$$

for some $c _ { 1 } > 0$ . Suppose also that for x real,

$$
f (x) = O (e ^ {- c _ {2} | x | ^ {2}})
$$

for some $c _ { 2 } > 0$ . Then

$$
| f (x + i y) | = O (e ^ {- a x ^ {2} + b y ^ {2}})
$$

for some $a , b > 0$ . The converse holds: if $|f(x+iy)| = O(e^{-ax^2 + by^2})$ for some $a, b > 0$, then restricting to the real axis ($y = 0$) gives $f(x) = O(e^{-ax^2})$, which is the second hypothesis with $c_2 = a$; and the whole-plane bound $f(z) = O(e^{c_1|z|^2})$ follows with $c_1 = b$, since $-ax^2 + by^2 \le b(x^2 + y^2) = b|z|^2$.
:::

::: {.solution}
We prove the nontrivial implication. Assume
\[
|f(z)|\le C e^{c_1|z|^2}
\qquad(z\in\mathbb C)
\]
and
\[
|f(x)|\le C e^{-c_2x^2}
\qquad(x\in\mathbb R),
\]
after increasing $C$ if necessary.

It is enough first to treat the sector
\[
D=\{z=x+iy: x\ge y\ge0\}.
\]
On the ray $z=re^{i\pi/4}$ the global growth bound gives
\[
|f(re^{i\pi/4})|\le C e^{c_1r^2}.
\tag{1}
\]
On the positive real axis,
\[
|f(r)|\le C e^{-c_2r^2}.
\tag{2}
\]

We use the following elementary Phragmén--Lindelöf lemma for the sector $D$: if $h$ is holomorphic in $D$, continuous on its boundary, satisfies $|h(z)|\le e^{K|z|^2}$ in $D$, and $|h|\le M$ on both boundary rays, then $|h|\le M$ in $D$. Indeed, after rotating $D$ to $|\arg z|\le\pi/8$, for $\delta>0$ consider
\[
h_\delta(z)=h(z)e^{-\delta z^3}.
\]
Since $\cos(3\arg z)\ge \cos(3\pi/8)>0$ in the rotated sector,
\[
|h_\delta(z)|\le \exp(K|z|^2-\delta |z|^3\cos(3\pi/8)),
\]
so on a sufficiently large circular arc it is at most $M$. The maximum principle on the truncated sector yields
\[
|h(z)|\le M e^{\delta |z|^3}.
\]
Letting $\delta\downarrow0$ proves the lemma.

Fix $\delta>0$ and set
\[
H_\delta(z)=f(z)\exp\!\bigl((c_2-\delta+i(c_1+\delta))z^2\bigr).
\]
It has order at most $2$. On the positive real axis, (2) gives
\[
|H_\delta(r)|\le C e^{-\delta r^2}\le C.
\]
On the ray $z=re^{i\pi/4}$, since $z^2=ir^2$,
\[
\left|e^{(c_2-\delta+i(c_1+\delta))z^2}\right|
=e^{-(c_1+\delta)r^2},
\]
so (1) gives $|H_\delta(re^{i\pi/4})|\le C e^{-\delta r^2}\le C$. The lemma therefore implies $|H_\delta(z)|\le C$ throughout $D$.

Writing $z=x+iy$ and then letting $\delta\downarrow0$, we obtain
\[
|f(z)|\le C\left|e^{-(c_2+ic_1)z^2}\right|
=C e^{-c_2(x^2-y^2)+2c_1xy}.
\tag{3}
\]
For any $\varepsilon>0$,
\[
2c_1xy\le c_1\varepsilon x^2+c_1\varepsilon^{-1}y^2.
\]
Choose $\varepsilon<c_2/c_1$. Then (3) yields
\[
|f(x+iy)|\le C e^{-a x^2+b y^2}
\]
throughout $D$, where
\[
a=c_2-c_1\varepsilon>0,
\qquad
b=c_2+c_1\varepsilon^{-1}>0.
\tag{4}
\]

The same argument applies to the reflected sectors in the other quadrants. In the complementary region $|y|\ge |x|$, the original growth estimate already gives
\[
c_1(x^2+y^2)\le -c_1x^2+3c_1y^2,
\]
so an estimate of the form (4) holds there as well. Enlarging the constants gives a single pair $a,b>0$ valid for all $x,y\in\mathbb R$.

Conversely, if
\[
|f(x+iy)|\le C e^{-ax^2+by^2},
\]
then on the real axis $|f(x)|\le Ce^{-ax^2}$, while
\[
-ax^2+by^2\le b(x^2+y^2)=b|z|^2.
\]
Hence $f(z)=O(e^{b|z|^2})$. This proves the converse.
:::
