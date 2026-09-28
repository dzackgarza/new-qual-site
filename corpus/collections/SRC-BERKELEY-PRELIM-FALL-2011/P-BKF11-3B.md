---
schema: qual/card@1
id: P-BKF11-3B
kind: problem
title: The automorphism group of the unit disk acts transitively
classification:
  areas: [prelim]
  topics: []
relations: []
review: draft
audit:
- event: source-checked
  by: chatgpt
  date: 2026-09-12
  note: Checked against Problem 3B of the retained Berkeley Fall 2011 preliminary-exam solution packet f11solutions.pdf.
- event: solution-written
  by: chatgpt
  date: 2026-09-24
- event: solution-reviewed
  by: chatgpt
  date: 2026-09-24
  note: >-
    Checked the disk-preserving identity for the Möbius transformations,
    their explicit inverses, and the composition sending a to b.
---

::: {.problem}
If $a$ and $b$ are points in the open unit disk of the complex plane, show that there is a holomorphic bijection of the open unit disk onto itself, with holomorphic inverse, that takes $a$ to $b$.
:::

::: {.solution}
Let
$$
\DD\coloneqq\{z\in\CC:\abs{z}<1\}.
$$
For $c\in\DD$, define
$$
\phi_c(z)\coloneqq\frac{z-c}{1-\overline c\,z}.
$$

<1>1. For every $c,z\in\DD$, the denominator of $\phi_c(z)$ is
nonzero and
$$
1-\abs{\phi_c(z)}^2
=\frac{(1-\abs c^2)(1-\abs z^2)}
       {\abs{1-\overline c\,z}^2}>0.
$$
Hence $\phi_c$ is holomorphic on $\DD$ and maps $\DD$ into itself.

::: {.proof}
Since $\abs{\overline c\,z}<1$, one has
$1-\overline c\,z\ne0$. Moreover,
$$
\begin{aligned}
\abs{1-\overline c\,z}^2-\abs{z-c}^2
&=(1-\overline c\,z)(1-c\overline z)
 -(z-c)(\overline z-\overline c)\\
&=(1-\abs c^2)(1-\abs z^2).
\end{aligned}
$$
Dividing by $\abs{1-\overline c\,z}^2$ gives the displayed
identity. Both factors in its numerator are positive for
$c,z\in\DD$, so $\abs{\phi_c(z)}<1$.
:::

<1>2. The map
$$
\psi_c(w)\coloneqq\frac{w+c}{1+\overline c\,w}
$$
is the inverse of $\phi_c$ on $\DD$.

::: {.proof}
The same denominator estimate as in step <1>1 gives
$1+\overline c\,w\ne0$ for $w\in\DD$. Direct substitution gives
$$
\phi_c(\psi_c(w))=w
\qquad\text{and}\qquad
\psi_c(\phi_c(z))=z.
$$
By step <1>1, $\phi_c$ maps $\DD$ into itself; applying the same
identity with $-c$ shows that
$$
\psi_c=\phi_{-c}
$$
also maps $\DD$ into itself. Thus the two maps are mutually inverse
holomorphic self-maps of $\DD$.
:::

<1>3. The map
$$
\boxed{F\coloneqq\psi_b\circ\phi_a}
$$
is a holomorphic bijection $\DD\to\DD$ with holomorphic inverse and
satisfies $F(a)=b$.

::: {.proof}
By step <1>2, both factors are holomorphic automorphisms of $\DD$, so
their composition is as well, with inverse
$$
F^{-1}=\psi_a\circ\phi_b.
$$
Also
$$
\phi_a(a)=0
\qquad\text{and}\qquad
\psi_b(0)=b,
$$
so $F(a)=b$.
:::

<1>4. Q.E.D.

::: {.proof}
Step <1>3 constructs the required map.
:::
:::
