---
schema: qual/card@1
id: P-TIE-F11-20
kind: problem
title: Uniform continuity of $z^2$ on disks but not on $\mathbb{C}$
classification:
  areas:
  - complex-analysis
  topics: []
relations: []
review: draft
audit:
- event: source-checked
  by: chatgpt
  date: 2026-09-12
  note: Checked against the retained Questions_from_Tie.pdf compilation, section Fall 2011, question 20.
- event: source-checked
  by: claude-opus-5
  date: 2026-09-16
  note: Split off the Laplace-equation problem that the source prints under Fall 2011, question 20, page 6 of Questions_from_Tie.pdf, leaving the uniform-continuity problem and a remark.
---

::: {.problem}
Show that $f(z) = z^2$ is uniformly continuous in any open disk $\abs{z} < R$, where $R > 0$ is fixed, but it is not uniformly continuous on $\mathbb{C}$.
:::

::: {.remark}
Under this number the source also prints, as parts (1) and (2), the Cauchy problem for the Laplace equation with $u(x,y) = \frac{e^{ny} - e^{-ny}}{2n^2}\sin nx$ on the unit disk, which is question 19 of the Fall 2009 list.
It is a separate problem, carried by its own card.
:::

::: {.solution}
<1>1. For all $z,w$ with $\abs{z}<R$ and $\abs{w}<R$,
$$
\abs{z^2-w^2}
<
2R\abs{z-w}.
$$

::: {.proof}
Factor the difference:
$$
z^2-w^2=(z-w)(z+w).
$$
Hence
$$
\begin{aligned}
\abs{z^2-w^2}
&=
\abs{z-w}\abs{z+w}\\
&\le
\abs{z-w}\left(\abs{z}+\abs{w}\right)\\
&<
2R\abs{z-w}.
\end{aligned}
$$
:::

<1>2. The function $f(z)=z^2$ is uniformly continuous on the open disk $\abs{z}<R$.

::: {.proof}
Let $\varepsilon>0$ and choose
$$
\delta\coloneqq\frac{\varepsilon}{2R}.
$$
If $\abs{z}<R$, $\abs{w}<R$, and $\abs{z-w}<\delta$, then by step <1>1,
$$
\abs{f(z)-f(w)}
<
2R\delta
=
\varepsilon.
$$
The choice of $\delta$ depends only on $\varepsilon$ and $R$, not on the points $z,w$, so $f$ is uniformly continuous on the disk.
:::

<1>3. The function $f(z)=z^2$ is not uniformly continuous on $\CC$.

::: {.proof}
For each positive integer $n$, let
$$
z_n=n,
\qquad
w_n=n+\frac1n.
$$
Then
$$
\abs{z_n-w_n}
=
\frac1n
\longrightarrow0,
$$
but
$$
\begin{aligned}
\abs{f(w_n)-f(z_n)}
&=
\left|
\left(n+\frac1n\right)^2-n^2
\right|\\
&=
2+\frac1{n^2}
\longrightarrow2.
\end{aligned}
$$
If $f$ were uniformly continuous on $\CC$, pairs of points whose distance tends to $0$ would have image distances tending to $0$. The displayed sequences contradict this.
:::

<1>4. Q.E.D.

::: {.proof}
Step <1>2 proves uniform continuity on every fixed open disk, and step <1>3 proves failure of uniform continuity on $\CC$.
:::
:::
