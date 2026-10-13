---
schema: qual/card@1
id: P-CAEXAMPREP-14
kind: problem
title: Electric potential in a disk with semicircular boundary values
classification: {areas: [complex-analysis], topics: []}
relations: []
review: draft
audit:
- event: source-checked
  by: gpt-5.6-sol
  date: 2026-09-14
  note: Checked against the deterministic MinerU Flash extraction assets/attachments/Complex_Analysis_Exam_Prep_Solutions_extracted.md.
---

::: {.problem}
On the unit disk $|z|<1$, the electric potential is maintained at $\phi=0$ on the lower semicircle and at $\phi=1$ on the upper semicircle.
Find $\phi$ inside the disk.
:::

::: {.solution}
Define
\[
W(z)=i\frac{1+z}{1-z}.
\]

<1>1. The map \(W\) is a biholomorphism from the unit disk \(\mathbb D\) onto the upper half-plane \(\mathbb H\).

::: {.proof}
For \(z\in\mathbb D\), direct calculation gives
\[
\operatorname{Im}W(z)
=\frac{1-|z|^2}{|1-z|^2}>0,
\]
so \(W(\mathbb D)\subseteq\mathbb H\). Solving \(w=W(z)\) gives
\[
z=\frac{w-i}{w+i}.
\]
If \(\operatorname{Im}w>0\), then
\[
|w+i|^2-|w-i|^2=4\operatorname{Im}w>0,
\]
so the inverse satisfies \(|z|<1\). Thus \(W\) is bijective between \(\mathbb D\) and \(\mathbb H\), and both \(W\) and its inverse are holomorphic there.
:::

<1>2. With the branch \(0<\operatorname{Arg}w<\pi\) on \(\mathbb H\), the function
\[
\phi(z)=\frac1\pi\operatorname{Arg}W(z)
\]
is harmonic on \(\mathbb D\).

::: {.proof}
On \(\mathbb H\), choose the holomorphic branch
\[
\operatorname{Log}w=\log|w|+i\operatorname{Arg}w,
\qquad 0<\operatorname{Arg}w<\pi.
\]
By step <1>1, \(\operatorname{Log}W(z)\) is holomorphic on \(\mathbb D\). The imaginary part of a holomorphic function is harmonic: the Cauchy--Riemann equations imply its Laplacian is zero. Therefore
\[
\phi(z)=\frac1\pi\operatorname{Im}(\operatorname{Log}W(z))
\]
is harmonic.
:::

<1>3. The boundary values of \(\phi\) are \(1\) on the open upper semicircle and \(0\) on the open lower semicircle.

::: {.proof}
For \(z=e^{i\theta}\) with \(0<\theta<2\pi\) and \(z\ne1\),
\[
W(e^{i\theta})
=i\frac{1+e^{i\theta}}{1-e^{i\theta}}
=-\cot\frac\theta2.
\]
When \(0<\theta<\pi\), this is negative real, and approaching the boundary from \(\mathbb H\) gives \(\operatorname{Arg}W\to\pi\); hence \(\phi\to1\). When \(\pi<\theta<2\pi\), it is positive real, so \(\operatorname{Arg}W\to0\); hence \(\phi\to0\). These are exactly the prescribed values away from the two boundary jump points \(z=\pm1\).
:::

<1>4. Hence the electric potential is
\[
\boxed{
\phi(z)=\frac1\pi\operatorname{Arg}\!\left(i\frac{1+z}{1-z}\right),
\qquad 0<\operatorname{Arg}<\pi}.
\]

::: {.proof}
Step <1>2 proves harmonicity in the disk, and step <1>3 gives the required boundary values on the two open semicircles.
:::

<1>5. Q.E.D.

::: {.proof}
Step <1>4 is the required potential.
:::
:::
