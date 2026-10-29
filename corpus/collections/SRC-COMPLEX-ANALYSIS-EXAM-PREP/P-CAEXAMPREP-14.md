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

::: pf

::: {.pf-step #s1-1}

The map \(W\) is a biholomorphism from the unit disk \(\DD\) onto the upper half-plane \(\halfplane\).


::: pf-proof

For \(z\in\DD\), direct calculation gives
\[
\operatorname{Im}W(z)
=\frac{1-|z|^2}{|1-z|^2}>0,
\]
so \(W(\DD)\subseteq\halfplane\). Solving \(w=W(z)\) gives
\[
z=\frac{w-i}{w+i}.
\]
If \(\operatorname{Im}w>0\), then
\[
|w+i|^2-|w-i|^2=4\operatorname{Im}w>0,
\]
so the inverse satisfies \(|z|<1\). Thus \(W\) is bijective between \(\DD\) and \(\halfplane\), and both \(W\) and its inverse are holomorphic there.

:::

:::

::: {.pf-step #s1-2}

With the branch \(0<\operatorname{Arg}w<\pi\) on \(\halfplane\), the function
\[
\phi(z)=\frac1\pi\operatorname{Arg}W(z)
\]
is harmonic on \(\DD\).


::: pf-proof

On \(\halfplane\), choose the holomorphic branch
\[
\operatorname{Log}w=\log|w|+i\operatorname{Arg}w,
\qquad 0<\operatorname{Arg}w<\pi.
\]
By step [](#s1-1){.pf-ref}, \(\operatorname{Log}W(z)\) is holomorphic on \(\DD\). The imaginary part of a holomorphic function is harmonic: the Cauchy--Riemann equations imply its Laplacian is zero. Therefore
\[
\phi(z)=\frac1\pi\operatorname{Im}(\operatorname{Log}W(z))
\]
is harmonic.

:::

:::

::: {.pf-step #s1-3}

The boundary values of \(\phi\) are \(1\) on the open upper semicircle and \(0\) on the open lower semicircle.


::: pf-proof

For \(z=e^{i\theta}\) with \(0<\theta<2\pi\) and \(z\ne1\),
\[
W(e^{i\theta})
=i\frac{1+e^{i\theta}}{1-e^{i\theta}}
=-\cot\frac\theta2.
\]
When \(0<\theta<\pi\), this is negative real, and approaching the boundary from \(\halfplane\) gives \(\operatorname{Arg}W\to\pi\); hence \(\phi\to1\). When \(\pi<\theta<2\pi\), it is positive real, so \(\operatorname{Arg}W\to0\); hence \(\phi\to0\). These are exactly the prescribed values away from the two boundary jump points \(z=\pm1\).

:::

:::

::: {.pf-step #s1-4}

Hence the electric potential is
\[
\boxed{
\phi(z)=\frac1\pi\operatorname{Arg}\!\left(i\frac{1+z}{1-z}\right),
\qquad 0<\operatorname{Arg}<\pi}.
\]


::: pf-proof

Step [](#s1-2){.pf-ref} proves harmonicity in the disk, and step [](#s1-3){.pf-ref} gives the required boundary values on the two open semicircles.

:::

:::

::: pf-qed

Step [](#s1-4){.pf-ref} is the required potential.

:::

:::

:::
