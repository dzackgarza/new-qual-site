---
schema: qual/card@1
id: P-UCLARA14S-02
kind: problem
title: Almost-everywhere finiteness of a fractional potential of an L1 function
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
  note: Transcribed from the UCLA Analysis Qualifying Exam Solutions compendium, Spring 2014 section.
---

::: {.problem}
Let $f\in L^1(\mathbb R)$ and $\beta\in(0,1)$.
Prove that
\[
\int_{\mathbb R}\frac{|f(x)|}{|x-a|^\beta}\,dx<\infty
\]
for Lebesgue-almost every $a\in\mathbb R$.
:::

For $a\in\mathbb R$, define
\[
F(a)
\coloneqq
\int_{\mathbb R}
\frac{|f(x)|}{|x-a|^\beta}\,dx
\in[0,\infty].
\]
Also set
\[
w(a)
\coloneqq
\frac1{1+a^2}.
\]

::: pf

::: pf-step

There is a constant $C_\beta<\infty$, depending only on $\beta$, such that for every $x\in\mathbb R$,
\[
\int_{\mathbb R}
\frac{w(a)}{|x-a|^\beta}\,da
\le
C_\beta.
\]


::: pf-proof

Split the integral into the regions $|a-x|<1$ and $|a-x|\ge1$.

On the first region, $w(a)\le1$, so after the change of variables $h=a-x$,
\[
\int_{|a-x|<1}
\frac{w(a)}{|x-a|^\beta}\,da
\le
\int_{|h|<1}|h|^{-\beta}\,dh
=
\frac{2}{1-\beta},
\]
which is finite because $0<\beta<1$.

On the second region, $|x-a|^{-\beta}\le1$, hence
\[
\int_{|a-x|\ge1}
\frac{w(a)}{|x-a|^\beta}\,da
\le
\int_{\mathbb R}\frac{da}{1+a^2}
=
\pi.
\]
Thus one may take
\[
C_\beta
=
\frac{2}{1-\beta}+\pi.
\]

:::

:::

::: pf-step

One has
\[
\int_{\mathbb R}w(a)F(a)\,da
\le
C_\beta\|f\|_{L^1(\mathbb R)}
<
\infty.
\]


::: pf-proof

The function
\[
(a,x)
\longmapsto
w(a)\frac{|f(x)|}{|x-a|^\beta}
\]
is nonnegative and measurable. Tonelli's theorem therefore gives
\[
\begin{aligned}
\int_{\mathbb R}w(a)F(a)\,da
&=
\int_{\mathbb R}
\int_{\mathbb R}
w(a)\frac{|f(x)|}{|x-a|^\beta}\,dx\,da\\
&=
\int_{\mathbb R}
|f(x)|
\left(
\int_{\mathbb R}
\frac{w(a)}{|x-a|^\beta}\,da
\right)dx.
\end{aligned}
\]
Apply step <1>1 to the inner integral:
\[
\int_{\mathbb R}w(a)F(a)\,da
\le
C_\beta
\int_{\mathbb R}|f(x)|\,dx.
\]
The right-hand side is finite because $f\in L^1(\mathbb R)$.

:::

:::

::: pf-step

The set
\[
E
\coloneqq
\{a\in\mathbb R:F(a)=\infty\}
\]
has Lebesgue measure zero.


::: pf-proof

The weight $w(a)=(1+a^2)^{-1}$ is strictly positive for every $a\in\mathbb R$. If $E$ had positive measure, then
\[
w(a)F(a)=\infty
\qquad
(a\in E),
\]
so the nonnegative integral
\[
\int_{\mathbb R}w(a)F(a)\,da
\]
would be infinite. This contradicts step <1>2. Hence $m(E)=0$.

:::

:::

::: pf-step

Therefore
\[
\boxed{
\int_{\mathbb R}
\frac{|f(x)|}{|x-a|^\beta}\,dx
<
\infty
}
\]
for Lebesgue-almost every $a\in\mathbb R$.


::: pf-proof

By definition, the integral is $F(a)$, and step <1>3 shows that $F(a)<\infty$ outside a null set.

:::

:::

::: pf-qed

Step <1>4 is the required conclusion.

:::

:::
