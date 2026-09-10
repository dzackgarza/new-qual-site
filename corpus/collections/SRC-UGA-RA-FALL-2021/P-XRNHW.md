---
schema: qual/card@1
id: P-XRNHW
kind: problem
title: The bound $\int_F|x-y|^{-2}\,dx\leq 2/\delta_F(y)$, with $I(x)=\int\delta_F(y)/|x-y|^2\,dy$
  infinite off $F$ and finite a.e. on $F$
classification:
  areas:
  - real-analysis
  topics:
  - Measure Theory
  - Integrals
  - Fubini-Tonelli
relations: []
review: draft
audit:
- event: source-checked
  by: gpt-5.6-sol
  date: 2026-09-10
  note: Checked against Problem 2 of the UGA Fall 2021 real-analysis qualifying exam.
- event: solution-reviewed
  by: gpt-5.6-sol
  date: 2026-09-10
  note: Replaced malformed substitutions and corrected the false claim that mere unboundedness on a positive-measure set forces divergence of an integral.
---

:::{.problem}
a.
Let $F \subset \mathbb{R}$ be closed, and define
\[
\delta_{F}(y):=\inf _{x \in F}|x-y| .
\]
For $y \notin F$, show that
\[
\int_{F}|x-y|^{-2} d x \leq \frac{2}{\delta_F(y)},
\]
b.
Let $F \subset \mathbb{R}$ be a closed set whose complement has finite measure, i.e. $m(\RR \sm F)< \infty$. 
Define the function
\[
I(x):=\int_{\mathbb{R}} \frac{\delta_{F}(y)}{|x-y|^{2}} d y
\]
Prove that $I(x)=\infty$ if $x \not\in F$, however $I(x)<\infty$ for almost every $x \in F$. 

  > Hint: investigate $\int_{F} I(x) d x$.

:::

::: solution
<1>1. Prove the bound in part (a).
::: proof
Fix $y\notin F$ and put
\[
d:=\delta_F(y)>0.
\]
By definition of distance,
\[
F\subseteq(-\infty,y-d]\cup[y+d,\infty).
\]
Hence, after the substitution $u=x-y$,
\[
\begin{aligned}
\int_F\frac{dx}{|x-y|^2}
&\le \int_{|x-y|\ge d}\frac{dx}{|x-y|^2}\\
&=\int_{|u|\ge d}\frac{du}{u^2}\\
&=2\int_d^\infty u^{-2}\,du\\
&=\frac2d.
\end{aligned}
\]
Therefore
\[
\boxed{
\int_F|x-y|^{-2}\,dx\le\frac{2}{\delta_F(y)}.}
\]
:::

<1>2. Show that $I(x)=\infty$ for every $x\notin F$.
::: proof
Fix $x\notin F$ and set
\[
d:=\delta_F(x)>0,
\qquad r:=d/2.
\]
The distance function is $1$-Lipschitz, so if $|y-x|<r$, then
\[
\delta_F(y)\ge \delta_F(x)-|x-y|>d-r=r.
\]
Therefore
\[
\begin{aligned}
I(x)
&\ge \int_{|y-x|<r}\frac{\delta_F(y)}{|x-y|^2}\,dy\\
&\ge r\int_{|y-x|<r}\frac{dy}{|x-y|^2}\\
&=\infty,
\end{aligned}
\]
because $t^{-2}$ is not locally integrable at $0$. Thus
\[
\boxed{I(x)=\infty\quad(x\notin F).}
\]
:::

<1>3. Show that $I$ is integrable over $F$.
::: proof
The integrand is nonnegative, so Tonelli's theorem gives
\[
\begin{aligned}
\int_F I(x)\,dx
&=\int_F\int_{\mathbb R}
\frac{\delta_F(y)}{|x-y|^2}\,dy\,dx\\
&=\int_{\mathbb R}\delta_F(y)
\left(\int_F\frac{dx}{|x-y|^2}\right)dy.
\end{aligned}
\]
For $y\in F$, the factor $\delta_F(y)$ is $0$. For $y\notin F$, Step 1 gives
\[
\delta_F(y)
\int_F\frac{dx}{|x-y|^2}
\le2.
\]
Hence
\[
\int_F I(x)\,dx
\le2m(\mathbb R\setminus F)<\infty.
\]
:::

<1>4. Deduce finiteness almost everywhere on $F$.
::: proof
The function $I$ is nonnegative. If the set
\[
E:=\{x\in F:I(x)=\infty\}
\]
had positive measure, then
\[
\int_F I(x)\,dx=\infty,
\]
contradicting Step 3. Therefore $m(E)=0$, and
\[
\boxed{I(x)<\infty\text{ for almost every }x\in F.}
\]
:::
:::

