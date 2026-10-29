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
Let $f\in L^1(\RR)$ and $\beta\in(0,1)$.
Prove that
\[
\int_{\RR}\frac{|f(x)|}{|x-a|^\beta}\,dx<\infty
\]
for Lebesgue-almost every $a\in\RR$.
:::

::: {.solution}

For $a\in\RR$, define
\[
F(a)
\coloneqq
\int_{\RR}
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

::: {.pf-step #s1-1}

There is a constant $C_\beta<\infty$, depending only on $\beta$, such that for every $x\in\RR$,
\[
\int_{\RR}
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
\int_{\RR}\frac{da}{1+a^2}
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

::: {.pf-step #s1-2}

One has
\[
\int_{\RR}w(a)F(a)\,da
\le
C_\beta\|f\|_{L^1(\RR)}
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
\int_{\RR}w(a)F(a)\,da
&=
\int_{\RR}
\int_{\RR}
w(a)\frac{|f(x)|}{|x-a|^\beta}\,dx\,da\\
&=
\int_{\RR}
|f(x)|
\left(
\int_{\RR}
\frac{w(a)}{|x-a|^\beta}\,da
\right)dx.
\end{aligned}
\]
Apply step [](#s1-1){.pf-ref} to the inner integral:
\[
\int_{\RR}w(a)F(a)\,da
\le
C_\beta
\int_{\RR}|f(x)|\,dx.
\]
The right-hand side is finite because $f\in L^1(\RR)$.

:::

:::

::: {.pf-step #s1-3}

The set
\[
E
\coloneqq
\{a\in\RR:F(a)=\infty\}
\]
has Lebesgue measure zero.


::: pf-proof

The weight $w(a)=(1+a^2)^{-1}$ is strictly positive for every $a\in\RR$. If $E$ had positive measure, then
\[
w(a)F(a)=\infty
\qquad
(a\in E),
\]
so the nonnegative integral
\[
\int_{\RR}w(a)F(a)\,da
\]
would be infinite. This contradicts step [](#s1-2){.pf-ref}. Hence $m(E)=0$.

:::

:::

::: {.pf-step #s1-4}

Therefore
\[
\boxed{
\int_{\RR}
\frac{|f(x)|}{|x-a|^\beta}\,dx
<
\infty
}
\]
for Lebesgue-almost every $a\in\RR$.


::: pf-proof

By definition, the integral is $F(a)$, and step [](#s1-3){.pf-ref} shows that $F(a)<\infty$ outside a null set.

:::

:::

::: pf-qed

Step [](#s1-4){.pf-ref} is the required conclusion.

:::

:::

:::
