---
schema: qual/card@1
id: PR-C9ZEK
kind: proposition
title: Exactness is checked on stalks, and global sections are only left exact
slogan: 'Sheaf exactness is stalkwise; global sections preserve kernels but can lose surjectivity.'
classification:
  areas:
  - algebraic-geometry
  topics:
  - Stalks
  - Exact Sequences
  - Cohomology
relations:
- kind: uses
  target: T-3VX80
review: draft
prompts:
- How do you check that a sequence of sheaves is exact?
- Is a surjection of sheaves surjective on sections?
- Where does the failure of right exactness go?
---

::: {.proposition}
Let $X$ be a topological space. A sequence $\mcf \to \mcg \to \mch$ of sheaves of abelian groups on $X$ is exact exactly when
$$
\mcf_p \to \mcg_p \to \mch_p
$$
is exact for every $p \in X$ [@Har77, Exercise II.1.2(c)].
For $0 \to \mcf \to \mcg \to \mch \to 0$ exact, the sequence of global sections
$$
0 \to \mcf(X) \to \mcg(X) \to \mch(X)
$$
is exact, but the last map need not be surjective.
:::

::: {.proof}
The stalkwise criterion is the exercise cited, worked on [[P-AGH212STALKEXACT]].

For the sections, the kernel subsheaf of a morphism $\varphi\colon\mcf\to\mcg$ satisfies $\ker\varphi(U)=\ker\bigl(\varphi(U)\bigr)$ for every open $U$, so $H^0$ is left exact [@Har77, Exercise II.1.8], worked on [[P-AGH218GAMMALEFTEX]]: $\mcf(X)\to\mcg(X)$ is injective, and a section $t\in\mcg(X)$ maps to $0$ in $\mch(X)$ exactly when $t$ lies in $(\ker\varphi)(X)$, which is the image of $\mcf(X)$.

Surjectivity can fail. On $X=\CC^\times$ the exponential is a morphism of sheaves $\OO_X\to\units{\OO_X}$ that is onto on stalks, because a nowhere-vanishing holomorphic function has a holomorphic logarithm on a simply connected neighbourhood of each point. The coordinate function $z$ is a global unit that is not $\exp(f)$ for any $f\in\OO_X(X)$: differentiating $\exp f=z$ gives $f'=1/z$, and $1/z$ has no primitive on $\CC^\times$, since
$$
\int_{\abs z=1}\frac{dz}{z}=2\pi i\neq0 .
$$
So the global sections of a surjection of sheaves need not be onto, and the failure is exactly what $\delta$ measures ([[D-DEFABCAT]]).
:::

::: {.remark}
The associated long exact cohomology sequence begins
$$
0\to H^0(X,\mcf)\to H^0(X,\mcg)\to H^0(X,\mch)\xrightarrow{\delta}H^1(X,\mcf).
$$
A section $s\in H^0(X,\mch)$ lifts to a global section of $\mcg$ exactly when $\delta(s)=0$. In Čech cohomology, local lifts of $s$ differ on overlaps by a $1$-cocycle in $\mcf$ representing $\delta(s)$.
:::
