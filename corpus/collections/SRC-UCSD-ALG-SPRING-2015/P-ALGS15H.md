---
schema: qual/card@1
id: P-ALGS15H
kind: problem
title: Minimal polynomial via Galois orbit; Artin–Schreier normality and separability
classification:
  areas:
  - algebra
  topics:
  - Galois Theory
  - Field Extensions
relations: []
review: draft
audit:
- event: source-checked
  by: OpenAI
  date: 2026-09-08
- event: solution-reviewed
  by: OpenAI
  date: 2026-09-08
---

::: problem
Let $K$ be a field with $G \subseteq \mathrm{Aut}(K)$ a finite group of automorphisms of $K$.
Let $F = \mathrm{Fix}(G)$.
Let $\alpha \in K$ and let $f = \mathrm{minpoly}_F(\alpha)$.
Let $H = \{g \in G \mid g(\alpha) = \alpha\}$ and fix $g_1, g_2, \ldots, g_m \in G$ such that $g_1 H, \ldots, g_m H$ are the distinct left cosets of $H$ in $G$.

(a) Show that $f(x) = (x - g_1(\alpha)) \cdots (x - g_m(\alpha))$.
(Hint: show the polynomial on the right has coefficients in $F$.)

(b) Use part (a) to conclude that the field extension $K/F$ is separable and normal.
:::

::: {.solution}
<1>1. Let $P_\alpha(x)=\prod_{j=1}^m(x-g_j(\alpha))$.
The elements $g_1(\alpha),\dots,g_m(\alpha)$ are precisely the distinct elements of the $G$-orbit of $\alpha$.
::: {.proof}
Two elements $g_i(\alpha)$ and $g_j(\alpha)$ are equal exactly when $g_j^{-1}g_i\in H$, equivalently when $g_iH=g_jH$.
:::

<1>2. The polynomial $P_\alpha(x)$ is fixed coefficientwise by every element of $G$, hence $P_\alpha(x)\in F[x]$.
::: {.proof}
For $g\in G$, applying $g$ to the coefficients permutes the orbit roots $g_j(\alpha)$.
Thus $g(P_\alpha)=P_\alpha$, so every coefficient lies in $F=\operatorname{Fix}(G)$.
:::

<1>3. Since $P_\alpha(\alpha)=0$ and $P_\alpha\in F[x]$, the minimal polynomial $f$ divides $P_\alpha$ in $F[x]$.
::: {.proof}
This is the defining divisibility property of the minimal polynomial.
:::

<1>4. Every $g_j(\alpha)$ is a root of $f$.
::: {.proof}
Because $f\in F[x]$ and $g_j$ fixes $F$, one has $f(g_j(\alpha))=g_j(f(\alpha))=0$.
:::

<1>5. The roots $g_j(\alpha)$ are distinct, so $P_\alpha$ divides $f$ in $K[x]$.
::: {.proof}
By <1>1 the roots are distinct, and by <1>4 each is a root of $f$.
Hence the product of those distinct linear factors divides $f$.
:::

<1>6. Both $f$ and $P_\alpha$ are monic, and the two divisibilities force
\[
f(x)=P_\alpha(x)=\prod_{j=1}^m(x-g_j(\alpha)).
\]
::: {.proof}
The two divisibilities imply equal degree; monicity then gives equality.
:::

<1>7. Every element $\alpha\in K$ is algebraic and separable over $F$.
::: {.proof}
The polynomial $P_\alpha\in F[x]$ annihilates $\alpha$, so $\alpha$ is algebraic.
By <1>6 its minimal polynomial splits into distinct linear factors.
:::

<1>8. The extension $K/F$ is normal.
::: {.proof}
If a monic irreducible $q\in F[x]$ has a root $\alpha\in K$, then $q$ is the minimal polynomial of $\alpha$.
By <1>6 it splits completely over $K$.
:::

<1>9. Therefore $K/F$ is separable and normal.
::: {.proof}
Combine <1>7 and <1>8.
:::
:::
