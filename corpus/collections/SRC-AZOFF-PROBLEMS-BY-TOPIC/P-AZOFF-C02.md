---
schema: qual/card@1
id: P-AZOFF-C02
kind: problem
title: Conformal map of a horizontal strip onto the unit disk
classification:
  areas: [complex-analysis]
  topics: []
relations: []
review: draft
audit:
- event: source-checked
  by: gpt-5.6-sol
  date: 2026-09-14
  note: Checked against Conformal mapping, Problem 2, in the deterministic MinerU Flash extraction assets/attachments/Azoff Problems by Topic_extracted.md.
- event: solution-written
  by: chatgpt
  date: 2026-09-21
- event: solution-reviewed
  by: chatgpt
  date: 2026-09-21
  note: >-
    Mapped the strip 0<Im z<1 biholomorphically to the upper half-plane by
    exp(pi z), using polar coordinates for surjectivity and the exponential
    period 2i for injectivity. Composing with the inverse Cayley transform
    (w-i)/(w+i) gives the disk. The source compilation contains no worked
    solution for this problem.
---

::: {.problem}
Exhibit a conformal map from the strip $\{ z \in \mathbb { C } : 0 < \operatorname { I m } ( z ) < 1 \}$ onto the open unit disk.
:::

::: {.solution}
Let
$$
S=\{z\in\CC:0<\operatorname{Im}z<1\},
\qquad
\mathcal H=\{w\in\CC:\operatorname{Im}w>0\}.
$$

<1>1. The map
$$
E:S\longrightarrow\mathcal H,
\qquad
E(z)=e^{\pi z},
$$
is a conformal bijection.

::: {.proof}
Write
$$
z=x+iy,
\qquad
0<y<1.
$$
Then
$$
E(z)
=
e^{\pi x}e^{i\pi y}.
$$
Its argument lies strictly between $0$ and $\pi$, so
$$
E(z)\in\mathcal H.
$$

Conversely, every $w\in\mathcal H$ has a unique polar representation
$$
w=re^{i\theta},
\qquad
r>0,
\quad
0<\theta<\pi.
$$
Then
$$
z=\frac{\log r}{\pi}+i\frac{\theta}{\pi}
$$
belongs to $S$ and satisfies $E(z)=w$. Thus $E$ is onto.

If $E(z_1)=E(z_2)$, then
$$
\pi(z_1-z_2)\in2\pi i\ZZ,
$$
so
$$
z_1-z_2\in2i\ZZ.
$$
But two points of $S$ have imaginary parts differing by a number strictly
between $-1$ and $1$, so the only possible multiple of $2i$ is $0$. Hence
$z_1=z_2$, and $E$ is injective.

Finally,
$$
E'(z)=\pi e^{\pi z}\neq0
$$
on $S$, so $E$ is conformal.
:::

<1>2. The map
$$
C:\mathcal H\longrightarrow\DD,
\qquad
C(w)=\frac{w-i}{w+i},
$$
is a conformal bijection.

::: {.proof}
For $w=u+iv$ with $v>0$,
$$
\abs{w+i}^2-\abs{w-i}^2
=
4v
>
0,
$$
so
$$
\abs{C(w)}<1.
$$

Solving
$$
\zeta=\frac{w-i}{w+i}
$$
for $w$ gives
$$
w=i\frac{1+\zeta}{1-\zeta},
$$
which maps $\DD$ into $\mathcal H$. Thus $C$ is bijective. Also
$$
C'(w)=\frac{2i}{(w+i)^2}\neq0
$$
on $\mathcal H$, so $C$ is conformal.
:::

<1>3. A conformal bijection from the strip $S$ onto the unit disk is
$$
\boxed{
T(z)
=
\frac{e^{\pi z}-i}{e^{\pi z}+i}
}.
$$

::: {.proof}
By steps <1>1--<1>2,
$$
T=C\circ E
$$
is a composition of conformal bijections
$$
S\xrightarrow{E}\mathcal H\xrightarrow{C}\DD.
$$
Therefore $T$ is a conformal bijection from $S$ onto $\DD$.
:::

<1>4. Q.E.D.

::: {.proof}
Step <1>3 gives the requested map.
:::
:::
