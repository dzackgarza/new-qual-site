---
schema: qual/card@1
id: P-TOPOLOGY-PHD-F95-07
kind: problem
title: Invariance of dimension for R, R^2, and R^3
classification:
  areas:
  - topology
  topics:
  - Homeomorphisms
  - Euclidean Spaces
  - Fundamental Group
relations: []
review: draft
audit:
- event: source-checked
  by: gpt-5.6-sol
  date: 2026-09-06
  note: Checked both parts against Section II, problem 2 of the 23 September 1995 topology qualifying exam.
- event: solution-written
  by: gpt-5.6-sol
  date: 2026-09-06
- event: solution-reviewed
  by: gpt-5.6-sol
  date: 2026-09-06
  note: >-
    Punctured the spaces. Connectedness distinguishes dimensions one and two;
    radial deformation retractions and fundamental groups distinguish
    dimensions two and three.
---

::: {.problem}
Prove by any method you know that:

(a) $\mathbb R$ is not homeomorphic to $\mathbb R^2$.

(b) $\mathbb R^2$ is not homeomorphic to $\mathbb R^3$.
:::

::: {.solution}
<1>1. If $h:X\to Y$ is a homeomorphism and $x\in X$, then
\[
h|_{X\setminus\{x\}}:X\setminus\{x\}\longrightarrow Y\setminus\{h(x)\}
\]
is a homeomorphism.
::: {.proof}
The restriction is bijective because $h$ is bijective, and its inverse is the restriction of $h^{-1}$ to $Y\setminus\{h(x)\}$.
Both restrictions are continuous.
:::

<1>2. The punctured line is disconnected, whereas the punctured plane is path connected.
::: {.proof}
For any $a\in\RR$,
\[
\RR\setminus\{a\}=(-\infty,a)\sqcup(a,\infty),
\]
a separation into two nonempty open subsets.
Hence $\RR\setminus\{a\}$ is disconnected.

For any $b\in\RR^2$, translation by $-b$ identifies $\RR^2\setminus\{b\}$ with $\RR^2\setminus\{0\}$.
The latter is path connected: if $x,y\ne0$, move radially from $x$ to $x/\|x\|$, follow an arc of the unit circle from $x/\|x\|$ to $y/\|y\|$, and then move radially to $y$.
All three pieces avoid the origin, so their concatenation is a path in $\RR^2\setminus\{0\}$ from $x$ to $y$.
:::

<1>3. Therefore $\RR$ is not homeomorphic to $\RR^2$.
::: {.proof}
Suppose $h:\RR\to\RR^2$ were a homeomorphism and choose $a\in\RR$.
By <1>1,
\[
\RR\setminus\{a\}\cong\RR^2\setminus\{h(a)\}.
\]
The left side is disconnected by <1>2, while the right side is path connected and hence connected.
Connectedness is preserved by homeomorphisms, a contradiction.
:::

<1>4. For $n\ge2$, the punctured Euclidean space $\RR^n\setminus\{0\}$ strongly deformation retracts onto $S^{n-1}$.
::: {.proof}
Define
\[
H:(\RR^n\setminus\{0\})\times[0,1]\longrightarrow\RR^n\setminus\{0\}
\]
by
\[
H(x,t)=\left((1-t)+\frac{t}{\|x\|}\right)x.
\]
The scalar multiplying $x$ is positive, so $H(x,t)\ne0$.
Moreover,
\[
H(x,0)=x,
\qquad
H(x,1)=\frac{x}{\|x\|}\in S^{n-1}.
\]
If $x\in S^{n-1}$, then $\|x\|=1$ and
\[
H(x,t)=x
\]
for all $t$.
Thus $H$ is a strong deformation retraction onto $S^{n-1}$.
:::

<1>5. The punctured plane has fundamental group $\ZZ$, while punctured three-space has trivial fundamental group.
::: {.proof}
By <1>4 and invariance of the fundamental group under strong deformation retraction,
\[
\pi_1(\RR^2\setminus\{0\})\cong\pi_1(S^1)\cong\ZZ
\]
and
\[
\pi_1(\RR^3\setminus\{0\})\cong\pi_1(S^2)=0.
\]
Here $\pi_1(S^1)\cong\ZZ$ is the standard computation from the universal covering map $\RR\to S^1$, $t\mapsto e^{2\pi i t}$.
Also $\pi_1(S^2)=0$ follows, for example, from Seifert--van Kampen applied to the cover of $S^2$ by the complements of the north and south poles: both members are homeomorphic to $\RR^2$ and hence simply connected, so their union has trivial fundamental group.
:::

<1>6. Therefore $\RR^2$ is not homeomorphic to $\RR^3$.
::: {.proof}
Suppose $h:\RR^2\to\RR^3$ were a homeomorphism and choose $a\in\RR^2$.
By <1>1,
\[
\RR^2\setminus\{a\}\cong\RR^3\setminus\{h(a)\}.
\]
Translations identify these spaces with $\RR^2\setminus\{0\}$ and $\RR^3\setminus\{0\}$, respectively.
Thus a homeomorphism would induce an isomorphism of fundamental groups.
But by <1>5 these groups are
\[
\ZZ
\quad\text{and}\quad
0,
\]
which are not isomorphic.
This contradiction proves
\[
\boxed{\RR^2\not\cong\RR^3}.
\]
:::
:::
