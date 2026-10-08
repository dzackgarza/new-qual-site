---
schema: qual/card@1
id: P-LRECB
kind: problem
title: $[E:F]\equiv 1\pmod{p}$ when $\Gal(K/E)$ contains $N_G(P)$
classification:
  areas:
  - algebra
  topics:
  - Galois Theory
  - Sylow Theory
  - Centralizers and Normalizers
relations: []
review: draft
---

::: {.problem}
Let $K$ be a Galois extension of $F$, and let $F \subset E \subset K$ be inclusions of fields.
Let $G \da \Gal(K/F)$ and $H \da \Gal(K/E)$, and suppose $H$ contains $N_G(P)$, where $P$ is a Sylow $p$-subgroup of $G$ for $p$ a prime.
Prove that \( [E: F] \equiv 1 \mod p \).
:::

::: {.concept}
The correspondence:

\begin{tikzcd}
	K &&&& 1 \\
	\\
	E &&&& {H \da \Gal(K/E)\hspace{4em}} \\
	\\
	F &&&& {G \da \Gal(K/F)\hspace{4em}}
	\arrow["{[E:F]}", hook, from=5-1, to=3-1]
	\arrow["{[K:E]}", hook, from=3-1, to=1-1]
	\arrow[""{name=0, anchor=center, inner sep=0}, "{[K:F]}"', curve={height=30pt}, hook, from=5-1, to=1-1]
	\arrow["{[H:1]}"', hook, from=1-5, to=3-5]
	\arrow["{[G:H]}"', hook, from=3-5, to=5-5]
	\arrow["{[G:1]}", curve={height=-30pt}, hook, from=1-5, to=5-5]
	\arrow["{\Gal(K/\wait)}"', shift right=5, shorten <=18pt, Rightarrow, from=0, to=3-5]
\end{tikzcd}

> [Link to Diagram](https://q.uiver.app/?q=WzAsNixbMCwyLCJFIl0sWzAsMCwiSyJdLFswLDQsIkYiXSxbNCwwLCIxIl0sWzQsMiwiSCBcXGRhIFxcR2FsKEsvRSlcXGhzcGFjZXs0ZW19Il0sWzQsNCwiRyBcXGRhIFxcR2FsKEsvRilcXGhzcGFjZXs0ZW19Il0sWzIsMCwiW0U6Rl0iLDAseyJzdHlsZSI6eyJ0YWlsIjp7Im5hbWUiOiJob29rIiwic2lkZSI6InRvcCJ9fX1dLFswLDEsIltLOkVdIiwwLHsic3R5bGUiOnsidGFpbCI6eyJuYW1lIjoiaG9vayIsInNpZGUiOiJ0b3AifX19XSxbMiwxLCJbSzpGXSIsMix7ImN1cnZlIjo1LCJzdHlsZSI6eyJ0YWlsIjp7Im5hbWUiOiJob29rIiwic2lkZSI6InRvcCJ9fX1dLFszLDQsIltIOjFdIiwyLHsic3R5bGUiOnsidGFpbCI6eyJuYW1lIjoiaG9vayIsInNpZGUiOiJ0b3AifX19XSxbNCw1LCJbRzpIXSIsMix7InN0eWxlIjp7InRhaWwiOnsibmFtZSI6Imhvb2siLCJzaWRlIjoidG9wIn19fV0sWzMsNSwiW0c6MV0iLDAseyJjdXJ2ZSI6LTUsInN0eWxlIjp7InRhaWwiOnsibmFtZSI6Imhvb2siLCJzaWRlIjoidG9wIn19fV0sWzgsNCwiXFxHYWwoSy9cXHdhaXQpIiwyLHsib2Zmc2V0Ijo1LCJzaG9ydGVuIjp7InNvdXJjZSI6MjB9fV1d)

Normalizers:
\[
N_G(P) = \ts{g\in G \st gPg\inv = P}
.\]

:::

::: {.solution}
<1>1. The field degree satisfies $[E:F]=[G:H]$.

::: {.proof}
Since $K/F$ is finite Galois and $H=\operatorname{Gal}(K/E)$, the Galois correspondence gives $[K:F]=|G|$ and $[K:E]=|H|$. The tower law therefore gives
\[
[E:F]=\frac{[K:F]}{[K:E]}=\frac{|G|}{|H|}=[G:H].
\]
:::

<1>2. The Sylow counts satisfy
\[
n_p(G)=[G:N_G(P)],\qquad
n_p(H)=[H:N_G(P)].
\]

::: {.proof}
The inclusions $P\subseteq N_G(P)\subseteq H$ imply that $P$ is a Sylow $p$-subgroup of $H$, since it already has the largest possible $p$-power order in $G$. Moreover,
\[
N_H(P)=H\cap N_G(P)=N_G(P).
\]
The Sylow conjugacy theorem identifies the numbers of Sylow $p$-subgroups with their normalizer indices, giving the formulas.
:::

<1>3. The field degree obeys
\[
\boxed{[E:F]\equiv1\pmod p}.
\]

::: {.proof}
By multiplicativity of subgroup indices and step <1>2,
\[
n_p(G)=[G:H][H:N_G(P)]=[G:H]n_p(H).
\]
Sylow's theorems give $n_p(G)\equiv n_p(H)\equiv1\pmod p$. Reducing the equality modulo $p$ therefore yields $1\equiv[G:H]\pmod p$. Substitute $[E:F]=[G:H]$ from step <1>1.
:::

<1>4. Q.E.D.

::: {.proof}
Step <1>3 proves the required congruence.
:::

:::
