---
schema: qual/card@1
id: D-MORSM
kind: definition
title: Smooth morphisms and relative dimension
classification:
  areas:
  - algebraic-geometry
  topics:
  - Smooth Morphisms
  - Relative Dimension
  - Flatness
relations:
- kind: uses
  target: D-MORETALE
- kind: uses
  target: D-MORFT
review: draft
prompts:
- What is a smooth morphism?
- What is a smooth morphism of relative dimension n?
- What does smoothness give you for free?
---

::: {.definition title="Smooth"}
$f : X \to Y$ is \dfn{smooth} if it is flat, locally of finite presentation, and has geometrically regular fibres.
It is \dfn{smooth of relative dimension $n$} if in addition every irreducible component of every fibre has dimension $n$.
:::

::: {.proposition title="Criteria for smoothness of relative dimension $n$"}
For a morphism $f \colon X \to Y$ the following are equivalent.

1. $f$ is smooth of relative dimension $n$.

2. $f$ is flat and locally of finite presentation, every fibre has pure dimension $n$, and $\Omega_{X/Y}$ is locally free of rank $n$.

3. $f$ is flat and locally of finite presentation, and every fibre $X_y$ is smooth of pure dimension $n$ over $\kappa(y)$.

4. $f$ is flat and locally of finite presentation, and every geometric fibre is a regular scheme of pure dimension $n$.

5. Locally on $X$ and $Y$, $f$ is induced by $B \to B[x_1, \ldots, x_{n+r}]/(g_1, \ldots, g_r)$ with $\det(\partial g_i / \partial x_j)_{1 \leq i, j \leq r}$ invertible.
:::

::: {.example}
The fibre-dimension hypothesis in condition 2 cannot be dropped.
Over $k = \FF_p$, the morphism $\Spec k[x]/(x^p) \to \Spec k$ is flat and of finite presentation, and $\Omega = (k[x]/(x^p))\, dx$ is free of rank $1$ because $d(x^p) = p x^{p-1} dx = 0$; but the fibre has dimension $0$, not $1$, and it is not reduced, so the morphism is not smooth.
:::

::: {.remark}
The definition is three conditions and each is doing separate work, which is exactly what gets asked.
Flatness makes it a family rather than a union of unrelated fibres; finite presentation makes it algebraic; geometric regularity of the fibres is the smoothness itself, and *geometrically* is not decoration.
Over a non-perfect field the fibre can be regular and not geometrically regular: $\Spec k[x]/(x^p - t)$ over $k = \FF_p(t)$ is a regular point that becomes non-reduced after base change to $\kbar$, so it is a regular fibre of a non-smooth morphism.

What smoothness buys is the whole toolkit at once: smooth implies flat, so numerical invariants are constant; $\Omega_{X/Y}$ is locally free, so there is a relative cotangent bundle and a relative canonical sheaf; and smooth morphisms are stable under base change and composition, so the class is closed under the constructions one performs.
Relative dimension $0$ is étale, and smoothness is thus "étale up to $n$ free parameters", which is the statement that a smooth morphism locally factors as an étale map to $\AA^n_Y$.
:::
