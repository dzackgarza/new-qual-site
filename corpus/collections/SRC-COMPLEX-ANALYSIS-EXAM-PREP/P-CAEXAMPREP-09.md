---
schema: qual/card@1
id: P-CAEXAMPREP-09
kind: problem
title: Images of standard lines and circles under $(z-1)/(z+1)$
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
Let
\[
f(z)=\frac{z-1}{z+1}.
\]
Determine the image under $f$ of each of the following:

1. the real axis (hint: this is a line);

2. the circle $|z|=2$ (hint: this is a circle);

3. the circle $|z|=1$;

4. the imaginary axis.
:::

::: {.solution}

Regard \(f\) as the Möbius transformation of the Riemann sphere \(\CC^*=\CC\cup\{\infty\}\), so that \(f(-1)=\infty\) and \(f(\infty)=1\). For \(w\ne1\), solving \(w=f(z)\) gives
\[
z=\frac{1+w}{1-w}.
\]

::: pf

::: {.pf-step #s1-1}

The image of the extended real axis is the extended real axis:
\[
\boxed{f(\RR\cup\{\infty\})=\RR\cup\{\infty\}}.
\]


::: pf-proof

If \(z\in\RR\setminus\{-1\}\), then \((z-1)/(z+1)\in\RR\). Also \(f(-1)=\infty\) and \(f(\infty)=1\). Conversely, if \(w\in\RR\setminus\{1\}\), then the inverse formula gives \(z=(1+w)/(1-w)\in\RR\). Thus the image is exactly the extended real axis.

:::

:::

::: {.pf-step #s1-2}

The image of \(|z|=2\) is the circle
\[
\boxed{\left|w-\frac53\right|=\frac43}.
\]


::: pf-proof

For \(w=f(z)\), the inverse formula gives
\[
|z|=2
\quad\Longleftrightarrow\quad
|1+w|=2|1-w|.
\]
Writing \(w=u+iv\) and squaring gives
\[
(1+u)^2+v^2=4\bigl((1-u)^2+v^2\bigr),
\]
which rearranges to
\[
\left(u-\frac53\right)^2+v^2=\frac{16}{9}.
\]
The point \(w=1\) does not satisfy this equation, so the inverse formula proves both inclusions.

:::

:::

::: {.pf-step #s1-3}

The image of \(|z|=1\) is the extended imaginary axis:
\[
\boxed{f(\{|z|=1\})=i\RR\cup\{\infty\}}.
\]


::: pf-proof

For finite \(w\ne1\),
\[
|z|=1
\quad\Longleftrightarrow\quad
|1+w|=|1-w|.
\]
If \(w=u+iv\), squaring this equality gives
\[
(1+u)^2+v^2=(1-u)^2+v^2,
\]
hence \(u=0\). Conversely, every finite \(w\) with \(\operatorname{Re}w=0\) satisfies the equality and therefore has a preimage on \(|z|=1\). Finally \(z=-1\) lies on the source circle and maps to \(\infty\).

:::

:::

::: {.pf-step #s1-4}

The image of the extended imaginary axis is the unit circle:
\[
\boxed{f(i\RR\cup\{\infty\})=\{|w|=1\}}.
\]


::: pf-proof

If \(z=iy\) with \(y\in\RR\), then
\[
|f(iy)|
=\frac{|iy-1|}{|iy+1|}
=1.
\]
Also \(f(\infty)=1\), so the image is contained in the unit circle. Conversely, if \(|w|=1\) and \(w\ne1\), then
\[
\overline{w}=\frac1w
\]
and the inverse formula satisfies
\[
\overline{\frac{1+w}{1-w}}
=\frac{1+\overline w}{1-\overline w}
=\frac{w+1}{w-1}
=-\frac{1+w}{1-w}.
\]
Thus its real part is zero, so its preimage lies on the imaginary axis. The remaining point \(w=1\) is the image of \(z=\infty\).

:::

:::

::: pf-qed

Steps [](#s1-1){.pf-ref} through [](#s1-4){.pf-ref} determine all four requested images.

:::

:::

:::
