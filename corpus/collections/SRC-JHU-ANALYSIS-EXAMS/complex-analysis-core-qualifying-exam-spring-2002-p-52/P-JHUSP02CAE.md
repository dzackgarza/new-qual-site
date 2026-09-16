---
schema: qual/card@1
id: P-JHUSP02CAE
kind: problem
title: Negative Laurent coefficients of $1/\sin z$ on $\pi<|z|<2\pi$
classification:
  areas:
  - complex-analysis
  topics:
  - Laurent Series
relations: []
review: draft
audit:
- event: source-checked
  by: chatgpt
  date: 2026-09-10
  note: "Compared the annulus, center-zero Laurent expansion, reciprocal sine function and request for all negative-index coefficients with Spring 2002 Complex Analysis question 5."
- event: solution-written
  by: chatgpt
  date: 2026-09-10
- event: solution-reviewed
  by: chatgpt
  date: 2026-09-10
  note: "Expressed each negative Laurent coefficient as a contour integral, summed the residues at 0 and plus/minus pi, and separated the parity cases including the exceptional coefficient a_{-1}."
---

::: {.problem}
5. Let $\scriptstyle \sum _ { n = - \infty } ^ { \infty } a _ { n } z ^ { n }$ be the Laurent series expansion of $\scriptstyle { \frac { 1 } { \sin z } }$ on the annulus $\left\{ z \in \mathbb { C } : \pi < | z | < 2 \pi \right\}$ . Evaluate the coefficients $a _ { n }$ for $n < 0$
:::

::: solution
For $m\ge1$, the negative coefficients are
$$
\boxed{
a_{-1}=-1,\qquad
a_{-2k}=0\ (k\ge1),\qquad
a_{-(2k+1)}=-2\pi^{2k}\ (k\ge1).
}
$$

<1>1. A negative Laurent coefficient is a residue sum inside any circle with $\pi<r<2\pi$.
::: proof
Fix $r$ with $\pi<r<2\pi$. The Laurent coefficient formula gives, for
$m\ge1$,
$$
a_{-m}
=\frac1{2\pi i}\int_{|z|=r}
\frac{1/\sin z}{z^{-m+1}}\,dz
=\frac1{2\pi i}\int_{|z|=r}\frac{z^{m-1}}{\sin z}\,dz.
$$
The zeros of sine are exactly the integer multiples of $\pi$, and they are
simple because $\cos(k\pi)=(-1)^k\ne0$. Inside $|z|<r$ the only such points
are $0,\pi,-\pi$. Therefore the residue theorem expresses $a_{-m}$ as the
sum of the residues of $z^{m-1}/\sin z$ at those three points.
:::

<1>2. The residues at $\pm\pi$ give the parity pattern.
::: proof
At $z=k\pi$, the residue of $1/\sin z$ is
$$
\frac1{\cos(k\pi)}=(-1)^k.
$$
Thus at both $\pi$ and $-\pi$ the residue is $-1$, and hence
$$
\operatorname{Res}_{\pi}\frac{z^{m-1}}{\sin z}
+\operatorname{Res}_{-\pi}\frac{z^{m-1}}{\sin z}
=-\pi^{m-1}-(-\pi)^{m-1}.
$$
If $m$ is even, then $m-1$ is odd and this sum is zero. If $m$ is odd, it is
$-2\pi^{m-1}$.
:::

<1>3. The origin contributes only when $m=1$.
::: proof
Near zero,
$$
\sin z=z+O(z^3),
\qquad
\frac{z^{m-1}}{\sin z}=z^{m-2}(1+O(z^2)).
$$
For $m=1$ this has residue $1$. For every $m\ge2$ it is holomorphic at zero,
so its residue there is zero.

Combining this with step <1>2 gives
$$
a_{-1}=1-1-1=-1.
$$
For even $m\ge2$, $a_{-m}=0$, while for odd $m\ge3$,
$a_{-m}=-2\pi^{m-1}$. Writing $m=2k$ or $m=2k+1$ gives exactly the displayed
formulas.
:::
:::
