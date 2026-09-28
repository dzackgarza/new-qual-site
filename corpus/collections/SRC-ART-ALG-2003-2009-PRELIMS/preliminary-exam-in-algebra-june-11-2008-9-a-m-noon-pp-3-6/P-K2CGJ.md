---
schema: qual/card@1
id: P-K2CGJ
kind: problem
title: Conjugacy class size equals the index of the centralizer; restriction to a
  subgroup of index $2$
classification:
  areas:
  - algebra
  topics:
  - Conjugacy
  - Centralizers and Normalizers
  - Class Equation
relations: []
review: draft
audit:
- event: solution-written
  by: muse-spark-1.2
  date: 2026-08-30
---

::: {.problem}
Let $G$ be a finite group.
For any $x \in G$ $$Z_G(x) = \{g \in G : gxg^{-1} = x\}$$ is the centralizer of $x$ in $G$ and $$x^G = \{gxg^{-1} : g \in G\}$$ is the conjugacy class of $x$ in $G$.

a. Show that $|x^G| = [G : Z_G(x)]$.

b. If $H \le G$ and $x \in H$, prove that $Z_H(x) = H \cap Z_G(x)$.

c. If $H$ is a subgroup of index 2 in $G$ and $x \in H$, prove that either $|x^H| = |x^G|$ or $|x^H| = \frac{1}{2}|x^G|$.
:::

::: {.solution}
<1>1. In part (a), $|x^G|=[G:Z_G(x)]$.

::: {.proof}
The map $\Phi\colon G/Z_G(x)\to x^G$, $gZ_G(x)\mapsto gxg^{-1}$, is well defined and injective, because
$$
g_1Z_G(x)=g_2Z_G(x)\iff g_2^{-1}g_1\in Z_G(x)\iff (g_2^{-1}g_1)x(g_2^{-1}g_1)^{-1}=x\iff g_1xg_1^{-1}=g_2xg_2^{-1}.
$$
It is surjective by the definition of $x^G$. Hence $|x^G|=\abs{G/Z_G(x)}=[G:Z_G(x)]$.
:::

<1>2. In part (b), $Z_H(x)=H\cap Z_G(x)$.

::: {.proof}
$Z_H(x)=\{h\in H: hxh^{-1}=x\}=\{g\in G: g\in H\text{ and }gxg^{-1}=x\}=H\cap Z_G(x)$.
:::

Assume for part (c) that $[G:H]=2$ and $x\in H$.

<1>3. $2\,|x^H|=|x^G|\,[Z_G(x):Z_H(x)]$.

::: {.proof}
By step <1>1 applied in $G$ and in $H$, $|x^G|=[G:Z_G(x)]$ and $|x^H|=[H:Z_H(x)]$.
Since $Z_H(x)\le H\le G$ and $Z_H(x)\le Z_G(x)\le G$ by step <1>2, multiplicativity of indices gives
$$
[G:Z_H(x)]=[G:H]\,[H:Z_H(x)]=2\,|x^H|,\qquad
[G:Z_H(x)]=[G:Z_G(x)]\,[Z_G(x):Z_H(x)]=|x^G|\,[Z_G(x):Z_H(x)].
$$
:::

<1>4. $[Z_G(x):Z_H(x)]\in\{1,2\}$.

::: {.proof}
A subgroup of index $2$ is normal, so $HZ_G(x)$ is a subgroup of $G$ containing $H$.
By step <1>2 and the second isomorphism theorem, $[Z_G(x):Z_H(x)]=[Z_G(x):H\cap Z_G(x)]=[HZ_G(x):H]$, which divides $[G:H]=2$.
:::

<1>5. Q.E.D.

::: {.proof}
By steps <1>3 and <1>4, if $[Z_G(x):Z_H(x)]=2$ then $|x^H|=|x^G|$, and if $[Z_G(x):Z_H(x)]=1$ then $|x^H|=\tfrac12|x^G|$. Steps <1>1 and <1>2 answer parts (a) and (b).
:::
:::
