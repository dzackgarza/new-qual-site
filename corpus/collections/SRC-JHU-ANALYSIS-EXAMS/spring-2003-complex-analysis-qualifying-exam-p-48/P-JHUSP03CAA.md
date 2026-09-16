---
schema: qual/card@1
id: P-JHUSP03CAA
kind: problem
title: Meromorphic functions on the sphere and rational boundary-modulus extensions
classification:
  areas:
  - complex-analysis
  topics:
  - Meromorphic Functions
relations: []
review: draft
audit:
- event: source-checked
  by: chatgpt
  date: 2026-09-10
  note: "Compared both parts with Spring 2003 Complex Analysis problem 1, including the pole-at-infinity hypothesis and the unit-circle boundary modulus condition."
- event: solution-written
  by: chatgpt
  date: 2026-09-10
- event: solution-reviewed
  by: chatgpt
  date: 2026-09-10
  note: "Proved rationality from finitely many principal parts and polynomial growth at infinity, then glued the reciprocal-reflection across the unit circle by Morera and applied the sphere result."
- event: source-checked
  by: chatgpt
  date: 2026-09-10
  note: "Visually read PDF page 48 and both complete cards. P-JHUSP03CAE repeats exactly problem 1(a); its finite-principal-parts proof is retained here with the complete two-part source item."
- event: solution-reviewed
  by: chatgpt
  date: 2026-09-10
  note: "Gave the explicit polynomial and principal parts, proved a nonvanishing collar at the unit circle, and replaced implicit curved-boundary gluing by a local fractional coordinate and a uniform translated-boundary estimate."
---

::: {.problem}
Let $\Delta=\{z\in\mathbb C:|z|<1\}$.

(a) Let $f : \mathbb{C} \to \mathbb{C}$ be meromorphic with a pole at infinity.
Show that $f$ must be a rational function.

(b) Use the above to prove the following: if $f : \Delta \to \mathbb{C}$ is holomorphic with a continuous extension to the boundary of $\Delta$ such that $|f(z)| = 1$ for all $|z| = 1$, then $f(z)$ is the restriction of a rational function.
:::

::: solution
<1>1. A meromorphic function on the sphere is rational; in particular, part (a) holds.
::: proof
Suppose $f$ is meromorphic on $\mathbb C$ and has either
a pole or a removable singularity at infinity. Then it
has no finite pole for $|z|>R$, for some $R>0$. Its
finite poles form a locally finite set: the local
meromorphic factorization at any point gives a neighborhood
with at most one pole. Compactness of $|z|\leq R$ therefore
makes the list of poles finite, say $a_1,\ldots,a_m$.

Let the principal part at $a_j$ be
$$
S_j(z)=\sum_{\ell=1}^{d_j}\frac{c_{j,\ell}}{(z-a_j)^\ell}.
$$
The Laurent expansion at infinity has the form
$$
f(z)=P_\infty(z)+b_0+O(1/z),\qquad
P_\infty(z)=\sum_{k=1}^{N}b_k z^k,
$$
where $N=0$ and $P_\infty=0$ are permitted in the removable
case [@SS03]. Subtracting all these principal parts gives
$$
G=f-P_\infty-\sum_{j=1}^m S_j.
$$
Every finite singularity of $G$ is removable. After their
removal $G$ is entire, and $G(z)\to b_0$ at infinity
because each $S_j(z)\to0$. It is bounded outside a disk
by that limit and on the remaining compact disk by
continuity. Liouville's theorem gives $G\equiv b_0$ [@SS03].
Thus
$$
f(z)=b_0+P_\infty(z)+\sum_{j=1}^{m}\sum_{\ell=1}^{d_j}
\frac{c_{j,\ell}}{(z-a_j)^\ell},
$$
which is rational. This proves (a), and also the removable
case at infinity that will be needed in (b).
:::

<1>2. The boundary condition in part (b) produces a meromorphic function on the sphere.
::: proof
Let $f$ be as in part (b). Define for $|z|>1$
$$
F(z)=\frac{1}{\overline{f(1/\overline z)}}.
$$
The function
$$
f^*(w)=\overline{f(\overline w)}
$$
is holomorphic on the unit disk: conjugating the Taylor
coefficients of $f$ gives its Taylor series. Thus on
$|z|>1$, the expression $F(z)=1/f^*(1/z)$ is meromorphic.
The boundary modulus excludes $f\equiv0$.

Uniform continuity of $f$ on $\overline\Delta$ gives
$0<\eta<1/2$ such that $|f(z)|>1/2$ whenever
$1-\eta<|z|\leq1$: compare $f(z)$ to the unit-modulus
value $f(z/|z|)$. The reflected expression consequently
has no pole for $1<|z|<1/(1-\eta)$.

On $|z|=1$, one has $1/\overline z=z$, and the boundary hypothesis gives
$$
\frac1{\overline{f(z)}}=f(z).
$$
Hence the inside definition $F=f$ and the outside reciprocal-reflection have
the same continuous boundary values on the unit circle.

Here is an explicit local gluing argument. Fix $p$ on
the unit circle and use the fractional coordinate
$$
w=i\frac{1-z/p}{1+z/p},\qquad z=p\frac{i-w}{i+w}.
$$
These inverse holomorphic maps take $p$ to zero and the
unit circle locally to the real axis. Indeed,
$$
1-\left|\frac{i-w}{i+w}\right|^2
=\frac{4\operatorname{Im}w}{|i+w|^2},
$$
so the upper and lower sides correspond to the inside
and outside of the circle. Choose $\varepsilon>0$ so
the inverse maps $|w|<\varepsilon$ into the pole-free
collar just established. The pullback
$K(w)=F(p(i-w)/(i+w))$ is continuous there and holomorphic
off the real axis.

For any closed triangle contained in $|w|<\varepsilon$,
cut it along the real axis into at most two polygons.
Translate its upper piece by $i\delta$ and its lower
piece by $-i\delta$. For sufficiently small $\delta>0$
both translated polygons remain in the disk and lie
in the respective open half-planes, so their boundary
integrals of $K$ are zero by Cauchy's theorem [@SS03].
For either piece $P$,
$$
\left|\int_{\partial P}(K(w\pm i\delta)-K(w))\,dw\right|
\leq\operatorname{length}(\partial P)
\sup_{w\in\partial P}|K(w\pm i\delta)-K(w)|\longrightarrow0.
$$
The limit follows from uniform continuity on a compact
neighborhood of the triangle. Degenerate pieces have
zero integral by cancellation. Passing to the limit and
adding the two integrals cancels the shared real segment,
so the original triangle integral is zero. Morera's
theorem proves that $K$, and hence $F$ near $p$, is
holomorphic [@SS03]. As $p$ was arbitrary, $F$ is
meromorphic on the whole plane.

At infinity, write $f(w)=w^k h(w)$ near zero, where $k\ge0$ and $h(0)\ne0$.
Then for large $z$,
$$
F(z)=\frac{z^k}{h^*(1/z)},
$$
so infinity is removable when $k=0$ and is a pole when $k>0$. Hence $F$ is
meromorphic on the Riemann sphere.
:::

<1>3. The reflected extension is rational, proving part (b).
::: proof
By step <1>1, the meromorphic sphere function $F$ from step <1>2 is rational.
On the unit disk its definition is exactly the original $f$. Therefore $f$ is
the restriction to $\Delta$ of a rational function, as required.
:::
:::
