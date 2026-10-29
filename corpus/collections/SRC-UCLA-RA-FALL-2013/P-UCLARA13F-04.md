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
Let $u$ be a nonnegative continuous function on $\DD\setminus\{0\}$ that is subharmonic there.
Suppose $u|_{\partial\DD}=0$ and
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

::: pf

::: {.pf-step #s1-1}

For every $0<r<R<1$, the maximum principle on the annulus $r<|z|<1$ gives
\[
u(z)\leq \frac{\log(1/|z|)}{\log(1/r)}
\max_{|w|=r}u(w)
\qquad(r\leq|z|\leq1).
\]


::: pf-proof

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

:::

::: {.pf-step #s1-2}

It is enough to find a sequence $r_j\downarrow0$ such that
\[
\frac{\max_{|z|=r_j}u(z)}{\log(1/r_j)}\longrightarrow0.
\]


::: pf-proof

Fix $z\ne0$. For all sufficiently large $j$, $r_j<|z|$. Step [](#s1-1){.pf-ref} then gives
\[
0\leq u(z)
\leq\log(1/|z|)
\frac{\max_{|w|=r_j}u(w)}{\log(1/r_j)}.
\]
If the displayed ratio tends to zero, then $u(z)=0$. Since $z$ was arbitrary in the punctured disk, this proves $u\equiv0$ there.

:::

:::

::: {.pf-step #s1-3}

For $0<r<1/2$ and every $z$ with $|z|=r$, the disk
\[
D(z,r/2)
\]
lies in
\[
\{w:r/2<|w|<3r/2\}.
\]


::: pf-proof

If $|w-z|<r/2$, then the reverse and ordinary triangle inequalities give
\[
r-r/2<|w|<r+r/2.
\]

:::

:::

::: {.pf-step #s1-4}

The sub-mean inequality gives
\[
u(z)\leq\frac4{\pi r^2}
\int_{r/2<|w|<3r/2}u(w)\,d\lambda(w)
\qquad(|z|=r).
\]


::: pf-proof

The function $u$ is subharmonic on the disk $D(z,r/2)$ because that disk avoids $0$ by step [](#s1-3){.pf-ref}. Hence
\[
u(z)\leq\frac1{\pi(r/2)^2}
\int_{D(z,r/2)}u(w)\,d\lambda(w).
\]
Use the containment from step [](#s1-3){.pf-ref} and nonnegativity of $u$.

:::

:::

::: {.pf-step #s1-5}

Consequently
\[
\max_{|z|=r}u(z)
\leq\frac4{\pi r^2}
\int_{0<|w|<2r}u(w)\,d\lambda(w).
\]


::: pf-proof

The annulus in step [](#s1-4){.pf-ref} is contained in $0<|w|<2r$. The right side is independent of $z$, so take the maximum over $|z|=r$.

:::

:::

::: {.pf-step #s1-6}

The hypothesis implies
\[
\frac{1}{r^2\log(1/r)}
\int_{0<|w|<2r}u(w)\,d\lambda(w)
\longrightarrow0.
\]


::: pf-proof

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

:::

::: {.pf-step #s1-7}

Combining steps [](#s1-5){.pf-ref} through [](#s1-6){.pf-ref} yields
\[
\frac{\max_{|z|=r}u(z)}{\log(1/r)}\longrightarrow0
\qquad(r\downarrow0).
\]


::: pf-proof

Divide the estimate in step [](#s1-5){.pf-ref} by $\log(1/r)$ and apply step [](#s1-6){.pf-ref}.

:::

:::

::: {.pf-step #s1-8}

Therefore $u(z)=0$ for every $z\in\DD\setminus\{0\}$.


::: pf-proof

Step [](#s1-7){.pf-ref} supplies the condition required in step [](#s1-2){.pf-ref}, indeed for all sufficiently small $r$ rather than merely along a sequence.

:::

:::

::: {.pf-step #s1-9}

Hence
\[
\boxed{u\equiv0.}
\]


::: pf-proof

The domain of $u$ in the problem is the punctured disk, and step [](#s1-8){.pf-ref} proves vanishing at every point of that domain.

:::

:::

::: pf-qed

Step [](#s1-9){.pf-ref} is the required conclusion.

:::

:::

:::
