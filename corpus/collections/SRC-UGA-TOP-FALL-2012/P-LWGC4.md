---
schema: qual/card@1
id: P-LWGC4
kind: problem
title: Fixed points of $\id_{\RP^2}\vee\ast$ and $\ast\vee\id_{S^1}$ on $\RP^2\vee
  S^1$
classification:
  areas:
  - topology
  topics:
  - Fixed Points
  - Homotopy
relations: []
review: draft
audit:
- event: source-checked
  by: gpt-5.6-sol
  date: 2026-09-05
  note: Checked the statement against problem 6 of the official UGA Fall 2012 topology exam.
- event: solution-written
  by: gpt-5.6-sol
  date: 2026-09-05
- event: solution-reviewed
  by: gpt-5.6-sol
  date: 2026-09-05
  note: >-
    Used rational Lefschetz numbers to rule out a fixed-point-free representative
    for id_RP2 wedge constant, and constructed an explicit rotating
    fixed-point-free representative of constant wedge id_S1.
---

::: problem
Let $f = \id_{\RP^2} \lor \ast$ and $g = \ast \lor id_{S^1}$ be two maps of $\RP^2 \lor S^1$ to itself where $\ast$ denotes the constant map of a space to its basepoint.

Show that one map is homotopic to a map with no fixed points, while the other is not.
:::

::: {.solution}
Put
\[
X=\RP^2\vee S^1
\]
and let $x_0$ denote the wedge point.

<1>1. With rational coefficients,
\[
H_k(X;\QQ)\cong
\begin{cases}
\QQ,&k=0,1,\\
0,&k\ge2.
\end{cases}
\]
The degree-$1$ generator comes from the $S^1$ summand.
::: {.proof}
The integral homology of $\RP^2$ is
\[
H_0(\RP^2;\ZZ)=\ZZ,
\qquad
H_1(\RP^2;\ZZ)=\ZZ/2\ZZ,
\qquad
H_k(\RP^2;\ZZ)=0\quad(k\ge2).
\]
After tensoring with $\QQ$, the torsion group in degree $1$ vanishes.
Reduced homology takes wedges to direct sums, while $S^1$ contributes one copy of $\QQ$ in degree $1$.
This gives the displayed groups.
:::

<1>2. For
\[
f=\id_{\RP^2}\vee *,
\]
one has
\[
L(f)=1.
\]
::: {.proof}
Since $X$ is connected, $f_*$ is the identity on $H_0(X;\QQ)$ and has trace $1$.
The only nonzero positive-degree rational homology is the circle class in $H_1$, and $f$ collapses the $S^1$ summand to $x_0$.
Hence
\[
f_*:H_1(X;\QQ)\longrightarrow H_1(X;\QQ)
\]
is zero and has trace $0$.
Therefore
\[
L(f)=1-0=1.
\]
:::

<1>3. No map homotopic to $f$ can be fixed-point-free.
::: {.proof}
If $h\simeq f$, homotopy invariance gives
\[
L(h)=L(f)=1\ne0.
\]
The space $X$ is a finite CW complex, so the Lefschetz fixed-point theorem applies and forces $h$ to have a fixed point.
:::

<1>4. The map
\[
g=*\vee\id_{S^1}
\]
is homotopic to a map $h:X\to X$ defined by a nontrivial rotation on the circle and a compatible constant map on $\RP^2$.
::: {.proof}
Identify the circle summand with the unit circle in $\CC$ and take the wedge point to be
\[
x_0=1\in S^1.
\]
Choose an angle
\[
0<\theta<2\pi.
\]
For $0\le t\le1$, define a map $H_t:X\to X$ by
\[
H_t(z)=e^{i\theta t}z
\qquad(z\in S^1)
\]
and
\[
H_t(x)=e^{i\theta t}
\qquad(x\in\RP^2).
\]
At the wedge point the two formulas agree, since
\[
H_t(1)=e^{i\theta t}.
\]
Hence the pasting lemma gives a continuous map $H_t$ on the wedge, continuously depending on $t$.

At $t=0$, the circle formula is the identity and the $\RP^2$ formula is constant at $x_0$, so
\[
H_0=g.
\]
Set
\[
h=H_1.
\]
Thus $h\simeq g$.
:::

<1>5. The map $h$ from <1>4 has no fixed points.
::: {.proof}
On the $S^1$ summand,
\[
h(z)=e^{i\theta}z.
\]
If this equaled $z$, then $e^{i\theta}=1$, contrary to $0<\theta<2\pi$.
Thus there are no fixed points on the circle.

For every $x\in\RP^2$,
\[
h(x)=e^{i\theta}\in S^1\setminus\{x_0\}.
\]
The two wedge summands intersect only at $x_0$, so this image cannot equal any $x\in\RP^2$.
In particular
\[
h(x_0)=e^{i\theta}\ne x_0.
\]
Hence $h$ is fixed-point-free on all of $X$.
:::

<1>6. Therefore
\[
\boxed{g=*\vee\id_{S^1}\text{ is homotopic to a fixed-point-free map, while }f=\id_{\RP^2}\vee *\text{ is not}.}
\]
::: {.proof}
The impossibility for $f$ is <1>3, and <1>4--<1>5 construct the required representative for $g$.
:::
:::
