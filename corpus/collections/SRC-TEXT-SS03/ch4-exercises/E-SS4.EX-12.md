---
schema: qual/card@1
id: E-SS4.EX-12
kind: problem
title: "The principle that a function and its Fourier transform cannot both be too small"
classification:
  areas:
  - complex-analysis
  topics: ['Fourier Transform', 'Poisson Summation']
relations: []
review: draft
audit:
- event: source-checked
  by: gpt-5.6-sol
  date: 2026-09-11
  note: Repaired the limiting parameter in part (b) from beta tending to pi to beta decreasing to 1, so the sectors exhaust the upper half-plane.
- event: solution-written
  by: gpt-5.6-sol
  date: 2026-09-11
---

::: exercise
12. The principle that a function and its Fourier transform cannot both be too small at infinity is illustrated by the following theorem of Hardy.

If $f$ is a function on R that satisfies

$$
f (x) = O (e ^ {- \pi x ^ {2}}) \quad \mathrm{and} \quad \hat {f} (\xi) = O (e ^ {- \pi \xi^ {2}}),
$$

then f is a constant multiple of $e ^ { - \pi x ^ { 2 } }$ . As a result, if $f ( x ) = O ( e ^ { - \pi A x ^ { 2 } } )$ , and $\hat { f } ( \xi ) = O ( e ^ { - \pi B \xi ^ { 2 } } )$ , with $A B > 1$ and $A , B > 0$ , then f is identically zero.

(a) If f is even, show that $\hat { f }$ extends to an even entire function.
Moreover, if $g ( \dot { z } ) = \hat { f } ( z ^ { 1 / 2 } )$ , then $g$ satisfies

$$
| g (x) | \leq c e ^ {- \pi x} \quad \text { and } \quad | g (z) | \leq c e ^ {\pi R \sin^ {2} (\theta / 2)} \leq c e ^ {\pi | z |}
$$

when $x \in \mathbb { R }$ and $z = R e ^ { i \theta }$ with $R \geq 0$ and $\theta \in \mathbb { R }$

(b) Apply the Phragm´en-Lindel¨of principle to the function

$$
F (z) = g (z) e ^ {\gamma z} \quad \mathrm{where} \gamma = i \pi \frac {e ^ {- i \pi / (2 \beta)}}{\sin \pi / (2 \beta)}
$$

and the sector $0 \leq \theta \leq \pi / \beta < \pi$ , and let $\beta \downarrow 1$ to deduce that $e ^ { \pi z } g ( z )$ is bounded in the closed upper half-plane.
The same result holds in the lower half-plane, so by Liouville’s theorem $e ^ { \pi z } g ( z )$ is constant, as desired.

(c) If $f$ is odd, then ${ \hat { f } } ( 0 ) = 0$ , and apply the above argument to $\hat { f } ( z ) / z$ to deduce that $\boldsymbol { f } = \boldsymbol { \hat { f } } = 0$ . Finally, write an arbitrary $f$ as an appropriate sum of an even function and an odd function.
:::

::: solution
We use the Fourier-transform convention
\[
\widehat f(\zeta)=\int_{\mathbb R}f(x)e^{-2\pi i x\zeta}\,dx.
\]
The hypothesis $|f(x)|\le Ce^{-\pi x^2}$ implies that this integral converges for every $\zeta\in\mathbb C$, locally uniformly in $\zeta$, because for $\zeta=\xi+i\eta$,
\[
|f(x)e^{-2\pi i x\zeta}|
\le C e^{-\pi x^2+2\pi |\eta||x|}.
\]
Hence $\widehat f$ extends to an entire function. Completing the square gives the global estimate
\[
|\widehat f(\xi+i\eta)|
\le C\int_{\mathbb R}e^{-\pi x^2+2\pi\eta x}\,dx
=C' e^{\pi\eta^2}.
\tag{1}
\]

Assume first that $f$ is even. Then $\widehat f$ is even. Its Taylor series therefore contains only even powers, so there is an entire function $g$ such that
\[
g(z)=\widehat f(\sqrt z);
\]
this notation is independent of the choice of square root. If $x\ge0$, the assumed real-axis decay of $\widehat f$ gives
\[
|g(x)|\le C e^{-\pi x}.
\tag{2}
\]
If $x<0$, choose $\sqrt x=i\sqrt{|x|}$ and use (1):
\[
|g(x)|\le C'e^{\pi|x|}=C'e^{-\pi x}.
\tag{3}
\]
More generally, for $z=Re^{i\theta}$ choose $\sqrt z=\sqrt R e^{i\theta/2}$. Then (1) yields
\[
|g(z)|\le C'e^{\pi R\sin^2(\theta/2)}\le C'e^{\pi|z|}.
\tag{4}
\]

Fix $\beta>1$ and consider the sector
\[
S_\beta=\{z:0\le\arg z\le\pi/\beta\}.
\]
Put
\[
\alpha=\frac{\pi}{2\beta},
\qquad
\gamma=i\pi\frac{e^{-i\alpha}}{\sin\alpha}
=\pi(1+i\cot\alpha),
\]
and
\[
F_\beta(z)=g(z)e^{\gamma z}.
\]
By (4), $F_\beta$ has exponential growth $O(e^{C_\beta|z|})$. Since the sector has opening $\pi/\beta$ and $1<\beta$, the Phragmén--Lindelöf principle applies.

On the ray $z=r\ge0$, $\Re\gamma=\pi$, so by (2)
\[
|F_\beta(r)|\le C.
\tag{5}
\]
On the other boundary ray $z=re^{2i\alpha}$, a direct calculation gives
\[
\Re(\gamma e^{2i\alpha})=-\pi.
\]
Together with (4), whose exponent there is $\pi r\sin^2\alpha$, this gives
\[
|F_\beta(re^{2i\alpha})|
\le C' e^{-\pi r+\pi r\sin^2\alpha}
=C'e^{-\pi r\cos^2\alpha}\le C'.
\tag{6}
\]
Thus Phragmén--Lindelöf and (5)--(6) imply that $F_\beta$ is bounded on $S_\beta$.

Now let $\beta\downarrow1$. Then $S_\beta$ exhausts the open upper half-plane and
\[
\gamma\longrightarrow\pi.
\]
For each fixed $z$ in the upper half-plane, the preceding bound may be taken with the same boundary constant $\max(C,C')$; hence
\[
|e^{\pi z}g(z)|\le C''
\]
in the closed upper half-plane. Applying the reflected argument in the lower half-plane gives the same bound there. Consequently the entire function $e^{\pi z}g(z)$ is bounded on $\mathbb C$, so Liouville's theorem gives
\[
g(z)=c e^{-\pi z}.
\]
Substituting $z=w^2$ yields
\[
\widehat f(w)=c e^{-\pi w^2}.
\]
The Gaussian is its own Fourier transform in this normalization, so Fourier inversion gives
\[
f(x)=c e^{-\pi x^2}.
\tag{7}
\]

Now suppose $f$ is odd. Then $\widehat f$ is odd and $\widehat f(0)=0$. Hence
\[
h(z)=\frac{\widehat f(z)}{z}
\]
extends to an even entire function. From (1) and the real-axis Gaussian bound, after increasing the constant on a neighborhood of $0$, $h$ satisfies the same type of estimates as the even function treated above:
\[
|h(x)|\le C e^{-\pi x^2},
\qquad
|h(\xi+i\eta)|\le C'e^{\pi\eta^2}.
\]
Therefore
\[
h(z)=c e^{-\pi z^2},
\qquad
\widehat f(z)=cz e^{-\pi z^2}.
\]
But the assumed bound $|\widehat f(x)|\le C e^{-\pi x^2}$ on the real axis forces $c=0$, since otherwise division by $e^{-\pi x^2}$ would give the unbounded function $|c||x|$. Thus $\widehat f=0$ and $f=0$.

For a general $f$, write
\[
f=f_e+f_o,
\qquad
f_e(x)=\frac{f(x)+f(-x)}2,
\quad
f_o(x)=\frac{f(x)-f(-x)}2.
\]
Both parts satisfy the same Gaussian bound, and
\[
\widehat{f_e}(\xi)=\frac{\widehat f(\xi)+\widehat f(-\xi)}2,
\qquad
\widehat{f_o}(\xi)=\frac{\widehat f(\xi)-\widehat f(-\xi)}2,
\]
so their Fourier transforms do also. The even case gives $f_e=ce^{-\pi x^2}$ and the odd case gives $f_o=0$. This proves Hardy's theorem.

Finally suppose
\[
|f(x)|\le Ce^{-\pi A x^2},
\qquad
|\widehat f(\xi)|\le Ce^{-\pi B\xi^2},
\qquad AB>1.
\]
Define $q(x)=f(x/\sqrt A)$. Then
\[
|q(x)|\le Ce^{-\pi x^2},
\]
and the scaling rule gives
\[
\widehat q(\xi)=\sqrt A\,\widehat f(\sqrt A\,\xi),
\]
so
\[
|\widehat q(\xi)|\le C\sqrt A\,e^{-\pi AB\xi^2}
\le C\sqrt A\,e^{-\pi\xi^2}.
\]
Hardy's theorem gives $q(x)=ce^{-\pi x^2}$, hence
\[
\widehat q(\xi)=ce^{-\pi\xi^2}.
\]
The stronger estimate with $AB>1$ is incompatible with $c\ne0$ as $|\xi|\to\infty$. Hence $c=0$, so $q=0$ and therefore $f=0$.
:::
