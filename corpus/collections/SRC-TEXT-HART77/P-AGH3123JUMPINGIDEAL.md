---
schema: qual/card@1
id: P-AGH3123JUMPINGIDEAL
kind: problem
title: Jumping cohomology for the ideal sheaf of a degenerating quartic curve
classification:
  areas:
  - algebraic-geometry
  topics:
  - Semicontinuity
  - Flat Families
  - Ideal Sheaves
  - Rational Curves
relations: []
review: draft
audit:
- event: source-checked
  by: chatgpt
  date: 2026-09-18
  note: >-
    Read Exercise III.12.3, Example III.9.8.3, and the twisted-quartic source context.
    The printed untwisted cohomology claim is false; the advertised jump is obtained after twisting by O(1).
- event: solution-written
  by: chatgpt
  date: 2026-09-18
---

::: {.problem}
Let $X_1 \subseteq \PP_k^4$ be the **rational normal quartic curve**, the $4\dash$uple embedding of $\PP^1$ in $\PP^4$. Let $X_0 \subseteq \PP_k^3$ be a nonsingular rational quartic curve, such as the one in (I, Ex. 3.18b).

Use (9.8.3) to construct a flat family $\ts{X_t}$ of curves in $\PP^4$, parametrized by $T = \AA^1$, with the given fibres $X_1$ and $X_0$ for $t = 1$ and $t = 0$.

Let $\mci \subseteq \mco_{\PP^4 \times T}$ be the ideal sheaf of the total family $X \subseteq \PP^4 \times T$. Show that $\mci$ is flat over $T$. Then show that
\[
h^0(t, \mci) =
\begin{cases}
0 & t \neq 0 \\
1 & t = 0
\end{cases}
\qquad
h^1(t, \mci) =
\begin{cases}
0 & t \neq 0 \\
1 & t = 0
\end{cases}
.\]

This gives another example of cohomology groups jumping at a special point.
:::

::: {.remark title="Erratum to the printed cohomology claim"}
The two displayed jumps are not correct for the untwisted ideal sheaves
$\mci_t$. In fact, every fibre in the family below is a connected reduced
rational curve, so
$$
H^0(X_t,\mco_{X_t})=k.
$$
From
$$
0\to\mci_t\to\mco_{\PP^4}\to\mco_{X_t}\to0
$$
and $H^1(\PP^4,\mco_{\PP^4})=0$, one obtains
$$
H^0(\PP^4,\mci_t)=H^1(\PP^4,\mci_t)=0
$$
for every $t$.

The advertised values are correct after replacing $\mci_t$ by
$\mci_t(1)$. The solution proves the flat-family construction and flatness
of $\mci$, records the untwisted calculation, and then proves this corrected
jump.
:::

::: {.solution}
Use homogeneous coordinates
$$
[x_0:x_1:x_2:x_3:x_4]
$$
on $\PP^4$. The rational normal quartic is
$$
\nu_1:\PP^1\longrightarrow\PP^4,
\qquad
[s:u]\longmapsto
[s^4:s^3u:s^2u^2:su^3:u^4].
$$

<1>1. Hartshorne's projection degeneration (III.9.8.3), applied by scaling
the coordinate $x_2$, gives a flat family
$$
X\longrightarrow T=\AA^1
$$
whose fibres for $a\ne0$ are
$$
X_a=
\left\{
[s^4:s^3u:a s^2u^2:su^3:u^4]
ight\},
$$
and whose special fibre is the reduced twisted quartic
$$
X_0=
\left\{
[s^4:s^3u:0:su^3:u^4]
ight\}
\subseteq V(x_2)\cong\PP^3.
$$

::: {.proof}
Let
$$
P=[0:0:1:0:0].
$$
This point does not lie on $X_1$. For $a\ne0$, let
$$
\sigma_a([x_0:x_1:x_2:x_3:x_4])
=
[x_0:x_1:a x_2:x_3:x_4].
$$
Then $X_a=\sigma_a(X_1)$, so over $\GG_m\subset\AA^1$ the family is
isomorphic to the product $X_1\times\GG_m$. Example III.9.8.3 takes its
flat projective closure over $\AA^1$. Set-theoretically the special fibre
is the projection of $X_1$ from $P$ to the hyperplane $x_2=0$, namely the
displayed twisted quartic.

Flatness makes the Hilbert polynomial of every fibre equal to that of the
rational normal quartic:
$$
P(m)=4m+1.
$$
The reduced projected curve is isomorphic to $\PP^1$ by
[[P-AGH318PROJNORMAL|Exercise I.3.18]], and its hyperplane bundle pulls
back to $\mco_{\PP^1}(4)$, so it has the same Hilbert polynomial $4m+1$.
Any nonzero nilpotent thickening supported on this curve would contribute a
nonzero Hilbert polynomial. Hence the flat special fibre has no extra
scheme structure and is exactly the reduced $X_0$.
:::

<1>2. The ideal sheaf
$$
\mci\subseteq\mco_{\PP^4\times T}
$$
of the total family is flat over $T$.

::: {.proof}
There is an exact sequence
$$
0
\longrightarrow
\mci
\longrightarrow
\mco_{\PP^4\times T}
\longrightarrow
\mco_X
\longrightarrow0.
$$
The middle term is flat over $T$, and $\mco_X$ is flat over $T$ because
$X\to T$ is flat. In an exact sequence, the kernel of a surjection between
flat modules is flat. Therefore $\mci$ is flat over $T$.
:::

<1>3. For the untwisted ideal sheaves, the printed jump does not occur:
$$
H^0(\PP^4,\mci_t)=H^1(\PP^4,\mci_t)=0
$$
for every $t\in T$.

::: {.proof}
Since $\mco_X$ is flat over $T$, restricting the exact sequence of
step <1>2 to a fibre remains exact:
$$
0
\longrightarrow
\mci_t
\longrightarrow
\mco_{\PP^4}
\longrightarrow
\mco_{X_t}
\longrightarrow0.
$$
Every $X_t$ is isomorphic to $\PP^1$, hence is connected and proper, so
$$
H^0(X_t,\mco_{X_t})=k.
$$
The restriction map
$$
H^0(\PP^4,\mco_{\PP^4})=k
\longrightarrow
H^0(X_t,\mco_{X_t})=k
$$
is the identity on constants and therefore an isomorphism. Since
$$
H^1(\PP^4,\mco_{\PP^4})=0,
$$
the long exact sequence gives
$$
H^0(\PP^4,\mci_t)=0
\qquad\text{and}\qquad
H^1(\PP^4,\mci_t)=0.
$$
Thus the two displayed functions in the printed statement are both
identically zero.
:::

<1>4. After twisting by $\mco_{\PP^4}(1)$, for every $a\ne0$ one has
$$
H^0(\PP^4,\mci_a(1))
=
H^1(\PP^4,\mci_a(1))
=
0.
$$

::: {.proof}
Twisting the fibre sequence gives
$$
0
\longrightarrow
\mci_a(1)
\longrightarrow
\mco_{\PP^4}(1)
\longrightarrow
\mco_{X_a}(1)
\longrightarrow0.
$$
For $a\ne0$, the embedding $X_a\cong\PP^1\hookrightarrow\PP^4$ is the
complete linear series $|\mco_{\PP^1}(4)|$. Therefore the restriction map
$$
H^0(\PP^4,\mco(1))
\longrightarrow
H^0(X_a,\mco_{X_a}(1))
$$
identifies two five-dimensional spaces and sends the five coordinate
linear forms to a basis of $H^0(\PP^1,\mco(4))$. Hence it is an
isomorphism. Since $H^1(\PP^4,\mco(1))=0$, the long exact sequence gives
the claimed vanishing.
:::

<1>5. For the special fibre,
$$
h^0(\PP^4,\mci_0(1))
=
h^1(\PP^4,\mci_0(1))
=
1.
$$

::: {.proof}
The pullback of $\mco_{X_0}(1)$ to $\PP^1$ is again
$\mco_{\PP^1}(4)$, so
$$
h^0(X_0,\mco_{X_0}(1))=5.
$$
Under the parametrization
$$
[s:u]\longmapsto[s^4:s^3u:0:su^3:u^4],
$$
the restriction map
$$
H^0(\PP^4,\mco(1))
\longrightarrow
H^0(\PP^1,\mco(4))
$$
sends the coordinate basis to
$$
s^4,\ s^3u,\ 0,\ su^3,\ u^4.
$$
Its kernel is therefore the one-dimensional span of $x_2$, and its image
has codimension one, missing the section $s^2u^2$.

The long exact sequence of
$$
0
\to
\mci_0(1)
\to
\mco_{\PP^4}(1)
\to
\mco_{X_0}(1)
\to0
$$
and the vanishing $H^1(\PP^4,\mco(1))=0$ identify
$$
H^0(\PP^4,\mci_0(1))
$$
with that kernel and
$$
H^1(\PP^4,\mci_0(1))
$$
with that cokernel. Both have dimension one.
:::

<1>6. Thus the intended semicontinuity example is
$$
h^0(t,\mci(1))
=
h^1(t,\mci(1))
=
\begin{cases}
0,&t\ne0,\\
1,&t=0.
\end{cases}
$$

::: {.proof}
Steps <1>4 and <1>5 give the displayed values. Step <1>3 proves that the
same assertion with $\mci$ in place of $\mci(1)$ is false.
:::

<1>7. Q.E.D. for the corrected statement.

::: {.proof}
Steps <1>1--<1>2 construct the required flat family and prove flatness of
its ideal sheaf. Step <1>3 resolves the printed cohomology claim, and
steps <1>4--<1>6 prove the missing-twist correction that has the advertised
jump.
:::
:::
