---
schema: qual/card@1
id: E-IIK8L
kind: problem
title: Closures in the ordered square
classification:
  areas:
  - topology
  topics:
  - Closure
  - Order Topology
relations: []
review: draft
audit:
- event: solution-written
  by: Gemini 3.7 Flash
  date: 2026-08-30
---

::: {.exercise}
Determine the **closures** of the following subsets of the **ordered square** $I_o^2 = [0, 1] \times [0, 1]$ equipped with the dictionary order topology:

$$
A = \left\{ \frac{1}{n} \times 0 \;\middle|\; n \in \mathbb{Z}_+ \right\},
$$

$$
B = \left\{ \left(1 - \frac{1}{n}\right) \times \frac{1}{2} \;\middle|\; n \in \mathbb{Z}_+ \right\},
$$

$$
C = \{ x \times 0 \mid 0 < x < 1 \},
$$

$$
D = \left\{ x \times \frac{1}{2} \;\middle|\; 0 < x < 1 \right\},
$$

$$
E = \left\{ \frac{1}{2} \times y \;\middle|\; 0 < y < 1 \right\}.
$$
:::

::: {.solution}
Write $(x,y)$ for $x\times y$.
The basis of the order topology on $I_o^2$ consists of the open intervals $(p,q)$, the intervals $[(0,0),q)$, and the intervals $(p,(1,1)]$.
Each closure below is found by showing that the listed added points are limit points and that the complement of the listed set is a union of basis elements.

<1>1. For $0<x\le1$, every neighborhood of $(x,0)$ contains $(a,x)\times[0,1]$ for some $a<x$; for $0\le x<1$, every neighborhood of $(x,1)$ contains $(x,c)\times[0,1]$ for some $c>x$.

::: {.proof}
A basis element containing $(x,0)$ with $x>0$ either is $[(0,0),q)$ with $q>(x,0)$, which contains $[0,x)\times[0,1]$, or has a lower endpoint $(a,b)<(x,0)$.
In the second case $a<x$, because no point has second coordinate below $0$, and the element contains every point with first coordinate in $(a,x)$.
The statement for $(x,1)$ follows in the same way from the upper endpoints, since no point has second coordinate above $1$.
:::

<1>2. $\overline A=\boxed{A\cup\{(0,1)\}}$.

::: {.proof}
By step <1>1, every neighborhood of $(0,1)$ contains $(1/n,0)$ for all large $n$.
The complement of $A\cup\{(0,1)\}$ is
$$
[(0,0),(0,1))\;\cup\;\bigcup_{n\ge1}\bigl((\tfrac1{n+1},0),(\tfrac1n,0)\bigr)\;\cup\;((1,0),(1,1)],
$$
a union of basis elements.
:::

<1>3. $\overline B=\boxed{B\cup\{(1,0)\}}$.

::: {.proof}
By step <1>1, every neighborhood of $(1,0)$ contains $(1-\frac1n,\frac12)$ for all large $n$.
The complement of $B\cup\{(1,0)\}$ is
$$
[(0,0),(0,\tfrac12))\;\cup\;\bigcup_{n\ge1}\bigl((1-\tfrac1n,\tfrac12),(1-\tfrac1{n+1},\tfrac12)\bigr)\;\cup\;((1,0),(1,1)],
$$
a union of basis elements.
:::

<1>4. $\overline C=\boxed{((0,1]\times\{0\})\cup([0,1)\times\{1\})}$.

::: {.proof}
By step <1>1, every neighborhood of $(1,0)$, and of $(x,1)$ for $0\le x<1$, contains points $(t,0)$ with $0<t<1$.
The complement of the listed set is
$$
[(0,0),(0,1))\;\cup\;\bigcup_{0<x<1}((x,0),(x,1))\;\cup\;((1,0),(1,1)],
$$
a union of basis elements.
:::

<1>5. $\overline D=\boxed{D\cup((0,1]\times\{0\})\cup([0,1)\times\{1\})}$.

::: {.proof}
By step <1>1, every neighborhood of $(x,0)$ for $0<x\le1$, and of $(x,1)$ for $0\le x<1$, contains points $(t,\frac12)$ with $0<t<1$.
The complement of the listed set is
$$
[(0,0),(0,1))\;\cup\;\bigcup_{0<x<1}\Bigl(((x,0),(x,\tfrac12))\cup((x,\tfrac12),(x,1))\Bigr)\;\cup\;((1,0),(1,1)],
$$
a union of basis elements.
:::

<1>6. $\overline E=\boxed{\{\frac12\}\times[0,1]}$.

::: {.proof}
A basis element containing $(\frac12,0)$ contains $\{\frac12\}\times[0,d)$ for some $d>0$, hence points of $E$; likewise a basis element containing $(\frac12,1)$ contains $\{\frac12\}\times(b,1]$ for some $b<1$.
The complement of $\{\frac12\}\times[0,1]$ is $[(0,0),(\frac12,0))\cup((\frac12,1),(1,1)]$.
:::

<1>7. Q.E.D.

::: {.proof}
Steps <1>2 through <1>6 give the five closures.
:::
:::
