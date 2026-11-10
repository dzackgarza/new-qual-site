---
schema: qual/card@1
id: E-Q7W4S
kind: problem
title: Separate continuity does not imply continuity
classification:
  areas:
  - topology
  topics:
  - Continuous Functions
  - Product Topology
relations: []
review: draft
audit:
- event: source-checked
  by: claude
  date: 2026-11-10
  note: >-
    Read against Munkres, Topology (2000), §18 Exercise 12, printed p. 112; the function and
    the three parts are stored as printed.
- event: solution-written
  by: claude
  date: 2026-11-10
  note: >-
    Transcribed from the located published solution: "positron0802", "Solutions to Topology,
    Chapter 2" (1 January 2021), Exercise 18.12, PDF p. 13. From them: the slices are
    constant when y_0 = 0 and rational otherwise, so separately continuous; g is 1/2 off 0
    and 0 at 0; and the neighbourhood (-1/2,1/2) of F(0 x 0) contains no image of a
    neighbourhood of 0 x 0, since every such neighbourhood contains points x x x with F =
    1/2. (tmp/sources/munkres-solutions-positron-ch2.pdf).
---

::: {.exercise}

Let $F: \RR \times \RR \to \RR$ be defined by the equation

$$
F(x \times y) =
\begin{cases}
xy/(x^2 + y^2) & \text{if } x \times y \neq 0 \times 0, \\
0 & \text{if } x \times y = 0 \times 0.
\end{cases}
$$

(a) Show that $F$ is continuous in each variable separately.

(b) Compute the function $g: \RR \to \RR$ defined by $g(x) = F(x \times x)$.

(c) Show that $F$ is not continuous.
:::

::: {.solution}
The complete published solution is **"positron0802", *Solutions to Topology, Chapter 2* (1 January 2021), Exercise 18.12, PDF p. 13** (`tmp/sources/munkres-solutions-positron-ch2.pdf`); the three parts are theirs, and Whitman, printed pp. 188--189, gives the same, proving (c) by composing with the diagonal map instead of testing the neighbourhood directly.

(a) Fix $y_{0}\in\RR$ and put $h(x)=F(x\times y_{0})$. If $y_{0}=0$ then $x\times y_{0}=x\times0$ has second coordinate $0$, so $h(x)=0$ for $x=0$ by the second clause and $h(x)=x\cdot0/(x^{2}+0)=0$ for $x\ne0$: $h$ is constant, hence continuous. If $y_{0}\ne0$ then $x^{2}+y_{0}^{2}>0$ for every $x$, so $h(x)=xy_{0}/(x^{2}+y_{0}^{2})$ is a quotient of polynomials with nonvanishing denominator, hence continuous. So $F$ is continuous in the first variable. The same computation with the roles of the variables exchanged shows it is continuous in the second variable.

(b) For $x\ne0$, $F(x\times x)=x\cdot x/(x^{2}+x^{2})=1/2$, and $F(0\times0)=0$. So
$$
g(x)=\begin{cases}\tfrac12,&x\ne0,\\ 0,&x=0.\end{cases}
$$

(c) $F$ is not continuous. The set $V=(-\tfrac12,\tfrac12)$ is a neighbourhood of $F(0\times0)=0$. Let $U$ be any neighbourhood of $0\times0$ in $\RR^{2}$; it contains a product $(a,b)\times(c,d)$ with $a<0<b$, $c<0<d$, and hence contains the point $x\times x$ for $x\ne0$ with $\abs{x}<\min(b,d)$. For that point $F(x\times x)=\tfrac12\notin V$. So no neighbourhood of $0\times0$ is mapped into $V$, and $F$ is not continuous at $0\times0$.
:::
