---
schema: qual/card@1
id: P-P6D6X
kind: problem
title: $f_n\to f$ almost everywhere in $L^1$ with $\int|f_n|\to\int|f|$ implies $\int
  f_n\to\int f$
classification:
  areas:
  - real-analysis
  topics:
  - Convergence of Integrals
  - Fatou
  - L¹
relations: []
review: draft
solved: true
---

Suppose that

- $f_n, f \in L^1$,
- $f_n \to f$ almost everywhere, and
- $\int\left|f_{n}\right| \rightarrow \int|f|$.

Show that $\int f_{n} \rightarrow \int f$.

:::{.solution}
:::{.concept}
- $\int \abs{f_n - f} \to \iff \int f_n = \int f$.
- Fatou:
\[
\int \liminf f_n \leq \liminf \int f_n \\
\int \limsup f_n \geq \limsup \int f_n
.\]
:::

- Since $\int \abs{f_n} \converges{n\to\infty}\to \int \abs{f}$, define
\[
h_n &= \abs{f_n - f} &\converges{n\to\infty}\to 0 ~a.e.\\
g_n &= \abs{f_n} + \abs{f} &\converges{n\to\infty}\to 2\abs {f} ~a.e.
\]

  - Note that $g_n - h_n \converges{n\to\infty}\to 2\abs{f} - 0 = 2\abs{f}$.

- Then
\[
\int 2 \abs {f} 
&= \int \liminf_n (g_n - h_n) \\
&= \int \liminf_n(g_n) + \int \liminf_n(-h_n) \\
&= \int \liminf_n(g_n) - \int \limsup_n(h_n) \\
&= \int 2 \abs{f} - \int \limsup_n(h_n) \\
&\leq \int 2\abs{f} - \limsup_n \int h_n \quad\text{by Fatou}
,\]

- Since $f\in L^1$, $\int 2\abs{f}  = 2\norm{f}_1 < \infty$ and it makes sense to subtract it from both sides, thus
\[
0 &\leq - \limsup_n \int h_n \\
&\definedas - \limsup_n \int \abs{f_n - f}
.\]
  which forces $\limsup_n \int \abs{f_n -f}  = 0$, since
    
    - The integral of a nonnegative function is nonnegative, so $\int \abs{f_n - f} \geq 0$.
    - So $\qty{ -\int \abs{f_n - f} } \leq 0$.
    - But the above inequality shows $\qty{ -\int \abs{f_n - f} } \geq 0$ as well.
- Since $\liminf_n \int h_n \leq \limsup_n \int h_n = 0$, $\lim_n \int h_n$ exists and is equal to zero.

- But then 
\[
\abs{\int f_n - \int f}
&= \abs{\int f_n -f}
\leq \int \abs{f_n - f}
,\]
  and taking $\lim_{n\to\infty}$ on both sides yields
  \[
  \lim_{n\to\infty} \abs{\int f_n - \int f} \leq \lim_{n\to\infty} \int \abs{f_n - f} = 0
  ,\]
  so $\lim_{n\to\infty} \int f_n = \int f$.
:::

