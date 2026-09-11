---
schema: qual/card@1
id: E-SS6.EX-10
kind: problem
title: "SS 6.10: Mellin transforms of cosine and sine"
classification:
  areas:
  - complex-analysis
  topics: ['Gamma Function', 'Zeta Function', 'Mellin Transform']
relations: []
review: draft
audit:
- event: solution-written
  by: gpt-5.6-sol
  date: 2026-09-11
---

::: exercise
10. An integral of the form

$$
F (z) = \int_ {0} ^ {\infty} f (t) t ^ {z - 1} d t
$$

is called a Mellin transform, and we shall write $\mathcal { M } ( f ) ( z ) = F ( z )$ . For example, the gamma function is the Mellin transform of the function $e ^ { - t }$

(a) Prove that

$$
\mathcal {M} (\cos) (z) = \int_ {0} ^ {\infty} \cos (t) t ^ {z - 1} d t = \Gamma (z) \cos \left(\pi \frac {z}{2}\right) \quad \mathrm{for} 0 <   \mathrm{Re} (z) <   1,
$$

and

$$
\mathcal {M} (\sin) (z) = \int_ {0} ^ {\infty} \sin (t) t ^ {z - 1} d t = \Gamma (z) \sin \left(\pi \frac {z}{2}\right) \quad \mathrm{for} 0 <   \mathrm{Re} (z) <   1.
$$

(b) Show that the second of the above identities is valid in the larger strip $- 1 < \operatorname { R e } ( z ) < 1$ , and that as a consequence, one has

$$
\int_ {0} ^ {\infty} \frac {\sin x}{x} d x = \frac {\pi}{2} \quad \mathrm{and} \quad \int_ {0} ^ {\infty} \frac {\sin x}{x ^ {3 / 2}} d x = \sqrt {2 \pi}.
$$

This generalizes the calculation in Exercise 2 of Chapter 2.

[Hint: For the first part, consider the integral of the function $f ( w ) = e ^ { - w } w ^ { z - 1 }$ around the contour illustrated in Figure 1. Use analytic continuation to prove the second part.]

Figure 1. The contour in Exercise 10
:::

::: solution
Let $z$ satisfy $0<\Re z<1$. On the principal branch, rotate the ray in the gamma integral through angle $-\pi/2$. The integrals over the connecting circular arcs vanish at $0$ and at infinity because $0<\Re z<1$. Thus
\[
\Gamma(z)=\int_0^\infty e^{-t}t^{z-1}\,dt
=e^{-i\pi z/2}\int_0^\infty e^{it}t^{z-1}\,dt,
\]
so
\[
\int_0^\infty e^{it}t^{z-1}\,dt=e^{i\pi z/2}\Gamma(z).
\tag{1}
\]
Taking real and imaginary parts of (1) gives
\[
\int_0^\infty \cos t\,t^{z-1}\,dt
=\Gamma(z)\cos\frac{\pi z}{2},
\]
\[
\int_0^\infty \sin t\,t^{z-1}\,dt
=\Gamma(z)\sin\frac{\pi z}{2}.
\]

For the sine integral, near $0$ we have $\sin t=O(t)$, so the integral converges there when $\Re z>-1$. At infinity, integration by parts (or Dirichlet's test, uniformly on compact vertical substrips) gives convergence when $\Re z<1$. Hence
\[
S(z)=\int_0^\infty \sin t\,t^{z-1}\,dt
\]
is holomorphic on $-1<\Re z<1$. The function $\Gamma(z)\sin(\pi z/2)$ is also holomorphic there: the pole of $\Gamma$ at $0$ is cancelled by the zero of the sine factor. Since the two functions agree on $0<\Re z<1$, the identity theorem gives
\[
S(z)=\Gamma(z)\sin\frac{\pi z}{2},\qquad -1<\Re z<1.
\]
At $z=0$, using $\Gamma(z)\sim1/z$ and $\sin(\pi z/2)\sim \pi z/2$,
\[
\int_0^\infty\frac{\sin x}{x}\,dx=\frac\pi2.
\]
At $z=-1/2$, since $\Gamma(-1/2)=-2\sqrt\pi$,
\[
\int_0^\infty\frac{\sin x}{x^{3/2}}\,dx
=\Gamma(-1/2)\sin(-\pi/4)=\sqrt{2\pi}.
\]
:::
