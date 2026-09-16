---
schema: qual/card@1
id: D-DIVAMPLE
kind: definition
title: Ample and very ample divisors
classification:
  areas:
  - algebraic-geometry
  topics:
  - Ample Divisors
  - Very Ample Divisors
  - Linear Systems
relations:
- kind: uses
  target: T-DIVMAPPN
review: draft
prompts:
- What is a very ample divisor?
- What is an ample divisor?
- What is the difference between ample and very ample?
- What is a hyperplane section?
---

::: {.definition title="Very ample"}
$\mcl$ is very ample when $\abs{\mcl}$ is base-point free and $\varphi_{\abs{\mcl}}$ is a closed immersion into some $\PP^n$ with $\varphi^*\OO(1) \cong \mcl$.
Equivalently, $D$ is very ample when $D \sim D'$ for $D'$ a hyperplane section of $X$ under some embedding $X \injects \PP^n$.
:::

::: {.definition title="Ample"}
$\mcl$ is ample when $\mcl\tensorpower{}{n}$ is very ample for some $n > 0$.
:::

::: {.remark}
Very ample is an embedding by *this* bundle; ample is an embedding by *some power* of it.
So very ample depends on the actual linear system and ample depends only on a numerical or asymptotic property — which is why ampleness is stable under tensoring, pullback along finite maps, and adding any bundle, while very ampleness is not.

Very ampleness is not a property of $X$ alone: it is the statement that $X$ sits in projective space with $\OO(1)$ restricting to $\mcl$.
The standard illustration that the notions differ is a divisor of degree $1$ on an elliptic curve: it is ample, but $h^0 = 1$, so its own linear system is a point and embeds nothing.
Degree $3$ is the first very ample case, giving the plane cubic.
:::

::: {.definition title="Hyperplane section"}
For a projective variety $X \subseteq \PP^n$ and a hyperplane $H \not\supseteq X$, the \dfn{hyperplane section} $X \cap H$ is the effective Cartier divisor on $X$ cut out by the linear form defining $H$.
The hyperplane sections form the linear system $\PP V \subseteq \abs{\OO_X(1)}$, where $V$ is the image of $H^0(\PP^n, \OO(1)) \to H^0(X, \OO_X(1))$.
:::

