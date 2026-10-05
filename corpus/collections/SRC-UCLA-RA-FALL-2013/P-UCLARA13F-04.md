---
schema: qual/card@1
id: P-UCLARA13F-04
kind: problem
title: A removable subharmonic singularity under an averaged growth condition
classification:
  areas:
  - real-analysis
  topics: []
relations: []
review: draft
audit:
- event: source-checked
  by: gpt-5.6-sol
  date: 2026-09-12
  note: Transcribed from the UCLA Analysis Qualifying Exam Solutions compendium, Fall 2013 section.
---

::: {.problem}
Let $u$ be a nonnegative continuous function on $\mathbb D\setminus\{0\}$ that is subharmonic there.
Suppose $u|_{\partial\mathbb D}=0$ and
\[
\lim_{r\to0^+}\frac{1}{r^2\log(1/r)}\int_{0<|z|<r}u(z)\,d\lambda(z)=0,
\]
where $\lambda$ is planar Lebesgue measure.
Show that $u\equiv0$.
:::

::: {.solution}
Write
\[
M(r)=\frac1{2\pi}\int_0^{2\pi}u(re^{i\theta})\,d\theta,
\qquad 0<r<1.
\]

<1>1. For every $0<r<R<1$, the maximum principle on the annulus $r<|z|<1$ gives
\[
u(z)\leq \frac{\log(1/|z|)}{\log(1/r)}
\max_{|w|=r}u(w)
\qquad(r\leq|z|\leq1).
\]

::: {.proof}
Let
\[
A_r=\max_{|w|=r}u(w)
\]
and define the harmonic radial function
\[
h_r(z)=A_r\frac{\log(1/|z|)}{\log(1/r)}.
\]
On $|z|=r$, $h_r=A_r\geq u$, while on $|z|=1$, $h_r=0=u$. Since $u-h_r$ is subharmonic on the annulus and nonpositive on its boundary, the subharmonic maximum principle gives $u\leq h_r$.
:::

<1>2. It is enough to find a sequence $r_j\downarrow0$ such that
\[
\frac{\max_{|z|=r_j}u(z)}{\log(1/r_j)}\longrightarrow0.
\]

::: {.proof}
Fix $z\ne0$. For all sufficiently large $j$, $r_j<|z|$. Step <1>1 then gives
\[
0\leq u(z)
\leq\log(1/|z|)
\frac{\max_{|w|=r_j}u(w)}{\log(1/r_j)}.
\]
If the displayed ratio tends to zero, then $u(z)=0$. Since $z$ was arbitrary in the punctured disk, this proves $u\equiv0$ there.
:::

<1>3. For $0<r<1/2$ and every $z$ with $|z|=r$, the disk
\[
D(z,r/2)
\]
lies in
\[
\{w:r/2<|w|<3r/2\}.
\]

::: {.proof}
If $|w-z|<r/2$, then the reverse and ordinary triangle inequalities give
\[
r-r/2<|w|<r+r/2.
\]
:::

<1>4. The sub-mean inequality gives
\[
u(z)\leq\frac4{\pi r^2}
\int_{r/2<|w|<3r/2}u(w)\,d\lambda(w)
\qquad(|z|=r).
\]

::: {.proof}
The function $u$ is subharmonic on the disk $D(z,r/2)$ because that disk avoids $0$ by step <1>3. Hence
\[
u(z)\leq\frac1{\pi(r/2)^2}
\int_{D(z,r/2)}u(w)\,d\lambda(w).
\]
Use the containment from step <1>3 and nonnegativity of $u$.
:::

<1>5. Consequently
\[
\max_{|z|=r}u(z)
\leq\frac4{\pi r^2}
\int_{0<|w|<2r}u(w)\,d\lambda(w).
\]

::: {.proof}
The annulus in step <1>4 is contained in $0<|w|<2r$. The right side is independent of $z$, so take the maximum over $|z|=r$.
:::

<1>6. The hypothesis implies
\[
\frac{1}{r^2\log(1/r)}
\int_{0<|w|<2r}u(w)\,d\lambda(w)
\longrightarrow0.
\]

::: {.proof}
Apply the hypothesis at radius $2r$:
\[
\int_{|w|<2r}u(w)\,d\lambda(w)
=o\!\left((2r)^2\log\frac1{2r}\right).
\]
Since
\[
\frac{(2r)^2\log(1/(2r))}{r^2\log(1/r)}
=4\frac{\log(1/r)-\log2}{\log(1/r)}\to4,
\]
the stated quotient tends to zero.
:::

<1>7. Combining steps <1>5--<1>6 yields
\[
\frac{\max_{|z|=r}u(z)}{\log(1/r)}\longrightarrow0
\qquad(r\downarrow0).
\]

::: {.proof}
Divide the estimate in step <1>5 by $\log(1/r)$ and apply step <1>6.
:::

<1>8. Therefore $u(z)=0$ for every $z\in\mathbb D\setminus\{0\}$.

::: {.proof}
Step <1>7 supplies the condition required in step <1>2, indeed for all sufficiently small $r$ rather than merely along a sequence.
:::

<1>9. Hence
\[
\boxed{u\equiv0.}
\]

::: {.proof}
The domain of $u$ in the problem is the punctured disk, and step <1>8 proves vanishing at every point of that domain.
:::

<1>10. Q.E.D.

::: {.proof}
Step <1>9 is the required conclusion.
:::
:::
