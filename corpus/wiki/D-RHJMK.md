---
schema: qual/card@1
id: D-RHJMK
kind: definition
title: "Projective Modules"
classification:
  areas:
  - algebra
  topics: []
relations: []
review: draft
---
:::{.definition title="Projective Modules"}
A module $P$ is **projective** iff it satisfies any of the following conditions:

- A universal property: for every surjective $N \mapsvia{g} M$ and $P \mapsvia{f} M$, the following lift exists:

\begin{tikzcd}
	&& P \\
	\\
	N && M && 0
	\arrow["g", two heads, from=3-1, to=3-3]
	\arrow[from=3-3, to=3-5]
	\arrow["f", from=1-3, to=3-3]
	\arrow["{\exists \tilde f}"', dashed, from=1-3, to=3-1]
\end{tikzcd}

> [Link to Diagram](https://q.uiver.app/?q=WzAsNCxbMiwwLCJQIl0sWzIsMiwiTSJdLFswLDIsIk4iXSxbNCwyLCIwIl0sWzIsMSwiZyIsMCx7InN0eWxlIjp7ImhlYWQiOnsibmFtZSI6ImVwaSJ9fX1dLFsxLDNdLFswLDEsImYiXSxbMCwyLCJcXGV4aXN0cyBcXHRpbGRlIGYiLDIseyJzdHlsZSI6eyJib2R5Ijp7Im5hbWUiOiJkYXNoZWQifX19XV0=)

- Direct summand:

  $P$ is a direct summand of a free module $F$, so $F = P \oplus T$ for some module $T\leq F$.

- Splitting:

  For every SES $0\to A\to B\to P\to 0$, there is a right section $P\to B$ such that $P\to B\to P = \id_P$.

  > Note that this implies $B\cong \im(P\to B) \oplus \ker(B\to P)$.
  
- Exactness:

  The (always left-exact) covariant hom functor $\Hom(P, \wait)$ is right-exact.
:::
