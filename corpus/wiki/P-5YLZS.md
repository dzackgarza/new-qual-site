---
schema: qual/card@1
id: P-5YLZS
kind: problem
title: "Suppose $f(x)$ and $xf(x)$ are integrable on $\\RR$. Define $F$ by $F(t)\\definedas \\int _{-\\infty}^{\\infty} f(x) \\cos (x t) dx$ Show that $F'(t)=-\\int _{-\\infty}^{\\infty} x f(x) \\sin (x t) dx$"
classification:
  areas:
  - real-analysis
  topics:
  - differentiation
  - integrals
relations: []
review: draft
---
Suppose $f(x)$ and $xf(x)$ are integrable on $\RR$.
Define $F$ by
\[
F(t)\definedas \int _{-\infty}^{\infty} f(x) \cos (x t) dx
\]
Show that 
\[
F'(t)=-\int _{-\infty}^{\infty} x f(x) \sin (x t) dx
.\]

:::{.solution}
\hfill
:::{.concept}
\hfill
- Mean Value Theorem
- DCT
:::
\[
\dd{}{t} F(t) 
&= \dd{}{t} \int_\RR f(x) \cos(xt) ~dx \\
&\overset{DCT}= \int_\RR f(x) \dd{}{t} \cos(xt) ~dx \\
&= \int_\RR xf(x) \cos(xt)~dx
,\]
so it only remains to justify the DCT.

- Fix $t$, then let $t_n \to t$ be arbitrary.
- Define 
$$
h_n(x, t) = f(x)
\left(\frac{\cos(tx) - \cos(t_n x)}{t_n - t}\right) \converges{n\to\infty}\to \dd{}{t} \qty{f(x) \cos(xt)}
$$
 since $\cos(tx)$ is differentiable in $t$ and this is the limit definition of differentiability.

- Note that
\[
\dd{}{t} \cos(tx) 
&\definedas \lim_{t_n \to t} \frac{\cos(tx) - \cos(t_n x)}{t_n - t} \\
&\overset{MVT} = \dd{}{t}\cos(tx)\mid_{t  = \xi_n} \hspace{6em} \text{for some } \xi_n \in [t, t_n] \text{ or } [t_n, t] \\
&= x\sin(\xi_n x)
\]
  where $\xi_n \converges{n\to\infty}\to t$ since wlog $t_n \leq \xi_n \leq t$ and $t_n \nearrow t$.

- We then have $$\abs{h_n(x)} = \abs{f(x) x\sin(\xi_n x)} \leq \abs{xf(x)}\quad\text{since } \abs{\sin(\xi_n x)} \leq  1$$ for every $x$ and every $n$.
- Since $xf(x) \in L^1(\RR)$ by assumption, the DCT applies. 
:::
