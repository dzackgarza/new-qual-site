---
schema: qual/card@1
id: P-BERK96S-04
kind: problem
title: Five roots of $\varepsilon z^7+z^2+1$ lie in a scaled annulus
classification:
  areas:
  - prelim
  topics: []
relations: []
review: draft
audit:
- event: source-checked
  by: gpt-5.6-sol
  date: 2026-09-13
- event: source-corrected
  by: chatgpt
  date: 2026-09-23
  note: >-
    The source prints r<1<R, but r>0 is necessary: for r<=0 the stated
    region contains all seven roots for sufficiently small epsilon. Added the
    missing positivity hypothesis.
- event: solution-written
  by: chatgpt
  date: 2026-09-23
- event: solution-reviewed
  by: chatgpt
  date: 2026-09-23
  note: >-
    Verified both Rouché comparisons, the strict boundary exclusions, the
    multiplicity count, and the necessity of the added hypothesis r>0.
---

::: {.problem}
Let $0<r<1<R$. Show that for all sufficiently small $\varepsilon>0$, the polynomial
\[
p(z)=\varepsilon z^7+z^2+1
\]
has exactly five roots, counted with multiplicity, in the annulus
\[
r\varepsilon^{-1/5}<|z|<R\varepsilon^{-1/5}.
\]
:::

::: {.solution}
Put
$$
\delta
\coloneqq
\min\{r^2-r^7,\ R^7-R^2\}.
$$
Since $0<r<1<R$, one has $\delta>0$. Choose $\varepsilon_0>0$ so that
$$
\varepsilon_0^{2/5}<\delta,
$$
and fix $0<\varepsilon<\varepsilon_0$.

<1>1. The polynomial $p$ has exactly two zeros, counted with multiplicity,
in
$$
\abs{z}<r\varepsilon^{-1/5}.
$$

::: {.proof}
On the circle
$$
\abs{z}=r\varepsilon^{-1/5},
$$
one has
$$
\begin{aligned}
\abs{\varepsilon z^7+1}
&\leq
\varepsilon\abs{z}^7+1\\
&=
r^7\varepsilon^{-2/5}+1\\
&<
r^7\varepsilon^{-2/5}
+(r^2-r^7)\varepsilon^{-2/5}\\
&=
r^2\varepsilon^{-2/5}
=
\abs{z^2}.
\end{aligned}
$$
The strict inequality uses
$$
\varepsilon^{2/5}<\delta\leq r^2-r^7.
$$
Thus, by Rouché's theorem, the functions
$$
p(z)=z^2+(\varepsilon z^7+1)
$$
and $z^2$ have the same number of zeros inside this circle. Hence $p$ has
exactly two such zeros.
:::

<1>2. The polynomial $p$ has exactly seven zeros, counted with multiplicity,
in
$$
\abs{z}<R\varepsilon^{-1/5}.
$$

::: {.proof}
On the circle
$$
\abs{z}=R\varepsilon^{-1/5},
$$
one has
$$
\begin{aligned}
\abs{z^2+1}
&\leq
\abs{z}^2+1\\
&=
R^2\varepsilon^{-2/5}+1\\
&<
R^2\varepsilon^{-2/5}
+(R^7-R^2)\varepsilon^{-2/5}\\
&=
R^7\varepsilon^{-2/5}
=
\abs{\varepsilon z^7}.
\end{aligned}
$$
Here
$$
\varepsilon^{2/5}<\delta\leq R^7-R^2.
$$
Rouché's theorem therefore shows that
$$
p(z)=\varepsilon z^7+(z^2+1)
$$
and $\varepsilon z^7$ have the same number of zeros inside this circle,
namely seven.
:::

<1>3. The annulus
$$
r\varepsilon^{-1/5}
<
\abs{z}
<
R\varepsilon^{-1/5}
$$
contains exactly
$$
\boxed{5}
$$
zeros of $p$, counted with multiplicity.

::: {.proof}
The strict inequalities in steps <1>1 and <1>2 show in particular that $p$
has no zero on either boundary circle. By step <1>2 there are seven zeros
inside the outer circle, while by step <1>1 exactly two lie inside the inner
circle. Therefore the number in the annulus is
$$
7-2=5.
$$
:::

<1>4. Q.E.D.

::: {.proof}
Step <1>3 proves the asserted root count for every
$0<\varepsilon<\varepsilon_0$.
:::
:::

::: {.remark}
The source prints only $r<1<R$. The omitted condition $r>0$ is necessary.
If $r\leq0$, choose $\varepsilon>0$ small enough that
$$
\varepsilon^{2/5}<R^7-R^2.
$$
Then the outer-circle argument in step <1>2 places all seven roots inside
$\abs{z}<R\varepsilon^{-1/5}$. Since $p(0)=1$, every root also satisfies
$r\varepsilon^{-1/5}<\abs{z}$. Thus the printed hypotheses would put all
seven roots, rather than five, in the displayed region.
:::
