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

::: problem
Let $G$ be a finite group.
For any $x \in G$ $$Z_G(x) = \{g \in G : gxg^{-1} = x\}$$ is the centralizer of $x$ in $G$ and $$x^G = \{gxg^{-1} : g \in G\}$$ is the conjugacy class of $x$ in $G$.

a. Show that $|x^G| = [G : Z_G(x)]$.

b. If $H \le G$ and $x \in H$, prove that $Z_H(x) = H \cap Z_G(x)$.

c. If $H$ is a subgroup of index 2 in $G$ and $x \in H$, prove that either $|x^H| = |x^G|$ or $|x^H| = \frac{1}{2}|x^G|$.
:::

::: {.solution}
**Part (a).**

<1>1. Consider the group action of $G$ on itself by conjugation: $(g, y) \mapsto gyg^{-1}$.
::: {.proof}
$(gh)y(gh)^{-1} = g(hyh^{-1})g^{-1}$ and $1y1^{-1} = y$.
:::

<1>2. The orbit of $x$ is the conjugacy class $x^G = \{gxg^{-1} : g \in G\}$, and the stabilizer of $x$ is the centralizer $Z_G(x) = \{g \in G : gxg^{-1} = x\}$.
::: {.proof}
definitions of orbit and stabilizer for the conjugation action.
:::

<1>3. By the Orbit–Stabilizer Theorem, the map $\Phi: G/Z_G(x) \to x^G$ given by $g Z_G(x) \mapsto gxg^{-1}$ is a well-defined bijection.
::: {.proof}
$g_1 Z_G(x) = g_2 Z_G(x) \iff g_2^{-1} g_1 \in Z_G(x) \iff (g_2^{-1} g_1)x(g_2^{-1} g_1)^{-1} = x \iff g_1 x g_1^{-1} = g_2 x g_2^{-1}$.
:::

<1>4. Therefore $|x^G| = |G / Z_G(x)| = [G : Z_G(x)]$.
::: {.proof}
<1>3.
:::

**Part (b).**

<1>5. For $H \le G$ and $x \in H$:
\[
Z_H(x) = \{h \in H : hxh^{-1} = x\} = \{g \in G : g \in H \text{ and } gxg^{-1} = x\} = H \cap Z_G(x).
\]
::: {.proof}
intersection of subsets in $G$.
:::

**Part (c).**

<1>6. Assume $[G : H] = 2$ and $x \in H$.
::: {.proof}
hypothesis.
:::

<1>7. Relate the indices of centralizers: <2>1. By (a), $|x^G| = [G : Z_G(x)]$ and $|x^H| = [H : Z_H(x)]$.
::: {.proof}
(a) applied to $G$ and $H$.
:::
<2>2. By the tower law for subgroup indices:
\[
[G : Z_H(x)] = [G : H][H : Z_H(x)] = 2 |x^H|.
\]
::: {.proof}
multiplicativity of index and $[G : H] = 2$.
:::
<2>3. On the other hand:
\[
[G : Z_H(x)] = [G : Z_G(x)][Z_G(x) : Z_H(x)] = |x^G| [Z_G(x) : Z_H(x)].
\]
::: {.proof}
$Z_H(x) = H \cap Z_G(x) \le Z_G(x) \le G$.
:::
<2>4. Equating the two expressions for $[G : Z_H(x)]$ yields:
\[
2 |x^H| = |x^G| [Z_G(x) : Z_H(x)].
\]
::: {.proof}
<2>2 and <2>3.
:::

<1>8. Determine the possible values of $[Z_G(x) : Z_H(x)]$: <2>1. By the Second Isomorphism Theorem / product formula:
\[
[Z_G(x) : Z_H(x)] = [Z_G(x) : H \cap Z_G(x)] = [H Z_G(x) : H].
\]
::: {.proof}
$H \cap Z_G(x) = Z_H(x)$ from (b). <2>2. Since $H \le H Z_G(x) \le G$ and $[G : H] = 2$, the index $[H Z_G(x) : H]$ divides $[G : H] = 2$.
:::
::: {.proof}
tower law $[G : H] = [G : H Z_G(x)][H Z_G(x) : H]$.
:::
<2>3. Thus $[Z_G(x) : Z_H(x)] \in \{1, 2\}$.
::: {.proof}
the only divisors of 2 are 1 and 2.
:::

<1>9. Evaluate $|x^H|$ for both cases: <2>1. **Case 1:** If $[Z_G(x) : Z_H(x)] = 2$ (equivalently $Z_G(x) \not\subseteq H$), then $2 |x^H| = 2 |x^G| \implies |x^H| = |x^G|$.
::: {.proof}
<1>7 and <1>8. <2>2. **Case 2:** If $[Z_G(x) : Z_H(x)] = 1$ (equivalently $Z_G(x) \subseteq H$), then $2 |x^H| = |x^G| \implies |x^H| = \frac{1}{2} |x^G|$.
:::
::: {.proof}
<1>7 and <1>8.
:::

<1>10. Conclusion: Either $|x^H| = |x^G|$ or $|x^H| = \frac{1}{2}|x^G|$.
::: {.proof}
<1>4, <1>5, and <1>9.
:::
Q.E.D.
:::
