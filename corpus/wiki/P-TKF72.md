---
schema: qual/card@1
id: P-TKF72
kind: problem
title: The integral of $f$ over a large circular arc of angle $\alpha$ tends to $iA\alpha$ when $zf(z)\to A$
classification:
  areas:
  - complex-analysis
  topics:
  - residues
  - contour-integration
  - laurent-series
relations: []
review: draft
solved: true
---
:::{.problem title="?"}
Let $0\leq \alpha \leq 2\pi$ be a fixed angle.
Suppose $f$ is continuous on the region $\Omega = \ts{\abs{z} \geq R, \Arg(z) \in [0, \alpha]}$ and $\lim_{z\to \infty} zf(z) = A$.
Show that
\[
\lim_{z\to \infty} \int_{\gamma_R} f(z) \dz = iA\alpha
,\]
where $\gamma_R \da \ts{ \abs{z} = R, \Arg(z) \in [0, \alpha]}$ is an arc.
:::

:::{.solution}
Key observation:
\[
iA\alpha = \int_\gamma {A\over z}\dz
.\]
Why this is true:
\[
\int_\gamma {A\over z}\dz = \int_0^\alpha {1\over Re^{it}} iRe^{it}dt
= \int_0^\alpha iA \dt = iA\alpha
.\]

Now estimate the difference:

\[
\abs{ \int_\gamma f(z) \dz - iA\alpha }
&= \abs{ \int_\gamma f(z) \dz - \int_\gamma {A\over z} \dz}\\
&= \abs{\int_\gamma f(z) - {A\over z} \dz} \\
&= \abs{\int_\gamma{zf(z) - A \over z} \dz} \\
&\leq \int_\gamma \abs{zf(z) - A \over z} \dz \\
&= \int_\gamma { \abs{zf(z) - A} \over R} \dz \\
&\leq {1\over R } \int_\gamma \norm{zf(z) - A}_{\infty, \gamma} \dz \\
&= {\eps\over R}\cdot \length(\gamma) \\
&= {\eps \over R} \cdot R\alpha \\
&= \eps \alpha \\
&\convergesto{R\to\infty}0
.\]



:::

