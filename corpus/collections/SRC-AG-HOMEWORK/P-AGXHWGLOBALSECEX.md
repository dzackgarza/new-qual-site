---
schema: qual/card@1
id: P-AGXHWGLOBALSECEX
kind: problem
title: Global sections is left exact but not exact, and the exponential sequence
classification:
  areas:
  - algebraic-geometry
  topics:
  - Sheaf Cohomology
  - Exact Sequences
  - Global Sections
relations: []
review: draft
---

::: {.problem}
For any open $U \subseteq X$ show that the functor
$$
\Gamma\qty{U, {-}}: \Sh(X) \to \mathsf{Ab}\mathsf{Grp}
$$
is left exact, but need not be exact.
:::

::: {.solution}
Let
$$
0\longrightarrow \mathcal F'
\xrightarrow{\alpha}
\mathcal F
\xrightarrow{\beta}
\mathcal F''
$$
be an exact sequence of sheaves of abelian groups on $X$, and fix an open subset $U\subseteq X$.

<1>1. The map $\alpha_U:\mathcal F'(U)\to\mathcal F(U)$ is injective.

::: {.proof}
The kernel sheaf of $\alpha$ is the zero sheaf because the given sheaf sequence is exact at $\mathcal F'$. Kernels of morphisms of sheaves are computed sectionwise, so
$$
\ker(\alpha_U)=(\ker\alpha)(U)=0.
$$
Hence $\alpha_U$ is injective.
:::

<1>2. One has $\operatorname{im}(\alpha_U)\subseteq\ker(\beta_U)$.

::: {.proof}
Exactness of the sheaf sequence gives $\beta\circ\alpha=0$. Evaluating this equality on $U$ gives $\beta_U\circ\alpha_U=0$, which is exactly the asserted inclusion.
:::

<1>3. One has $\ker(\beta_U)\subseteq\operatorname{im}(\alpha_U)$.

<2>1. Every $s\in\ker(\beta_U)$ lifts locally through $\alpha$.

::: {.proof}
Fix $p\in U$. Exactness may be checked on stalks, so
$$
\ker(\beta_p)=\operatorname{im}(\alpha_p).
$$
For $s\in\ker(\beta_U)$, its germ $s_p\in\mathcal F_p$ therefore equals $\alpha_p(t_p)$ for some $t_p\in\mathcal F'_p$. Choose a representative of $t_p$ on a neighborhood of $p$. Equality of the two germs then allows that neighborhood to be shrunk to an open set $V_p\subseteq U$ on which there is a section $t_p'\in\mathcal F'(V_p)$ satisfying
$$
\alpha_{V_p}(t_p')=s|_{V_p}.
$$
:::

<2>2. The local lifts from step <2>1 agree on overlaps.

::: {.proof}
On $V_p\cap V_q$,
$$
\alpha_{V_p\cap V_q}(t_p'|_{V_p\cap V_q})
=s|_{V_p\cap V_q}
=\alpha_{V_p\cap V_q}(t_q'|_{V_p\cap V_q}).
$$
By step <1>1 applied to the open set $V_p\cap V_q$, the map $\alpha_{V_p\cap V_q}$ is injective. Hence
$$
t_p'|_{V_p\cap V_q}=t_q'|_{V_p\cap V_q}.
$$
:::

<2>3. The section $s$ lies in $\operatorname{im}(\alpha_U)$.

::: {.proof}
The sets $V_p$ cover $U$, and step <2>2 shows that the sections $t_p'$ are compatible on overlaps. The sheaf gluing axiom gives a unique section $t\in\mathcal F'(U)$ restricting to each $t_p'$. The sections $\alpha_U(t)$ and $s$ have equal restrictions to every $V_p$, so the uniqueness part of the sheaf axiom gives $\alpha_U(t)=s$. Thus $s\in\operatorname{im}(\alpha_U)$.
:::

<2>4. Q.E.D.

::: {.proof}
Step <2>3 proves the inclusion claimed in step <1>3.
:::

<1>4. Therefore
$$
0\longrightarrow\Gamma(U,\mathcal F')
\xrightarrow{\alpha_U}
\Gamma(U,\mathcal F)
\xrightarrow{\beta_U}
\Gamma(U,\mathcal F'')
$$
is exact.

::: {.proof}
Step <1>1 gives exactness at $\Gamma(U,\mathcal F')$, while steps <1>2 and <1>3 give
$$
\operatorname{im}(\alpha_U)=\ker(\beta_U).
$$
Hence $\Gamma(U,-)$ is left exact.
:::

<1>5. The functor $\Gamma(U,-)$ need not be exact.

<2>1. On $X=\CC^\times$, the exponential sequence
$$
0\longrightarrow\underline{\ZZ}
\longrightarrow\mathcal O_X
\xrightarrow{\exp(2\pi i\,\cdot)}
\mathcal O_X^\times
\longrightarrow 1
$$
is exact as a sequence of sheaves of abelian groups.

::: {.proof}
The kernel consists of holomorphic functions whose values lie in $\ZZ$; such functions are locally constant, so the kernel is $\underline{\ZZ}$. Every nowhere-vanishing holomorphic function admits a holomorphic logarithm locally, so the exponential map is surjective on stalks. Thus the sequence is exact as a sequence of sheaves.
:::

<2>2. The induced map
$$
\Gamma(X,\mathcal O_X)
\xrightarrow{\exp(2\pi i\,\cdot)}
\Gamma(X,\mathcal O_X^\times)
$$
is not surjective.

::: {.proof}
The identity function $z\mapsto z$ is a nowhere-vanishing holomorphic function on $\CC^\times$. Suppose there were $h\in\mathcal O_X(X)$ with
$$
e^{2\pi i h(z)}=z.
$$
Taking logarithmic derivatives gives
$$
2\pi i\,h'(z)=\frac1z.
$$
Integrating around the positively oriented unit circle $\gamma$ yields
$$
2\pi i\int_\gamma h'(z)\,dz
=\int_\gamma\frac{dz}{z}.
$$
The left side is $0$ because $h'$ has the global primitive $h$, whereas the right side is $2\pi i$. This contradiction shows that the identity function has no global holomorphic logarithm, so the map on global sections is not surjective.
:::

<2>3. Q.E.D.

::: {.proof}
Step <2>2 exhibits a short exact sequence of sheaves whose image under global sections fails to be exact at the rightmost nonzero term.
:::

<1>6. Q.E.D.

::: {.proof}
Step <1>4 proves left exactness for every open $U\subseteq X$, and step <1>5 gives an explicit failure of exactness.
:::
:::
