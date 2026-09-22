---
schema: qual/card@1
id: P-BERK91S-06
kind: problem
title: A radial vector field has zero circulation around every closed path avoiding the origin
classification:
  areas: [prelim]
  topics: []
relations: []
review: draft
audit:
- event: source-checked
  by: gpt-5.6-sol
  date: 2026-09-13
- event: source-checked
  by: chatgpt
  date: 2026-09-22
  note: Compared the radial field, smoothness domain of g, and closed-path conclusion with Problem 6 in the retained MinerU Flash extraction of Spring91.pdf.
- event: solution-written
  by: chatgpt
  date: 2026-09-22
---

::: {.problem}
Let
$$
F(r)=g(\norm{r})r,
\qquad r\ne0,
$$
be a vector field on $\RR^3\setminus\{0\}$, where $g:(0,\infty)\to\RR$ is smooth. Prove that
$$
\int_C F\cdot ds=0
$$
for every smooth closed path $C$ in $\RR^3$ that avoids the origin.
:::

::: {.solution}
Let $U\coloneqq\RR^3\setminus\{0\}$. Define $G:(0,\infty)\to\RR$ and
$\Phi:U\to\RR$ by
$$
G(s)\coloneqq\int_1^s t g(t)\,dt,
\qquad
\Phi(r)\coloneqq G(\norm{r}).
$$

<1>1. The function $\Phi$ is smooth on $U$ and $\nabla\Phi=F$.

::: {.proof}
The fundamental theorem of calculus gives $G'(s)=s g(s)$ for $s>0$.
Since $g$ is smooth, so is $G$. The Euclidean norm is smooth on $U$,
so $\Phi$ is smooth there. For $r=(r_1,r_2,r_3)\in U$ and $1\le j\le3$,
the chain rule gives
$$
\frac{\partial\Phi}{\partial r_j}(r)
=G'(\norm{r})\frac{r_j}{\norm{r}}
=\norm{r}g(\norm{r})\frac{r_j}{\norm{r}}
=g(\norm{r})r_j.
$$
These are the components of $F(r)$, proving $\nabla\Phi(r)=F(r)$.
:::

<1>2. For every smooth closed path $C$ in $U$, $\int_C F\cdot ds=0$.

::: {.proof}
Let $\gamma:[a,b]\to U$ parametrize $C$, with $\gamma(a)=\gamma(b)$.
By step <1>1 and the chain rule,
$$
\begin{aligned}
\int_C F\cdot ds
&=\int_a^b F(\gamma(t))\cdot\gamma'(t)\,dt\\
&=\int_a^b\frac{d}{dt}\Phi(\gamma(t))\,dt\\
&=\Phi(\gamma(b))-\Phi(\gamma(a))\\
&=0.
\end{aligned}
$$
:::

<1>3. Q.E.D.

::: {.proof}
Step <1>2 proves the required vanishing for every smooth closed path
avoiding the origin.
:::
:::
