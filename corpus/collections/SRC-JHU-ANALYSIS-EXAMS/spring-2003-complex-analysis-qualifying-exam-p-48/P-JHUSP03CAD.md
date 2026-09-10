---
schema: qual/card@1
id: P-JHUSP03CAD
kind: problem
title: Rouché's theorem, segment estimates, and a univalence criterion
classification:
  areas:
  - complex-analysis
  topics:
  - Rouché
relations: []
review: draft
audit:
- event: source-checked
  by: chatgpt
  date: 2026-09-10
  note: "Compared all three parts, including the coefficient condition sum n|a_n| <= 1, with Spring 2003 problem 4 in the retained source."
- event: solution-written
  by: chatgpt
  date: 2026-09-10
- event: solution-reviewed
  by: chatgpt
  date: 2026-09-10
  note: "Stated Rouche with its contour hypotheses, derived the convex-segment estimate by integrating phi', and obtained strict contraction for the nonlinear tail on each segment in the open disk."
---

(a) State Rouche's Theorem.

(b) Let $\varphi : \Omega \to \mathbb{C}$ be holomorphic on an open convex set $\Omega$.
Show that for $z, w \in \Omega$

$$|\varphi(z) - \varphi(w)| \leq \max_{\xi \in L} |\varphi'(\xi)| \cdot |z - w|,$$

where $L$ is the straight line segment from $z$ to $w$.

(c) Use the above to prove the following: suppose

$$f(z) = z + \sum_{n=2}^\infty a_n z^n$$

where

$$\sum_{n=2}^\infty n|a_n| \leq 1.$$

Show that $f(z)$ is a 1-1 holomorphic function on $\Delta$.


::: solution
<1>1. Part (a): Rouché's theorem.
::: proof
Let $C$ be a positively oriented simple closed contour and suppose $F,G$ are
holomorphic on an open set containing $C$ and its interior. If
$$
|G(z)|<|F(z)|\qquad(z\in C),
$$
then $F$ and $F+G$ have the same number of zeros inside $C$, counted with
multiplicity.

Indeed, $F$ has no zero on $C$, and for $0\le t\le1$ the functions
$F+tG$ also have no zero on $C$, since $|tG|<|F|$. Therefore the integer
$$
\frac1{2\pi i}\int_C\frac{F'(z)+tG'(z)}{F(z)+tG(z)}\,dz
$$
is constant in $t$ by continuity and the argument principle. Its values at
$t=0$ and $t=1$ are the zero counts of $F$ and $F+G$.
:::

<1>2. Part (b): integrate $\varphi'$ along the line segment.
::: proof
Because $\Omega$ is convex, the segment
$$
L=\{w+t(z-w):0\le t\le1\}
$$
lies in $\Omega$. The fundamental theorem of calculus applied to
$t\mapsto\varphi(w+t(z-w))$ gives
$$
\varphi(z)-\varphi(w)
=(z-w)\int_0^1\varphi'(w+t(z-w))\,dt.
$$
Hence
$$
|\varphi(z)-\varphi(w)|
\le |z-w|\int_0^1|\varphi'(w+t(z-w))|\,dt
\le |z-w|\max_{\xi\in L}|\varphi'(\xi)|.
$$
The maximum exists because $L$ is compact and $\varphi'$ is continuous.
:::

<1>3. Part (c): the nonlinear tail is a strict contraction on every segment in $\Delta$.
::: proof
Write
$$
h(z)=f(z)-z=\sum_{n=2}^\infty a_nz^n.
$$
The coefficient hypothesis implies uniform convergence of the differentiated
series on every closed disk of radius $r<1$, since
$$
\sum_{n=2}^\infty n|a_n|r^{n-1}\le\sum_{n=2}^\infty n|a_n|<\infty.
$$
Thus
$$
h'(z)=\sum_{n=2}^\infty n a_nz^{n-1}.
$$
Take distinct $z,w\in\Delta$ and let $L$ be their segment. Compactness of $L$
and openness of the disk give
$$
r:=\max_{\xi\in L}|\xi|<1.
$$
If every $a_n=0$, then $f(z)=z$ and injectivity is immediate. Otherwise,
for every $\xi\in L$,
$$
|h'(\xi)|
\le\sum_{n=2}^\infty n|a_n|r^{n-1}
<\sum_{n=2}^\infty n|a_n|
\le1,
$$
because $r^{n-1}<1$ for every $n\ge2$ and at least one coefficient is nonzero.
Applying part (b) to $h$ on the convex disk gives
$$
|h(z)-h(w)|<|z-w|.
$$
Therefore
$$
|f(z)-f(w)|
=|(z-w)+(h(z)-h(w))|
\ge |z-w|-|h(z)-h(w)|>0.
$$
Hence $f(z)\ne f(w)$ whenever $z\ne w$, so $f$ is one-to-one on $\Delta$.
:::
:::
