---
schema: qual/card@1
id: P-UCLARA17S-07
kind: problem
title: Conformal homeomorphisms of closed annuli preserve the modulus
classification:
  areas:
  - real-analysis
  topics: []
relations: []
review: draft
audit:
- event: source-checked
  by: gpt-5.6-sol
  date: 2026-09-13
  note: Transcribed from the official UCLA Analysis Qualifying Exam, Spring 2017, and reconciled with the retained UCLA Analysis Qualifying Exam Solutions compendium.
---

::: {.problem}
Let $f(z)$ be a one-to-one continuous mapping from the closed annulus
$$
\{1\le\abs{z}\le R\}
$$
onto the closed annulus
$$
\{1\le\abs{z}\le S\}
$$
such that $f$ is analytic on the open annulus $\{1<\abs{z}<R\}$. Prove that $S=R$.
:::

::: {.solution}

Let
$$
A_R\coloneqq\{z:1<\abs{z}<R\},
\qquad
A_S\coloneqq\{w:1<\abs{w}<S\}.
$$

::: pf

::: {.pf-step #s1-1}

The map $f:A_R\to A_S$ is biholomorphic, and its extension to the closed annuli sends the two boundary circles of the source onto the two boundary circles of the target, possibly interchanging them.


::: pf-proof

The given map is a continuous bijection between compact Hausdorff spaces, hence a homeomorphism of the closed annuli. A boundary point of a two-dimensional manifold with boundary is characterized topologically by having a half-disk neighborhood rather than a disk neighborhood, so the homeomorphism preserves the boundary. Since each boundary circle is connected and the target boundary has exactly two connected components, the two source boundary circles map onto the two target boundary circles, possibly swapped.

On the interior, $f$ is analytic and injective. An injective nonconstant holomorphic function has nonvanishing derivative, and its inverse is holomorphic. Hence $f:A_R\to A_S$ is biholomorphic.

:::

:::

::: {.pf-step #s1-2}

Define
$$
u(w)\coloneqq\frac{\log\abs{w}}{\log S}
\qquad(w\in A_S).
$$
Then $u$ is harmonic, equals $0$ on $\abs{w}=1$, equals $1$ on $\abs{w}=S$, and
$$
\int_{A_S}\norm{\nabla u}^2\,dA
=\frac{2\pi}{\log S}.
$$


::: pf-proof

Since $\log\abs{w}$ is harmonic away from $0$, $u$ is harmonic on $A_S$. In polar coordinates $w=re^{i\theta}$,
$$
\norm{\nabla u}=\frac1{r\log S}.
$$
Therefore
$$
\begin{aligned}
\int_{A_S}\norm{\nabla u}^2\,dA
&=\int_0^{2\pi}\int_1^S
\frac1{r^2(\log S)^2}\,r\,dr\,d\theta\\
&=\frac{2\pi}{(\log S)^2}\int_1^S\frac{dr}{r}\\
&=\frac{2\pi}{\log S}.
\end{aligned}
$$

:::

:::

::: pf-step

The pullback
$$
v\coloneqq u\circ f
$$
is harmonic on $A_R$, extends continuously to the closed annulus, and its boundary values are either
$$
v=0\text{ on }\abs{z}=1,
\qquad
v=1\text{ on }\abs{z}=R,
$$
or the reverse.


::: pf-proof

Composition of a harmonic function with a biholomorphic map is harmonic. Continuity up to the boundary follows from the given continuous extension of $f$. The boundary values follow from step [](#s1-1){.pf-ref} and the boundary values of $u$ from step [](#s1-2){.pf-ref}.

:::

:::

::: {.pf-step #s1-4}

One has either
$$
v(z)=\frac{\log\abs{z}}{\log R}
$$
for all $z\in A_R$, or
$$
v(z)=1-\frac{\log\abs{z}}{\log R}.
$$


::: pf-proof

The function
$$
h(z)=\frac{\log\abs{z}}{\log R}
$$
is harmonic on $A_R$, continuous on its closure, and has boundary values $0$ on $\abs{z}=1$ and $1$ on $\abs{z}=R$. By the maximum principle, the Dirichlet problem on the annulus has at most one continuous harmonic solution with prescribed boundary values: the difference of two such solutions is harmonic, continuous on the closure, and vanishes on the boundary, hence vanishes identically. Thus $v=h$ in the first boundary-order case and $v=1-h$ in the swapped case.

:::

:::

::: {.pf-step #s1-5}

The Dirichlet energy of $v$ is
$$
\int_{A_R}\norm{\nabla v}^2\,dA
=\frac{2\pi}{\log R}.
$$


::: pf-proof

By step [](#s1-4){.pf-ref}, $\norm{\nabla v}=\norm{\nabla h}$ in either case. The computation in step [](#s1-2){.pf-ref} with $R$ in place of $S$ gives
$$
\int_{A_R}\norm{\nabla h}^2\,dA=\frac{2\pi}{\log R}.
$$

:::

:::

::: {.pf-step #s1-6}

Conformal invariance of Dirichlet energy gives
$$
\int_{A_R}\norm{\nabla(u\circ f)}^2\,dA
=\int_{A_S}\norm{\nabla u}^2\,dA.
$$


::: pf-proof

At each point of $A_R$, the real differential $Df$ is a rotation followed by multiplication of lengths by $\abs{f'}$. Hence
$$
\norm{\nabla(u\circ f)}^2
=\abs{f'}^2\,\norm{\nabla u}^2\circ f.
$$
The Jacobian determinant of $f$ is $\abs{f'}^2$. The change-of-variables formula for the biholomorphism $f:A_R\to A_S$ therefore yields the claimed equality.

:::

:::

::: {.pf-step #s1-7}

One has
$$
\boxed{S=R}.
$$


::: pf-proof

By steps [](#s1-2){.pf-ref} and [](#s1-5){.pf-ref}, and [](#s1-6){.pf-ref},
$$
\frac{2\pi}{\log R}
=\frac{2\pi}{\log S}.
$$
Since $R,S>1$, both logarithms are positive, so $\log R=\log S$ and hence $R=S$.

:::

:::

::: pf-qed

Step [](#s1-7){.pf-ref} is the required conclusion.

:::

:::

:::
