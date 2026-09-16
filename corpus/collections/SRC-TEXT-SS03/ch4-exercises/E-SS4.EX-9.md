---
schema: qual/card@1
id: E-SS4.EX-9
kind: problem
title: "Here are further results similar to the Phragm´en-Lindel¨of theorem"
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
9. Here are further results similar to the Phragm´en-Lindel¨of theorem.

(a) Let $F$ be a holomorphic function in the right half-plane that extends continuously to the boundary, that is, the imaginary axis.
Suppose that $| F ( i y ) | \le 1$ for all $y \in \mathbb { R }$ , and

$$
| F (z) | \leq C e ^ {c | z | ^ {\gamma}}
$$

for some $c , C > 0$ and $\gamma < 1$ . Prove that $| F ( z ) | \le 1$ for all z in the right half-plane.

(b) More generally, let S be a sector whose vertex is the origin, and forming an angle of $\pi / \beta$ . Let $F$ be a holomorphic function in S that is continuous on the closure of $S ,$ , so that $| F ( z ) | \le 1$ on the boundary of S and

$$
| F (z) | \leq C e ^ {c | z | ^ {\alpha}} \text {   for   all   } z \in S
$$

for some $c , C > 0$ and $0 < \alpha < \beta$ . Prove that $| F ( z ) | \le 1$ for all $z \in S$
:::

::: {.solution}
For (a), work in the right half-plane with the branch of $z^\delta$ determined by
\[
-\frac\pi2<\arg z<\frac\pi2.
\]
Choose $\delta$ so that
\[
\gamma<\delta<1.
\]
For $\varepsilon>0$, set
\[
F_\varepsilon(z)=F(z)e^{-\varepsilon z^\delta}.
\]
If $z=re^{i\theta}$ in the closed right half-plane, then
\[
\Re(z^\delta)=r^\delta\cos(\delta\theta)
\ge r^\delta\cos\frac{\delta\pi}{2}>0.
\]
Hence on the imaginary axis
\[
|F_\varepsilon(iy)|\le|F(iy)|\le1.
\]
On the large semicircle $|z|=R$ in the right half-plane,
\[
|F_\varepsilon(z)|
\le C\exp\!\left(cR^\gamma
-\varepsilon R^\delta\cos\frac{\delta\pi}{2}\right),
\]
which tends to $0$ as $R\to\infty$ because $\delta>\gamma$. Thus, for sufficiently large $R$, the maximum principle on the right half-disc gives $|F_\varepsilon|\le1$. Letting $R\to\infty$ and then $\varepsilon\downarrow0$ yields
\[
|F(z)|\le1
\]
throughout the right half-plane.

For (b), rotate the sector so that it is symmetric about the positive real axis:
\[
S=\left\{z:\left|\arg z\right|\le\frac{\pi}{2\beta}\right\}.
\]
Choose
\[
\alpha<\delta<\beta.
\]
The branch $z^\delta=r^\delta e^{i\delta\theta}$ is holomorphic in the sector, and
\[
\Re(z^\delta)
=r^\delta\cos(\delta\theta)
\ge r^\delta\cos\frac{\delta\pi}{2\beta}>0.
\]
For
\[
F_\varepsilon(z)=F(z)e^{-\varepsilon z^\delta},
\]
the boundary-ray bound remains at most $1$, while on the circular arc $|z|=R$,
\[
|F_\varepsilon(z)|
\le C\exp\!\left(cR^\alpha
-\varepsilon R^\delta\cos\frac{\delta\pi}{2\beta}\right)
\longrightarrow0.
\]
The maximum principle on truncated sectors therefore gives $|F_\varepsilon|\le1$. Letting $\varepsilon\downarrow0$ proves
\[
|F(z)|\le1
\]
for all $z\in S$.
:::
