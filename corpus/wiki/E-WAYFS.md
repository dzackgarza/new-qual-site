---
schema: qual/card@1
id: E-WAYFS
kind: exercise
title: "Zeros of $\\sin(\\pi z)$ and singularities of $\\csc(\\pi z)$"
classification:
  areas:
  - complex-analysis
  topics: []
relations: []
review: draft
---
:::{.exercise title="Zeros of $\sin(\pi z)$ and singularities of $\csc(\pi z)$"}
Show that the complex zeros of $f(z) \da \sin(\pi z)$ are exactly $\ZZ$, and each is order 1.
Calculate the residue of $1/\sin(\pi x)$ at $z=n\in \ZZ$.

:::

:::{.solution}
Write
\[
f(z) = \sin(\pi z) = (2i)\inv (e^{i\pi z} - e^{-i\pi z}) = 0 \iff e^{i 2\pi z} = 1 = e^{i 2k\pi} \iff 2\pi z = 2k\pi \iff z=k\in \ZZ
.\]
To see that these zeros are order one, write
\[
\sin(\pi z) 
&= \sin(\pi(z-k) + k\pi) \\
&= \pm \sin(\pi(z-k)) \\
&= \pm\qty{ \pi(z-k) - {\pi^3\over 3!}(z-k)^3 + \cdots } \\
&= (z-k)^1 \cdot \pm \qty{ \pi - {\pi^3\over 3!}(z-k)^2 + \cdots } \da (z-k)g(z) \\
\]
where $g(k) = \pm \pi \neq 0$, making $z=k$ an order 1 zero.

For the residues:
\[
\Res_{z=k} \csc(\pi z) = \lim_{z\to k} (z-k)\csc(\pi z) \eqLH \sec(k\pi) = (-1)^{k+1}
.\]
:::
