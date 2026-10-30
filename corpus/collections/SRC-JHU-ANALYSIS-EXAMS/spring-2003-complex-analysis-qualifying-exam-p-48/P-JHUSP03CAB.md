---
schema: qual/card@1
id: P-JHUSP03CAB
kind: problem
title: A second zero of a disk self-map satisfies $\abs{w}\geq\abs{f'(0)}$
classification:
  areas:
  - complex-analysis
  topics:
  - Schwarz Lemma
relations: []
review: draft
audit:
- event: source-checked
  by: chatgpt
  date: 2026-09-10
  note: "Compared the disk self-map, normalization at zero, derivative modulus M and second-zero bound with Spring 2003 problem 2."
- event: solution-written
  by: chatgpt
  date: 2026-09-10
- event: solution-reviewed
  by: chatgpt
  date: 2026-09-10
  note: "Factored f(z)=zg(z), used Schwarz and the maximum principle to make g a disk map, and applied Schwarz-Pick to obtain the stronger bound M <= |w|."
- event: source-checked
  by: chatgpt
  date: 2026-09-10
  note: "Visually checked problem 2 and the unit-disk convention on PDF page 48; restored Delta's definition and avoided a positive-separation claim when M=0."
---

::: {.problem}
Let $\Delta=\{z\in\CC:\abs{z}<1\}$, and let $f : \Delta \to \Delta$ be a holomorphic function with $f(0) = 0$ and $\abs{f'(0)} = M$.
If $0 \neq w \in \Delta$ is any other zero of $f(z)$, show that:

$$\frac{M}{1 + M} \leq \abs{w}.$$
:::

::: {.solution}
In fact the stronger estimate
$$
\boxed{M\le \abs{w}}
$$
holds.

::: pf

::: pf-step

Dividing by the fixed zero produces a holomorphic disk map.

::: pf-proof

Because $f(0)=0$, define
$$
g(z)=\begin{cases}f(z)/z,&z\ne0,\\ f'(0),&z=0.\end{cases}
$$
The Taylor expansion of $f$ at zero shows that $g$ is holomorphic on $\Delta$.
Schwarz's lemma [@SS03] applied to $f:\Delta\to\Delta$ gives $\abs{f(z)}\le \abs{z}$, so
$\abs{g(z)}\le1$ throughout the disk. Since $w\ne0$ and $f(w)=0$, one has
$g(w)=0$. Thus $g$ is not a constant of modulus one. The maximum modulus
principle therefore gives $\abs{g(z)}<1$ for every $z\in\Delta$; hence
$g:\Delta\to\Delta$ is a holomorphic self-map.

:::

:::

::: pf-step

Schwarz-Pick gives a stronger inequality than required.

::: pf-proof

Apply the Schwarz-Pick inequality [@SS03] to $g$ at the two points $0$ and $w$:
$$
\abs{\frac{g(0)-g(w)}{1-\overline{g(w)}g(0)}}
\le
\abs{\frac{0-w}{1-\overline w\,0}}.
$$
Since $g(0)=f'(0)$ and $g(w)=0$, this reduces to
$$
M=\abs{f'(0)}\le \abs{w}.
$$
Finally $M\ge0$, so
$$
\frac{M}{1+M}\le M\le \abs{w}.
$$
This is the claimed estimate.

:::

:::

:::

:::
