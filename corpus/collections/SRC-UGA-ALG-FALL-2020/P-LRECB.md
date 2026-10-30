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
Let $G \coloneqq \Gal(K/F)$ and $H \coloneqq \Gal(K/E)$, and suppose $H$ contains $N_G(P)$, where $P$ is a Sylow $p$-subgroup of $G$ for $p$ a prime.
Prove that $[E: F] \equiv 1 \mod p$.
:::

::: {.concept}
The correspondence:

\begin{tikzcd}
	K &&&& 1 \\
	\\
	E &&&& {H \coloneqq \Gal(K/E)\hspace{4em}} \\
	\\
	F &&&& {G \coloneqq \Gal(K/F)\hspace{4em}}
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
$$
N_G(P) = \theset{g\in G \st gP\inverseof{g} = P}
.$$

:::

::: {.solution}

::: pf

::: {.pf-step #index}

$[E:F]=[G:H]$.

::: pf-proof

$K/F$ is Galois, so $K/E$ is Galois, $\cardinality{G}=[K:F]$ and $\cardinality{H}=[K:E]$. By the tower law $[E:F]=[K:F]/[K:E]=\cardinality{G}/\cardinality{H}$.

:::

:::

::: {.pf-step #normalizers}

$P\in\Syl_p(H)$ and $N_H(P)=N_G(P)$.

::: pf-proof

$P\subseteq N_G(P)\subseteq H\subseteq G$, and a $p$-subgroup of $H$ of maximal $p$-power order in $G$ is a Sylow $p$-subgroup of $H$. Next, $N_H(P)=N_G(P)\cap H=N_G(P)$ because $N_G(P)\subseteq H$.

:::

:::

::: {.pf-step #count}

$[G:N_G(P)]\equiv1\pmod p$ and $[H:N_H(P)]\equiv1\pmod p$.

::: pf-proof

By Sylow's theorems, the number of Sylow $p$-subgroups of a finite group is the index of the normalizer of one of them and is $\equiv1\pmod p$. Apply this to $G$ and, by Step [](#normalizers){.pf-ref}, to $H$.

:::

:::

::: pf-qed

Let $N=N_G(P)=N_H(P)$. Then
$$
[G:N]=[G:H]\,[H:N].
$$
Reducing modulo $p$ with Step [](#count){.pf-ref} gives $1\equiv[G:H]\cdot1$, so $[G:H]\equiv1\pmod p$. By Step [](#index){.pf-ref}, $[E:F]\equiv1\pmod p$.

:::

:::

:::
