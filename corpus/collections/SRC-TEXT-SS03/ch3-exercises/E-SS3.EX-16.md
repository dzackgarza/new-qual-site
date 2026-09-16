---
schema: qual/card@1
id: E-SS3.EX-16
kind: problem
title: "Rouche's theorem from a simple-zero comparison"
classification:
  areas:
  - complex-analysis
  topics: ['Meromorphic Functions', 'Residue Theorem', 'Argument Principle']
relations: []
review: draft
audit:
- event: solution-written
  by: gpt-5.6-sol
  date: 2026-09-11
---

::: {.exercise}
16. Suppose f and g are holomorphic in a region containing the disc $| z | \leq 1$ Suppose that f has a simple zero at $z = 0$ and vanishes nowhere else in $| z | \leq 1$ Let

$$
f _ {\epsilon} (z) = f (z) + \epsilon g (z).
$$

Show that if ǫ is suficiently small, then

(a) $f _ { \epsilon } ( z )$ has a unique zero in $| z | \leq 1$ , and

(b) $\mathrm { i f } \ z _ { \epsilon }$ is this zero, the mapping $\epsilon \mapsto z _ { \epsilon }$ is continuous.
:::

::: {.solution}
Because $f$ has a simple zero at $0$ and no other zero on $|z|\le1$, choose $0<r<1$ so small that $0$ is the only zero of $f$ in $|z|\le r$. Since $f$ is nonzero on $|z|=r$, set
\[
m=\min_{|z|=r}|f(z)|>0,
\qquad
M=\max_{|z|=r}|g(z)|.
\]
If $|\epsilon|M<m$, then on $|z|=r$,
\[
|\epsilon g(z)|<|f(z)|.
\]
Rouché's theorem implies that $f_\epsilon=f+\epsilon g$ has exactly one zero in $|z|<r$, counted with multiplicity. On the compact annulus $r\le|z|\le1$, $f$ has positive minimum $m_1$, while $g$ has finite maximum $M_1$. If also $|\epsilon|M_1<m_1$, then $f_\epsilon$ has no zero there. Thus, for sufficiently small $\epsilon$, $f_\epsilon$ has a unique zero $z_\epsilon$ in $|z|\le1$.

To prove continuity, let $\epsilon_n\to\epsilon$ within this small disc of parameters. The zeros $z_{\epsilon_n}$ lie in the compact disc $|z|\le r$. Any convergent subsequence has a limit $z_*$. Since
\[
f(z_{\epsilon_n})+\epsilon_n g(z_{\epsilon_n})=0,
\]
continuity gives
\[
f(z_*)+\epsilon g(z_*)=0.
\]
By uniqueness of the zero for parameter $\epsilon$, $z_*=z_\epsilon$. Every convergent subsequence has the same limit, so the entire sequence converges to $z_\epsilon$. Hence $\epsilon\mapsto z_\epsilon$ is continuous.
:::
