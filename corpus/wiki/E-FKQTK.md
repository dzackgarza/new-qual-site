---
schema: qual/card@1
id: E-FKQTK
kind: exercise
title: "Automorphisms of $\\CC$"
classification:
  areas:
  - complex-analysis
  topics: []
relations: []
review: draft
---
:::{.exercise title="Automorphisms of $\CC$"}
Show that $\Aut(\CC) = \ts{ z \mapsto az+b\st a\in \CC\units, b\in \CC }$.

#complex/exercise/completed

:::

:::{.solution}
$\supseteq$:
Clear, every affine function is bijective with inverse $g(z) \da a\inv(z-b)$, and holomorphic since
\[
g(f(z)) = z \implies g'(f(z)) f'(z) = 1 \implies g'(w) = {1\over f'(f\inv(w))}
.\]

$\subseteq$:
Suppose $f$ is entire and bijective.
If $f$ is bounded, then $f(z) = b$ is constant by Liouville and we're done, so suppose not.
Then $\abs{f(z)}\to \infty$ as $\abs{z}\to \infty$, making $z=\infty$ either an essential singularity or a pole, since it is isolated and not removable since $f$ is unbounded in every small enough neighborhood of $\infty$.
If $f(b) = 0$ without loss of generality we can translate to assume $f(0) = 0$ by replacing $f(z)$ with $f(z) - b$.
By bijectivity, $z=0$ must be a zero of order 1, so ${1\over f(z)}$ has a pole of order 1 at $z=0$.
So define $G(z) \da {z\over f(z)}$, which is now an entire function.

On a large enough disc, $\abs{f(z)} > 1$ for all $\abs{z} > R$, so $\abs{G(z)} < 1R\inv$ on $\abs{z} > R$.
Since $G$ is holomorphic and thus continuous on $\abs{z}\leq R$, which is compact, $G$ is bounded here too.
Thus $G$ is constant by Liouville, and $G(z) = c \implies f(z) = c\inv z \da az$.
Unwinding the initial translation that ensured $f(0)=0$, we get $f(z) = az + b$.
:::
