---
schema: qual/card@1
id: P-JHUFA01CAE
kind: problem
title: Growth bound for a disk map into a vertical strip
classification:
  areas:
  - complex-analysis
  topics:
  - Schwarz Lemma
relations: []
review: draft
audit:
- event: source-checked
  by: chatgpt
  date: 2026-09-10
  note: "Compared the normalization g(0)=0, strict vertical-strip bound, and logarithmic radial estimate with Fall 2001 Complex Analysis problem 5 and its reference to problem 4."
- event: solution-written
  by: chatgpt
  date: 2026-09-10
- event: solution-reviewed
  by: chatgpt
  date: 2026-09-10
  note: "Constructed an explicit biholomorphism from the disk to the vertical strip, applied the preceding subordination result through Schwarz's lemma, and bounded its power series sharply on each smaller disk."
- event: source-checked
  by: chatgpt
  date: 2026-09-10
  note: "Visually compared problems 4 and 5 and the disk convention on PDF page 55; stated the referenced subordination result locally."
- event: solution-reviewed
  by: chatgpt
  date: 2026-09-10
  note: "Corrected the step heading and used the closed radius-|z| disk, including radius zero; checked the logarithm branch and exact radial power-series bound."
---

Let $D_r(0)=\{z\in\mathbb C:|z|<r\}$ and $\Delta=D_1(0)$.
Use the following subordination result: if $F:\Delta\to\mathbb C$
is injective and holomorphic, and $g:\Delta\to F(\Delta)$
is holomorphic with $g(0)=F(0)$, then
$g(D_r(0))\subset F(D_r(0))$ for $0\leq r<1$.
Prove that if $g$ is holomorphic on $\Delta$, $g(0)=0$
and $|\operatorname{Re}g(z)|<1$ for every $z\in\Delta$, then

$$
| g ( z ) | \leq { \frac { 2 } { \pi } } \log \left\{ { \frac { 1 + | z | } { 1 - | z | } } \right\}
$$

for all $z \in D _ { 1 } ( 0 )$


::: solution
Let
$$
S=\{w\in\mathbb C:|\operatorname{Re}w|<1\}.
$$

<1>1. The function
$$
F(\zeta)=\frac{2i}{\pi}\log\frac{1+\zeta}{1-\zeta}
$$
is a biholomorphism from the unit disk onto $S$ and satisfies $F(0)=0$.
::: proof
The Möbius map
$$
M(\zeta)=\frac{1+\zeta}{1-\zeta}
$$
maps the unit disk biholomorphically onto the right half-plane. On that
half-plane take the logarithm with argument in $(-\pi/2,\pi/2)$. Its image is
the horizontal strip
$$
\{u+iv:|v|<\pi/2\}.
$$
Multiplication by $2i/\pi$ maps that strip biholomorphically onto
$S$, because
$$
\operatorname{Re}\left(\frac{2i}{\pi}(u+iv)\right)=-\frac{2v}{\pi}.
$$
The composition is the displayed $F$, and $F(0)=0$.
:::

<1>2. Pointwise subordination uses the closed disk of radius $|z|$.
::: proof
The hypothesis $|\operatorname{Re}g(z)|<1$ says exactly that
$g:\Delta\to S=F(\Delta)$, and $g(0)=F(0)$. Equivalently,
$$
h=F^{-1}\circ g:\Delta\to\Delta
$$
is holomorphic with $h(0)=0$. Schwarz's lemma [@SS03] gives
$$
|h(z)|\le|z|.
$$
Thus, for $r=|z|$, put $K_r=\{\zeta\in\mathbb C:|\zeta|\leq r\}$.
Then $h(z)\in K_r$ and
$$
g(z)=F(h(z))\in F(K_r).
$$
This includes $r=0$, where $K_0=\{0\}$ and $g(0)=0$.
The open-disk subordination statement above follows
from the same estimate whenever $|z|<r$; the pointwise
estimate at $r=|z|$ needs the closed disk instead.
:::

<1>3. The explicit strip map has the required radial bound.
::: proof
For $|\zeta|<1$,
$$
\log\frac{1+\zeta}{1-\zeta}
=2\sum_{n=0}^{\infty}\frac{\zeta^{2n+1}}{2n+1}.
$$
Hence for $|\zeta|\le r<1$,
$$
\begin{aligned}
|F(\zeta)|
&\le \frac4\pi\sum_{n=0}^{\infty}\frac{r^{2n+1}}{2n+1}\\
&=\frac4\pi\operatorname{arctanh}r
=\frac2\pi\log\frac{1+r}{1-r}.
\end{aligned}
$$
Apply this with $\zeta=h(z)$ and $r=|z|$ from step <1>2. Then
$$
|g(z)|=|F(h(z))|
\le\frac2\pi\log\frac{1+|z|}{1-|z|},
$$
which is the required estimate.
:::
:::
