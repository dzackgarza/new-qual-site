---
schema: qual/card@1
id: P-LRECB
kind: problem
title: $[E:F]\equiv 1\pmod{p}$ when $\Gal(K/E)$ contains $N_G(P)$
classification:
  areas:
  - algebra
  topics:
  - galois-theory
  - sylow-theory
  - centralizers-and-normalizers
relations: []
review: draft
solved: true
---
Let $K$ be a Galois extension of $F$, and let $F \subset E \subset K$ be inclusions of fields.
Let $G \da \Gal(K/F)$ and $H \da \Gal(K/E)$, and suppose $H$ contains $N_G(P)$, where $P$ is a Sylow $p$-subgroup of $G$ for $p$ a prime.
Prove that \( [E: F] \equiv 1 \mod p \).

:::{.concept}
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

:::{.solution}
\envlist

- Reduce to a group theory problem: $[E:F] = [G:H]$, despite the fact that $E/F$ is not necessarily Galois.
  This is because we can count in towers:
  \[
  [K:F] = [K:E][E:F] &\implies [G:1] = [K:E][H:1] \\
  &\implies \size G = [K:E] \size H \\
  &\implies [G:H] = {\size G \over \size H} = [K:E]
  .\]

- Essential fact: if $P \in \Syl_p(G)$, we can use that $P \subseteq N_G(P) \subset H$ and so $P\in \Syl_p(H)$ as well.
- Now use that $N_G(P) \subseteq H$, and do Sylow theory for $P$ in both $G$ and $H$:
  - Sylow 3 on $G$ yields $n_p(G) = [G: N_G(P)] \equiv 1 \mod p$.
  - Sylow 3 on $H$ yields $n_p(H) = [G: N_H(P)] \equiv 1 \mod p$.
- Claim: $N_H(P) = N_G(P)$.
  - We have $N_H(P) \subseteq N_G(P)$ since $H \subseteq G$, so $hPh\inv = P$ remains true regarding either $h\in H$ or $h\in G$.
  - For $N_G(P) \subseteq N_H(P)$, use that $N_G(P) \subseteq H$ and so $gPg\inv = P$ implies $g\in H$, so $g\in N_H(P)$.

- Now morally one might want to apply an isomorphism theorem:
\[
{G/ N_G(P) \over H/N_H(P)}=
{G/ N_H(P) \over H/N_H(P)}\cong
{G\over H}
,\]
  but we don't have normality.
  However, we can still get away with the corresponding counting argument if everything is finite:
  \[
  {[G: N_G(P)] \over [H:N_H(P)] }=
  {[G: N_H(P)] \over [H:N_H(P)] }=
  {\size G / \size N_H(P) \over \size H / \size N_H(P)}
  = {\size G \over \size H} 
  = [G: H]
  .\]

- We have an equation of the form $n_p(G)/n_p(H) = m$, and we want to show $m\equiv 1 \mod p$.
  So write
  \[
  {n_p(G) \over n_p(H) } 
  = m \implies m n_p(H) &= n_p(G) \\
  \implies m n_p(H) &\equiv n_p(G) \mod p \\
  \implies m\cdot 1 &\equiv 1 \mod p \\
  \implies m &\equiv 1 \mod p
  .\]

:::

